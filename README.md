# TypoFlip 🔄

[![CI](https://github.com/DiegoUA/TypoFlip/actions/workflows/build.yml/badge.svg)](https://github.com/DiegoUA/TypoFlip/actions)
[![License: GPLv3](https://img.shields.io/badge/license-GPLv3-blue.svg)](C:/Users/maksi/OneDrive/Projects/Python/TypoFlip/LICENSE)

Privacy-first, open-source layout converter, password generator, and text utility built with Python and Kivy. All processing happens on-device — no network communication, no tracking.

Table of Contents
- [Key Features](#key-features)
- [Screenshots](#screenshots)
- [Installation](#installation)
- [Quickstart](#quickstart)
- [Usage](#usage)
- [Architecture](#architecture)
- [Generating Assets](#generating-assets)
- [Tests & CI](#tests--ci)
- [Contributing](#contributing)
- [Security](#security)
- [License](#license)

Key Features
- Real-time layout conversion between Ukrainian and US QWERTY layouts.
- Local password generator that calculates entropy for produced strings.
- One-tap clipboard integration with status feedback.
- 100% local processing — no telemetry, no analytics, no network access.

Screenshots
- See the `assets/` folder for app icons and presplash assets (e.g., presplash.png and icon_foreground.png).

Installation
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

Quickstart

Run the desktop app (Kivy):

```bash
python main.py
```

Library usage (layout conversion engine):

```python
from engines.layout_converter import LayoutConverterEngine
engine = LayoutConverterEngine()
print(engine.convert("ghbdtn", mode="UKR_TO_ENG"))  # sample usage
```

Usage
- Open the app, enter or paste text, results update in real time.
- Use "Copy to Clipboard" to copy converted text.
- Use the password entropy helper from the UI (if exposed) or via engines/password_gen.py.

Architecture

High-level project layout

```text
TypoFlip/
├── .github/workflows/build.yml    # CI build & packaging
├── assets/                        # icons and generated PNG assets
│   └── generate_assets.py         # helper to render SVGs (PyMuPDF + Pillow)
├── data/                          # static character maps
│   └── character_maps.py
├── engines/                       # conversion and password engines
│   ├── layout_converter.py
│   └── password_gen.py
├── main.py                        # Kivy application entry point
├── buildozer.spec                 # Android packaging configuration
├── PRIVACY_POLICY.md              # privacy statement (local processing)
├── PLAY_STORE_LISTING.md          # store listing text
└── LICENSE                        # GPLv3 license
```

Generating Assets

Assets SVGs are rendered to PNGs by `assets/generate_assets.py`. This is used in CI before packaging so Buildozer has PNG assets available.

```bash
python assets/generate_assets.py
```

If building for Android locally, prefer building on Linux or WSL and ensure Buildozer requirements are met. See [buildozer.spec](C:/Users/maksi/OneDrive/Projects/Python/TypoFlip/buildozer.spec).

Tests & CI

Run unit tests locally with pytest:

```bash
pip install -r requirements-dev.txt
pytest -q
```

CI
- The GitHub Actions workflow that builds release APKs is at `.github/workflows/build.yml` — it now installs Python deps and generates assets in CI prior to packaging.

Contributing
- Contributions are welcome. Please open issues or PRs on GitHub: https://github.com/DiegoUA/TypoFlip
- Add tests for new features and run the test suite locally.

Security
- TypoFlip processes all data locally and does not collect or transmit user data. For security issues, open a private issue on GitHub if disclosure requires confidentiality.

License
- This project is licensed under the GNU GPLv3. See [LICENSE](C:/Users/maksi/OneDrive/Projects/Python/TypoFlip/LICENSE).

References
- Privacy policy: [PRIVACY_POLICY.md](C:/Users/maksi/OneDrive/Projects/Python/TypoFlip/PRIVACY_POLICY.md)
- Play Store listing draft: [PLAY_STORE_LISTING.md](C:/Users/maksi/OneDrive/Projects/Python/TypoFlip/PLAY_STORE_LISTING.md)
- CI workflow: [.github/workflows/build.yml](C:/Users/maksi/OneDrive/Projects/Python/TypoFlip/.github/workflows/build.yml)
- Build configuration: [buildozer.spec](C:/Users/maksi/OneDrive/Projects/Python/TypoFlip/buildozer.spec)

---

Notes / Recommendations
- Consider committing generated PNG assets (logo.png, presplash.png, icon_foreground.png) to avoid depending on PyMuPDF during local mobile builds.
- Add a `requirements.txt` and a `requirements-dev.txt` (pytest, black) — these have been added by the automation changes.
- Add basic CONTRIBUTING.md and SECURITY.md if you want to formalize contribution and vulnerability reporting procedures.
