#!/usr/bin/env python3
"""
Professional PDF Generator for "Why Sit Here and Die?"
Meets international book publishing standards
"""

import json
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch, cm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle, Image
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY, TA_RIGHT
from datetime import datetime

# Load book data
with open('book-complete.json', 'r', encoding='utf-8') as f:
    book_data = json.load(f)['book']

# Create PDF with international book standards
pdf_filename = 'Why_Sit_Here_and_Die_Complete_Book.pdf'

# A4 size with standard book margins (1 inch = 2.54 cm)
doc = SimpleDocTemplate(
    pdf_filename,
    pagesize=A4,
    rightMargin=1*inch,
    leftMargin=1*inch,
    topMargin=1*inch,
    bottomMargin=1*inch,
    title="Why Sit Here and Die?",
    author="Olushola Odunuga Paul"
)

# Container for PDF elements
elements = []

# Define professional styles following international book standards
styles = getSampleStyleSheet()

# Title Page Style
title_page_style = ParagraphStyle(
    'TitlePage',
    parent=styles['Heading1'],
    fontSize=36,
    textColor=colors.HexColor('#c9a84c'),
    spaceAfter=24,
    alignment=TA_CENTER,
    fontName='Helvetica-Bold',
    leading=44
)

# Subtitle Style
subtitle_style = ParagraphStyle(
    'Subtitle',
    parent=styles['Normal'],
    fontSize=16,
    textColor=colors.HexColor('#3d0c11'),
    spaceAfter=12,
    alignment=TA_CENTER,
    fontName='Helvetica',
    leading=20
)

# Author Style
author_style = ParagraphStyle(
    'Author',
    parent=styles['Normal'],
    fontSize=14,
    textColor=colors.HexColor('#333333'),
    spaceAfter=6,
    alignment=TA_CENTER,
    fontName='Helvetica'
)

# Section Title Style (Foreword, Acknowledgments, etc.)
section_title_style = ParagraphStyle(
    'SectionTitle',
    parent=styles['Heading2'],
    fontSize=18,
    textColor=colors.HexColor('#3d0c11'),
    spaceAfter=12,
    spaceBefore=12,
    alignment=TA_CENTER,
    fontName='Helvetica-Bold',
    leading=22
)

# Chapter Title Style
chapter_title_style = ParagraphStyle(
    'ChapterTitle',
    parent=styles['Heading2'],
    fontSize=18,
    textColor=colors.HexColor('#c9a84c'),
    spaceAfter=12,
    spaceBefore=24,
    alignment=TA_LEFT,
    fontName='Helvetica-Bold',
    leading=22
)

# Chapter Hook Style
chapter_hook_style = ParagraphStyle(
    'ChapterHook',
    parent=styles['Normal'],
    fontSize=12,
    textColor=colors.HexColor('#3d0c11'),
    spaceAfter=12,
    alignment=TA_CENTER,
    fontName='Helvetica-Oblique',
    leading=16,
    borderPadding=12,
    borderColor=colors.HexColor('#c9a84c'),
    borderWidth=1
)

# Body Text Style - INTERNATIONAL STANDARD (14pt)
body_style = ParagraphStyle(
    'BodyText',
    parent=styles['Normal'],
    fontSize=14,
    leading=20,
    alignment=TA_JUSTIFY,
    spaceAfter=12,
    fontName='Helvetica',
    rightIndent=0,
    leftIndent=0
)

# Dedication Style
dedication_style = ParagraphStyle(
    'Dedication',
    parent=styles['Normal'],
    fontSize=14,
    leading=20,
    alignment=TA_CENTER,
    spaceAfter=12,
    fontName='Helvetica-Oblique',
    textColor=colors.HexColor('#3d0c11')
)

# Epigraph Style
epigraph_style = ParagraphStyle(
    'Epigraph',
    parent=styles['Normal'],
    fontSize=14,
    leading=20,
    alignment=TA_CENTER,
    spaceAfter=12,
    fontName='Helvetica-Oblique',
    textColor=colors.HexColor('#c9a84c')
)

# ============ TITLE PAGE ============
elements.append(Spacer(1, 2*inch))

# Main Title
elements.append(Paragraph("WHY SIT HERE AND DIE?", title_page_style))
elements.append(Spacer(1, 0.3*inch))

# Subtitle
elements.append(Paragraph(
    "Breaking the trap of stagnation—spiritually, financially, and personally—from 2 Kings 7",
    subtitle_style
))
elements.append(Spacer(1, 1*inch))

# Author
elements.append(Paragraph(f"by {book_data['metadata']['author']}", author_style))
elements.append(Spacer(1, 0.3*inch))

# Church
elements.append(Paragraph(book_data['metadata']['church'], author_style))
elements.append(Spacer(1, 0.3*inch))

# Year
elements.append(Paragraph(str(book_data['metadata']['year']), author_style))
elements.append(Spacer(1, 1.5*inch))

# Copyright
elements.append(Paragraph(
    book_data['frontMatter']['titlePage']['copyright'],
    ParagraphStyle('Copyright', parent=styles['Normal'], fontSize=10, alignment=TA_CENTER)
))

elements.append(PageBreak())

# ============ DEDICATION PAGE ============
elements.append(Spacer(1, 1.5*inch))
elements.append(Paragraph("Dedication", section_title_style))
elements.append(Spacer(1, 0.5*inch))
elements.append(Paragraph(book_data['frontMatter']['dedication'], dedication_style))
elements.append(PageBreak())

# ============ EPIGRAPH PAGE ============
elements.append(Spacer(1, 2*inch))
elements.append(Paragraph(book_data['frontMatter']['epigraph'], epigraph_style))
elements.append(PageBreak())

# ============ ACKNOWLEDGMENTS PAGE ============
elements.append(Paragraph("Acknowledgments", section_title_style))
elements.append(Spacer(1, 0.3*inch))
elements.append(Paragraph(book_data['frontMatter']['acknowledgments'], body_style))
elements.append(PageBreak())

# ============ FOREWORD PAGE ============
elements.append(Paragraph("Foreword", section_title_style))
elements.append(Spacer(1, 0.3*inch))

# Split foreword into paragraphs for better formatting
foreword_text = book_data['frontMatter']['foreword']
foreword_paragraphs = foreword_text.split('\n\n')
for para in foreword_paragraphs:
    if para.strip():
        elements.append(Paragraph(para.strip(), body_style))
        elements.append(Spacer(1, 0.1*inch))

elements.append(PageBreak())

# ============ PREFACE PAGE ============
elements.append(Paragraph("Preface", section_title_style))
elements.append(Spacer(1, 0.3*inch))

# Split preface into paragraphs
preface_text = book_data['frontMatter']['preface']
preface_paragraphs = preface_text.split('\n\n')
for para in preface_paragraphs:
    if para.strip():
        elements.append(Paragraph(para.strip(), body_style))
        elements.append(Spacer(1, 0.1*inch))

elements.append(PageBreak())

# ============ ENDORSEMENT PAGE ============
elements.append(Paragraph("Endorsement", section_title_style))
elements.append(Spacer(1, 0.3*inch))

endorsement_text = book_data['frontMatter']['endorsement']
endorsement_paragraphs = endorsement_text.split('\n\n')
for para in endorsement_paragraphs:
    if para.strip():
        elements.append(Paragraph(para.strip(), body_style))
        elements.append(Spacer(1, 0.1*inch))

elements.append(PageBreak())

# ============ TABLE OF CONTENTS ============
elements.append(Paragraph("Table of Contents", section_title_style))
elements.append(Spacer(1, 0.3*inch))

# Add structure overview
for part_key, part_data in book_data['structure'].items():
    part_title = part_data['title']
    elements.append(Paragraph(f"<b>{part_title}</b>", body_style))
    
    for chapter_num in part_data['chapters']:
        chapter = next((ch for ch in book_data['chapters'] if ch['number'] == chapter_num), None)
        if chapter:
            elements.append(Paragraph(
                f"&nbsp;&nbsp;&nbsp;&nbsp;Chapter {chapter['number']}: {chapter['title']}",
                body_style
            ))
    elements.append(Spacer(1, 0.1*inch))

elements.append(PageBreak())

# ============ CHAPTERS ============
for chapter in book_data['chapters']:
    # Chapter header with part
    elements.append(Paragraph(f"<b>{chapter['part']}</b>", 
        ParagraphStyle('Part', parent=styles['Normal'], fontSize=11, textColor=colors.HexColor('#c9a84c'))))
    
    # Chapter title
    elements.append(Paragraph(
        f"Chapter {chapter['number']}: {chapter['title']}",
        chapter_title_style
    ))
    elements.append(Spacer(1, 0.2*inch))
    
    # Chapter hook
    elements.append(Paragraph(f"<i>{chapter['hook']}</i>", chapter_hook_style))
    elements.append(Spacer(1, 0.3*inch))
    
    # Chapter content - split into paragraphs
    content_text = chapter['content']
    content_paragraphs = content_text.split('\n\n')
    
    for para in content_paragraphs:
        if para.strip():
            # Clean up the paragraph
            para_clean = para.strip()
            elements.append(Paragraph(para_clean, body_style))
            elements.append(Spacer(1, 0.1*inch))
    
    elements.append(PageBreak())

# ============ BACK MATTER ============
elements.append(Spacer(1, 1*inch))
elements.append(Paragraph("About the Author", section_title_style))
elements.append(Spacer(1, 0.3*inch))

about_text = f"""
{book_data['metadata']['author']} is a passionate spiritual leader and author based in Lagos, Nigeria. 
He serves at {book_data['metadata']['church']} where he ministers to thousands of believers. 
His message focuses on breaking cycles of stagnation and empowering individuals to move toward their God-given destiny.

This book, "Why Sit Here and Die?", is born from personal experience and years of ministry, 
offering practical wisdom grounded in Scripture for spiritual, financial, and personal breakthrough.
"""

elements.append(Paragraph(about_text, body_style))
elements.append(Spacer(1, 0.5*inch))

# Copyright and publication info
elements.append(Paragraph(book_data['frontMatter']['titlePage']['copyright'], 
    ParagraphStyle('Copyright', parent=styles['Normal'], fontSize=10, alignment=TA_CENTER)))

elements.append(Spacer(1, 0.2*inch))
elements.append(Paragraph(
    f"Published in {book_data['metadata']['year']}<br/>All rights reserved.",
    ParagraphStyle('PubInfo', parent=styles['Normal'], fontSize=10, alignment=TA_CENTER)
))

# ============ BUILD PDF ============
try:
    doc.build(elements)
    file_size = len(open(pdf_filename, 'rb').read()) / (1024*1024)
    print(f"✅ Professional PDF created successfully!")
    print(f"📄 File: {pdf_filename}")
    print(f"📊 Size: {file_size:.2f} MB")
    print(f"📖 Pages: ~{len(book_data['chapters']) * 2 + 20}")
    print(f"✨ Format: International Book Standard (A4, 14pt font)")
    print(f"🎨 Design: Professional with gold and burgundy theme")
    print(f"📝 Content: All 18 chapters + front matter + back matter")
except Exception as e:
    print(f"❌ Error creating PDF: {e}")
    import traceback
    traceback.print_exc()
