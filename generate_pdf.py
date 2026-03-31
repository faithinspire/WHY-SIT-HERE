#!/usr/bin/env python3
"""
Professional PDF Book Generator
Extracts manuscript from DOCX and creates a publication-ready PDF
"""

import zipfile
import xml.etree.ElementTree as ET
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Image, Table, TableStyle
from reportlab.pdfgen import canvas
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
import os
from PIL import Image as PILImage

# Colors
GOLD = HexColor('#D4AF37')
DARK = HexColor('#2C3E50')
LIGHT = HexColor('#ECF0F1')
GRAY = HexColor('#999999')

def extract_docx_text():
    """Extract all text from DOCX file"""
    docx_path = 'WHY SIT HERE AND DIE.docx'
    
    try:
        with zipfile.ZipFile(docx_path, 'r') as zip_ref:
            xml_content = zip_ref.read('word/document.xml')
    except Exception as e:
        print(f"Error reading DOCX: {e}")
        return []
    
    # Parse XML
    root = ET.fromstring(xml_content)
    
    # Namespace
    ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
    
    paragraphs = []
    for para in root.findall('.//w:p', ns):
        texts = []
        for text_elem in para.findall('.//w:t', ns):
            if text_elem.text:
                texts.append(text_elem.text)
        
        para_text = ''.join(texts).strip()
        if para_text:
            paragraphs.append(para_text)
    
    return paragraphs

def create_styles():
    """Create custom paragraph styles"""
    styles = getSampleStyleSheet()
    
    # Title style
    styles.add(ParagraphStyle(
        name='CustomTitle',
        parent=styles['Heading1'],
        fontSize=28,
        textColor=GOLD,
        spaceAfter=30,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    ))
    
    # Chapter style
    styles.add(ParagraphStyle(
        name='ChapterTitle',
        parent=styles['Heading1'],
        fontSize=16,
        textColor=GOLD,
        spaceAfter=20,
        spaceBefore=20,
        fontName='Helvetica-Bold'
    ))
    
    # Part style
    styles.add(ParagraphStyle(
        name='PartTitle',
        parent=styles['Heading1'],
        fontSize=14,
        textColor=GOLD,
        spaceAfter=15,
        spaceBefore=15,
        fontName='Helvetica-Bold'
    ))
    
    # Body style
    styles.add(ParagraphStyle(
        name='CustomBody',
        parent=styles['BodyText'],
        fontSize=11,
        textColor=DARK,
        spaceAfter=12,
        alignment=TA_JUSTIFY,
        fontName='Helvetica'
    ))
    
    # Subtitle style
    styles.add(ParagraphStyle(
        name='Subtitle',
        parent=styles['Normal'],
        fontSize=14,
        textColor=DARK,
        spaceAfter=12,
        alignment=TA_CENTER,
        fontName='Helvetica'
    ))
    
    return styles

def create_pdf():
    """Create the professional PDF"""
    print("Extracting manuscript from DOCX...")
    paragraphs = extract_docx_text()
    print(f"Extracted {len(paragraphs)} paragraphs")
    
    # Create PDF
    pdf_filename = 'Why-Sit-Here-and-Die-Complete.pdf'
    doc = SimpleDocTemplate(
        pdf_filename,
        pagesize=A4,
        rightMargin=50,
        leftMargin=50,
        topMargin=50,
        bottomMargin=50,
        title='Why Sit Here and Die?',
        author='Olushola O. Paul'
    )
    
    styles = create_styles()
    story = []
    
    # Front Cover
    story.append(Spacer(1, 1.5*inch))
    
    # Add book cover image if available
    try:
        if os.path.exists('book-cover.jpg'):
            img = Image('book-cover.jpg', width=3*inch, height=4*inch)
            story.append(img)
            story.append(Spacer(1, 0.3*inch))
    except Exception as e:
        print(f"Could not add book cover: {e}")
    
    story.append(Paragraph('WHY SIT HERE AND DIE?', styles['CustomTitle']))
    story.append(Paragraph('Breaking the trap of stagnation', styles['Subtitle']))
    story.append(Paragraph('spiritually, financially, and personally', styles['Subtitle']))
    story.append(Spacer(1, 0.2*inch))
    story.append(Paragraph('from 2 Kings 7', styles['Subtitle']))
    story.append(Spacer(1, 0.5*inch))
    story.append(Paragraph('By OLUSHOLA O. PAUL', styles['Subtitle']))
    story.append(PageBreak())
    
    # Title Page
    story.append(Spacer(1, 1*inch))
    story.append(Paragraph('WHY SIT HERE AND DIE?', styles['CustomTitle']))
    story.append(Spacer(1, 0.3*inch))
    story.append(Paragraph(
        'Breaking the trap of stagnation—spiritually, financially, and personally—from 2 Kings 7',
        styles['Subtitle']
    ))
    story.append(Spacer(1, 0.8*inch))
    story.append(Paragraph('By OLUSHOLA O. PAUL', styles['Subtitle']))
    story.append(PageBreak())
    
    # Copyright Page
    story.append(Paragraph('WHY SIT HERE AND DIE?', styles['Heading2']))
    story.append(Spacer(1, 0.2*inch))
    story.append(Paragraph(
        'Breaking the trap of stagnation—spiritually, financially, and personally—from 2 Kings 7',
        styles['Normal']
    ))
    story.append(Spacer(1, 0.3*inch))
    story.append(Paragraph(
        'Copyright © 2026 by OLUSHOLA O PAUL<br/>All rights reserved. No part of this book may be reproduced or transmitted in any form or by any means without written permission from the publisher, except for brief quotations in reviews.',
        styles['Normal']
    ))
    story.append(Spacer(1, 0.2*inch))
    story.append(Paragraph(
        'Scripture quotations marked KJV are from the King James Version, public domain.',
        styles['Normal']
    ))
    story.append(Spacer(1, 0.2*inch))
    story.append(Paragraph(
        'Disclaimer: This book provides spiritual and practical principles. It does not replace professional medical, legal, financial, or psychological advice.',
        styles['Normal']
    ))
    story.append(PageBreak())
    
    # Table of Contents
    story.append(Paragraph('TABLE OF CONTENTS', styles['CustomTitle']))
    story.append(Spacer(1, 0.3*inch))
    
    toc_items = [
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
    ]
    
    for item in toc_items:
        if item == '':
            story.append(Spacer(1, 0.1*inch))
        elif 'PART' in item:
            story.append(Paragraph(item, styles['PartTitle']))
        else:
            story.append(Paragraph('• ' + item, styles['Normal']))
    
    story.append(PageBreak())
    
    # Main Content
    for para in paragraphs:
        if not para.strip():
            story.append(Spacer(1, 0.1*inch))
        elif 'Chapter' in para and 'Movement' not in para:
            story.append(Paragraph(para, styles['ChapterTitle']))
        elif 'PART' in para or 'PREFACE' in para or 'Foreword' in para:
            story.append(Paragraph(para, styles['PartTitle']))
        elif len(para) > 200:
            story.append(Paragraph(para, styles['CustomBody']))
        else:
            story.append(Paragraph(para, styles['CustomBody']))
    
    story.append(PageBreak())
    
    # About the Author
    story.append(Paragraph('ABOUT THE AUTHOR', styles['CustomTitle']))
    story.append(Spacer(1, 0.3*inch))
    
    # Add author photo if available
    try:
        if os.path.exists('author.jpg'):
            img = Image('author.jpg', width=1.5*inch, height=1.5*inch)
            story.append(img)
            story.append(Spacer(1, 0.2*inch))
    except Exception as e:
        print(f"Could not add author photo: {e}")
    
    about_text = """
    <b>OLUSHOLA O. PAUL</b> is the Lead Pastor of Ruach Apostolic Center in Lagos, Nigeria. 
    He is a speaker, author, and leadership coach with a passion for helping individuals and 
    organizations break through stagnation and move toward their God-given potential.<br/><br/>
    
    With a background in both ministry and technology, Olushola brings a unique perspective 
    to the integration of faith and function. He has worked with churches, businesses, and 
    non-profits across Africa and beyond, helping leaders and teams navigate seasons of 
    difficulty and discover breakthrough.<br/><br/>
    
    His message is rooted in Scripture, tested in real life, and designed for practical application. 
    He believes that the same God who saved the lepers at the gate is still making ways where 
    there seem to be no ways.<br/><br/>
    
    Olushola is married and is passionate about mentoring the next generation of leaders. 
    When he is not writing or speaking, he enjoys technology, reading, and spending time 
    with his family.
    """
    
    story.append(Paragraph(about_text, styles['CustomBody']))
    
    # Build PDF
    print(f"Building PDF: {pdf_filename}...")
    doc.build(story)
    
    print(f"✓ PDF created successfully: {pdf_filename}")
    print(f"✓ File size: {os.path.getsize(pdf_filename) / (1024*1024):.2f} MB")

if __name__ == '__main__':
    try:
        create_pdf()
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
