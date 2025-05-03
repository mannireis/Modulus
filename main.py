from PyQt5 import QtWidgets
import sys
import subprocess

class LauncherWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Modulus")
        self.setGeometry(100, 100, 300, 200)
        self.setup_ui()

    def setup_ui(self):
        layout = QtWidgets.QVBoxLayout()

        self.version_label = QtWidgets.QLabel("Select Minecraft Version:")
        layout.addWidget(self.version_label)

        self.version_input = QtWidgets.QLineEdit()
        layout.addWidget(self.version_input)

        self.launch_button = QtWidgets.QPushButton("Launch")
        layout.addWidget(self.launch_button)

        self.setLayout(layout)

app = QtWidgets.QApplication(sys.argv)
window = LauncherWindow()
window.show()
sys.exit(app.exec_())
