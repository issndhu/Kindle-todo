from PIL import Image, ImageDraw, ImageFont

WIDTH = 600
HEIGHT = 800

BG = 255
FG = 0

img = Image.new("L", (WIDTH, HEIGHT), BG)
draw = ImageDraw.Draw(img)

title_font = ImageFont.truetype("JetBrainsMono-Bold.ttf", 42)
body_font  = ImageFont.truetype("JetBrainsMonoNL-Regular.ttf", 30)

x = 60
y = 80

# Title
draw.text((x, y), "TODO — TODAY", font=title_font, fill=FG)
y += 70

# Separator line (terminal style)
draw.text((x, y), "────────────", font=body_font, fill=FG)
y += 60

line_height = 50

with open("todo.txt", "r", encoding="utf-8") as f:
    for line in f:
        line = line.rstrip()
        if not line:
            y += line_height // 2
            continue
        draw.text((x, y), line, font=body_font, fill=FG)
        y += line_height

img.save("todo.png")
print("Generated todo.png")
