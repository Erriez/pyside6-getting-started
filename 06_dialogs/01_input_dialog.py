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

from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QInputDialog
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.resize(300, 100)
        self.setWindowTitle('Input dialog')

        self.button = QPushButton('Dialog', self)
        self.button.move(20, 20)
        self.button.clicked.connect(self.show_dialog)

        self.line_edit = QLineEdit(self)
        self.line_edit.move(130, 22)

    def show_dialog(self):
        # https://doc.qt.io/qtforpython/PySide6/QtWidgets/QInputDialog.html
        text, ok = QInputDialog.getText(self, 'Input Dialog', 'Enter your name:')

        if ok:
            self.line_edit.setText(str(text))


def main():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
