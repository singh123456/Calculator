from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton
from PyQt5.QtCore import Qt
import sys

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.left = 1000
        self.top = 800
        self.width = 800
        self.height = 800
        self.setWindowTitle("Calculator")
        self.setGeometry(self.left, self.top, self.width, self.height)
       

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.text_display = QLineEdit()
        layout.addWidget(self.text_display)

        buttons = ["7", "8", "9", "+", "4", "5", "6", "-", "1", "2", "3", "*", "0", ".",  "/"]

        for btn_text in buttons:
            button = QPushButton(btn_text)
            button.clicked.connect(self.button_click)
            layout.addWidget(button)

        equals_button = QPushButton("=")
        equals_button.clicked.connect(self.evaluate_expression)
        layout.addWidget(equals_button)

        self.show()

    def button_click(self):
        clicked_button = self.sender()
        current_text = self.text_display.text()
        new_text = current_text + clicked_button.text()
        self.text_display.setText(new_text)

    def evaluate_expression(self):
        expression = self.text_display.text()
        try:
            result = eval(expression)
            self.text_display.setText(str(result))
        except Exception as e:
            self.text_display.setText("Error")


if __name__ == '__main__':
    App = QApplication(sys.argv)
    calculator = Calculator()
    sys.exit(App.exec_())






