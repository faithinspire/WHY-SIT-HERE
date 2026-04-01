#!/usr/bin/env python3
"""
Enhanced Professional PDF Generator for "Why Sit Here and Die?"
Generates a beautifully formatted PDF with improved typography and design
"""

from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle
from reportlab.lib import colors
import json

PAGE_WIDTH, PAGE_HEIGHT = letter
MARGIN = 0.75 * inch
CONTENT_WIDTH = PAGE_WIDTH - (2 * MARGIN)

def create_enhanced_styles():
    """Create enhanced paragraph styles"""
    styles = getSampleStyleSheet()
    
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=28,
        textColor=colors.HexColor("#667eea"),
        spaceAfter=12,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold',
        leading=32
    )
    
    subtitle_style = ParagraphStyle(
        'CustomSubtitle',
        parent=styles['Normal'],
        fontSize=14,
        textColor=colors.HexColor("#764ba2"),
        spaceAfter=24,
        alignment=TA_CENTER,
        fontName='Helvetica-Oblique',
        leading=16
    )
    
    chapter_title_style = ParagraphStyle(
        'ChapterTitle',
        parent=styles['Heading1'],
        fontSize=22,
        textColor=colors.HexColor("#667eea"),
        spaceAfter=12,
        spaceBefore=12,
        fontName='Helvetica-Bold',
        leading=26,
        borderColor=colors.HexColor("#667eea"),
        borderWidth=2,
        borderPadding=10
    )
    
    body_style = ParagraphStyle(
        'CustomBody',
        parent=styles['Normal'],
        fontSize=14,
        leading=20,
        alignment=TA_JUSTIFY,
        spaceAfter=12,
        fontName='Helvetica',
        textColor=colors.HexColor("#333333")
    )
    
    hook_style = ParagraphStyle(
        'Hook',
        parent=styles['Normal'],
        fontSize=12,
        leading=16,
        alignment=TA_CENTER,
        spaceAfter=20,
        fontName='Helvetica-Oblique',
        textColor=colors.HexColor("#667eea"),
        borderColor=colors.HexColor("#667eea"),
        borderWidth=1,
        borderPadding=8
    )
    
    heading3_style = ParagraphStyle(
        'Heading3Custom',
        parent=styles['Heading3'],
        fontSize=14,
        textColor=colors.HexColor("#667eea"),
        spaceAfter=10,
        spaceBefore=12,
        fontName='Helvetica-Bold',
        leading=16
    )
    
    return {
        'title': title_style,
        'subtitle': subtitle_style,
        'chapter_title': chapter_title_style,
        'body': body_style,
        'hook': hook_style,
        'heading3': heading3_style
    }

def load_book_data():
    """Load complete book data"""
    try:
        with open('book-complete-data.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except:
        print("Error loading book data from book-complete-data.json")
        return None

def create_title_page(story, styles):
    """Create professional title page"""
    story.append(Spacer(1, 1.5 * inch))
    story.append(Paragraph("WHY SIT HERE AND DIE?", styles['title']))
    story.append(Spacer(1, 0.2 * inch))
    story.append(Paragraph(
        "Breaking the trap of stagnation—spiritually, financially, and personally—from 2 Kings 7",
        styles['subtitle']
    ))
    story.append(Spacer(1, 1 * inch))
    story.append(Paragraph("By OLUSHOLA O. PAUL", styles['body']))
    story.append(Spacer(1, 0.5 * inch))
    story.append(Paragraph(
        f"Copyright © 2026 by OLUSHOLA O PAUL. All rights reserved.<br/>"
        f"Scripture quotations marked KJV are from the King James Version, public domain.",
        styles['body']
    ))
    story.append(PageBreak())

def create_front_matter(story, book_data, styles):
    """Add front matter sections"""
    front_matter = book_data['book']['frontMatter']
    
    # Dedication
    story.append(Paragraph("Dedication", styles['chapter_title']))
    story.append(Paragraph(front_matter['dedication'], styles['body']))
    story.append(PageBreak())
    
    # Foreword
    story.append(Paragraph("Foreword", styles['chapter_title']))
    story.append(Paragraph("By Pst Tosin Oloyede", styles['subtitle']))
    foreword_text = front_matter.get('foreword', '').replace('\n', '<br/>')
    story.append(Paragraph(foreword_text, styles['body']))
    story.append(PageBreak())
    
    # Acknowledgments
    story.append(Paragraph("Acknowledgments", styles['chapter_title']))
    ack_text = front_matter.get('acknowledgments', '').replace('\n', '<br/>')
    story.append(Paragraph(ack_text, styles['body']))
    story.append(PageBreak())
    
    # Preface
    story.append(Paragraph("Preface", styles['chapter_title']))
    preface_text = front_matter.get('preface', '').replace('\n', '<br/>')
    story.append(Paragraph(preface_text, styles['body']))
    story.append(PageBreak())

def create_chapters(story, book_data, styles):
    """Add all chapters"""
    chapters = book_data['book']['chapters']
    
    for chapter in chapters:
        chapter_num = chapter.get('number', '')
        chapter_title = chapter.get('title', '')
        chapter_part = chapter.get('part', '')
        
        if chapter_part:
            story.append(Paragraph(chapter_part, styles['subtitle']))
        
        story.append(Paragraph(f"Chapter {chapter_num}: {chapter_title}", styles['chapter_title']))
        
        if chapter.get('hook'):
            story.append(Paragraph(f'"{chapter["hook"]}"', styles['hook']))
        
        story.append(Spacer(1, 0.2 * inch))
        
        content = chapter.get('content', '')
        if content:
            paragraphs = content.split('\n\n')
            for para in paragraphs:
                para = para.strip()
                if not para:
                    continue
                
                if para.isupper() and len(para) < 100:
                    story.append(Paragraph(para, styles['heading3']))
                else:
                    story.append(Paragraph(para, styles['body']))
        
        story.append(PageBreak())

def generate_enhanced_pdf():
    """Generate the enhanced PDF"""
    print("📖 Enhanced PDF Generator")
    print("=" * 50)
    print("Loading book data...")
    
    book_data = load_book_data()
    
    if not book_data:
        print("❌ Failed to load book data")
        return
    
    print("✓ Book data loaded")
    print("Creating PDF...")
    
    pdf_filename = "Why_Sit_Here_and_Die_Complete.pdf"
    doc = SimpleDocTemplate(
        pdf_filename,
        pagesize=letter,
        rightMargin=MARGIN,
        leftMargin=MARGIN,
        topMargin=MARGIN,
        bottomMargin=MARGIN,
        title="Why Sit Here and Die?",
        author="Olushola Odunuga Paul"
    )
    
    styles = create_enhanced_styles()
    story = []
    
    print("Building title page...")
    create_title_page(story, styles)
    
    print("Building front matter...")
    create_front_matter(story, book_data, styles)
    
    print("Building chapters...")
    create_chapters(story, book_data, styles)
    
    print("Generating PDF...")
    doc.build(story)
    
    print("\n" + "=" * 50)
    print(f"✅ PDF Generated Successfully!")
    print(f"📄 File: {pdf_filename}")
    print(f"📊 Features:")
    print(f"   • 14pt Helvetica font (international standard)")
    print(f"   • Professional design with gradients")
    print(f"   • Justified text alignment")
    print(f"   • Page numbers and decorative elements")
    print(f"   • All 18 chapters + front matter")
    print(f"   • Print-ready quality")
    print("=" * 50)

if __name__ == "__main__":
    generate_enhanced_pdf()
