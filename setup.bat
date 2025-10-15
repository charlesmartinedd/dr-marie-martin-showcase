@echo off
echo ========================================
echo Dr. Marie Martin Video Showcase Setup
echo ========================================
echo.

echo Step 1: Installing Python dependencies...
pip install moviepy pillow
echo.

echo Step 2: Creating output directory...
if not exist "output" mkdir output
echo.

echo Step 3: Processing videos...
python process_videos.py
echo.

echo ========================================
echo Setup Complete!
echo ========================================
echo.
echo Next steps:
echo 1. Create screenshots of cover slides (see INSTRUCTIONS.md)
echo 2. Re-run this script to add covers to videos
echo 3. Open index.html to view the website
echo.

pause
