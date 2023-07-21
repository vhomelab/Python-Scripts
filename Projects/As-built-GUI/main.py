#import sys
#from PySide6.QtWidgets import  QApplication, QLabel

import sys
from PySide6.QtWidgets import QApplication, QLabel, QPushButton
from PySide6.QtCore import Slot

# Greetings
@Slot()
def say_hello():
    print(f'Button client, Hello!')

app = QApplication(sys.argv)

label_fn = QLabel("First Name")
btn_click1 = QPushButton("Login")

btn_click1.clicked.connect(say_hello)

label_fn.show()
btn_click1.show()

app.exec()


