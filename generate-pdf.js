const PDFDocument = require('pdfkit');
const fs = require('fs');
const path = require('path');
const zlib = require('zlib');

// Extract text from DOCX
function extractDocxText() {
  const docxPath = 'WHY SIT HERE AND DIE.docx';
  const buf = fs.readFileSync(docxPath);

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

// Create professional PDF
function createPDF() {
  console.log('Extracting manuscript...');
  const paragraphs = extractDocxText();
  console.log(`Extracted ${paragraphs.length} paragraphs`);

  const doc = new PDFDocument({
    size: 'A4',
    margin: 50,
    bufferPages: true
  });

  const filename = 'Why-Sit-Here-and-Die-Complete.pdf';
  const stream = fs.createWriteStream(filename);
  doc.pipe(stream);

  // Colors
  const goldColor = '#D4AF37';
  const darkColor = '#2C3E50';
  const lightColor = '#ECF0F1';

  // Helper functions
  function addPageNumber() {
    const pages = doc.bufferedPageRange().count;
    for (let i = 0; i < pages; i++) {
      doc.switchToPage(i);
      doc.fontSize(10).fillColor('#999999');
      doc.text(String(i + 1), 50, doc.page.height - 40, { align: 'center' });
    }
  }

  function newPage() {
    doc.addPage();
  }

  // Front Cover
  doc.fillColor(darkColor).rect(0, 0, doc.page.width, doc.page.height).fill();
  
  // Add book cover image if available
  try {
    doc.image('book-cover.jpg', 100, 80, { width: 300, height: 400 });
  } catch (e) {
    console.log('Book cover image not found, skipping');
  }

  doc.fontSize(28).fillColor(goldColor).font('Helvetica-Bold');
  doc.text('WHY SIT HERE AND DIE?', 50, 520, { width: 500, align: 'center' });
  
  doc.fontSize(14).fillColor(lightColor).font('Helvetica');
  doc.text('Breaking the trap of stagnation', 50, 560, { width: 500, align: 'center' });
  doc.text('spiritually, financially, and personally', 50, 580, { width: 500, align: 'center' });
  
  doc.fontSize(12).fillColor(goldColor).font('Helvetica-Oblique');
  doc.text('from 2 Kings 7', 50, 620, { width: 500, align: 'center' });

  doc.fontSize(14).fillColor(lightColor).font('Helvetica');
  doc.text('By OLUSHOLA O. PAUL', 50, 680, { width: 500, align: 'center' });

  // Title Page
  newPage();
  doc.fillColor(darkColor);
  doc.fontSize(32).font('Helvetica-Bold').fillColor(goldColor);
  doc.text('WHY SIT HERE AND DIE?', 50, 100, { width: 500, align: 'center' });
  
  doc.fontSize(16).fillColor(darkColor).font('Helvetica');
  doc.text('Breaking the trap of stagnation—spiritually, financially, and personally—from 2 Kings 7', 50, 180, { width: 500, align: 'center' });
  
  doc.fontSize(14).font('Helvetica-Bold').fillColor(goldColor);
  doc.text('By OLUSHOLA O. PAUL', 50, 280, { width: 500, align: 'center' });

  // Copyright Page
  newPage();
  doc.fontSize(10).fillColor(darkColor).font('Helvetica');
  doc.text('WHY SIT HERE AND DIE?', 50, 100);
  doc.text('Breaking the trap of stagnation—spiritually, financially, and personally—from 2 Kings 7', 50, 120);
  
  doc.text('', 50, 160);
  doc.text('Copyright © 2026 by OLUSHOLA O PAUL', 50, 180);
  doc.text('All rights reserved. No part of this book may be reproduced or transmitted in any form or by any means without written permission from the publisher, except for brief quotations in reviews.', 50, 200, { width: 500 });
  
  doc.text('', 50, 260);
  doc.text('Scripture quotations marked KJV are from the King James Version, public domain.', 50, 280, { width: 500 });
  
  doc.text('', 50, 320);
  doc.text('Disclaimer: This book provides spiritual and practical principles. It does not replace professional medical, legal, financial, or psychological advice.', 50, 340, { width: 500 });

  // Table of Contents
  newPage();
  doc.fontSize(18).font('Helvetica-Bold').fillColor(goldColor);
  doc.text('TABLE OF CONTENTS', 50, 50);
  
  doc.fontSize(11).fillColor(darkColor).font('Helvetica');
  const toc = [
    'Foreword',
    'Acknowledgments',
    'Preface: Before You Read This Book',
    'Introduction: The Gate Is Not Your Home',
    '',
    'PART ONE — THE TRAP: WHEN STAYING PUT FEELS "SAFE"',
    'Chapter 1: The Gate Mentality',
    'Chapter 2: Name the Famine',
    'Chapter 3: When Rejection Becomes a Teacher',
    'Chapter 4: The Conversation That Changed Everything',
    '',
    'PART TWO — THE MOVE: COURAGE, STRATEGY, AND WISE RISK',
    'Chapter 5: Faith That Walks',
    'Chapter 6: Risk Management for Believers',
    'Chapter 7: Night Moves: Winning When Nobody Claps',
    'Chapter 8: God Can Make the Enemy Hear Something',
    '',
    'PART THREE — ABUNDANCE: WHAT YOU DO AFTER YOU "FIND THE CAMP"',
    'Chapter 9: The First Tent: Small Wins Matter',
    'Chapter 10: Stewardship: Don\'t Eat Your Future',
    'Chapter 11: The Sin of "Me Alone"',
    'Chapter 12: Credibility and Communication',
    '',
    'PART FOUR — LEADERSHIP, SYSTEMS, AND SUSTAINABLE CHANGE',
    'Chapter 13: The Economy Can Turn Overnight',
    'Chapter 14: Unbelief Has Consequences',
    'Chapter 15: From Miracle to Model',
    'Chapter 16: Raise Movers: Legacy Leadership',
    '',
    'About the Author'
  ];

  let y = 100;
  for (const item of toc) {
    if (item === '') {
      y += 8;
    } else if (item.includes('PART')) {
      doc.fontSize(10).font('Helvetica-Bold').fillColor(goldColor);
      doc.text(item, 50, y);
      y += 18;
    } else {
      doc.fontSize(10).font('Helvetica').fillColor(darkColor);
      doc.text(item, 70, y);
      y += 14;
    }
  }

  // Main Content - Process all paragraphs
  newPage();
  doc.fontSize(12).fillColor(darkColor).font('Helvetica');
  
  let currentY = 50;
  const pageHeight = doc.page.height;
  const bottomMargin = 50;

  for (let i = 0; i < paragraphs.length; i++) {
    const para = paragraphs[i];
    
    // Check if we need a new page
    if (currentY > pageHeight - bottomMargin - 40) {
      newPage();
      currentY = 50;
    }

    // Format based on content
    if (para.includes('Chapter') && !para.includes('Movement')) {
      doc.fontSize(16).font('Helvetica-Bold').fillColor(goldColor);
      doc.text(para, 50, currentY, { width: 500 });
      currentY += 30;
    } else if (para.includes('PART') || para.includes('PREFACE') || para.includes('Foreword')) {
      doc.fontSize(14).font('Helvetica-Bold').fillColor(goldColor);
      doc.text(para, 50, currentY, { width: 500 });
      currentY += 25;
    } else if (para.length > 200) {
      doc.fontSize(11).font('Helvetica').fillColor(darkColor);
      const height = doc.heightOfString(para, { width: 500 });
      doc.text(para, 50, currentY, { width: 500, align: 'justify' });
      currentY += height + 12;
    } else if (para.trim()) {
      doc.fontSize(11).font('Helvetica').fillColor(darkColor);
      doc.text(para, 50, currentY, { width: 500 });
      currentY += 16;
    } else {
      currentY += 8;
    }
  }

  // About the Author Page
  newPage();
  doc.fontSize(18).font('Helvetica-Bold').fillColor(goldColor);
  doc.text('ABOUT THE AUTHOR', 50, 50);
  
  // Add author photo if available
  try {
    doc.image('author.jpg', 50, 100, { width: 150, height: 150 });
  } catch (e) {
    console.log('Author image not found, skipping');
  }

  doc.fontSize(12).fillColor(darkColor).font('Helvetica');
  const aboutText = `OLUSHOLA O. PAUL is the Lead Pastor of Ruach Apostolic Center in Lagos, Nigeria. He is a speaker, author, and leadership coach with a passion for helping individuals and organizations break through stagnation and move toward their God-given potential.

With a background in both ministry and technology, Olushola brings a unique perspective to the integration of faith and function. He has worked with churches, businesses, and non-profits across Africa and beyond, helping leaders and teams navigate seasons of difficulty and discover breakthrough.

His message is rooted in Scripture, tested in real life, and designed for practical application. He believes that the same God who saved the lepers at the gate is still making ways where there seem to be no ways.

Olushola is married and is passionate about mentoring the next generation of leaders. When he is not writing or speaking, he enjoys technology, reading, and spending time with his family.

Connect with Olushola:
Website: [Your Website]
Email: [Your Email]
Social Media: @olushola.paul`;

  doc.text(aboutText, 220, 100, { width: 300, align: 'left' });

  // Back Cover
  newPage();
  doc.fillColor(darkColor).rect(0, 0, doc.page.width, doc.page.height).fill();
  
  doc.fontSize(14).fillColor(lightColor).font('Helvetica');
  doc.text('When life is starving you—of joy, money, progress, peace—there is a question that exposes every excuse:', 50, 100, { width: 500, align: 'center' });
  
  doc.fontSize(20).fillColor(goldColor).font('Helvetica-Bold');
  doc.text('Why sit here and die?', 50, 180, { width: 500, align: 'center' });
  
  doc.fontSize(12).fillColor(lightColor).font('Helvetica');
  doc.text('In 2 Kings 7, four rejected lepers made one decision that saved a city: they moved. Their story is not just ancient history; it is a blueprint for spiritual renewal, career direction, academic excellence, leadership growth, and business breakthrough.', 50, 260, { width: 500, align: 'center' });
  
  doc.text('This book will help you confront stagnation, take wise risks, build discipline, steward increase, and turn your testimony into impact—without denying reality and without losing faith.', 50, 360, { width: 500, align: 'center' });
  
  doc.fontSize(11).fillColor(goldColor).font('Helvetica-Bold');
  doc.text('By OLUSHOLA O. PAUL', 50, 480, { width: 500, align: 'center' });

  // Add page numbers to all pages
  addPageNumber();

  // Finalize
  doc.end();

  stream.on('finish', () => {
    console.log(`✓ PDF created successfully: ${filename}`);
    console.log(`✓ Total pages: ${doc.bufferedPageRange().count}`);
  });

  stream.on('error', (err) => {
    console.error('Error creating PDF:', err);
  });
}

// Run
try {
  createPDF();
} catch (err) {
  console.error('Error:', err.message);
  process.exit(1);
}
