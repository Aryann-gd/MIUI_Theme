"""
Boot Animation Generator for POCO M6 5G (HyperOS 2.0)
Resolution: 720 x 1650 px @ 30 fps (75 frames, 2.5 seconds)
Format: Uncompressed store-only zip (ZIP_STORED) containing desc.txt and part0/
Outputs to: theme_src/boots/bootanimation.zip (and theme_src/bootanimation.zip fallback)
"""
import os
import shutil
import zipfile
from PIL import Image, ImageDraw

FRAME_WIDTH = 720
FRAME_HEIGHT = 1650
FPS = 30
TOTAL_FRAMES = 75

TMP_DIR = r"D:\ONGOING PROJECTS\MIUI_Theme\build_tmp\bootanimation"
PART0_DIR = os.path.join(TMP_DIR, "part0")
BOOTS_OUTPUT_ZIP = r"D:\ONGOING PROJECTS\MIUI_Theme\theme_src\boots\bootanimation.zip"
ROOT_OUTPUT_ZIP = r"D:\ONGOING PROJECTS\MIUI_Theme\theme_src\bootanimation.zip"

os.makedirs(PART0_DIR, exist_ok=True)
os.makedirs(os.path.dirname(BOOTS_OUTPUT_ZIP), exist_ok=True)

print(f"Generating {TOTAL_FRAMES} frames ({FRAME_WIDTH}x{FRAME_HEIGHT} @ {FPS}fps)...")

for i in range(TOTAL_FRAMES):
    progress = i / float(TOTAL_FRAMES - 1)
    img = Image.new("RGBA", (FRAME_WIDTH, FRAME_HEIGHT), (10, 13, 18, 255))
    draw = ImageDraw.Draw(img)
    
    cx, cy = FRAME_WIDTH // 2, FRAME_HEIGHT // 2
    
    # Pulsing crimson core aura
    pulse = (1.0 - abs(progress - 0.5) * 2.0)
    core_radius = int(80 + 180 * progress)
    
    for r in range(core_radius, 0, -12):
        alpha = int(45 * (1.0 - (r / float(core_radius))) * pulse)
        draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(255, 46, 46, alpha))
        
    # Concentric cursed energy shockwaves
    for wave in range(3):
        wave_phase = (progress * 2.0 + wave * 0.33) % 1.0
        wave_r = int(60 + 320 * wave_phase)
        wave_alpha = int(220 * (1.0 - wave_phase) * pulse)
        if wave_alpha > 0 and wave_r > 0:
            draw.ellipse(
                [cx - wave_r, cy - wave_r, cx + wave_r, cy + wave_r],
                outline=(255, 60, 60, wave_alpha),
                width=3
            )
            
    # Minimalist central torii silhouette / geometric mark
    torii_alpha = int(min(255, progress * 400))
    if torii_alpha > 0:
        # Crossbars
        draw.rectangle([cx - 90, cy - 50, cx + 90, cy - 42], fill=(230, 235, 242, torii_alpha))
        draw.rectangle([cx - 110, cy - 70, cx + 110, cy - 60], fill=(255, 46, 46, torii_alpha))
        # Pillars
        draw.rectangle([cx - 55, cy - 60, cx - 45, cy + 80], fill=(230, 235, 242, torii_alpha))
        draw.rectangle([cx + 45, cy - 60, cx + 55, cy + 80], fill=(230, 235, 242, torii_alpha))

    # Convert to RGB and save PNG
    frame_rgb = img.convert("RGB")
    frame_path = os.path.join(PART0_DIR, f"{i:05d}.png")
    frame_rgb.save(frame_path, "PNG", compress_level=1)

# Write desc.txt (strictly requires trailing newline)
desc_path = os.path.join(TMP_DIR, "desc.txt")
with open(desc_path, "w", newline="\n") as f:
    f.write(f"{FRAME_WIDTH} {FRAME_HEIGHT} {FPS}\n")
    f.write("p 1 0 part0\n")

print("Building store-only uncompressed bootanimation.zip...")

def build_zip(target_path):
    with zipfile.ZipFile(target_path, "w", compression=zipfile.ZIP_STORED) as zf:
        zf.write(desc_path, "desc.txt")
        for frame_file in sorted(os.listdir(PART0_DIR)):
            abs_frame = os.path.join(PART0_DIR, frame_file)
            zf.write(abs_frame, os.path.join("part0", frame_file))
    size_mb = os.path.getsize(target_path) / (1024 * 1024)
    print(f"Created: {target_path} ({size_mb:.2f} MB)")

build_zip(BOOTS_OUTPUT_ZIP)
build_zip(ROOT_OUTPUT_ZIP)

print("Boot animation build complete.")

