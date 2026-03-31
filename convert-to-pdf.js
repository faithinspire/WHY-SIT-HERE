#!/usr/bin/env node
/**
 * Convert HTML to PDF using Puppeteer
 */

const puppeteer = require('puppeteer');
const fs = require('fs');
const path = require('path');

async function convertToPDF() {
  let browser;
  try {
    console.log('Launching browser...');
    browser = await puppeteer.launch({
      headless: 'new',
      args: ['--no-sandbox', '--disable-setuid-sandbox']
    });

    console.log('Opening HTML file...');
    const htmlPath = path.resolve('book-complete.html');
    const fileUrl = `file://${htmlPath}`;

    const page = await browser.newPage();
    
    // Set viewport for better rendering
    await page.setViewport({ width: 1200, height: 1600 });
    
    console.log('Loading page...');
    await page.goto(fileUrl, { waitUntil: 'networkidle0', timeout: 60000 });

    console.log('Generating PDF...');
    await page.pdf({
      path: 'Why-Sit-Here-and-Die-Complete.pdf',
      format: 'A4',
      margin: {
        top: '0.5in',
        right: '0.5in',
        bottom: '0.5in',
        left: '0.5in'
      },
      printBackground: true,
      displayHeaderFooter: true,
      headerTemplate: '<div></div>',
      footerTemplate: '<div style="width: 100%; text-align: center; font-size: 10px; color: #999;">Page <span class="pageNumber"></span> of <span class="totalPages"></span></div>',
      scale: 1
    });

    console.log('✓ PDF created successfully: Why-Sit-Here-and-Die-Complete.pdf');
    
    // Get file size
    const stats = fs.statSync('Why-Sit-Here-and-Die-Complete.pdf');
    console.log(`✓ File size: ${(stats.size / (1024 * 1024)).toFixed(2)} MB`);
    
    await browser.close();
    process.exit(0);
  } catch (err) {
    console.error('Error:', err.message);
    if (browser) await browser.close();
    process.exit(1);
  }
}

convertToPDF();
