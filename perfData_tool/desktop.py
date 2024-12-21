#! /usr/bin/env python3
# _*_ coding:utf-8 _*_
# datetime: 2023-12-15
# author: jinHui

import sys
from PyQt6.QtWidgets import (QWidget, QLabel, QPushButton,  QGridLayout, QHBoxLayout, QVBoxLayout, QApplication)

class DesktopShow(QWidget):

    def __init__(self):
        super().__init__()
        self.init_UI()

    def init_UI(self):
        ok_button = QPushButton("OK")
        cancel_button = QPushButton("Cancel")

        title = QLabel('Title')

        h_box = QHBoxLayout()
        h_box.addStretch(1)
        h_box.addWidget(ok_button)
        h_box.addWidget(cancel_button)

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(title, 1, 0)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(h_box)

        self.setLayout(vbox)

        self.setGeometry(300, 300, 350, 250)
        self.center()
        self.setWindowTitle('hello world')
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()

        qr.moveCenter(cp)
        self.move(qr.topLeft())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    desktop = DesktopShow()
    sys.exit(app.exec())
