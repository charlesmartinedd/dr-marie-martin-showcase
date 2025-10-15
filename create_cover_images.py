"""
Create cover slide images from design specifications
"""
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

OUTPUT_DIR = Path(__file__).parent / "output"
WIDTH, HEIGHT = 1920, 1080

def create_gradient(width, height, color_start, color_end):
    """Create a gradient image"""
    base = Image.new('RGB', (width, height), color_start)
    top = Image.new('RGB', (width, height), color_end)

    mask = Image.new('L', (width, height))
    mask_data = []
    for y in range(height):
        for x in range(width):
            # Diagonal gradient
            mask_data.append(int(255 * (x + y) / (width + height)))
    mask.putdata(mask_data)

    base.paste(top, (0, 0), mask)
    return base

def hex_to_rgb(hex_color):
    """Convert hex color to RGB tuple"""
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def create_cover_slide(filename, title, gradient_colors, output_path):
    """Create a cover slide image"""
    # Create gradient background
    img = create_gradient(WIDTH, HEIGHT, gradient_colors[0], gradient_colors[1])
    draw = ImageDraw.Draw(img)

    # Try to use a nice font, fallback to default
    try:
        title_font = ImageFont.truetype("arial.ttf", 120)
        subtitle_font = ImageFont.truetype("arial.ttf", 90)
        brand_font = ImageFont.truetype("arialbd.ttf", 60)
    except:
        title_font = ImageFont.load_default()
        subtitle_font = ImageFont.load_default()
        brand_font = ImageFont.load_default()

    # Draw "Dr. Marie Martin" title
    name_text = "Dr. Marie Martin"
    name_bbox = draw.textbbox((0, 0), name_text, font=title_font)
    name_width = name_bbox[2] - name_bbox[0]
    name_x = (WIDTH - name_width) // 2
    name_y = 350

    # Add text shadow
    draw.text((name_x + 4, name_y + 4), name_text, fill=(0, 0, 0, 100), font=title_font)
    draw.text((name_x, name_y), name_text, fill=(255, 255, 255), font=title_font)

    # Draw subtitle
    subtitle_bbox = draw.textbbox((0, 0), title, font=subtitle_font)
    subtitle_width = subtitle_bbox[2] - subtitle_bbox[0]
    subtitle_x = (WIDTH - subtitle_width) // 2
    subtitle_y = 520

    draw.text((subtitle_x + 3, subtitle_y + 3), title, fill=(0, 0, 0, 80), font=subtitle_font)
    draw.text((subtitle_x, subtitle_y), title, fill=(255, 255, 255, 240), font=subtitle_font)

    # Draw brand badges at bottom
    badge_y = 720

    # Cell Collective badge
    badge1_text = "Cell Collective"
    badge1_bbox = draw.textbbox((0, 0), badge1_text, font=brand_font)
    badge1_width = badge1_bbox[2] - badge1_bbox[0]
    badge1_x = WIDTH // 2 - badge1_width - 40

    # Draw rounded rectangle for badge 1
    draw.rounded_rectangle(
        [badge1_x - 60, badge_y - 30, badge1_x + badge1_width + 60, badge_y + 90],
        radius=50,
        fill=(255, 255, 255, 40),
        outline=(255, 255, 255, 80),
        width=3
    )
    draw.text((badge1_x, badge_y), badge1_text, fill=(255, 255, 255), font=brand_font)

    # ModelIt badge
    badge2_text = "ModelIt"
    badge2_bbox = draw.textbbox((0, 0), badge2_text, font=brand_font)
    badge2_width = badge2_bbox[2] - badge2_bbox[0]
    badge2_x = WIDTH // 2 + 40

    # Draw rounded rectangle for badge 2
    draw.rounded_rectangle(
        [badge2_x - 60, badge_y - 30, badge2_x + badge2_width + 60, badge_y + 90],
        radius=50,
        fill=(255, 255, 255, 40),
        outline=(255, 255, 255, 80),
        width=3
    )
    draw.text((badge2_x, badge_y), badge2_text, fill=(255, 255, 255), font=brand_font)

    # Save image
    img.save(output_path, quality=95)
    print(f"Created: {output_path}")

def main():
    """Create all cover slide images"""
    print("Creating cover slide images...")

    # Cover slide 1: Purple/Indigo gradient
    create_cover_slide(
        "cover1",
        "Computational Modeling Platform",
        (hex_to_rgb("#667eea"), hex_to_rgb("#764ba2")),
        OUTPUT_DIR / "clip1_computational_modeling_cover.png"
    )

    # Cover slide 2: Pink/Rose gradient
    create_cover_slide(
        "cover2",
        "Transforming School Pedagogy",
        (hex_to_rgb("#f093fb"), hex_to_rgb("#f5576c")),
        OUTPUT_DIR / "clip2_pedagogy_cover.png"
    )

    # Cover slide 3: Cyan/Blue gradient
    create_cover_slide(
        "cover3",
        "AI Revolution in Education",
        (hex_to_rgb("#4facfe"), hex_to_rgb("#00f2fe")),
        OUTPUT_DIR / "clip3_ai_revolution_cover.png"
    )

    print("\nAll cover slides created successfully!")

if __name__ == "__main__":
    main()
