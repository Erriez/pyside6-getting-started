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
from pathlib import Path
import os
import sys


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Create exit action with icon, shortcut, status tip and close window click event
        path_data = os.path.join(Path(__file__).resolve().parent, 'data')

        self.resize(400, 250)
        self.setWindowTitle('Main window')

        # Create text edit and center on window
        self.text_edit = QTextEdit()
        self.setCentralWidget(self.text_edit)
        
        # Load text file
        file_info = os.path.join(path_data, 'info.txt')
        if os.path.exists(file_info):
            with open(file_info, 'r') as f:
                self.text_edit.setText(f.read())
        
        # Set window icon
        self.setWindowIcon(QIcon(os.path.join(path_data, 'app.png')))

        # New menu
        menu_file_new = QAction(QIcon(os.path.join(path_data, 'new.png')), '&New', self)
        menu_file_new.setShortcut('Ctrl+N')
        menu_file_new.setStatusTip('New File')
        menu_file_new.triggered.connect(self.on_file_new)

        # Open menu
        menu_file_open = QAction(QIcon(os.path.join(path_data, 'open.png')), '&Open', self)
        menu_file_open.setShortcut('Ctrl+O')
        menu_file_open.setStatusTip('Open new File')
        menu_file_open.triggered.connect(self.on_file_open)

        # Exit menu
        menu_exit = QAction(QIcon(os.path.join(path_data, 'exit.png')), '&Exit', self)
        menu_exit.setShortcut('Ctrl+Q')
        menu_exit.setStatusTip('Exit application')
        menu_exit.triggered.connect(self.close)

        # Create menubar
        menubar = self.menuBar()

        # Create File menu
        menu_file = menubar.addMenu('&File')
        menu_file.addAction(menu_file_new)
        menu_file.addAction(menu_file_open)
        menu_file.addSeparator()
        menu_file.addAction(menu_exit)
        
        # Add New to toolbar
        toolbar_open = self.addToolBar('New')
        toolbar_open.addAction(menu_file_new)
        
        # Add Open to toolbar
        toolbar_open = self.addToolBar('Open')
        toolbar_open.addAction(menu_file_open)

        # Add Exit to toolbar
        toolbar_exit = self.addToolBar('Exit')
        toolbar_exit.addAction(menu_exit)

        # Create statusbar
        self.statusBar()
    
    def on_file_new(self):
        self.text_edit.setText('')
    
    def on_file_open(self):
        path, _ = QFileDialog.getOpenFileName(self, 'Open file', '/home')

        if not path:
            self.statusBar().showMessage('No file selected'.format())
        elif not os.path.exists(path):
            self.statusBar().showMessage('File {} not found'.format(path))
        else:
            try:
                with open(path, 'r') as f:
                    data = f.read()
                    self.text_edit.setText(data)
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
