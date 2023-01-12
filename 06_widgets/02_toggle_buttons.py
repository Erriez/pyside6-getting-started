#
# MIT License
#
# Copyright (c) 2023 Erriez
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
# Source: https://github.com/Erriez/pyside6-getting-started
#

from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QFrame
from PySide6.QtGui import QColor
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('Toggle button')

        self.col = QColor(0, 0, 0)

        btn_red = QPushButton('Red', self)
        btn_red.setCheckable(True)
        btn_red.move(10, 10)
        btn_red.clicked.connect(self.set_color)

        btn_green = QPushButton('Green', self)
        btn_green.setCheckable(True)
        btn_green.move(10, 60)
        btn_green.clicked.connect(self.set_color)

        btn_blue = QPushButton('Blue', self)
        btn_blue.setCheckable(True)
        btn_blue.move(10, 110)
        btn_blue.clicked.connect(self.set_color)

        self.frame = QFrame(self)
        self.frame.setGeometry(150, 20, 100, 100)
        self.frame.setStyleSheet("QWidget { background-color: %s }" % self.col.name())

    def set_color(self, pressed):
        source = self.sender()

        if pressed:
            val = 255
        else:
            val = 0

        if source.text() == "Red":
            self.col.setRed(val)
        elif source.text() == "Green":
            self.col.setGreen(val)
        else:
            self.col.setBlue(val)

        self.frame.setStyleSheet("QFrame { background-color: %s }" % self.col.name())


def main():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
