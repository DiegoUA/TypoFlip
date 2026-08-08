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
├── main.py                  # Kivy UI layout & entry point
├── engines/                 # Business logic & security algorithms
│   ├── layout_converter.py
│   └── password_gen.py
└── data/                    # Mappings and datasets
    └── character_maps.py