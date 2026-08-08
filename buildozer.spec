[app]

# (str) Title of your application
title = TypoFlip

# (str) Package name (lower case, single word recommended)
package.name = typoflip

# (str) Package domain (needed for android packaging)
package.domain = com.typoflip

# (str) Source code location where main.py resides
source.dir = .

# (list) Source files extensions to include
source.include_exts = py,png,jpg,kv,atlas,json,txt

# (str) Application versioning
version = 0.1

# (list) Application requirements
# Add any extra PyPI packages your app imports here (e.g., requests, urllib3)
requirements = python3,kivy

# (str) Supported orientation (portrait, landscape, sensorLandscape, or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen
fullscreen = 0

#
# Android specific options
#

# (list) Permissions required by your application
android.permissions = INTERNET

# (int) Target Android API (API 33 is standard for current Play Store targets)
android.api = 33

# (int) Minimum API supported by your APK
android.minapi = 21

# (bool) Automatically accept Android SDK licenses
android.accept_sdk_license = True

# (bool) Enable AndroidX support (Required for API 28+)
android.enable_androidx = True

# (list) List of Android architectures to build for
# Standardized to arm64-v8a to ensure fast build times on CI/CD runners
android.archs = arm64-v8a

#
# Python-for-Android (p4a) specific fixes
#

# Forces Buildozer to pull the latest p4a toolchain to bypass pip import errors
p4a.fork = kivy
p4a.branch = master


[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug with command output)
log_level = 2

# (int) Display warning if buildozer is run as root (0 = false, 1 = true)
warn_on_root = 1