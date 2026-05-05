[app]
title = AI Agent
package.name = aiagent
package.domain = org.jules
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,csv,joblib
version = 0.1
requirements = python3,kivy,pandas,scikit-learn,joblib,numpy,scipy,threadpoolctl
orientation = portrait
osx.python_version = 3
osx.kivy_version = 1.9.1
fullscreen = 0
android.permissions = INTERNET
android.api = 31
android.minapi = 21
android.sdk = 31
android.ndk = 25b
android.archs = arm64-v8a, armeabi-v7a
p4a.branch = master

[buildozer]
log_level = 2
warn_on_root = 1
