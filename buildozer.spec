[app]

# (str) Title of your application
title = TypoFlip

# (str) Icon of the application
icon.filename = %(source.dir)s/logo.png

# (str) Presplash of the application (the image shown during app loading)
presplash.filename = %(source.dir)s/logo.png

# (str) Presplash background color (for Android)
presplash.color = #1E1E1E

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
requirements = python3,kivy

# (str) Supported orientation
orientation = portrait

# (bool) Indicate if the application should be fullscreen
fullscreen = 0

#
# Android specific options
#

# (list) Permissions required by your application
android.permissions = 

# (int) Target Android API (API 36 for Android 16 compliance)
android.api = 36

# (int) Minimum API supported by your APK
android.minapi = 24

# (bool) Automatically accept Android SDK licenses
android.accept_sdk_license = True

# (bool) Enable AndroidX support
android.enable_androidx = True

# (list) List of Android architectures to build for
android.archs = arm64-v8a

#
# Python-for-Android (p4a) specific settings
#

# Use p4a master branch for upstream Android 16 / SDK 36 toolchain fixes
p4a.fork = kivy
p4a.branch = master


[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug with command output)
log_level = 2

# (int) Display warning if buildozer is run as root
warn_on_root = 1