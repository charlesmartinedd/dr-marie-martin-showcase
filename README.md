# Dr. Marie Martin - Educational Insights Showcase

A beautiful, modern website showcasing Dr. Marie Martin's perspectives on computational modeling, educational transformation, and the future of science education.

## 🎯 Project Overview

This project features:
- **3 Professionally Edited Video Clips** with custom cover slides
- **Beautiful Single-Page Website** with Cell Collective/ModelIt branding
- **Responsive Grid Layout** optimized for all devices
- **Comprehensive Bio** of Dr. Marie Martin's work and impact

## 🎨 Features

### Video Clips
1. **Computational Modeling Platform** (2:15) - Cell Collective and ModelIt platform overview
2. **Transforming School Pedagogy** (1:00) - Redefining modeling in education
3. **AI Revolution in Education** (1:10) - The intelligent age and educational transformation

### Website Components
- Hero section with gradient background
- Professional bio section with contact info
- Grid-based video showcase
- Fully responsive design
- Cell Collective color scheme (#6366f1, #8b5cf6, gradients)

## 🚀 Quick Start

### Option 1: View Website Only (No Video Processing)

Simply open `index.html` in your browser to see the website structure. Videos will show placeholders until processed.

### Option 2: Full Setup with Video Processing

#### Step 1: Install Python Dependencies
```bash
pip install moviepy pillow
```

#### Step 2: Run the Setup Script
**Windows:**
```bash
setup.bat
```

**Mac/Linux:**
```bash
chmod +x setup.sh
./setup.sh
```

Or manually:
```bash
python process_videos.py
```

#### Step 3: Create Cover Slide Screenshots

1. Open each HTML file in your browser (1920x1080 window):
   - `coverslide1.html`
   - `coverslide2.html`
   - `coverslide3.html`

2. Screenshot each and save to `output/` folder as:
   - `clip1_computational_modeling_cover.png`
   - `clip2_pedagogy_cover.png`
   - `clip3_ai_revolution_cover.png`

3. Re-run the Python script to add cover slides to videos

#### Step 4: Open the Website
```bash
# Windows
start index.html

# Mac
open index.html

# Linux
xdg-open index.html
```

## 📁 Project Structure

```
dr-marie-martin-showcase/
├── index.html                 # Main website
├── styles.css                 # Website styling
├── coverslide1.html          # Cover: Computational Modeling
├── coverslide2.html          # Cover: Transforming Pedagogy
├── coverslide3.html          # Cover: AI Revolution
├── process_videos.py         # Video processing script
├── README.md                 # This file
├── INSTRUCTIONS.md           # Detailed instructions
└── output/                    # Generated videos
    ├── clip1_computational_modeling_final.mp4
    ├── clip2_pedagogy_final.mp4
    └── clip3_ai_revolution_final.mp4
```

## 🎨 Design Details

### Colors (Cell Collective Branding)
- Primary: #6366f1 (Indigo Blue)
- Secondary: #8b5cf6 (Purple)
- Accent: #ec4899 (Pink)
- Gradients: Purple/Indigo, Pink/Rose, Cyan/Blue

### Typography
- Font: Inter (Google Fonts)
- Weights: 300, 400, 500, 600, 700, 800

### Layout
- Max width: 1280px
- Grid: Auto-fit responsive (min 380px)
- Fully responsive breakpoints: 1024px, 768px, 480px

## 🎬 Video Timestamps

- **Clip 1:** 03:40:32 - 03:42:47 (Computational Modeling Platform)
- **Clip 2:** 04:28:44 - 04:29:45 (Transforming School Pedagogy)
- **Clip 3:** 00:07:09 - 00:08:19 (AI Revolution in Education)

## 📧 Contact

**Email:** info@discoverycollective.com

## 🙏 Credits

- **Featured:** Dr. Marie Martin
- **Organizations:** Cell Collective, ModelIt, Discovery Collective
- **Source:** K-12 2030 Global Education Conference (Day 2)

## 📝 License

All content © 2025 Dr. Marie Martin / Discovery Collective

---

Built with ❤️ for transforming education through computational modeling
