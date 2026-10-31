# Sukuna Crimson - Xiaomi HyperOS 2.0 / MIUI Theme

A custom personal `.mtz` theme designed specifically for **POCO M6 5G** (Dimensity 6100+, 720 x 1650 px, 90 Hz display) running **Xiaomi HyperOS 2.0** (Android 15).

## Features
- **Dynamic Reactive Lockscreen (MAML):**
  - Ultra-condensed display typography (`Antonio` OFL 1.1).
  - Physics-based interactive drag: The clock follows your finger with damping (0.4x), fades alpha, and scales smoothly.
  - Spring-back return: Dynamic recovery using `<VariableAnimation>` with `BackEaseOut` easing curve.
  - Swipe-up unlock threshold: Smooth threshold trigger at `-260 px` without blocking system status bar or navigation gesture areas.
  - Information widgets: Hourglass timer, calendar progress arc, profile shortcut, flashlight toggle, and camera quick launch.
- **Custom Boot Animation:**
  - 720 x 1650 @ 30 fps uncompressed store-only zip (`bootanimation.zip`, 3.47 MB).
  - Concentric cursed energy pulse shockwaves and torii gate silhouette.
- **Ready-to-Install MTZ Package:**
  - Packaged at `dist/Sukuna_Crimson.mtz` (3.50 MB).

## Project Structure
```text
MIUI_Theme/
├── dist/
│   └── Sukuna_Crimson.mtz              # Compiled theme package ready for device install
├── theme_src/
│   ├── description.xml                 # Theme metadata (uiVersion=16, miuiAdapterVersion=4.0)
│   ├── preview/                        # Theme manager catalog and lockscreen previews
│   ├── wallpaper/                      # System fallback lockscreen wallpaper
│   ├── boots/                          # Boot animation package
│   └── lockscreen/
│       └── advance/
│           ├── manifest.xml            # MAML engine markup (reactive clock & triggers)
│           ├── clock.ttf               # Antonio-Bold condensed typography
│           └── *.png                   # Procedural lockscreen assets
├── scripts/
│   ├── generate_assets.py              # Procedural PNG asset generator
│   ├── generate_bootanimation.py       # 30 fps boot animation frame builder
│   └── build_mtz.py                    # Production MTZ packager
├── preview_simulator.html              # Standalone interactive 1:1 HTML5 lockscreen simulator
├── design_spec.json                    # Display geometry and color tokens
└── instructions.md                     # Engineering guidelines and specifications
```

## How to Preview

### Method 1: VS Code Lockscreen Preview Extension
1. Open [`theme_src/lockscreen/advance/manifest.xml`](file:///d:/ONGOING%20PROJECTS/MIUI_Theme/theme_src/lockscreen/advance/manifest.xml).
2. Look at the top-right editor tab bar and click the **phone icon** (`打开锁屏预览` / Open Lockscreen Preview).
   - Alternatively, press `Ctrl + Shift + P`, type **`打开锁屏预览`** or `lockscreen-preview.openPreview`, and hit Enter.
3. The preview panel will open alongside your code, updating in real time as you edit.

### Method 2: Standalone Interactive Simulator
Open [`preview_simulator.html`](file:///d:/ONGOING%20PROJECTS/MIUI_Theme/preview_simulator.html) in your browser or VS Code Simple Browser. It runs an exact replica of the MAML spring equations, touch coordinates, and unlock threshold.

## Building the MTZ Package
Run the packaging script using Python:
```bash
python scripts/build_mtz.py
```
The output `.mtz` is generated in `dist/Sukuna_Crimson.mtz`.

## Installation on POCO M6 5G (HyperOS 2.0)
1. Transfer `dist/Sukuna_Crimson.mtz` to your phone's internal storage.
2. Install **ChaoMe Theme Editor** (or official MIUI Theme Editor) from Google Play.
3. In ChaoMe Theme Editor:
   - Tap **Browse** and select `Sukuna_Crimson.mtz`.
   - Tap **Start** > **Next** > **Finish** > **Install**.
4. Open the built-in **Themes** app > **My account** > **Themes** > select **Sukuna Crimson** > tap **Apply**.

## License
Refer to [LICENSE.md](LICENSE.md).
