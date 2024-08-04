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

from PySide6.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QPushButton
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Calculator')

        # Create grid layout. It resizes the window automatically.
        # https://doc.qt.io/qtforpython/PySide6/QtWidgets/QGridLayout.html
        grid = QGridLayout()

        # Button names
        button_names = ['Cls', 'Bck', '', 'Close',
                        '7', '8', '9', '/',
                        '4', '5', '6', '*',
                        '1', '2', '3', '-',
                        '0', '.', '=', '+']

        # Create push buttons and add to grid layout
        for i in range(0, len(button_names)):
            row = i / 4
            col = i % 4
            if not button_names[i]:
                grid.addWidget(QLabel(''), row, col)
            else:
                button = QPushButton(button_names[i])
                grid.addWidget(button, row, col)

        # Add grid layout to window
        self.setLayout(grid)


def main():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
