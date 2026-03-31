#!/usr/bin/env python3
"""
Extract full chapters from manuscript and generate book-data-complete.js
"""

import re
import json

# Read the chunk files
chunks = []
for i in range(1, 7):
    try:
        with open(f'chunk{i}.txt', 'r', encoding='utf-8') as f:
            chunks.append(f.read())
    except:
        pass

# Combine all chunks
full_text = ''.join(chunks)

# Split by chapter markers
chapters_raw = re.split(r'CHAPTER\s+(\d+)', full_text)

# Parse chapters
chapters = {}
for i in range(1, len(chapters_raw), 2):
    if i+1 < len(chapters_raw):
        chapter_num = int(chapters_raw[i])
        chapter_content = chapters_raw[i+1].strip()
        chapters[chapter_num] = chapter_content

print(f"Extracted {len(chapters)} chapters")
for num in sorted(chapters.keys()):
    content_preview = chapters[num][:100].replace('\n', ' ')
    print(f"Chapter {num}: {content_preview}...")
