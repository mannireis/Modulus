from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QPushButton, QComboBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
import sys
import subprocess
import minecraft_launcher_lib
import os



class LauncherWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Modulus")
        self.setGeometry(200, 200, 600, 400)
        self.setup_ui()
        self.launch_button.setStyleSheet(
            """
            QPushButton {
            background-color: #282A36;
            color: #F8F8F2;
            border: 2px solid #BD93F9;
            border-radius: 5px;
            margin: 2px;
            padding: 15px;
            }
            QPushButton:hover {
                background-color: #1E1F29;
            }
            """
        )

        self.selectver.setStyleSheet(
            """
            QComboBox {
            color: #F8F8F2;
            margin: 2px;
            padding: 15px;
            border: 2px solid #BD93F9;
            border-radius: 5px;
            }
            """
        )

        self.modldr.setStyleSheet(
            """
            QComboBox {
            color: #F8F8F2;
            margin: 2px;
            padding: 15px;
            border: 2px solid #BD93F9;
            border-radius: 5px;
            }
            """
        )


        self.setStyleSheet("background-color: #282A36;")


    def setup_ui(self):
        layout = QtWidgets.QVBoxLayout()

        self.selectver = QComboBox()
        self.selectver.addItems(['1.21.1', '1.21', '1.20.6', '1.20.5'])

        self.modldr = QComboBox()
        self.modldr.addItems(['Vanilla', 'Fabric', 'Forge'])

        self.launch_button = QtWidgets.QPushButton("Launch")
        self.launch_button.clicked.connect(self.on_button_clicked)  

        layout.addWidget(self.selectver)
        layout.addWidget(self.modldr)
        layout.addWidget(self.launch_button)


        self.setLayout(layout)

    def on_button_clicked(self):
        print(f"Selected mod loader: {self.modldr.currentText()}")
        print(self.selectver.currentText())
        natives_directory = f".minecraft/versions/1.21.1/natives" 
        minecraft_directory = minecraft_launcher_lib.utils.get_minecraft_directory()
        version = self.selectver.currentText()
        forge_version = minecraft_launcher_lib.forge.find_forge_version(version)


        callback = {
            "setStatus": lambda text: print(text)
        }

        minecraft_launcher_lib.install.install_minecraft_version(version, minecraft_directory)

        if self.modldr.currentText() == 'Fabric':
            minecraft_launcher_lib.fabric.install_fabric(version, minecraft_directory, callback=callback)
            print("this works FABRIC")
        if self.modldr.currentText() == 'Forge':
            minecraft_launcher_lib.forge.install_forge_version(forge_version, minecraft_directory, callback=callback)
            print("this works FORGE ")
        


        options = {
            "username": "Player",
            "uuid": "00000000-0000-0000-0000-000000000000",
            "token": "",
            "executablePath": "/usr/bin/java",
        }


        # Get the Minecraft launch command
        minecraft_command = minecraft_launcher_lib.command.get_minecraft_command(version, minecraft_directory, options)

        # Add the Java library path argument for LWJGL
        lwjgl_path = os.path.join(minecraft_directory, "versions", version, "natives")
        minecraft_command[2:2] = ["-Djava.library.path=" + lwjgl_path]
        subprocess.call(minecraft_command)

# Initialize the application
app = QtWidgets.QApplication(sys.argv)
window = LauncherWindow()
window.show()
sys.exit(app.exec_())


