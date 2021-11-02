import requests
import zipfile
import io
import subprocess
import os
import shutil

# Constants
JAVA_BIN = R"C:\Program Files (x86)\Minecraft Launcher\runtime\jre-legacy\windows-x64\jre-legacy\bin\java.exe"
MINECRAFT_PATH = None
PACKAGE_URL = "http://140.238.155.211:8000/InsomniaMC.zip"
APPDATA_PATH = os.environ['APPDATA']

def download_package():
    r = requests.get(PACKAGE_URL)
    z = zipfile.ZipFile(io.BytesIO(r.content))
    z.extractall("./InsomniaMC")

def install_forge():
    subprocess.call([JAVA_BIN, '-jar', 'InsomniaMC/forge-1.16.5-36.2.8-installer.jar'])

def check_java():
    if shutil.which("java") is not None:
        JAVA_BIN = "java"

def install_mods():
    # Create the mods folder if it doesn't exist
    if not os.path.exists(ROAMINGAPPDATA_PATH + "\\.minecraft\\mods"):
        os.makedirs(ROAMINGAPPDATA_PATH + "\\.minecraft\\mods")
    # Move the mods to the mods folder
    for file in os.listdir("./InsomniaMC/mods"):
        if file.endswith(".jar"):
            shutil.move("./InsomniaMC/mods/" + file, ROAMINGAPPDATA_PATH + "\\.minecraft\\mods")

def main():
    print("Downloading mods...")
    download_package()
    print("Checking Java version...")
    check_java()
    print("Installing Forge...")
    install_forge()
    print("Installing mods...")
    install_mods()

main()