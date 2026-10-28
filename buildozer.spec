[app]
# ---- Unique identity: final Android ID = package.domain + "." + package.name ----
# Result: com.oneai.customapp2  (different from your old app, so both stay installed)
title = One AI 2
package.name = customapp2
package.domain = com.oneai

source.dir = .
source.include_exts = py,png,jpg,html,json,js
version = 1.0.0

requirements = python3,kivy,pyjnius,android
orientation = portrait
fullscreen = 0

# INTERNET for chat; RECORD_AUDIO for voice features
android.permissions = INTERNET,RECORD_AUDIO
android.api = 34
android.minapi = 24
android.archs = arm64-v8a, armeabi-v7a
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
