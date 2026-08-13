# TypoFlip 🔄

[![CI](https://github.com/DiegoUA/TypoFlip/actions/workflows/build.yml/badge.svg)](https://github.com/DiegoUA/TypoFlip/actions)
[![License: GPLv3](https://img.shields.io/badge/license-GPLv3-blue.svg)](LICENSE)

Privacy-first, open-source keyboard layout converter and text utility for Android and desktop. TypoFlip keeps the workflow local, fast, and easy to trust — all conversion, generation, and clipboard actions happen on-device.

Table of Contents
- [Overview](#overview)
- [Key Features](#key-features)
- [Installation](#installation)
- [Quickstart](#quickstart)
- [Project Structure](#project-structure)
- [Generating Assets](#generating-assets)
- [Testing & CI](#testing--ci)
- [Contributing](#contributing)
- [Security](#security)
- [Privacy](#privacy)
- [License](#license)

## Overview

TypoFlip is a compact utility designed to solve the common real-world problem of wrong keyboard layouts and text cleanup. It converts text between layouts in real time, helps generate secure passwords locally, and offers a responsive Android-first user experience that adapts cleanly to modern handset sizes and soft-keyboard behavior.

The project is built with Python and Kivy, with a clean separation between app logic and styling. The UI is intentionally designed to feel closer to Android 16 native app patterns while staying maintainable for future changes.

## Key Features
- Real-time conversion between Ukrainian and US QWERTY layouts.
- Local secure password generation with entropy-aware output.
- One-tap clipboard actions with quick visual feedback.
- Android-native styling with rounded surfaces, consistent button sizing, and keyboard-aware resizing.
- 100% local processing — no telemetry, no analytics, no cloud dependency.
- Open-source release under GNU GPLv3.

## Installation

Supported Python: 3.11 (tested)

Windows (recommended: use a virtual environment)

```powershell
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

Linux / WSL / macOS

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Quickstart

Run the app locally:

```bash
python main.py
```

Generate the project PNG assets used by Android packaging:

```bash
python assets/generate_assets.py
```

If the app appears blank, the icon shows a white background, or the Android asset pipeline looks stale, regenerate the icon set and rebuild the APK from the updated source. This repo now uses transparent foreground assets plus a dedicated background layer for adaptive icons.

Example of converting text via the engine:

```python
from engines.layout_converter import LayoutConverterEngine

engine = LayoutConverterEngine()
print(engine.convert("ghbdtn", mode="UKR_TO_ENG"))
```

## Project Structure

```text
TypoFlip/
├── .github/workflows/build.yml    # CI workflow for install + asset generation + tests
├── assets/                        # launcher icons, presplash, and generated PNGs
│   ├── generate_assets.py         # SVG-to-PNG generation for Android packaging
│   └── logo.svg                   # source vector asset
├── data/                          # static keyboard mapping data
│   └── character_maps.py
├── engines/                       # conversion and password logic
│   ├── layout_converter.py
│   └── password_gen.py
├── main.py                        # Kivy application entry point
├── theme.py                       # reusable Material-inspired theme definitions
├── buildozer.spec                 # Android packaging config
├── CONTRIBUTING.md                # contribution guidelines
├── SECURITY.md                    # vulnerability reporting process
├── PRIVACY_POLICY.md              # local-processing privacy terms
├── PLAY_STORE_LISTING.md          # app-store listing draft
├── CHANGELOG.md                   # release notes
├── LICENSE                        # GNU GPLv3
└── README.md                      # project overview
```

## Generating Assets

The SVG sources in `assets/` are rendered to PNGs by `assets/generate_assets.py`. This is used in CI before Android packaging so Buildozer has the required launcher and splash files.

```bash
python assets/generate_assets.py
```

For Android builds, use a Linux or WSL shell and ensure the Buildozer dependencies are installed. See [buildozer.spec](buildozer.spec).

## Testing & CI

Run the test suite locally:

```bash
pip install -r requirements-dev.txt
pytest -q
```

The project CI workflow at [.github/workflows/build.yml](.github/workflows/build.yml) installs dependencies, generates assets, and runs the test suite before packaging.

## Contributing

Contributions are welcome. Please open an issue or start a pull request on GitHub:

- https://github.com/DiegoUA/TypoFlip

Before submitting changes:
- keep PRs focused and easy to review,
- add tests for new logic,
- run the test suite locally,
- update the changelog if the change is user-facing.

## Security

TypoFlip processes data locally and does not require cloud access. If you discover a vulnerability, please follow the responsible disclosure procedure in [SECURITY.md](SECURITY.md).

## Privacy

TypoFlip does not collect, transmit, or sell personal data. All text conversion, password generation, and clipboard actions are performed on-device. See [PRIVACY_POLICY.md](PRIVACY_POLICY.md) for the full policy.

## License

This project is licensed under the GNU General Public License v3.0. See [LICENSE](LICENSE).

---

References
- Privacy policy: [PRIVACY_POLICY.md](PRIVACY_POLICY.md)
- Play Store listing draft: [PLAY_STORE_LISTING.md](PLAY_STORE_LISTING.md)
- CI workflow: [.github/workflows/build.yml](.github/workflows/build.yml)
- Build configuration: [buildozer.spec](buildozer.spec)
- Theme system: [theme.py](theme.py)
