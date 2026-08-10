# TypoFlip 🔄

Privacy-first, open-source layout converter, password generator, and multi-script text utility built with Python and Kivy.

## Key Features
- ⚡ **Real-Time Layout Conversion**: Instant translation between Ukrainian and US QWERTY layouts.
- 🛡️ **Cybersecurity Password Mode**: Convert memorable native phrases into high-entropy, complex passwords.
- 📋 **Clipboard Integration**: One-touch copy button with instant status feedback.
- 🔒 **Privacy First**: Processed 100% locally on-device with zero network communication.

## Architecture
```text
TypoFlip/
├── .github/
│   └── workflows/
│       └── build.yml          # Automated GitHub Actions build pipeline
├── assets/
│   ├── clipboard.png          # Rendered copy checkmark icon for Kivy UI
│   ├── clipboard.svg          # Clipboard vector source
│   ├── feature_graphic.png    # Store feature banner graphic
│   ├── feature_graphic.svg    # Store feature banner vector source
│   ├── generate_assets.py     # Local SVG -> PNG asset renderer (PyMuPDF & Pillow)
│   ├── logo.png               # Primary app icon
│   ├── logo.svg               # Vector app logo source
│   └── presplash.png          # Centered rounded logo for Android splash screen
├── engines/
│   └── layout_converter.py    # Core Ukrainian/English layout conversion engine
├── buildozer.spec             # Android packaging & build configuration
├── main.py                    # Main Application entry point & Kivy UI
└── README.md