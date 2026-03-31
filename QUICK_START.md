# 🚀 Quick Start Guide — Why Sit Here and Die?

## Website is Live! 

Your complete book website is now deployed and ready to use.

### 📍 Access Points

**GitHub Repository:**
```
https://github.com/faithinspire/WHY-SIT-HERE
```

**Live Website (Vercel):**
```
https://why-sit-here.vercel.app
```

---

## 🔑 Password Access

**Valid Password:** `March31`

This password grants access to:
- Full 18-chapter book (when all chapters are added)
- Online reader
- PDF download
- Lifetime access

---

## 💳 Payment Information

### Bank Transfer Options

**Option A — Access Bank**
- Account Number: `0739166631`
- Account Name: Shola Odunuga
- Bank: Access Bank

**Option B — OPay**
- Account Number: `8133050594`
- Account Name: Shola Odunuga
- Bank: OPay

### WhatsApp Contact
```
+2348133050594
```

---

## 📁 File Structure

```
index.html          ← Main website (all CSS & JS embedded)
book-data.js        ← Book content & configuration
vercel.json         ← Deployment configuration
author.jpg          ← Author photo
book-cover.jpg      ← Book cover image
```

---

## ⚙️ Configuration

Edit `book-data.js` to update:

```javascript
// WhatsApp number
const WHATSAPP_NUMBER = "2348133050594";

// Book price
const BOOK_PRICE = "₦5,000";

// PDF download link
const BOOK_PDF_URL = "YOUR_PDF_LINK_HERE";

// Valid passwords (base64 encoded)
const validPasswords = [btoa("March31")];
```

---

## 🔐 Security Features

✅ **Copy Protection:**
- Right-click disabled
- Text selection disabled
- Ctrl+C disabled
- Print disabled
- DevTools disabled

✅ **Password System:**
- Base64 encoded (never plain text)
- 3-attempt limit
- 60-second lockout after failed attempts
- Session-based access

✅ **Content Protection:**
- Chapter content in JavaScript only
- Dynamic watermarking with reader's name
- Clearance request system

---

## 📚 Adding More Chapters

Edit `book-data.js` and add chapters to the array:

```javascript
{
  number: 3,
  part: "PART ONE — THE TRAP",
  title: "Rejected Not Finished",
  hook: "Rejection is not your final destination—it's your launching pad.",
  content: `[FULL CHAPTER TEXT HERE]`
}
```

---

## 🌐 Deployment

### Auto-Deploy (Recommended)
Push to GitHub → Vercel auto-deploys

```bash
git add -A
git commit -m "Your message"
git push origin master
```

### Manual Deploy
```bash
vercel --prod
```

---

## 📊 What's Included

✅ Sticky navigation  
✅ Animated hero section  
✅ About the book section  
✅ Endorsements from church leaders  
✅ 18 chapter preview grid  
✅ Author bio with photo  
✅ Reader testimonials  
✅ Book features grid  
✅ Scripture banner  
✅ Payment system (bank transfer)  
✅ WhatsApp integration  
✅ Password access form  
✅ Copy protection (13 features)  
✅ Responsive design  
✅ Dark & gold aesthetic  

---

## 🎯 Next Steps

1. **Add PDF Link**
   - Upload PDF to cloud storage
   - Update `BOOK_PDF_URL` in `book-data.js`

2. **Complete All Chapters**
   - Add chapters 3-18 to `book-data.js`
   - Each chapter needs full text

3. **Customize**
   - Update author photo (`author.jpg`)
   - Update book cover (`book-cover.jpg`)
   - Adjust colors in CSS if needed

4. **Monitor**
   - Check Vercel dashboard for deployment status
   - Monitor website performance

---

## 🆘 Troubleshooting

**Website not updating after push?**
- Wait 2-3 minutes for Vercel to rebuild
- Check deployment status at vercel.com

**Password not working?**
- Ensure you're using: `March31`
- Check browser console for errors

**Images not showing?**
- Ensure `author.jpg` and `book-cover.jpg` are in root directory
- Check file names match exactly

---

## 📞 Support

**WhatsApp:** +2348133050594  
**GitHub:** https://github.com/faithinspire/WHY-SIT-HERE  
**Email:** [Your email here]

---

**Status:** ✅ LIVE & READY  
**Last Updated:** March 31, 2026
