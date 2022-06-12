from PySide2.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton
from PySide2.QtCore import QSize, Qt

# SubClass the QMainWindow for customization

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Files Migration")
        self.setMaximumSize(QSize(800,400))
        self.setMinimumSize(QSize(800,400))

