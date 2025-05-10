import subprocess
import requests
import os
from zipfile import ZipFile

libs_url = "https://hc-cdn.hel1.your-objectstorage.com/s/v3/6511d995a83b247e053bad690bc524a1043afd6a_lwjgl-release-3.3.3-arm.zip"

response = requests.get(libs_url)
file_Path = './minecraft/libs/lwjgl.zip'
os.mkdir(file_Path) 

if response.status_code == 200:
    with open(file_Path, 'wb') as file:
        file.write(response.content)
    print('File downloaded success')
else:
    print('failed')


