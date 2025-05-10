from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QPushButton, QComboBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
import sys



class LauncherWindow(QtWidgets.QWidget) :
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


    def setup_ui(self) :
        layout = QtWidgets.QVBoxLayout()

        self.selectver = QComboBox()
        self.selectver.addItems(['1.21.1', '1.21', '1.20.6', '1.20.5'])

        self.launch_button = QtWidgets.QPushButton("Launch")
        self.launch_button.clicked.connect(self.on_button_clicked)  

        layout.addWidget(self.selectver)

        layout.addWidget(self.launch_button)


        self.setLayout(layout)

    def on_button_clicked(self) :
        print(f"Selected mod loader: {self.modldr.currentText()}")
        print(self.selectver.currentText())

        options = {
            "username": "Player",
            "uuid": "00000000-0000-0000-0000-000000000000",
            "token": "",
            "executablePath": "/usr/bin/java",
        }


# Initialize the application
app = QtWidgets.QApplication(sys.argv)
window = LauncherWindow()
window.show()
sys.exit(app.exec_())


