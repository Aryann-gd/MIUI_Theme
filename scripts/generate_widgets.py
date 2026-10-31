"""
Improved widget and icon asset generator - frosted glass circular widgets
matching the reference lockscreen aesthetic.
"""
import os
import math
from PIL import Image, ImageDraw, ImageFilter, ImageFont

LOCKSCREEN_DIR = r"D:\ONGOING PROJECTS\MIUI_Theme\theme_src\lockscreen\advance"
os.makedirs(LOCKSCREEN_DIR, exist_ok=True)

def generate_frosted_circle(size=140, border_color=(255, 255, 255, 180), fill_color=(40, 45, 55, 100)):
    """Create a frosted glass circular widget base."""
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    pad = 4
    # Outer glow
    for i in range(6, 0, -1):
        alpha = int(15 * (7 - i))
        draw.ellipse([pad - i, pad - i, size - pad + i, size - pad + i],
                      fill=(255, 255, 255, alpha // 4))
    # Fill
    draw.ellipse([pad, pad, size - pad, size - pad], fill=fill_color)
    # Border
    draw.ellipse([pad, pad, size - pad, size - pad], outline=border_color, width=3)
    return img


def generate_widget_timer():
    base = generate_frosted_circle(140)
    draw = ImageDraw.Draw(base)
    cx, cy = 70, 70
    # Hourglass shape
    draw.polygon([(cx - 18, cy - 28), (cx + 18, cy - 28), (cx + 4, cy - 2), (cx - 4, cy - 2)],
                 fill=(255, 255, 255, 220))
    draw.polygon([(cx - 4, cy + 2), (cx + 4, cy + 2), (cx + 18, cy + 28), (cx - 18, cy + 28)],
                 fill=(255, 255, 255, 220))
    # Sand particles
    for angle in range(0, 360, 45):
        px = cx + int(8 * math.cos(math.radians(angle)))
        py = cy + int(8 * math.sin(math.radians(angle)))
        draw.ellipse([px - 1, py - 1, px + 1, py + 1], fill=(255, 255, 255, 160))
    # Strike-through X
    draw.line([(cx - 22, cy - 22), (cx + 22, cy + 22)], fill=(255, 255, 255, 200), width=3)
    draw.line([(cx + 22, cy - 22), (cx - 22, cy + 22)], fill=(255, 255, 255, 200), width=3)
    base.save(os.path.join(LOCKSCREEN_DIR, "widget_timer.png"), "PNG")
    print("Generated widget_timer.png")


def generate_widget_calendar():
    base = generate_frosted_circle(140)
    draw = ImageDraw.Draw(base)
    cx, cy = 70, 70
    # Moon crescent
    draw.ellipse([cx - 20, cy - 32, cx + 8, cy - 4], fill=(255, 255, 255, 220))
    draw.ellipse([cx - 12, cy - 34, cx + 10, cy - 6], fill=(0, 0, 0, 0))
    # Arc progress ring (partial)
    draw.arc([12, 12, 128, 128], start=200, end=520, fill=(255, 255, 255, 200), width=3)
    base.save(os.path.join(LOCKSCREEN_DIR, "widget_calendar.png"), "PNG")
    print("Generated widget_calendar.png")


def generate_widget_profile():
    base = generate_frosted_circle(140)
    draw = ImageDraw.Draw(base)
    cx, cy = 70, 70
    # Head
    draw.ellipse([cx - 14, cy - 26, cx + 14, cy - 2], fill=(255, 255, 255, 220))
    # Shoulders
    draw.pieslice([cx - 28, cy + 2, cx + 28, cy + 38], start=180, end=360,
                  fill=(255, 255, 255, 220))
    base.save(os.path.join(LOCKSCREEN_DIR, "widget_profile.png"), "PNG")
    print("Generated widget_profile.png")


def generate_icon_camera():
    size = 64
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    # Camera body
    draw.rounded_rectangle([8, 16, 56, 50], radius=6, outline=(255, 255, 255, 220), width=3)
    # Lens
    draw.ellipse([24, 24, 40, 40], outline=(255, 255, 255, 220), width=3)
    # Flash bump
    draw.rectangle([18, 10, 30, 16], fill=(255, 255, 255, 220))
    img.save(os.path.join(LOCKSCREEN_DIR, "icon_camera.png"), "PNG")
    print("Generated icon_camera.png")


def generate_icon_torch():
    size = 64
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    # Flashlight body
    draw.polygon([(24, 10), (40, 10), (36, 26), (28, 26)], fill=(255, 255, 255, 220))
    draw.rectangle([28, 26, 36, 52], fill=(255, 255, 255, 220))
    # Beam dot
    draw.ellipse([30, 4, 34, 8], fill=(255, 200, 100, 200))
    img.save(os.path.join(LOCKSCREEN_DIR, "icon_torch.png"), "PNG")
    print("Generated icon_torch.png")


if __name__ == "__main__":
    generate_widget_timer()
    generate_widget_calendar()
    generate_widget_profile()
    generate_icon_camera()
    generate_icon_torch()
    print("All improved widget assets generated.")
