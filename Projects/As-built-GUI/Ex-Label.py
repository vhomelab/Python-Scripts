import sys
from PySide6.QtWidgets import QApplication, QLabel

MyApp = QApplication(sys.argv)

MyLabel_1 = QLabel("This is Label String")
MyLabel_1.show()

MyApp.exec()