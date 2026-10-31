"""
Process generated images:
1. Resize wallpaper to 720x1650 and save as bg.png
2. Remove white background from character art, resize, save as fg_character.png
"""
from PIL import Image, ImageDraw, ImageFilter
import numpy as np
import os

BRAIN_DIR = r"C:\Users\Dell\.gemini\antigravity\brain\8038ac24-77ba-4383-92f7-ffe061a728f3"
OUT_DIR = r"D:\ONGOING PROJECTS\MIUI_Theme\theme_src\lockscreen\advance"
WALLPAPER_DIR = r"D:\ONGOING PROJECTS\MIUI_Theme\theme_src\wallpaper"
PREVIEW_DIR = r"D:\ONGOING PROJECTS\MIUI_Theme\theme_src\preview"

# 1. Process wallpaper
bg_src = os.path.join(BRAIN_DIR, "crimson_anime_lockscreen_wallpaper_1793429723220.jpg")
bg = Image.open(bg_src).convert("RGBA")
bg = bg.resize((720, 1650), Image.LANCZOS)
bg.save(os.path.join(OUT_DIR, "bg.png"), "PNG")
bg.convert("RGB").save(os.path.join(WALLPAPER_DIR, "default_lock_wallpaper.jpg"), "JPEG", quality=95)
bg.convert("RGB").save(os.path.join(PREVIEW_DIR, "cover.jpg"), "JPEG", quality=90)
bg.convert("RGB").save(os.path.join(PREVIEW_DIR, "preview_lockscreen_0.jpg"), "JPEG", quality=90)
print(f"Wallpaper processed: {bg.size}")

# 2. Process character foreground - remove white/light background
fg_src = os.path.join(BRAIN_DIR, "fg_character_1793429740793.jpg")
fg = Image.open(fg_src).convert("RGBA")
fg = fg.resize((720, 1100), Image.LANCZOS)

# Convert to numpy for background removal
data = np.array(fg)
r, g, b, a = data[:, :, 0], data[:, :, 1], data[:, :, 2], data[:, :, 3]

# Compute luminance
luminance = 0.299 * r.astype(float) + 0.587 * g.astype(float) + 0.114 * b.astype(float)

# Create alpha mask: bright pixels become transparent
# Threshold: pixels with luminance > 200 are mostly background
alpha_mask = np.where(luminance > 200, 0,
             np.where(luminance > 160, ((200 - luminance) / 40.0 * 255).astype(int),
             255)).astype(np.uint8)

# Also fade very light/desaturated edge pixels
saturation = np.max(data[:, :, :3], axis=2).astype(float) - np.min(data[:, :, :3], axis=2).astype(float)
desat_mask = np.where((saturation < 30) & (luminance > 140), 0, 255).astype(np.uint8)
alpha_mask = np.minimum(alpha_mask, desat_mask)

# Apply soft edge feathering
data[:, :, 3] = alpha_mask
fg = Image.fromarray(data)

# Slight gaussian blur on edges for natural blending
fg_blurred_alpha = fg.split()[3].filter(ImageFilter.GaussianBlur(radius=1.5))
fg.putalpha(fg_blurred_alpha)

fg.save(os.path.join(OUT_DIR, "fg_character.png"), "PNG")
print(f"Character foreground processed: {fg.size}")
print("Done.")
