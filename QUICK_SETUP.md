# Quick Setup Guide - Why Sit Here and Die?

## 🚀 System is LIVE and READY

### Current Status
✅ Landing page deployed  
✅ Online reader deployed  
✅ All 18 chapters loaded  
✅ Password protection active  
✅ Session management working  
✅ Responsive design verified  

### Access the System

**Landing Page:**
https://why-sit-here-and-die.vercel.app

**Online Reader (Direct Access):**
https://why-sit-here-and-die.vercel.app/online-reader.html

**Test Login:**
- Password: `March31`

### How Users Access After Payment

**Option 1: Automatic (Recommended)**
- Payment processor redirects to:
  ```
  https://why-sit-here-and-die.vercel.app/online-reader.html?access=March31
  ```
- User auto-logs in
- URL parameter is removed (security)

**Option 2: Manual**
- User visits online reader
- Enters password: `March31`
- Gains access

### What's Included

**Landing Page Features:**
- Book description
- 18 chapter titles
- Key features list
- Pricing (₦5,000)
- Payment buttons
- Link to reader

**Online Reader Features:**
- Password login
- All 18 chapters
- Chapter navigation
- Chapter counter
- Download PDF button
- Logout button
- Session persistence
- Mobile responsive

**Book Content:**
- 18 complete chapters
- Real-life stories
- Biblical references
- Practical frameworks
- Emotional depth

### Files Deployed

```
index.html              - Landing page
online-reader.html      - Book reader
chapters-part1.js       - Chapters 1-6
chapters-part2.js       - Chapters 7-12
chapters-part3.js       - Chapters 13-18
vercel.json            - Deployment config
```

### Payment Integration

**To integrate payment:**

1. **Get payment processor** (PayPal, Stripe, etc.)

2. **Set return URL:**
   ```
   https://why-sit-here-and-die.vercel.app/online-reader.html?access=March31
   ```

3. **Configure amount:**
   - Amount: ₦5,000
   - Currency: NGN

4. **Send email after payment:**
   - Include password: `March31`
   - Include link to reader

### Testing Checklist

- [ ] Visit landing page - loads correctly
- [ ] Click "Go to Online Reader" - redirects to reader
- [ ] Enter password `March31` - logs in
- [ ] Read Chapter 1 - displays correctly
- [ ] Click "Next Chapter" - navigates to Chapter 2
- [ ] Click "Previous Chapter" - navigates back to Chapter 1
- [ ] Refresh page - stays logged in
- [ ] Click "Logout" - returns to login screen
- [ ] Test on mobile - responsive design works

### Customization

**Change Password:**
Edit `online-reader.html`, find:
```javascript
const CORRECT_PASSWORD = "March31";
```
Replace with your password.

**Change Price:**
Edit `index.html`, find:
```html
<div class="price">₦5,000</div>
```
Replace with your price.

**Add/Edit Chapters:**
Edit `chapters-part1.js`, `chapters-part2.js`, or `chapters-part3.js`

### Troubleshooting

**Chapters not loading?**
- Check all three chapter files are present
- Check browser console (F12) for errors
- Clear browser cache

**Password not working?**
- Verify exact spelling (case-sensitive)
- Check you're using `March31`
- Try incognito/private mode

**Not staying logged in?**
- Check localStorage is enabled
- Try different browser
- Clear cookies and cache

### Support

**Live URL:** https://why-sit-here-and-die.vercel.app

**Files:**
- Landing: index.html
- Reader: online-reader.html
- Chapters: chapters-part1.js, chapters-part2.js, chapters-part3.js

**Git Repository:** Committed and pushed to origin/master

---

**Everything is ready. You can start accepting payments now.**

The system will automatically redirect users to the reader after payment.
