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

from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QProgressBar, QGridLayout
from PySide6.QtCore import QBasicTimer
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('QProgressBar')

        # https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QProgressBar.html
        self.progress_bar = QProgressBar()
        self.progress_bar.setGeometry(30, 40, 200, 25)

        self.button_start = QPushButton('Start')
        self.button_start.move(40, 80)
        self.button_start.clicked.connect(self.on_button_start)

        # https://doc.qt.io/qtforpython-6/PySide6/QtCore/QBasicTimer.html
        self.timer = QBasicTimer()
        self.step = 0

        grid = QGridLayout()
        grid.addWidget(self.progress_bar, 0, 0)
        grid.addWidget(self.button_start, 0, 1)

        self.setLayout(grid)

    def timerEvent(self, e):
        if self.step >= 100:
            self.timer.stop()
            self.step = 0
            self.button_start.setText('Finished')
        else:
            self.step += 1
            self.progress_bar.setValue(self.step)

    def on_button_start(self):
        if self.timer.isActive():
            self.timer.stop()
            self.button_start.setText('Start')
        else:
            self.timer.start(50, self)
            self.button_start.setText('Stop')


def main():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
