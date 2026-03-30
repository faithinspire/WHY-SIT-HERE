// Extract text from docx (which is a ZIP containing word/document.xml)
const fs = require('fs');
const path = require('path');

const docxPath = 'WHY SIT HERE AND DIE.docx';
const buf = fs.readFileSync(docxPath);

// Parse ZIP manually - find the local file header for word/document.xml
// ZIP local file header signature: 0x04034b50
function findEntry(buf, filename) {
  const sig = Buffer.from([0x50, 0x4b, 0x03, 0x04]);
  let pos = 0;
  while (pos < buf.length - 30) {
    if (buf[pos] === 0x50 && buf[pos+1] === 0x4b && buf[pos+2] === 0x03 && buf[pos+3] === 0x04) {
      const fnLen = buf.readUInt16LE(pos + 26);
      const extraLen = buf.readUInt16LE(pos + 28);
      const fn = buf.slice(pos + 30, pos + 30 + fnLen).toString('utf8');
      const dataStart = pos + 30 + fnLen + extraLen;
      const compSize = buf.readUInt32LE(pos + 18);
      const uncompSize = buf.readUInt32LE(pos + 22);
      const method = buf.readUInt16LE(pos + 8);
      if (fn === filename) {
        return { dataStart, compSize, uncompSize, method };
      }
      pos = dataStart + compSize;
    } else {
      pos++;
    }
  }
  return null;
}

const entry = findEntry(buf, 'word/document.xml');
if (!entry) { console.error('Not found'); process.exit(1); }

let xmlBuf;
if (entry.method === 0) {
  xmlBuf = buf.slice(entry.dataStart, entry.dataStart + entry.uncompSize);
} else if (entry.method === 8) {
  const zlib = require('zlib');
  const compressed = buf.slice(entry.dataStart, entry.dataStart + entry.compSize);
  xmlBuf = zlib.inflateRawSync(compressed);
}

const xml = xmlBuf.toString('utf8');

// Extract text from XML - get all <w:t> text nodes
const texts = [];
const regex = /<w:t[^>]*>([^<]*)<\/w:t>/g;
const paraRegex = /<w:p[ >]/g;

// Build paragraphs
const paragraphs = [];
const paraBlocks = xml.split('<w:p ').concat(xml.split('<w:p>'));

// Simpler approach: extract all text runs grouped by paragraph
let cleanXml = xml;
// Remove all namespace prefixes for easier parsing
const allParas = xml.split(/<w:p[ >\/]/);
for (let i = 0; i < allParas.length; i++) {
  const block = allParas[i];
  const tMatches = [...block.matchAll(/<w:t[^>]*>([^<]*)<\/w:t>/g)];
  const text = tMatches.map(m => m[1]).join('').trim();
  if (text) paragraphs.push(text);
}

// Write output
const output = paragraphs.join('\n');
fs.writeFileSync('manuscript.txt', output, 'utf8');
console.log('Total paragraphs:', paragraphs.length);
console.log('--- FIRST 100 PARAGRAPHS ---');
paragraphs.slice(0, 100).forEach((p, i) => console.log(i + ': ' + p));
