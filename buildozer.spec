[app]

# Title and Package details
title = TypoFlip
package.name = typoflip
package.domain = org.typoflip

# Source files
source.dir = .
source.include_exts = py,png,jpg,kv,atlas

# Application details
version = 0.1
requirements = python3==3.11.0,kivy
orientation = portrait
fullscreen = 0

# Android SDK & NDK configuration
android.accept_sdk_license = True
android.api = 33
android.minapi = 21
android.ndk = 25b
android.ndk_api = 21

[buildozer]
log_level = 2
warn_on_root = 1