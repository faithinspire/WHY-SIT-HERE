const fs = require('fs');
const buf = fs.readFileSync('WHY SIT HERE AND DIE.docx');

function findEntry(buf, filename) {
  let pos = 0;
  while (pos < buf.length - 30) {
    if (buf[pos]===0x50&&buf[pos+1]===0x4b&&buf[pos+2]===0x03&&buf[pos+3]===0x04) {
      const fnLen = buf.readUInt16LE(pos+26);
      const extraLen = buf.readUInt16LE(pos+28);
      const fn = buf.slice(pos+30, pos+30+fnLen).toString('utf8');
      const dataStart = pos+30+fnLen+extraLen;
      const compSize = buf.readUInt32LE(pos+18);
      const uncompSize = buf.readUInt32LE(pos+22);
      const method = buf.readUInt16LE(pos+8);
      if (fn===filename) return {dataStart,compSize,uncompSize,method};
      pos = dataStart+compSize;
    } else pos++;
  }
  return null;
}

const entry = findEntry(buf, 'word/document.xml');
let xmlBuf;
if (entry.method===0) xmlBuf = buf.slice(entry.dataStart, entry.dataStart+entry.uncompSize);
else { const zlib=require('zlib'); xmlBuf=zlib.inflateRawSync(buf.slice(entry.dataStart,entry.dataStart+entry.compSize)); }

const xml = xmlBuf.toString('utf8');
const allParas = xml.split(/<w:p[ >\/]/);
const paragraphs = [];
for (let i=0;i<allParas.length;i++) {
  const tMatches=[...allParas[i].matchAll(/<w:t[^>]*>([^<]*)<\/w:t>/g)];
  const text=tMatches.map(m=>m[1]).join('').trim();
  if(text) paragraphs.push(text);
}

// Print paragraphs from index 1384 to 3490
const start = parseInt(process.argv[2]) || 1384;
const end = parseInt(process.argv[3]) || 1900;
paragraphs.slice(start, end).forEach((p,i) => console.log((start+i) + '|||' + p));
