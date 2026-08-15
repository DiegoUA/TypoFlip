# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.32] - 2026-08-16

### Fixed
- **Thread-Safe Insets Handling (Android 15/16):** Removed the JNI-based `View.OnApplyWindowInsetsListener` interface to eliminate cross-thread interpreter crashes caused by Android UI thread callbacks during keyboard events. Replaced with a Kivy `Clock`-scheduled polling mechanism using `getRootWindowInsets()` directly on Kivy's thread.
- **Insets Error Visibility:** Replaced silent `try/except: pass` blocks in inset initialization with explicit logging to prevent silent failures during window inset detection.

---

## [0.1.31] - 2026-08-16

### Fixed
- **Edge-to-Edge Status Bar Overlap (Android 15/16):** Replaced one-shot `get_status_bar_height()` static lookup and hardcoded 12dp fallback with dynamic window insets processing for gesture navigation, orientation shifts, and API 36 edge-to-edge requirements.
- **`MaterialButton` Text Truncation & Garbling:** Moved `text_size` recalculation inside `_update_canvas` so text bounding updates dynamically on every size/position change rather than once during `__init__` before Kivy layout passes. Prevents button text (e.g., "Copy to Clipboard") from wrapping onto stale 100x100 default widget boundaries, and added `shorten=True` safety handling.
- **`MaterialTextInput` Hint Text Visibility:** Added explicit `hint_text` color definitions to light and dark theme palettes in `theme.py`. Bound `hint_text_color` and `disabled_foreground_color` properties to guarantee proper contrast against dark surface colors instead of falling back to Kivy default text colors.

---

## [0.1.30] - 2026-08-10

### Added
- Android-first Material-inspired theme layer in `theme.py` for cleaner reuse and future styling changes.
- Responsive Kivy layout refinements for smaller screens and keyboard-aware resizing.
- Asset and packaging metadata alignment for better Android launcher and splash compatibility.
- Standard project docs for contributing, security disclosure, privacy, and release messaging.
- Transparent adaptive icon generation flow with dedicated foreground and background layers for GitHub Actions / Android packaging.

### Changed
- Refined the app to behave like a native Android 16-style experience with rounded surfaces, even button sizing, and system-managed safe-area behavior.
- Updated the Kivy app entry point to use the reusable theme system instead of ad hoc styling.
- Tightened the README and release copy to match the actual product status and GPLv3 licensing.
- Normalized project metadata and documentation to reflect an open-source, privacy-first toolchain.
- Switched GitHub build validation to fail fast when generated Android assets are missing or invalid.

### Fixed
- Removed fixed status-bar padding in favor of system-aware layout behavior.
- Corrected action button alignment and sizing so Copy and Clear are equal-sized and centered.
- Improved input/output field responsiveness so both remain visible with the Android keyboard open.
- Resolved broken widget initialization issues that were preventing the UI from being constructed cleanly.
- Fixed the launcher icon generation pipeline to produce transparent foreground assets and proper adaptive background files.
- Stabilized asset generation, local setup, and CI execution for consistent builds.