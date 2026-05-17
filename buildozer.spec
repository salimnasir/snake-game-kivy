[app]

title = SnakeGame
package.name = snakegame
package.domain = org.yourname

source.dir = .
source.include_exts = py,png,jpg,kv

version = 1.0

requirements = python3,kivy==2.2.1

orientation = portrait
fullscreen = 1

android.api = 34
android.minapi = 21
android.archs = arm64-v8a

android.enable_androidx = True
android.ndk_version = 25b
android.build_tools_version = 34.0.0

android.release_artifact = aab

log_level = 2
