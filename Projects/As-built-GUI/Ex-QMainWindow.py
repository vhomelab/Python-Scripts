import sys
from PySide6.QtWidgets import QApplication, QMainWindow

MyApp = QApplication(sys.argv)

MyMainWindow = QMainWindow()

MyMainWindow.show()

MyApp.exec()