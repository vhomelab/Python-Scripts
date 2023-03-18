import sys
from PySide6.QtWidgets import QApplication, QDialog, QPushButton, QLineEdit, QVBoxLayout

class Form(QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.setWindowTitle("My Form")

        self.edit = QLineEdit("write your name here...")
        self.button = QPushButton("Show Greetings")

        layout = QVBoxLayout(self)
        layout.addWidget(self.edit)
        layout.addWidget(self.button)

        #self.edit.hasFocus(self.edit.text.clear())

        self.button.clicked.connect(self.To_Console)

    def To_Console(self):
        print(f"Hello {self.edit.text()}")


if __name__ == '__main__':
    # create Qt Application
    MyApp = QApplication(sys.argv)
    # create and show form

    MyForm = Form()
    MyForm.show()

    sys.exit(MyApp.exec())

