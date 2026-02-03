[app]
# (1) App title shown on phone
title = MyKivyApp

# (2) Package name (lowercase, no spaces)
package.name = mykivyapp

# (3) Package domain (reverse domain)
package.domain = org.example

# (4) Source code location
source.dir = .
source.include_exts = py,png,jpg,kv

# (5) App version
version = 0.1

# (6) Python & Kivy only (VERY IMPORTANT)
requirements = python3,kivy

# (7) App orientation
orientation = portrait

# (8) Fullscreen mode
fullscreen = 1


# -------------------------
# ANDROID CONFIGURATION
# -------------------------

# Minimum Android version (Android 5.0)
android.minapi = 21

# Target Android version (safe & stable)
android.api = 31

# NDK version (DO NOT CHANGE)
android.ndk = 25b

# Use AndroidX
android.enable_androidx = 1

# Permissions (none needed now)
android.permissions = INTERNET


# -------------------------
# BUILD OPTIONS
# -------------------------

[buildozer]
log_level = 2
warn_on_root = 1
