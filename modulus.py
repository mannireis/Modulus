from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
import sys
import subprocess
import minecraft_launcher_lib
import os

# Define the path to the natives (LWJGL libraries)
natives_directory = f".minecraft/versions/1.21.1/natives"
minecraft_directory = minecraft_launcher_lib.utils.get_minecraft_directory()
version = "1.21.1"

# Install the Minecraft version if not already installed
minecraft_launcher_lib.install.install_minecraft_version(version, minecraft_directory)

options = {
    "username": "Player",
    "uuid": "00000000-0000-0000-0000-000000000000",
    "token": "",
    "executablePath": "/usr/bin/java",
    # Force ARM64 LWJGL and disable Wayland
    "jvmArguments": [
        "-Dorg.lwjgl.librarypath=" + os.path.join(minecraft_directory, "versions", version, "natives"),
        "-Dorg.lwjgl.util.Debug=true",  # Debug LWJGL loading
        "-Dorg.lwjgl.util.DebugLoader=true",
        "-Djava.awt.headless=true",  # Avoid GUI issues
    ],
}

callback = {
    "setStatus": lambda text: print(text)
}

# Get the Minecraft launch command
minecraft_command = minecraft_launcher_lib.command.get_minecraft_command(version, minecraft_directory, options)
minecraft_launcher_lib.fabric.install_fabric(version, minecraft_directory, callback=callback)


# Add the Java library path argument for LWJGL 
lwjgl_path = os.path.join(minecraft_directory, "versions", version, "natives")
minecraft_command[2:2] = ["-Djava.library.path=" + lwjgl_path]

class LauncherWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Modulus")
        self.setGeometry(200, 200, 600, 400)
        self.setup_ui()

    def setup_ui(self):
        layout = QtWidgets.QVBoxLayout()
        self.textbox = QLineEdit(self)
        self.launch_button = QtWidgets.QPushButton("Launch")
        self.launch_button.clicked.connect(self.on_button_clicked)  

        self.setLayout(layout)

    def on_button_clicked(self):
        subprocess.call(minecraft_command)

# Initialize the application
app = QtWidgets.QApplication(sys.argv)
window = LauncherWindow()
window.show()
sys.exit(app.exec_())


