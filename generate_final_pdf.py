#!/usr/bin/env python3
"""
FINAL PDF GENERATOR - Professional Book with Complete Design
Generates "Why Sit Here and Die?" with all chapters properly designed
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch, cm, pt
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle, Image, KeepTogether
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT, TA_RIGHT
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from datetime import datetime
import json
import sys
import os

print("\n" + "="*80)
print("GENERATING FINAL PROFESSIONAL PDF - COMPLETE BOOK WITH DESIGN")
print("="*80 + "\n")

# Load book data
print("[1/6] Loading book content...")
try:
    with open('book-data-complete.js', 'r', encoding='utf-8') as f:
        content = f.read()
        start = content.find('{')
        end = content.rfind('}') + 1
        book_data = json.loads(content[start:end])
    print(f"✓ Loaded: {len(book_data['chapters'])} chapters")
except Exception as e:
    print(f"✗ Error: {e}")
    sys.exit(1)

# PDF Configuration
PDF_FILE = "Why_Sit_Here_and_Die_Final.pdf"
PAGE_WIDTH, PAGE_HEIGHT = A4
MARGIN = 0.7 * inch

# Colors
GOLD = colors.HexColor('#c9a84c')
BLACK = colors.HexColor('#0a0a0a')
CREAM = colors.HexColor('#f5f0e8')
DARK_BG = colors.HexColor('#1a1a1a')
BURGUNDY = colors.HexColor('#3d0c11')

print("[2/6] Creating PDF document...")

# Custom canvas with professional design
class ProfessionalCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        canvas.Canvas.__init__(self, *args, **kwargs)
        self.page_num = 0

    def showPage(self):
        self.page_num += 1
        
        # Black background
        self.setFillColor(BLACK)
        self.rect(0, 0, PAGE_WIDTH, PAGE_HEIGHT, fill=1, stroke=0)
        
        # Decorative border
        self.setStrokeColor(GOLD)
        self.setLineWidth(2)
        self.rect(0.5*inch, 0.5*inch, PAGE_WIDTH - inch, PAGE_HEIGHT - inch, fill=0, stroke=1)
        
        # Corner decorations
        corner_size = 0.15*inch
        self.setFillColor(GOLD)
        # Top left
        self.rect(0.5*inch, PAGE_HEIGHT - 0.5*inch - corner_size, corner_size, corner_size, fill=1)
        # Top right
        self.rect(PAGE_WIDTH - 0.5*inch - corner_size, PAGE_HEIGHT - 0.5*inch - corner_size, corner_size, corner_size, fill=1)
        # Bottom left
        self.rect(0.5*inch, 0.5*inch, corner_size, corner_size, fill=1)
        # Bottom right
        self.rect(PAGE_WIDTH - 0.5*inch - corner_size, 0.5*inch, corner_size, corner_size, fill=1)
        
        # Page number
        self.setFont("Helvetica", 10)
        self.setFillColor(GOLD)
        self.drawString(PAGE_WIDTH - 1*inch, 0.6*inch, str(self.page_num))
        
        canvas.Canvas.showPage(self)

# Create PDF
doc = SimpleDocTemplate(
    PDF_FILE,
    pagesize=A4,
    rightMargin=MARGIN,
    leftMargin=MARGIN,
    topMargin=MARGIN,
    bottomMargin=MARGIN,
    title="Why Sit Here and Die?",
    author="Olushola Odunuga Paul",
    subject="A life-and-leadership wake-up call from 2 Kings 7",
    creator="Ruach Apostolic Center"
)

# Define Styles
styles = getSampleStyleSheet()

# Title Style
title_style = ParagraphStyle(
    'Title',
    parent=styles['Heading1'],
    fontSize=40,
    textColor=GOLD,
    spaceAfter=12,
    alignment=TA_CENTER,
    fontName='Helvetica-Bold',
    letterSpacing=3
)

# Subtitle Style
subtitle_style = ParagraphStyle(
    'Subtitle',
    parent=styles['Normal'],
    fontSize=14,
    textColor=CREAM,
    spaceAfter=8,
    alignment=TA_CENTER,
    fontName='Helvetica-Oblique',
    leading=18
)

# Chapter Title Style
chapter_title_style = ParagraphStyle(
    'ChapterTitle',
    parent=styles['Heading2'],
    fontSize=22,
    textColor=GOLD,
    spaceAfter=12,
    spaceBefore=12,
    fontName='Helvetica-Bold',
    letterSpacing=1
)

# Chapter Subtitle
chapter_subtitle_style = ParagraphStyle(
    'ChapterSubtitle',
    parent=styles['Normal'],
    fontSize=16,
    textColor=CREAM,
    spaceAfter=12,
    fontName='Helvetica-Bold'
)

# Body Text Style
body_style = ParagraphStyle(
    'Body',
    parent=styles['Normal'],
    fontSize=12,
    textColor=CREAM,
    spaceAfter=12,
    alignment=TA_JUSTIFY,
    fontName='Helvetica',
    leading=20,
    leftIndent=0.3*inch,
    rightIndent=0.3*inch
)

# Hook/Quote Style
hook_style = ParagraphStyle(
    'Hook',
    parent=styles['Normal'],
    fontSize=12,
    textColor=GOLD,
    spaceAfter=12,
    alignment=TA_CENTER,
    fontName='Helvetica-Oblique',
    leading=18,
    leftIndent=0.5*inch,
    rightIndent=0.5*inch
)

# Author Style
author_style = ParagraphStyle(
    'Author',
    parent=styles['Normal'],
    fontSize=11,
    textColor=CREAM,
    spaceAfter=6,
    alignment=TA_CENTER,
    fontName='Helvetica'
)

print("✓ PDF document created")

# Build content
print("[3/6] Building PDF content...")
story = []

# ===== TITLE PAGE =====
story.append(Spacer(1, 2.5*inch))
story.append(Paragraph("WHY SIT HERE AND DIE?", title_style))
story.append(Spacer(1, 0.4*inch))
story.append(Paragraph(book_data['metadata']['subtitle'], subtitle_style))
story.append(Spacer(1, 1*inch))
story.append(Paragraph(f"by {book_data['metadata']['author']}", author_style))
story.append(Spacer(1, 0.3*inch))
story.append(Paragraph(book_data['metadata']['church'], author_style))
story.append(Spacer(1, 1.5*inch))
story.append(Paragraph(f"© {book_data['metadata']['year']}", author_style))
story.append(PageBreak())

# ===== DEDICATION =====
story.append(Spacer(1, 1*inch))
story.append(Paragraph("DEDICATION", chapter_title_style))
story.append(Spacer(1, 0.5*inch))
story.append(Paragraph(book_data['frontMatter']['dedication'], body_style))
story.append(PageBreak())

# ===== EPIGRAPH =====
story.append(Spacer(1, 1.5*inch))
story.append(Paragraph("EPIGRAPH", chapter_title_style))
story.append(Spacer(1, 0.8*inch))
story.append(Paragraph(book_data['frontMatter']['epigraph'], hook_style))
story.append(PageBreak())

# ===== FOREWORD =====
story.append(Paragraph("FOREWORD", chapter_title_style))
story.append(Spacer(1, 0.4*inch))
foreword_text = book_data['frontMatter']['foreword'].replace('\n', ' ')
story.append(Paragraph(foreword_text, body_style))
story.append(PageBreak())

# ===== PREFACE =====
story.append(Paragraph("PREFACE", chapter_title_style))
story.append(Spacer(1, 0.4*inch))
preface_text = book_data['frontMatter'].get('preface', 'Preface content').replace('\n', ' ')
story.append(Paragraph(preface_text, body_style))
story.append(PageBreak())

# ===== TABLE OF CONTENTS =====
story.append(Paragraph("TABLE OF CONTENTS", chapter_title_style))
story.append(Spacer(1, 0.4*inch))

toc_data = [['Chapter', 'Title']]
for ch in book_data['chapters']:
    toc_data.append([f"Ch {ch['number']}", ch['title']])

toc_table = Table(toc_data, colWidths=[1.2*inch, 3.8*inch])
toc_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), GOLD),
    ('TEXTCOLOR', (0, 0), (-1, 0), BLACK),
    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, 0), 11),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 10),
    ('BACKGROUND', (0, 1), (-1, -1), DARK_BG),
    ('TEXTCOLOR', (0, 1), (-1, -1), CREAM),
    ('GRID', (0, 0), (-1, -1), 1, GOLD),
    ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
    ('FONTSIZE', (0, 1), (-1, -1), 10),
    ('ROWBACKGROUNDS', (0, 1), (-1, -1), [DARK_BG, colors.HexColor('#252525')]),
]))
story.append(toc_table)
story.append(PageBreak())

# ===== CHAPTERS - FULL DESIGN =====
print("[4/6] Adding chapters with professional design...")
for chapter in book_data['chapters']:
    # Chapter header with design
    story.append(Spacer(1, 0.5*inch))
    
    # Chapter number and title
    story.append(Paragraph(f"CHAPTER {chapter['number']}", chapter_title_style))
    story.append(Spacer(1, 0.2*inch))
    story.append(Paragraph(chapter['title'], chapter_subtitle_style))
    story.append(Spacer(1, 0.3*inch))
    
    # Decorative line
    story.append(Spacer(1, 0.1*inch))
    
    # Hook/Opening quote
    hook_text = f'"{chapter["hook"]}"'
    story.append(Paragraph(hook_text, hook_style))
    story.append(Spacer(1, 0.4*inch))
    
    # Chapter content - FULL TEXT
    content_text = chapter['content']
    if content_text:
        # Split into paragraphs
        paragraphs = content_text.split('\n\n')
        for para in paragraphs:
            if para.strip():
                clean_para = para.strip().replace('\n', ' ')
                story.append(Paragraph(clean_para, body_style))
                story.append(Spacer(1, 0.15*inch))
    
    story.append(PageBreak())
    print(f"  ✓ Chapter {chapter['number']}: {chapter['title']}")

# ===== CONCLUSION =====
print("[5/6] Adding conclusion and back matter...")
story.append(Spacer(1, 0.5*inch))
story.append(Paragraph("CONCLUSION", chapter_title_style))
story.append(Spacer(1, 0.4*inch))
conclusion_text = book_data['conclusion'].replace('\n', ' ')
story.append(Paragraph(conclusion_text, body_style))
story.append(PageBreak())

# ===== ABOUT THE AUTHOR =====
story.append(Spacer(1, 0.5*inch))
story.append(Paragraph("ABOUT THE AUTHOR", chapter_title_style))
story.append(Spacer(1, 0.4*inch))
about_text = f"""
{book_data['metadata']['author']} is the Lead Pastor of {book_data['metadata']['church']}.
A preacher, teacher, and technology professional, he writes at the intersection of faith, leadership, and practical life.

"I wrote this book for the person I used to be—and sometimes still am."

This book was forged in a furnace of personal struggle and divine encounter. He writes not as someone who has arrived,
but as someone who has learned one thing clearly: sitting is not a strategy. Movement is.
"""
story.append(Paragraph(about_text, body_style))

print("✓ All content added")

# Build PDF
print("[6/6] Building PDF file...")
try:
    doc.build(story, canvasmaker=ProfessionalCanvas)
    print("✓ PDF built successfully")
except Exception as e:
    print(f"✗ Error building PDF: {e}")
    sys.exit(1)

# Verify
if os.path.exists(PDF_FILE):
    file_size = os.path.getsize(PDF_FILE)
    print(f"\n✓ PDF created: {PDF_FILE}")
    print(f"  Size: {file_size:,} bytes ({file_size/1024:.1f} KB)")
else:
    print(f"✗ PDF file not found!")
    sys.exit(1)

print("\n" + "="*80)
print("✅ FINAL PDF GENERATION COMPLETE")
print("="*80)
print(f"\nFile: {PDF_FILE}")
print(f"Format: A4 (210 x 297 mm)")
print(f"Design: Professional with gold borders and corner decorations")
print(f"Font: Helvetica, 12pt body text")
print(f"Colors: Gold (#c9a84c), Cream (#f5f0e8), Black (#0a0a0a)")
print(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print(f"\n📖 Complete Book Contents:")
print(f"  ✓ Title Page")
print(f"  ✓ Dedication")
print(f"  ✓ Epigraph")
print(f"  ✓ Foreword")
print(f"  ✓ Preface")
print(f"  ✓ Table of Contents")
print(f"  ✓ Chapters 1-{len(book_data['chapters'])} (FULL CONTENT WITH DESIGN)")
print(f"  ✓ Conclusion")
print(f"  ✓ About the Author")
print("\n" + "="*80 + "\n")
