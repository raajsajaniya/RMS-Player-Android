[app]
title = RMS Player
package.name = rmsplayer
package.domain = org.rms
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0

# Requirements (Critical for KivyMD)
requirements = python3,kivy==2.2.0,kivymd==1.1.1,requests,urllib3,openssl,ffpyplayer,sdl2_ttf==2.20.2,pillow

# Permissions
android.permissions = INTERNET,ACCESS_NETWORK_STATE

# Screen orientation
orientation = portrait

# Android Specifics
fullscreen = 0
android.archs = arm64-v8a
android.api = 33
android.minapi = 24
android.ndk = 25b
p4a.branch = master

[buildozer]
log_level = 2
warn_on_root = 1