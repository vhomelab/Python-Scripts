import sys
from PySide6.QtWidgets import QApplication, QPushButton
from PySide6.QtCore import Slot


@Slot()
def To_Console():
    print(f"Print to console static or dynamic using variables")


def To_Console2():
    print(f"This is second")


# Create the Qt Application
MyApp = QApplication(sys.argv)

# Create a button, connect it and show it
MyBtn = QPushButton("Click")
MyBtn.clicked.connect(To_Console)
MyBtn.show()

MyApp.exec()
