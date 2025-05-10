import subprocess
import requests
import os 
from zipfile import ZipFile

class MinecraftLaunch :
    def __init__(self):
        self.version = version
        self.mod_loader = mod_loader
        self.options = options
        self.natives_dir = "./minecraft/versions/1.21.1/natives"
        self.libraries_dir = "./libraries"
        self.assets_dir = "./assets"
        os.makedirs(self.natives_dir, exist_ok=True)
        os.makedirs(self.libraries_dir, exist_ok=True)
        os.makedirs(self.assets_dir, exist_ok=True)




nativesarmlinux = "https://hc-cdn.hel1.your-objectstorage.com/s/v3/6511d995a83b247e053bad690bc524a1043afd6a_lwjgl-release-3.3.3-arm.zip"