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

from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QHBoxLayout
import sys


class Widget(QWidget):
    def __init__(self, parent):
        super().__init__()

        # Store parent
        self.parent = parent

        # Create buttons
        button1 = QPushButton("Button 1")
        button2 = QPushButton("Button 2")

        # Create button event
        button1.clicked.connect(self.on_button)
        button2.clicked.connect(self.on_button)

        # Add buttons to horizontal box layout
        hbox = QHBoxLayout(self)
        hbox.addWidget(button1)
        hbox.addWidget(button2)

    def on_button(self):
        # Get event from sender
        sender = self.sender()

        # Update statusbar
        self.parent.statusbar.showMessage(sender.text() + ' was pressed')


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set window title
        self.setWindowTitle('Event sender')

        # Create statusbar
        self.statusbar = self.statusBar()

        # Create widget
        widget = Widget(parent=self)

        # Center widget
        self.setCentralWidget(widget)


def main():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
