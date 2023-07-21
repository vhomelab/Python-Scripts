import sys
from PySide6.QtWidgets import QApplication, QWidget

MyApp = QApplication(sys.argv)
MyWindow = QWidget()
MyWindow.show()
MyApp.exec()