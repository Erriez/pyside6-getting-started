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

from PySide6.QtWidgets import QApplication, QMainWindow, QTextEdit, QFileDialog
from PySide6.QtGui import QAction, QIcon
import os
import sys


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.resize(400, 300)
        self.setWindowTitle('File dialog')

        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)

        file_open = QAction(QIcon('../images/open.png'), 'Open', self)
        file_open.setShortcut('Ctrl+O')
        file_open.setStatusTip('Open new File')
        file_open.triggered.connect(self.show_dialog)

        file_exit = QAction(QIcon('../images/exit.png'), '&Exit', self)
        file_exit.setShortcut('Ctrl+Q')
        file_exit.setStatusTip('Exit application')
        file_exit.triggered.connect(self.close)

        menubar = self.menuBar()
        menu_file = menubar.addMenu('&File')
        menu_file.addAction(file_open)
        menu_file.addSeparator()
        menu_file.addAction(file_exit)

        self.statusBar().showMessage('Click File | Open to read a file')

    def show_dialog(self):
        # https://doc.qt.io/qtforpython/PySide6/QtWidgets/QFontDialog.html
        path, _ = QFileDialog.getOpenFileName(self, 'Open file', '/home')

        if not path:
            self.statusBar().showMessage('No file selected'.format())
        elif not os.path.exists(path):
            self.statusBar().showMessage('File {} not found'.format(path))
        else:
            try:
                with open(path, 'r') as f:
                    data = f.read()
                    self.textEdit.setText(data)
                    self.statusBar().showMessage('File {} opened'.format(path))
            except OSError as err:
                self.statusBar().showMessage(err)


def main():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
