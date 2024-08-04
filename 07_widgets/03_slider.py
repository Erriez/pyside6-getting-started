#
# MIT License
#
# Copyright (c) 2023-2024 Erriez
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

from PySide6.QtWidgets import QApplication, QWidget, QSlider, QLabel, QHBoxLayout
from PySide6.QtGui import Qt, QPixmap
from pathlib import Path
import os
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.path = Path(__file__).resolve().parent

        self.resize(250, 150)
        self.setWindowTitle('QSlider')

        # https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QSlider.html
        slider = QSlider(Qt.Horizontal)
        slider.setFocusPolicy(Qt.NoFocus)
        slider.setGeometry(30, 40, 100, 30)
        slider.valueChanged.connect(self.change_value)

        self.label = QLabel()
        self.label.setPixmap(QPixmap(os.path.join(self.path, '..', 'images', 'mute.png')))
        self.label.setGeometry(160, 40, 80, 30)

        hbox = QHBoxLayout()
        hbox.setContentsMargins(20, 0, 20, 0)
        hbox.addWidget(slider)
        hbox.addWidget(self.label)

        self.setLayout(hbox)

    def change_value(self, value):
        if value <= 0:
            self.label.setPixmap(QPixmap(os.path.join(self.path, '..', 'images', 'mute.png')))
        elif value <= 30:
            self.label.setPixmap(QPixmap(os.path.join(self.path, '..', 'images', 'min.png')))
        elif value <= 80:
            self.label.setPixmap(QPixmap(os.path.join(self.path, '..', 'images', 'med.png')))
        else:
            self.label.setPixmap(QPixmap(os.path.join(self.path, '..', 'images', 'max.png')))


def main():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
