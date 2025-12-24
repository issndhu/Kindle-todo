from PIL import Image, ImageDraw, ImageFont
import os

# Dimensions
WIDTH = 600
HEIGHT = 800

BG = 255
FG = 0

# Create image
img = Image.new("L", (WIDTH, HEIGHT), BG)
draw = ImageDraw.Draw(img)

# Font paths (relative to this script)
base_path = os.path.dirname(__file__)
title_font_path = os.path.join(base_path, "fonts", "JetBrainsMono-Bold.ttf")
body_font_path  = os.path.join(base_path, "fonts", "JetBrainsMonoNL-Regular.ttf")

# Load fonts
title_font = ImageFont.truetype(title_font_path, 42)
body_font  = ImageFont.truetype(body_font_path, 30)

x = 60
y = 80

# Title
draw.text((x, y), "TODO — TODAY", font=title_font, fill=FG)
y += 70

# Separator line (terminal style)
draw.text((x, y), "────────────", font=body_font, fill=FG)
y += 60

line_height = 50

# Read todo.txt and render lines
todo_file = os.path.join(base_path, "todo.txt")
with open(todo_file, "r", encoding="utf-8") as f:
    for line in f:
        line = line.rstrip()
        if not line:
            y += line_height // 2
            continue
        draw.text((x, y), line, font=body_font, fill=FG)
        y += line_height

# Save PNG
output_file = os.path.join(base_path, "todo.png")
img.save(output_file)
print(f"Generated {output_file}")
