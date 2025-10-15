# Dr. Marie Martin Video Showcase - Setup Instructions

## Quick Start

### Step 1: Install Python Dependencies

```bash
pip install moviepy pillow
```

### Step 2: Create Cover Slide Screenshots

1. Open each cover slide HTML file in your browser:
   - `coverslide1.html`
   - `coverslide2.html`
   - `coverslide3.html`

2. Resize browser window to 1920x1080 (or use browser dev tools)

3. Take screenshots and save them in the `output` folder as:
   - `clip1_computational_modeling_cover.png`
   - `clip2_pedagogy_cover.png`
   - `clip3_ai_revolution_cover.png`

**Quick Method**: Use a screenshot tool or browser extension to capture full page

### Step 3: Run the Video Processor

```bash
python process_videos.py
```

This will:
- Extract the 3 clips from the source video
- Add 2-second cover slides with fade effects
- Save final videos in the `output` folder

### Step 4: View the Website

Open `index.html` in your browser to see the beautiful showcase!

## Optional: Add Background Music

To add soft instrumental music to the cover slides:

1. Find a 2-second royalty-free music clip (suggestions: Artlist, Epidemic Sound, or YouTube Audio Library)
2. Save as `coverslide_music.mp3` in this folder
3. The Python script will automatically include it

## Troubleshooting

**Issue**: MoviePy installation fails
**Solution**: Try `pip install imageio-ffmpeg` first, then `pip install moviepy`

**Issue**: Video processing is slow
**Solution**: This is normal for video processing. Each clip may take 2-5 minutes.

**Issue**: Cover slide screenshots don't look right
**Solution**: Make sure browser window is exactly 1920x1080 pixels

## File Structure

```
dr-marie-martin-showcase/
├── coverslide1.html           # Cover slide: Computational Modeling
├── coverslide2.html           # Cover slide: Transforming Pedagogy
├── coverslide3.html           # Cover slide: AI Revolution
├── process_videos.py          # Video processing script
├── index.html                 # Main showcase website
├── styles.css                 # Website styles
├── INSTRUCTIONS.md           # This file
└── output/                    # Generated videos folder
    ├── clip1_computational_modeling_final.mp4
    ├── clip2_pedagogy_final.mp4
    └── clip3_ai_revolution_final.mp4
```
