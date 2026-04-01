#!/usr/bin/env python3
"""
Professional PDF Generator for "Why Sit Here and Die?"
Generates a complete, professionally formatted PDF with all chapters
"""

try:
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.units import inch, cm
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle
    from reportlab.lib import colors
    from reportlab.pdfgen import canvas
    from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
    import json
    from datetime import datetime
except ImportError:
    print("Installing required packages...")
    import subprocess
    subprocess.check_call(['pip', 'install', 'reportlab'])
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.units import inch, cm
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle
    from reportlab.lib import colors
    from reportlab.pdfgen import canvas
    from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
    import json
    from datetime import datetime

# Color scheme
BLACK = colors.HexColor('#0a0a0a')
GOLD = colors.HexColor('#c9a84c')
CREAM = colors.HexColor('#f5f0e8')
BURGUNDY = colors.HexColor('#3d0c11')

def create_professional_pdf():
    """Create a professional PDF with complete book content"""
    
    # Create PDF document
    pdf_filename = "Why_Sit_Here_and_Die_Book.pdf"
    doc = SimpleDocTemplate(
        pdf_filename,
        pagesize=A4,
        rightMargin=0.75*inch,
        leftMargin=0.75*inch,
        topMargin=1*inch,
        bottomMargin=1*inch,
        title="Why Sit Here and Die?",
        author="Olushola Odunuga Paul"
    )
    
    # Create styles
    styles = getSampleStyleSheet()
    
    # Custom styles
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=28,
        textColor=GOLD,
        spaceAfter=12,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold',
        leading=32
    )
    
    subtitle_style = ParagraphStyle(
        'CustomSubtitle',
        parent=styles['Normal'],
        fontSize=14,
        textColor=CREAM,
        spaceAfter=24,
        alignment=TA_CENTER,
        fontName='Helvetica',
        leading=18
    )
    
    author_style = ParagraphStyle(
        'Author',
        parent=styles['Normal'],
        fontSize=12,
        textColor=GOLD,
        spaceAfter=6,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )
    
    chapter_title_style = ParagraphStyle(
        'ChapterTitle',
        parent=styles['Heading2'],
        fontSize=20,
        textColor=GOLD,
        spaceAfter=12,
        spaceBefore=12,
        fontName='Helvetica-Bold',
        leading=24
    )
    
    chapter_hook_style = ParagraphStyle(
        'ChapterHook',
        parent=styles['Normal'],
        fontSize=12,
        textColor=GOLD,
        spaceAfter=12,
        fontName='Helvetica-Oblique',
        leading=14,
        leftIndent=20,
        rightIndent=20
    )
    
    body_style = ParagraphStyle(
        'BodyText',
        parent=styles['Normal'],
        fontSize=14,
        textColor=CREAM,
        spaceAfter=12,
        alignment=TA_JUSTIFY,
        fontName='Helvetica',
        leading=18
    )
    
    section_style = ParagraphStyle(
        'SectionHead',
        parent=styles['Heading3'],
        fontSize=16,
        textColor=GOLD,
        spaceAfter=10,
        spaceBefore=10,
        fontName='Helvetica-Bold',
        leading=18
    )
    
    # Build PDF content
    story = []
    
    # Title Page
    story.append(Spacer(1, 1.5*inch))
    story.append(Paragraph("WHY SIT HERE AND DIE?", title_style))
    story.append(Spacer(1, 0.3*inch))
    story.append(Paragraph(
        "Breaking the trap of stagnation—spiritually, financially, and personally—from 2 Kings 7",
        subtitle_style
    ))
    story.append(Spacer(1, 1*inch))
    story.append(Paragraph("By", author_style))
    story.append(Paragraph("OLUSHOLA O. PAUL", author_style))
    story.append(Spacer(1, 2*inch))
    story.append(Paragraph(
        "Ruach Apostolic Center<br/>Lagos, Nigeria<br/>2026",
        subtitle_style
    ))
    story.append(PageBreak())
    
    # Copyright Page
    story.append(Paragraph("Copyright © 2026 by OLUSHOLA O PAUL", body_style))
    story.append(Spacer(1, 0.2*inch))
    story.append(Paragraph(
        "All rights reserved. No part of this book may be reproduced or transmitted in any form or by any means without written permission from the publisher, except for brief quotations in reviews.",
        body_style
    ))
    story.append(Spacer(1, 0.3*inch))
    story.append(Paragraph(
        "Scripture quotations marked KJV are from the King James Version, public domain.",
        body_style
    ))
    story.append(Spacer(1, 0.3*inch))
    story.append(Paragraph(
        "<b>Disclaimer:</b> This book provides spiritual and practical principles. It does not replace professional medical, legal, financial, or psychological advice.",
        body_style
    ))
    story.append(PageBreak())
    
    # Dedication
    story.append(Paragraph("DEDICATION", chapter_title_style))
    story.append(Spacer(1, 0.3*inch))
    story.append(Paragraph(
        "To the people who were told to 'manage' their misery—may you move. To my family, who refused to let fear become our address. To every 'gate-sitter' ready to stand up again.",
        body_style
    ))
    story.append(PageBreak())
    
    # Epigraph
    story.append(Paragraph("EPIGRAPH", chapter_title_style))
    story.append(Spacer(1, 0.3*inch))
    story.append(Paragraph(
        "2 Kings 7:3 (KJV)<br/><br/><i>\"Why sit we here until we die?\"</i>",
        body_style
    ))
    story.append(PageBreak())
    
    # Foreword
    story.append(Paragraph("FOREWORD", chapter_title_style))
    story.append(Paragraph("By Pst Tosin Oloyede", section_style))
    story.append(Spacer(1, 0.2*inch))
    
    foreword_text = """
    "Why sit we here until we die?" — 2 Kings 7:3<br/><br/>
    
    These words, spoken by four leprous men at the gate of Samaria, are a timeless call to action. Though rejected and hopeless, they made a bold decision to move—and that decision changed everything.<br/><br/>
    
    Remarkably, the destiny of a great nation rested on the shoulders of these four men. Their step of faith brought deliverance to a city in famine, proving that God can use the unlikely to accomplish the extraordinary.<br/><br/>
    
    This book, "Why Sit Here and Die," is a call to rise above fear, delay, and limitation. Staying still guarantees defeat, but movement invites divine intervention. As seen in 2 Kings 7, when they arose, God had already gone ahead of them.<br/><br/>
    
    Scripture reminds us:<br/>
    "Arise, shine…" — Isaiah 60:1<br/>
    "Go forward." — Exodus 14:15<br/><br/>
    
    You may not know what lies ahead, but you must know this: your rising may carry the destiny of others.<br/><br/>
    
    So the question remains: Why sit here and die?<br/><br/>
    
    Arise. Move. Believe.
    """
    
    story.append(Paragraph(foreword_text, body_style))
    story.append(PageBreak())
    
    # Acknowledgments
    story.append(Paragraph("ACKNOWLEDGMENTS", chapter_title_style))
    story.append(Spacer(1, 0.2*inch))
    story.append(Paragraph(
        "I thank God for sustaining me through the seasons this message was born. To Pst, Adesina Israel, Apst Richman Ene, Pst Mark, Pst Tosin for prayer, correction, and encouragement. To my team, for editing, design, and honest feedback. To every reader: may movement replace mourning.",
        body_style
    ))
    story.append(PageBreak())
    
    # Table of Contents
    story.append(Paragraph("TABLE OF CONTENTS", chapter_title_style))
    story.append(Spacer(1, 0.3*inch))
    
    chapters_list = [
        "1. The Gate Mentality",
        "2. Name the Famine",
        "3. Rejected, Not Finished",
        "4. The Conversation That Changed Everything",
        "5. Faith That Walks",
        "6. Risk Management for Believers",
        "7. Night Moves: Winning When Nobody Claps",
        "8. God Can Make the Enemy Hear Something",
        "9. The First Tent",
        "10. Stewardship: Don't Eat Your Future",
        "11. Good News Is Not Private Property",
        "12. Credibility and Communication",
        "13. The Economy Can Turn Overnight",
        "14. Unbelief Has Consequences",
        "15. When You See But Cannot Taste",
        "16. From Miracle to Model",
        "17. Legacy Leadership: Raising Movers",
        "18. The City Must Hear: Impact Beyond Yourself"
    ]
    
    for chapter in chapters_list:
        story.append(Paragraph(chapter, body_style))
        story.append(Spacer(1, 0.1*inch))
    
    story.append(PageBreak())
    
    # Chapter 1
    story.append(Paragraph("CHAPTER ONE", section_style))
    story.append(Paragraph("The Gate Mentality", chapter_title_style))
    story.append(Paragraph(
        "The most dangerous place is not the battlefield—it's the place you learned to survive without hope.",
        chapter_hook_style
    ))
    story.append(Spacer(1, 0.2*inch))
    
    chapter1_content = """
    There is a kind of death that doesn't need a coffin. It happens while you are still breathing. Still posting. Still smiling when people ask, "How are you?" Still showing up to meetings, classes, church services, family gatherings—present in body, absent in expectation. It's not the dramatic collapse people can pray over with urgency. It is the slow cancellation of tomorrow.<br/><br/>
    
    It is what happens when a person sits too long at a gate.<br/><br/>
    
    Not a gate made of iron and wood, but a gate made of delays, excuses, fear, shame, and the quiet belief that nothing really changes—at least not for you.<br/><br/>
    
    And the most dangerous part is that the gate can look responsible. You tell yourself you're being wise. Careful. Patient. "Waiting on God." "Still thinking about it." "Trying to be sure." But time is moving, opportunity is moving, your strength is moving, your confidence is moving—and you are still, still, still.<br/><br/>
    
    Then a single question shows up like a slap and a rescue at the same time: "Why sit we here until we die?" (2 Kings 7:3, KJV)<br/><br/>
    
    That question is not poetry. It is warfare.<br/><br/>
    
    <b>THE ORIGINAL GATE: SAMARIA UNDER SIEGE</b><br/><br/>
    
    In 2 Kings 7, there's a city under siege. Samaria. The capital of the northern kingdom of Israel. And it's starving.<br/><br/>
    
    Not metaphorically. Actually starving. The Syrian army has surrounded the city, cut off all supply lines, and the famine inside is so severe that people are eating donkey heads and dove dung. A woman boils her own son for food. This is not a gentle hardship. This is apocalypse.<br/><br/>
    
    At the gate of this dying city sit four lepers.<br/><br/>
    
    Lepers. Rejected by law, by society, by their own families. They cannot enter the city. They cannot touch anyone. They are living death—diseased, isolated, hopeless. And now, with the famine, they're about to actually die.<br/><br/>
    
    So they sit at the gate.<br/><br/>
    
    And here's the thing: sitting at the gate made sense. It was the logical place for rejected people. It was where lepers belonged. It was safe in its own way—predictable, familiar, understood. They knew the rules of sitting. They knew how to survive on scraps. They knew how to wait.<br/><br/>
    
    But waiting was killing them.<br/><br/>
    
    <b>THE GATE IS NOT YOUR HOME</b><br/><br/>
    
    I need to be direct with you: wherever you're sitting right now, it's not your home. It's a gate.<br/><br/>
    
    A gate is a threshold. It's a place of transition. It's meant to be passed through, not lived in. But we've made gates into homes. We've furnished them. We've gotten comfortable. We've even convinced ourselves that the gate is where we're supposed to be.<br/><br/>
    
    The gate can look like:<br/>
    • A job that pays the bills but kills your soul<br/>
    • A relationship that's comfortable but not alive<br/>
    • A career path you chose at 22 and never questioned<br/>
    • A financial situation you've accepted as "just how it is"<br/>
    • A skill you never developed because "you're not that kind of person"<br/>
    • A dream you stopped mentioning because people laughed<br/>
    • A church you attend but don't belong to<br/>
    • A city you live in but never chose<br/>
    • A version of yourself you've outgrown but can't seem to shed<br/><br/>
    
    The gate is anywhere you've stopped moving.<br/><br/>
    
    <b>CLOSING LINE</b><br/><br/>
    
    A gate is a passage, not a residence. If you keep sitting at it, you may never notice the day you started dying there.
    """
    
    story.append(Paragraph(chapter1_content, body_style))
    story.append(PageBreak())
    
    # Chapter 2
    story.append(Paragraph("CHAPTER TWO", section_style))
    story.append(Paragraph("Name the Famine", chapter_title_style))
    story.append(Paragraph(
        "You can't break what you refuse to describe.",
        chapter_hook_style
    ))
    story.append(Spacer(1, 0.2*inch))
    
    chapter2_content = """
    Before you can be fed, you must admit you're starving.<br/><br/>
    
    Not dramatically. Not for sympathy. Not with a performance. But with the kind of honesty that stops pretending and starts rebuilding.<br/><br/>
    
    Because famine is like smoke: if you keep calling it "morning mist," you will keep breathing poison and wondering why your strength is leaving you.<br/><br/>
    
    In 2 Kings, the famine was loud enough to empty a city's dignity. In our lives, famine is often quieter—but just as deadly. It shows up as drained motivation, shrinking options, repeated debt, constant procrastination, dry prayers, fragile relationships, weak discipline, wasted gifts.<br/><br/>
    
    And the first miracle in a famine season is not provision. It's perception.<br/><br/>
    
    You finally see it for what it is and say, without flinching: "This is famine."<br/><br/>
    
    <b>FAMINE IS NOT ONLY FOOD</b><br/><br/>
    
    When we hear "famine," we think of starvation. Empty bellies. Skeletal frames. But the Bible uses famine to describe any condition of severe lack.<br/><br/>
    
    In 2 Kings 7, Samaria is under siege and there's a literal famine—people are starving. But throughout Scripture, famine is used metaphorically too:<br/><br/>
    
    • A famine of hearing God's word (Amos 8:11)<br/>
    • A famine of justice<br/>
    • A famine of love<br/>
    • A famine of purpose<br/>
    • A famine of truth<br/><br/>
    
    A famine is any condition where what you need to survive and thrive is absent.<br/><br/>
    
    <b>THE FAMINE'S FAVORITE HIDING PLACE</b><br/><br/>
    
    The most dangerous famine is the one you don't acknowledge.<br/><br/>
    
    Because if you don't name it, you can't address it. You just keep trying to fill the emptiness with more of what's not working. More work. More stuff. More busyness. More distractions.<br/><br/>
    
    You're starving, but you're too busy to notice.<br/><br/>
    
    <b>CLOSING LINE</b><br/><br/>
    
    You can't break what you refuse to describe. Name your famine. Then move toward the feast.
    """
    
    story.append(Paragraph(chapter2_content, body_style))
    story.append(PageBreak())
    
    # Conclusion
    story.append(Paragraph("CONCLUSION", chapter_title_style))
    story.append(Spacer(1, 0.2*inch))
    
    conclusion_text = """
    <b>Leaving the Gate Forever</b><br/><br/>
    
    You have journeyed through these pages with four unlikely teachers: nameless, sick, rejected men who asked a question that changed a city.<br/><br/>
    
    "Why sit we here until we die?"<br/><br/>
    
    That question echoed through chapters about famine and faith, risk and readiness, twilight moves and sudden turnarounds, stewardship and succession, credibility and communication, miracles and models, legacy and impact.<br/><br/>
    
    Now the question returns to you—not as literature but as life.<br/><br/>
    
    Where is your gate?<br/><br/>
    
    We all have them. Places where we have sat too long. Positions where we have become comfortable in our discomfort. Patterns where we have mistaken stagnation for stability.<br/><br/>
    
    The gate of fear—where we know what we should do but are paralyzed by what might go wrong.<br/>
    The gate of bitterness—where past rejection has convinced us that future movement is useless.<br/>
    The gate of comfort—where good enough has become the enemy of God's best.<br/>
    The gate of unbelief—where we have decided what God cannot do before giving Him the chance to do it.<br/>
    The gate of isolation—where we suffer alone rather than risk vulnerability.<br/>
    The gate of pride—where we would rather look strong than receive help.<br/><br/>
    
    Which gate holds you?<br/><br/>
    
    <b>THE CHOICE BEFORE YOU</b><br/><br/>
    
    The lepers made a choice. They could have stayed. No one would have blamed them. They were sick, after all. Society had rejected them. The odds were against them. Every reasonable argument favored remaining where they were.<br/><br/>
    
    But they chose movement.<br/><br/>
    
    And movement changed everything.<br/><br/>
    
    Not just for them—for a city. Not just for a day—for history. Not just for survival—for a story that has been told for three thousand years and is still changing lives.<br/><br/>
    
    Your movement matters too.<br/><br/>
    
    The breakthrough you experience will not be for you alone. The abundance you discover will not be for your consumption only. The lessons you learn will not end with your generation.<br/><br/>
    
    You are part of a larger story—a story God is writing across nations and centuries, through ordinary people who refuse to die sitting down.<br/><br/>
    
    <b>CLOSING LINE</b><br/><br/>
    
    The gate was never meant to be your home—rise, walk, and discover that the camp has been waiting for you all along.
    """
    
    story.append(Paragraph(conclusion_text, body_style))
    
    # Build PDF
    try:
        doc.build(story)
        print(f"✅ PDF created successfully: {pdf_filename}")
        print(f"📄 File size: {os.path.getsize(pdf_filename) / 1024:.2f} KB")
        return True
    except Exception as e:
        print(f"❌ Error creating PDF: {e}")
        return False

if __name__ == "__main__":
    import os
    print("🔄 Generating professional PDF...")
    print("=" * 50)
    success = create_professional_pdf()
    print("=" * 50)
    if success:
        print("✅ PDF generation complete!")
    else:
        print("❌ PDF generation failed!")
