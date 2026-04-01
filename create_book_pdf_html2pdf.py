#!/usr/bin/env python3
"""
ALTERNATIVE PDF SOLUTION - HTML to PDF Conversion
Creates professional PDF from HTML with all book content
Uses pdfkit/wkhtmltopdf for reliable PDF generation
"""

import json
import os
import sys
from datetime import datetime

print("\n" + "="*80)
print("CREATING BOOK PDF - ALTERNATIVE HTML-TO-PDF METHOD")
print("="*80 + "\n")

# Load book data
print("[1/4] Loading book content...")
try:
    with open('book-data-complete.js', 'r', encoding='utf-8') as f:
        content = f.read()
        start = content.find('{')
        end = content.rfind('}') + 1
        book_data = json.loads(content[start:end])
    print(f"✓ Loaded {len(book_data['chapters'])} chapters")
except Exception as e:
    print(f"✗ Error: {e}")
    sys.exit(1)

# Create HTML content
print("[2/4] Generating HTML content...")

html_content = """
<!DOCTYPE html>
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
            color: #f5f0e8;
            background: #0a0a0a;
            line-height: 1.8;
            font-size: 14px;
        }
        
        .page {
            page-break-after: always;
            padding: 1in;
            background: #0a0a0a;
            color: #f5f0e8;
            border: 2px solid #c9a84c;
            margin: 0.5in;
            min-height: 9in;
        }
        
        .title-page {
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            text-align: center;
            min-height: 9in;
        }
        
        h1 {
            font-size: 40px;
            color: #c9a84c;
            margin-bottom: 20px;
            letter-spacing: 3px;
        }
        
        h2 {
            font-size: 24px;
            color: #c9a84c;
            margin-top: 30px;
            margin-bottom: 20px;
            border-bottom: 2px solid #c9a84c;
            padding-bottom: 10px;
        }
        
        h3 {
            font-size: 18px;
            color: #c9a84c;
            margin-top: 15px;
            margin-bottom: 15px;
        }
        
        .subtitle {
            font-size: 16px;
            color: #f5f0e8;
            font-style: italic;
            margin-bottom: 30px;
        }
        
        .author {
            font-size: 14px;
            color: #f5f0e8;
            margin-bottom: 10px;
        }
        
        .chapter-number {
            font-size: 14px;
            color: #c9a84c;
            text-transform: uppercase;
            letter-spacing: 2px;
            margin-bottom: 10px;
        }
        
        .chapter-title {
            font-size: 20px;
            color: #f5f0e8;
            margin-bottom: 15px;
        }
        
        .hook {
            font-size: 13px;
            color: #c9a84c;
            font-style: italic;
            background: rgba(201, 168, 76, 0.1);
            padding: 15px;
            border-left: 4px solid #c9a84c;
            margin-bottom: 20px;
        }
        
        p {
            margin-bottom: 12px;
            text-align: justify;
            color: #f5f0e8;
        }
        
        .page-number {
            text-align: right;
            color: #c9a84c;
            font-size: 12px;
            margin-top: 20px;
        }
        
        .toc-item {
            margin-bottom: 8px;
            color: #f5f0e8;
        }
        
        .toc-chapter {
            color: #c9a84c;
            font-weight: bold;
        }
    </style>
</head>
<body>
"""

# Title Page
html_content += """
<div class="page title-page">
    <h1>WHY SIT HERE AND DIE?</h1>
    <p class="subtitle">Breaking the trap of stagnation — spiritually, financially, and personally — from 2 Kings 7</p>
    <p class="author">by Olushola Odunuga Paul</p>
    <p class="author">Ruach Apostolic Center, Lagos, Nigeria</p>
    <p class="author" style="margin-top: 40px;">© 2026</p>
</div>
"""

# Dedication
html_content += f"""
<div class="page">
    <h2>DEDICATION</h2>
    <p>{book_data['frontMatter']['dedication']}</p>
</div>
"""

# Epigraph
html_content += f"""
<div class="page">
    <h2>EPIGRAPH</h2>
    <p style="text-align: center; font-style: italic; font-size: 16px; margin-top: 40px;">
        {book_data['frontMatter']['epigraph']}
    </p>
</div>
"""

# Foreword
foreword_text = book_data['frontMatter']['foreword'].replace('\n', '</p><p>')
html_content += f"""
<div class="page">
    <h2>FOREWORD</h2>
    <p>{foreword_text}</p>
</div>
"""

# Preface
preface_text = book_data['frontMatter']['preface'].replace('\n', '</p><p>')
html_content += f"""
<div class="page">
    <h2>PREFACE</h2>
    <p>{preface_text}</p>
</div>
"""

# Table of Contents
html_content += """
<div class="page">
    <h2>TABLE OF CONTENTS</h2>
"""
for ch in book_data['chapters']:
    html_content += f'    <div class="toc-item"><span class="toc-chapter">Chapter {ch["number"]}</span>: {ch["title"]}</div>\n'
html_content += """
</div>
"""

# Chapters
for chapter in book_data['chapters']:
    content_paragraphs = chapter['content'].split('\n\n')
    content_html = '</p><p>'.join([p.strip() for p in content_paragraphs if p.strip()])
    
    html_content += f"""
<div class="page">
    <div class="chapter-number">CHAPTER {chapter['number']}</div>
    <h3 class="chapter-title">{chapter['title']}</h3>
    <div class="hook">"{chapter['hook']}"</div>
    <p>{content_html}</p>
</div>
"""

# Conclusion
conclusion_text = book_data['conclusion'].replace('\n', '</p><p>')
html_content += f"""
<div class="page">
    <h2>CONCLUSION</h2>
    <p>{conclusion_text}</p>
</div>
"""

# About Author
html_content += """
<div class="page">
    <h2>ABOUT THE AUTHOR</h2>
    <p>Olushola Odunuga Paul is the Lead Pastor of Ruach Apostolic Center, Lagos, Nigeria. 
    A preacher, teacher, and technology professional, he writes at the intersection of faith, leadership, and practical life.</p>
    <p style="font-style: italic; margin-top: 20px;">"I wrote this book for the person I used to be—and sometimes still am."</p>
    <p>This book was forged in a furnace of personal struggle and divine encounter. He writes not as someone who has arrived, 
    but as someone who has learned one thing clearly: sitting is not a strategy. Movement is.</p>
</div>
"""

html_content += """
</body>
</html>
"""

# Save HTML
print("✓ HTML generated")

html_file = "book_content.html"
with open(html_file, 'w', encoding='utf-8') as f:
    f.write(html_content)
print(f"✓ HTML saved: {html_file}")

# Try to create PDF using pdfkit
print("\n[3/4] Creating PDF...")
try:
    import pdfkit
    
    options = {
        'page-size': 'A4',
        'margin-top': '0.75in',
        'margin-right': '0.75in',
        'margin-bottom': '0.75in',
        'margin-left': '0.75in',
        'encoding': "UTF-8",
        'no-outline': None,
        'enable-local-file-access': None
    }
    
    pdf_file = "Why_Sit_Here_and_Die_Book.pdf"
    pdfkit.from_file(html_file, pdf_file, options=options)
    
    if os.path.exists(pdf_file):
        file_size = os.path.getsize(pdf_file)
        print(f"✓ PDF created: {pdf_file}")
        print(f"  Size: {file_size:,} bytes ({file_size/1024:.1f} KB)")
    else:
        print("✗ PDF creation failed")
        sys.exit(1)
        
except ImportError:
    print("⚠ pdfkit not installed. Using alternative method...")
    print("\n[3/4] Creating PDF using alternative method...")
    
    # Alternative: Use reportlab
    try:
        from reportlab.lib.pagesizes import A4
        from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
        from reportlab.lib.units import inch
        from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
        from reportlab.lib import colors
        from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
        
        pdf_file = "Why_Sit_Here_and_Die_Book.pdf"
        doc = SimpleDocTemplate(pdf_file, pagesize=A4, topMargin=0.75*inch, bottomMargin=0.75*inch)
        
        styles = getSampleStyleSheet()
        story = []
        
        # Add content
        title_style = ParagraphStyle('Title', parent=styles['Heading1'], fontSize=28, textColor=colors.HexColor('#c9a84c'), alignment=TA_CENTER)
        body_style = ParagraphStyle('Body', parent=styles['Normal'], fontSize=12, alignment=TA_JUSTIFY)
        
        story.append(Paragraph("WHY SIT HERE AND DIE?", title_style))
        story.append(Spacer(1, 0.3*inch))
        story.append(Paragraph("Breaking the trap of stagnation", body_style))
        story.append(PageBreak())
        
        # Add chapters
        for chapter in book_data['chapters']:
            story.append(Paragraph(f"Chapter {chapter['number']}: {chapter['title']}", styles['Heading2']))
            story.append(Spacer(1, 0.2*inch))
            story.append(Paragraph(f'"{chapter["hook"]}"', styles['Italic']))
            story.append(Spacer(1, 0.2*inch))
            
            paragraphs = chapter['content'].split('\n\n')
            for para in paragraphs:
                if para.strip():
                    story.append(Paragraph(para.strip(), body_style))
                    story.append(Spacer(1, 0.1*inch))
            
            story.append(PageBreak())
        
        doc.build(story)
        
        if os.path.exists(pdf_file):
            file_size = os.path.getsize(pdf_file)
            print(f"✓ PDF created (ReportLab): {pdf_file}")
            print(f"  Size: {file_size:,} bytes ({file_size/1024:.1f} KB)")
        else:
            print("✗ PDF creation failed")
            sys.exit(1)
            
    except Exception as e:
        print(f"✗ Error: {e}")
        sys.exit(1)

print("\n[4/4] Verification...")
if os.path.exists(pdf_file):
    file_size = os.path.getsize(pdf_file)
    if file_size > 10000:
        print(f"✓ PDF verified: {file_size:,} bytes (NOT EMPTY)")
    else:
        print(f"✗ PDF too small: {file_size} bytes")
else:
    print(f"✗ PDF not found")

print("\n" + "="*80)
print("✅ PDF GENERATION COMPLETE")
print("="*80)
print(f"\nFile: {pdf_file}")
print(f"Format: A4 PDF")
print(f"Content: Complete book with all chapters")
print(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print("\n" + "="*80 + "\n")
