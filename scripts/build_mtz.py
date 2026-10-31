"""
MTZ Theme Packager for HyperOS 2.0 / POCO M6 5G
Builds production-ready .mtz theme package adhering strictly to Xiaomi MTZ internal archive grammar.
"""
import os
import shutil
import zipfile

BASE_DIR = r"D:\ONGOING PROJECTS\MIUI_Theme"
THEME_SRC = os.path.join(BASE_DIR, "theme_src")
BUILD_TMP = os.path.join(BASE_DIR, "build_tmp")
DIST_DIR = os.path.join(BASE_DIR, "dist")
OUTPUT_MTZ = os.path.join(DIST_DIR, "Sukuna_Crimson.mtz")

os.makedirs(BUILD_TMP, exist_ok=True)
os.makedirs(DIST_DIR, exist_ok=True)

def package_sub_module(source_dir, archive_name):
    """Packages a module into an unextended zip archive (e.g. 'lockscreen' or 'icons')."""
    zip_target = os.path.join(BUILD_TMP, archive_name)
    if os.path.exists(zip_target):
        os.remove(zip_target)
    with zipfile.ZipFile(zip_target, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for root, dirs, files in os.walk(source_dir):
            for file in files:
                abs_path = os.path.join(root, file)
                rel_path = os.path.relpath(abs_path, source_dir)
                zf.write(abs_path, rel_path)
    print(f"Packed sub-module '{archive_name}' ({os.path.getsize(zip_target):,} bytes)")
    return zip_target

def build_mtz():
    print("Building Sukuna Crimson MTZ Theme Package...")
    
    # 1. Package lockscreen sub-archive
    lockscreen_src = os.path.join(THEME_SRC, "lockscreen")
    lockscreen_archive = package_sub_module(lockscreen_src, "lockscreen")
    
    # 2. Package icons sub-module placeholder if exists
    icons_src = os.path.join(THEME_SRC, "icons_src")
    icons_archive = None
    if os.path.exists(icons_src):
        icons_archive = package_sub_module(icons_src, "icons")
        
    # 3. Create final .mtz container
    if os.path.exists(OUTPUT_MTZ):
        os.remove(OUTPUT_MTZ)
        
    with zipfile.ZipFile(OUTPUT_MTZ, "w", compression=zipfile.ZIP_DEFLATED) as mtz:
        # description.xml
        desc_path = os.path.join(THEME_SRC, "description.xml")
        mtz.write(desc_path, "description.xml")
        
        # lockscreen archive (no extension)
        mtz.write(lockscreen_archive, "lockscreen")
        
        # icons archive if present
        if icons_archive and os.path.exists(icons_archive):
            mtz.write(icons_archive, "icons")
            
        # preview files
        preview_dir = os.path.join(THEME_SRC, "preview")
        if os.path.exists(preview_dir):
            for f in os.listdir(preview_dir):
                mtz.write(os.path.join(preview_dir, f), os.path.join("preview", f))
                
        # wallpaper files
        wallpaper_dir = os.path.join(THEME_SRC, "wallpaper")
        if os.path.exists(wallpaper_dir):
            for f in os.listdir(wallpaper_dir):
                mtz.write(os.path.join(wallpaper_dir, f), os.path.join("wallpaper", f))
                
        # boots directory
        boots_zip = os.path.join(THEME_SRC, "boots", "bootanimation.zip")
        if os.path.exists(boots_zip):
            mtz.write(boots_zip, "boots/bootanimation.zip")
            
        # fallback root bootanimation.zip
        root_boot_zip = os.path.join(THEME_SRC, "bootanimation.zip")
        if os.path.exists(root_boot_zip):
            mtz.write(root_boot_zip, "bootanimation.zip")

    size_mb = os.path.getsize(OUTPUT_MTZ) / (1024 * 1024)
    print(f"SUCCESS: Package created at '{OUTPUT_MTZ}' ({size_mb:.2f} MB)")

if __name__ == "__main__":
    build_mtz()

