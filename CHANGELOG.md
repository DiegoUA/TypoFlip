# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

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
- Resolved the broken widget initialization issues that were preventing the UI from being constructed cleanly.
- Fixed the launcher icon generation pipeline to produce transparent foreground assets and proper adaptive background files.
- Stabilized asset generation, local setup, and CI execution for consistent builds.
