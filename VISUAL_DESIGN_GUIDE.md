# Visual Design Guide

## 🎨 COLOR PALETTE

```
Gold Accent:     #c9a84c  ████████████ (headings, borders, accents)
Dark:            #0a0a0a  ████████████ (backgrounds, text)
Cream:           #faf7f2  ████████████ (page background)
Text:            #1a1a1a  ████████████ (body text)
Muted:           #5a5a5a  ████████████ (secondary text)
```

## 📐 PAGE LAYOUT

```
┌─────────────────────────────────────┐
│         20mm (top margin)           │
│  ┌─────────────────────────────┐    │
│  │                             │    │
│  │   18mm left margin          │ 16mm
│  │                             │ right
│  │   Content Area              │ margin
│  │   (148mm × 170mm)           │    │
│  │                             │    │
│  │   Footer at 15mm from bottom│    │
│  └─────────────────────────────┘    │
│         20mm (bottom margin)        │
└─────────────────────────────────────┘
     A5 Page: 148mm × 210mm
```

## 🔤 TYPOGRAPHY HIERARCHY

```
Cover Title
═══════════════════════════════════════
Font: Playfair Display, 3rem, 900
Color: Gold (#c9a84c)
Example: "Why Sit Here and Die?"

Chapter Title
───────────────────────────────────────
Font: Playfair Display, 1.8rem, 700
Color: Dark (#1a1a1a)
Example: "Before You Read This Book"

Section Heading
───────────────────────────────────────
Font: Playfair Display, 1.05rem, 700
Color: Dark (#1a1a1a)
Border: 1px gold underline
Example: "Why I Chose This Title"

Body Text
───────────────────────────────────────
Font: EB Garamond, 11pt, 400
Color: Dark (#1a1a1a)
Line Height: 1.8
Alignment: Justified
```

## 📦 COMPONENT STYLES

### Scripture Pull
```
┌─────────────────────────────────────┐
│ ▌ "And there were four leprous men  │
│ ▌ at the entering in of the gate..."│
│ ▌                                   │
│ ▌ 2 KINGS 7:3, KJV                 │
└─────────────────────────────────────┘
Gold left border, light background
```

### Movement Box
```
┌─────────────────────────────────────┐
│ REFLECTION & ACTION                 │
│ ─────────────────────────────────── │
│ Take time to reflect on your own    │
│ gates. What patterns are keeping    │
│ you stuck?                          │
└─────────────────────────────────────┘
Cream background, gold border
```

### Prayer Box
```
┌─────────────────────────────────────┐
│ ▌ PRAYER                            │
│ ▌ Father, give me eyes to see my    │
│ ▌ gates and courage to walk through │
│ ▌ them. Amen.                       │
└─────────────────────────────────────┘
Burgundy left border, light background
```

## 📄 PAGE STRUCTURE

### Cover Page
```
[Dark Gradient Background]

        Why Sit Here
        and Die?

Breaking the trap of stagnation—
spiritually, financially, and personally—
from 2 Kings 7

        ─────────

Olushola Odunuga Paul
Lead Pastor · Ruach Apostolic Center
```

### Inner Page
```
PART ONE · CHAPTER ONE
01
The Gate Mentality

The most dangerous place is not the
battlefield — it's the place you learned
to survive without hope.

[Content flows here with proper spacing]

─────────────────────────────────────
Why Sit Here and Die?                1
```

## 🎯 SPACING STANDARDS

```
Paragraph spacing:        0.9rem
Section heading margin:   1.5rem top, 0.6rem bottom
Box padding:              1.2rem
Footer position:          15mm from bottom
Line height:              1.8
Letter spacing (labels):  0.2em
```

## 📱 RESPONSIVE BREAKPOINTS

```
Desktop (Full)
├─ Page width: 148mm
├─ Margins: 20/20/18/16mm
└─ Font sizes: Full

Tablet (≤768px)
├─ Page width: 100%
├─ Margins: 15mm
└─ Font sizes: Reduced

Mobile (≤480px)
├─ Page width: 100%
├─ Margins: 12mm
└─ Font sizes: Further reduced
```

## ✨ DESIGN PRINCIPLES

1. **Hierarchy** - Clear visual order guides reading
2. **Consistency** - Uniform spacing and styling
3. **Readability** - Optimal line height and font sizes
4. **Elegance** - Professional serif fonts
5. **Balance** - Proper margins and padding
6. **Professionalism** - Publication-quality appearance

## 🎨 CUSTOMIZATION EXAMPLES

### Change Gold Accent
```css
:root {
  --gold: #8B7355;  /* Change to brown */
}
```

### Change Background
```css
:root {
  --cream: #f5f5f5;  /* Change to light gray */
}
```

### Change Font
```css
.chapter-title {
  font-family: 'Georgia', serif;  /* Change font */
}
```

## 📊 VISUAL BALANCE

```
Top Section (20%)
├─ Chapter label
├─ Chapter number
└─ Chapter title

Middle Section (60%)
├─ Chapter hook
├─ Body content
├─ Scripture pulls
└─ Boxes

Bottom Section (20%)
├─ Closing line
└─ Footer
```

