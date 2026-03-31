#!/usr/bin/env node
/**
 * Professional PDF Book Generator
 * Extracts manuscript from DOCX and creates publication-ready PDF
 */

const fs = require('fs');
const path = require('path');
const zlib = require('zlib');

// Extract text from DOCX
function extractDocxText() {
  const docxPath = 'WHY SIT HERE AND DIE.docx';
  const buf = fs.readFileSync(docxPath);

  function findEntry(buf, filename) {
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
  if (!entry) throw new Error('document.xml not found in DOCX');

  let xmlBuf;
  if (entry.method === 0) {
    xmlBuf = buf.slice(entry.dataStart, entry.dataStart + entry.uncompSize);
  } else if (entry.method === 8) {
    const compressed = buf.slice(entry.dataStart, entry.dataStart + entry.compSize);
    xmlBuf = zlib.inflateRawSync(compressed);
  }

  const xml = xmlBuf.toString('utf8');
  const allParas = xml.split(/<w:p[ >\/]/);
  const paragraphs = [];
  
  for (let i = 0; i < allParas.length; i++) {
    const block = allParas[i];
    const tMatches = [...block.matchAll(/<w:t[^>]*>([^<]*)<\/w:t>/g)];
    const text = tMatches.map(m => m[1]).join('').trim();
    if (text) paragraphs.push(text);
  }

  return paragraphs;
}

// Create HTML version for conversion
function createHTML(paragraphs) {
  const html = `<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Why Sit Here and Die?</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Georgia', serif;
            line-height: 1.6;
            color: #2C3E50;
            background: white;
        }
        
        .page {
            page-break-after: always;
            padding: 50px;
            min-height: 100vh;
            background: white;
        }
        
        .cover {
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            background: linear-gradient(135deg, #2C3E50 0%, #34495E 100%);
            color: white;
            text-align: center;
            padding: 50px;
        }
        
        .cover h1 {
            font-size: 48px;
            color: #D4AF37;
            margin-bottom: 20px;
            font-weight: bold;
        }
        
        .cover .subtitle {
            font-size: 18px;
            color: #ECF0F1;
            margin-bottom: 40px;
            line-height: 1.8;
        }
        
        .cover .author {
            font-size: 16px;
            color: #D4AF37;
            margin-top: 60px;
            font-weight: bold;
        }
        
        .cover img {
            max-width: 300px;
            max-height: 400px;
            margin-bottom: 30px;
            border-radius: 5px;
        }
        
        .title-page {
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            text-align: center;
        }
        
        .title-page h1 {
            font-size: 42px;
            color: #D4AF37;
            margin-bottom: 30px;
            font-weight: bold;
        }
        
        .title-page .subtitle {
            font-size: 16px;
            color: #2C3E50;
            margin-bottom: 60px;
            line-height: 1.8;
        }
        
        .title-page .author {
            font-size: 14px;
            color: #D4AF37;
            font-weight: bold;
        }
        
        .copyright-page {
            padding: 50px;
        }
        
        .copyright-page h2 {
            font-size: 18px;
            color: #D4AF37;
            margin-bottom: 20px;
        }
        
        .copyright-page p {
            font-size: 11px;
            line-height: 1.8;
            margin-bottom: 15px;
            color: #2C3E50;
        }
        
        .toc {
            padding: 50px;
        }
        
        .toc h1 {
            font-size: 28px;
            color: #D4AF37;
            margin-bottom: 30px;
            text-align: center;
            font-weight: bold;
        }
        
        .toc-item {
            font-size: 12px;
            margin-bottom: 10px;
            color: #2C3E50;
            line-height: 1.6;
        }
        
        .toc-item.part {
            font-weight: bold;
            color: #D4AF37;
            margin-top: 15px;
            margin-bottom: 10px;
        }
        
        .content {
            padding: 50px;
        }
        
        .content h1 {
            font-size: 28px;
            color: #D4AF37;
            margin-top: 30px;
            margin-bottom: 20px;
            font-weight: bold;
        }
        
        .content h2 {
            font-size: 18px;
            color: #D4AF37;
            margin-top: 25px;
            margin-bottom: 15px;
            font-weight: bold;
        }
        
        .content p {
            font-size: 12px;
            line-height: 1.8;
            margin-bottom: 12px;
            text-align: justify;
            color: #2C3E50;
        }
        
        .about-author {
            padding: 50px;
        }
        
        .about-author h1 {
            font-size: 28px;
            color: #D4AF37;
            margin-bottom: 30px;
            text-align: center;
            font-weight: bold;
        }
        
        .about-author img {
            max-width: 150px;
            max-height: 150px;
            margin-bottom: 20px;
            border-radius: 5px;
        }
        
        .about-author p {
            font-size: 12px;
            line-height: 1.8;
            margin-bottom: 12px;
            color: #2C3E50;
        }
        
        .back-cover {
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            background: linear-gradient(135deg, #2C3E50 0%, #34495E 100%);
            color: white;
            text-align: center;
            padding: 50px;
        }
        
        .back-cover p {
            font-size: 14px;
            line-height: 1.8;
            margin-bottom: 20px;
            color: #ECF0F1;
        }
        
        .back-cover h2 {
            font-size: 24px;
            color: #D4AF37;
            margin: 30px 0;
            font-weight: bold;
        }
        
        .back-cover .author {
            font-size: 14px;
            color: #D4AF37;
            margin-top: 60px;
            font-weight: bold;
        }
        
        @media print {
            body { margin: 0; padding: 0; }
            .page { page-break-after: always; }
        }
    </style>
</head>
<body>
    <!-- Front Cover -->
    <div class="page cover">
        <h1>WHY SIT HERE AND DIE?</h1>
        <p class="subtitle">Breaking the trap of stagnation<br/>spiritually, financially, and personally<br/>from 2 Kings 7</p>
        <p class="author">By OLUSHOLA O. PAUL</p>
    </div>
    
    <!-- Title Page -->
    <div class="page title-page">
        <h1>WHY SIT HERE AND DIE?</h1>
        <p class="subtitle">Breaking the trap of stagnation—spiritually, financially, and personally—from 2 Kings 7</p>
        <p class="author">By OLUSHOLA O. PAUL</p>
    </div>
    
    <!-- Copyright Page -->
    <div class="page copyright-page">
        <h2>WHY SIT HERE AND DIE?</h2>
        <p>Breaking the trap of stagnation—spiritually, financially, and personally—from 2 Kings 7</p>
        <p><strong>Copyright © 2026 by OLUSHOLA O PAUL</strong></p>
        <p>All rights reserved. No part of this book may be reproduced or transmitted in any form or by any means without written permission from the publisher, except for brief quotations in reviews.</p>
        <p>Scripture quotations marked KJV are from the King James Version, public domain.</p>
        <p><strong>Disclaimer:</strong> This book provides spiritual and practical principles. It does not replace professional medical, legal, financial, or psychological advice.</p>
    </div>
    
    <!-- Table of Contents -->
    <div class="page toc">
        <h1>TABLE OF CONTENTS</h1>
        <div class="toc-item">Foreword</div>
        <div class="toc-item">Acknowledgments</div>
        <div class="toc-item">Preface: Before You Read This Book</div>
        <div class="toc-item">Introduction: The Gate Is Not Your Home</div>
        <div class="toc-item part">PART ONE — THE TRAP: WHEN STAYING PUT FEELS "SAFE"</div>
        <div class="toc-item">Chapter 1: The Gate Mentality</div>
        <div class="toc-item">Chapter 2: Name the Famine</div>
        <div class="toc-item">Chapter 3: When Rejection Becomes a Teacher</div>
        <div class="toc-item">Chapter 4: The Conversation That Changed Everything</div>
        <div class="toc-item part">PART TWO — THE MOVE: COURAGE, STRATEGY, AND WISE RISK</div>
        <div class="toc-item">Chapter 5: Faith That Walks</div>
        <div class="toc-item">Chapter 6: Risk Management for Believers</div>
        <div class="toc-item">Chapter 7: Night Moves: Winning When Nobody Claps</div>
        <div class="toc-item">Chapter 8: God Can Make the Enemy Hear Something</div>
        <div class="toc-item part">PART THREE — ABUNDANCE: WHAT YOU DO AFTER YOU "FIND THE CAMP"</div>
        <div class="toc-item">Chapter 9: The First Tent: Small Wins Matter</div>
        <div class="toc-item">Chapter 10: Stewardship: Don't Eat Your Future</div>
        <div class="toc-item">Chapter 11: The Sin of "Me Alone"</div>
        <div class="toc-item">Chapter 12: Credibility and Communication</div>
        <div class="toc-item part">PART FOUR — LEADERSHIP, SYSTEMS, AND SUSTAINABLE CHANGE</div>
        <div class="toc-item">Chapter 13: The Economy Can Turn Overnight</div>
        <div class="toc-item">Chapter 14: Unbelief Has Consequences</div>
        <div class="toc-item">Chapter 15: From Miracle to Model</div>
        <div class="toc-item">Chapter 16: Raise Movers: Legacy Leadership</div>
        <div class="toc-item">About the Author</div>
    </div>
    
    <!-- Main Content -->
    <div class="page content">
        ${paragraphs.map((para, idx) => {
          if (!para.trim()) return '';
          if (para.includes('Chapter') && !para.includes('Movement')) {
            return `<h1>${para}</h1>`;
          }
          if (para.includes('PART') || para.includes('PREFACE') || para.includes('Foreword')) {
            return `<h2>${para}</h2>`;
          }
          return `<p>${para}</p>`;
        }).join('\n')}
    </div>
    
    <!-- About the Author -->
    <div class="page about-author">
        <h1>ABOUT THE AUTHOR</h1>
        <p><strong>OLUSHOLA O. PAUL</strong> is the Lead Pastor of Ruach Apostolic Center in Lagos, Nigeria. He is a speaker, author, and leadership coach with a passion for helping individuals and organizations break through stagnation and move toward their God-given potential.</p>
        <p>With a background in both ministry and technology, Olushola brings a unique perspective to the integration of faith and function. He has worked with churches, businesses, and non-profits across Africa and beyond, helping leaders and teams navigate seasons of difficulty and discover breakthrough.</p>
        <p>His message is rooted in Scripture, tested in real life, and designed for practical application. He believes that the same God who saved the lepers at the gate is still making ways where there seem to be no ways.</p>
        <p>Olushola is married and is passionate about mentoring the next generation of leaders. When he is not writing or speaking, he enjoys technology, reading, and spending time with his family.</p>
    </div>
    
    <!-- Back Cover -->
    <div class="page back-cover">
        <p>When life is starving you—of joy, money, progress, peace—there is a question that exposes every excuse:</p>
        <h2>Why sit here and die?</h2>
        <p>In 2 Kings 7, four rejected lepers made one decision that saved a city: they moved. Their story is not just ancient history; it is a blueprint for spiritual renewal, career direction, academic excellence, leadership growth, and business breakthrough.</p>
        <p>This book will help you confront stagnation, take wise risks, build discipline, steward increase, and turn your testimony into impact—without denying reality and without losing faith.</p>
        <p class="author">By OLUSHOLA O. PAUL</p>
    </div>
</body>
</html>`;

  return html;
}

// Main execution
try {
  console.log('Extracting manuscript from DOCX...');
  const paragraphs = extractDocxText();
  console.log(`✓ Extracted ${paragraphs.length} paragraphs`);
  
  console.log('Creating HTML version...');
  const html = createHTML(paragraphs);
  fs.writeFileSync('book-complete.html', html, 'utf8');
  console.log('✓ HTML version created: book-complete.html');
  
  console.log('\nTo convert to PDF, use one of these methods:');
  console.log('1. Open book-complete.html in a browser and print to PDF');
  console.log('2. Use: npm install -g puppeteer && node convert-to-pdf.js');
  console.log('3. Use an online HTML to PDF converter');
  
} catch (err) {
  console.error('Error:', err.message);
  process.exit(1);
}
