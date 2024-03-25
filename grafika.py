import random
import time 
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QInputDialog, QLabel

class InputDialogExample(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.label = QLabel(self)
        layout.addWidget(self.label)

        button = QPushButton('Get Text', self)
        button.clicked.connect(self.showInputDialog)
        layout.addWidget(button)

        self.setLayout(layout)
        self.setWindowTitle('Input Dialog Example')
        self.show()

    def showInputDialog(self):
        text, ok = QInputDialog.getText(self, 'Input Dialog', 'Enter your name:')
        if ok:
            self.label.setText(f'Hello, {text}!')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = InputDialogExample()
    sys.exit(app.exec_())