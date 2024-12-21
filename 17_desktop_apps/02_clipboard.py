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

from PySide6.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QTextEdit, QMessageBox
import sys

class Window(QWidget):
    DEFAULT_TEXT = "Enter your text here"

    def __init__(self):
        super().__init__()

        # Set window size and title
        self.resize(300, 200)
        self.setWindowTitle('Clipboard example')

        # Create clipboard object
        self.clipboard = QApplication.clipboard()

        # Create line edit
        self.text = QTextEdit(self.DEFAULT_TEXT)
        self.text.selectAll()

        # Create buttons
        self.button_default_text = QPushButton("Default text")
        self.button_select_all = QPushButton("Select all")
        self.button_delete = QPushButton("Delete")
        self.button_copy = QPushButton("Copy to clipboard")
        self.button_paste = QPushButton("Paste from clipboard")
        self.button_clear = QPushButton("Clear clipboard")

        # Create grid
        self.grid = QGridLayout(self)

        # Add widgets to grid
        self.grid.addWidget(self.text, 0, 0, 3, 2)
        self.grid.addWidget(self.button_default_text, 0, 2)
        self.grid.addWidget(self.button_select_all, 1, 2)
        self.grid.addWidget(self.button_delete, 2, 2)

        self.grid.addWidget(self.button_copy, 3, 0)
        self.grid.addWidget(self.button_paste, 3, 1)
        self.grid.addWidget(self.button_clear, 3, 2)

        # Connect button events
        self.button_default_text.clicked.connect(self.on_default_text)
        self.button_select_all.clicked.connect(self.on_select_all)
        self.button_delete.clicked.connect(self.on_delete)
        self.button_copy.clicked.connect(self.on_copy)
        self.button_paste.clicked.connect(self.on_paste)
        self.button_clear.clicked.connect(self.on_clear)

    def on_default_text(self):
        self.text.setText(self.DEFAULT_TEXT)

    def on_select_all(self):
        self.text.selectAll()
        self.text.setFocus()

    def on_delete(self):
        self.text.setText("")

    def on_copy(self):
        cursor = self.text.textCursor()
        selection_start = cursor.selectionStart()
        selection_end = cursor.selectionEnd()
        if selection_end:
            text = self.text.toPlainText()
            selected_text = text[selection_start:selection_end]
            self.clipboard.setText(selected_text)
            QMessageBox.information(self, "Clipboard", "Selected text copied to clipboard!")
        else:
            QMessageBox.information(self, "Clipboard", "Nothing to copy.")

    def on_paste(self):
        clipboard_text = self.clipboard.text()
        self.text.setText(clipboard_text)
        self.text.selectAll()
        self.text.setFocus()

    def on_clear(self):
        self.clipboard.clear()
        QMessageBox.information(self, "Clipboard", "Clipboard cleared!")


def main():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
