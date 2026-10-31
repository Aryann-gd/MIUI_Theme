"""
Procedural Asset Generator for POCO M6 5G (720 x 1650)
Generates non-copyrighted PNG placeholder graphics matching the Sukuna Crimson theme specification.
"""
import os
import math
from PIL import Image, ImageDraw, ImageFilter

BASE_DIR = r"D:\ONGOING PROJECTS\MIUI_Theme\theme_src"
LOCKSCREEN_DIR = os.path.join(BASE_DIR, "lockscreen", "advance")
WALLPAPER_DIR = os.path.join(BASE_DIR, "wallpaper")
PREVIEW_DIR = os.path.join(BASE_DIR, "preview")

for d in [LOCKSCREEN_DIR, WALLPAPER_DIR, PREVIEW_DIR]:
    os.makedirs(d, exist_ok=True)

def generate_background():
    img = Image.new("RGBA", (720, 1650), (10, 13, 18, 255))
    draw = ImageDraw.Draw(img)
    
    # Crimson radial aura center
    center_x, center_y = 360, 950
    for r in range(450, 0, -10):
        alpha = int(35 * (1.0 - (r / 450.0)))
        draw.ellipse(
            [center_x - r, center_y - r, center_x + r, center_y + r],
            fill=(255, 46, 46, alpha)
        )
    
    # Atmospheric upper haze
    for y in range(0, 400):
        alpha = int(25 * (1.0 - (y / 400.0)))
        draw.line([(0, y), (720, y)], fill=(30, 36, 48, alpha))
        
    bg_png = os.path.join(LOCKSCREEN_DIR, "bg.png")
    img.save(bg_png, "PNG")
    
    # Also save as wallpaper and previews
    bg_rgb = img.convert("RGB")
    bg_rgb.save(os.path.join(WALLPAPER_DIR, "default_lock_wallpaper.jpg"), "JPEG", quality=95)
    bg_rgb.save(os.path.join(PREVIEW_DIR, "cover.jpg"), "JPEG", quality=90)
    bg_rgb.save(os.path.join(PREVIEW_DIR, "preview_lockscreen_0.jpg"), "JPEG", quality=90)
    print(f"Generated: {bg_png}")

def generate_widget_timer():
    img = Image.new("RGBA", (120, 120), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    # Background circle
    draw.ellipse([4, 4, 116, 116], fill=(30, 36, 48, 120), outline=(255, 255, 255, 220), width=4)
    # Hourglass icon
    pts_top = [(42, 38), (78, 38), (60, 60)]
    pts_bot = [(60, 60), (78, 82), (42, 82)]
    draw.polygon(pts_top, outline=(255, 255, 255, 240), width=2)
    draw.polygon(pts_bot, outline=(255, 255, 255, 240), width=2)
    path = os.path.join(LOCKSCREEN_DIR, "widget_timer.png")
    img.save(path, "PNG")
    print(f"Generated: {path}")

def generate_widget_calendar():
    img = Image.new("RGBA", (120, 120), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    # Outer progress arc (270 degrees)
    draw.arc([4, 4, 116, 116], start=135, end=405, fill=(255, 255, 255, 220), width=4)
    path = os.path.join(LOCKSCREEN_DIR, "widget_calendar.png")
    img.save(path, "PNG")
    print(f"Generated: {path}")

def generate_widget_profile():
    img = Image.new("RGBA", (120, 120), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    # Translucent circle fill
    draw.ellipse([4, 4, 116, 116], fill=(50, 58, 72, 160))
    # Silhouette: head
    draw.ellipse([46, 32, 74, 60], fill=(255, 255, 255, 240))
    # Silhouette: shoulders
    draw.pieslice([30, 64, 90, 110], start=180, end=360, fill=(255, 255, 255, 240))
    path = os.path.join(LOCKSCREEN_DIR, "widget_profile.png")
    img.save(path, "PNG")
    print(f"Generated: {path}")

def generate_icon_camera():
    img = Image.new("RGBA", (48, 48), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    draw.rounded_rectangle([6, 12, 42, 38], radius=4, outline=(255, 255, 255, 240), width=3)
    draw.ellipse([18, 18, 30, 30], outline=(255, 255, 255, 240), width=3)
    draw.rectangle([14, 8, 22, 12], fill=(255, 255, 255, 240))
    path = os.path.join(LOCKSCREEN_DIR, "icon_camera.png")
    img.save(path, "PNG")
    print(f"Generated: {path}")

def generate_icon_torch():
    img = Image.new("RGBA", (48, 48), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    draw.polygon([(16, 8), (32, 8), (28, 20), (20, 20)], fill=(255, 255, 255, 240))
    draw.rectangle([20, 20, 28, 40], fill=(255, 255, 255, 240))
    draw.ellipse([22, 26, 26, 30], fill=(10, 13, 18, 255))
    path = os.path.join(LOCKSCREEN_DIR, "icon_torch.png")
    img.save(path, "PNG")
    print(f"Generated: {path}")

if __name__ == "__main__":
    generate_background()
    generate_widget_timer()
    generate_widget_calendar()
    generate_widget_profile()
    generate_icon_camera()
    generate_icon_torch()
    print("All procedural placeholder assets successfully generated.")

