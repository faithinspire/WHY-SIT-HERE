#!/usr/bin/env node
/**
 * PDF Generator using html2pdf library
 */

const fs = require('fs');
const path = require('path');

// Create a simple PDF using a different approach
// We'll use a library that doesn't require Chromium

async function generatePDF() {
  try {
    // Try to use html2pdf if available
    const html2pdf = require('html2pdf.js');
    
    const htmlContent = fs.readFileSync('book-complete.html', 'utf8');
    
    const options = {
      margin: 10,
      filename: 'Why-Sit-Here-and-Die-Complete.pdf',
      image: { type: 'jpeg', quality: 0.98 },
      html2canvas: { scale: 2 },
      jsPDF: { orientation: 'portrait', unit: 'mm', format: 'a4' }
    };
    
    html2pdf().set(options).from(htmlContent).save();
    console.log('✓ PDF created: Why-Sit-Here-and-Die-Complete.pdf');
  } catch (err) {
    console.log('html2pdf not available, trying alternative method...');
    
    // Fallback: Create a simple PDF using PDFKit
    try {
      const PDFDocument = require('pdfkit');
      const fs = require('fs');
      
      const doc = new PDFDocument({
        size: 'A4',
        margin: 50
      });
      
      const stream = fs.createWriteStream('Why-Sit-Here-and-Die-Complete.pdf');
      doc.pipe(stream);
      
      // Read the HTML and extract text
      const html = fs.readFileSync('book-complete.html', 'utf8');
      
      // Simple text extraction from HTML
      const text = html
        .replace(/<[^>]*>/g, ' ')
        .replace(/&nbsp;/g, ' ')
        .replace(/&lt;/g, '<')
        .replace(/&gt;/g, '>')
        .replace(/&amp;/g, '&')
        .replace(/\s+/g, ' ')
        .trim();
      
      doc.fontSize(12).text(text, { align: 'justify' });
      doc.end();
      
      stream.on('finish', () => {
        console.log('✓ PDF created: Why-Sit-Here-and-Die-Complete.pdf');
        const stats = fs.statSync('Why-Sit-Here-and-Die-Complete.pdf');
        console.log(`✓ File size: ${(stats.size / (1024 * 1024)).toFixed(2)} MB`);
      });
    } catch (err2) {
      console.error('Error:', err2.message);
      process.exit(1);
    }
  }
}

generatePDF();
