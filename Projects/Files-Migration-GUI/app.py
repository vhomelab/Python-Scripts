from PySide2.QtGui import (QFocusEvent)
from PySide2.QtWidgets import (
    QApplication, QWidget, QMainWindow, QPushButton, QAction,
    QLabel, QLineEdit,QVBoxLayout)

from PySide2.QtCore import QSize, Qt

# SubClass the QMainWindow for customization

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Files Migration")
        self.setMaximumSize(QSize(800,600))
        self.setMinimumSize(QSize(800,600))

        # btn_action_login = QPushButton("Login")
        # btn_action_login.setMinimumSize(QSize(100,70))
        
        self.label = QLabel()
        self.input = QLineEdit()
        self.input.textChanged.connect(self.label.setText)
        self.input.setText("Comment here")
        

        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.label)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

app = QApplication()
app_interface = MainWindow()
app_interface.show()
app.exec_()