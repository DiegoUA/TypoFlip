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
│       └── build.yml          # Automated release workflow
├── assets/
│   ├── generate_assets.py     # Local SVG -> PNG converter (PyMuPDF)
│   ├── logo.svg               # Vector app logo
│   ├── logo.png               # Rendered app icon & splash asset
│   ├── feature_graphic.svg    # Store feature banner source
│   ├── feature_graphic.png    # Store feature banner graphic
│   ├── clipboard.svg          # Clipboard success icon vector
│   └── clipboard.png          # Rendered clipboard icon for Kivy UI
├── buildozer.spec             # Android build & packaging configuration
├── main.py                    # Main Application logic & Kivy UI
└── README.md