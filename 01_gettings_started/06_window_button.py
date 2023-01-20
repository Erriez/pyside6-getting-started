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

from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from PySide6.QtCore import Qt
import random
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()

        # Resize window
        self.resize(300, 150)

        # Set window title
        self.setWindowTitle('Button')

        # List with messages
        self.hello = [
            "Hello World in English!",
            "Hallo wereld in Dutch!",
            "Hallo Welt in German!",
            "Bonjour le monde in French!",
            "Ciao mondo in Italian!",
            "Hola Mundo in Spanish!"
        ]

        # Create push button
        self.button = QPushButton("Click me!")
        self.button.setFixedWidth(150)
        self.button.clicked.connect(self.on_button_click)

        # Create label and center text
        # https://doc.qt.io/qtforpython/PySide6/QtWidgets/QLabel.html
        self.label = QLabel("I want to say something...")
        self.label.setAlignment(Qt.AlignCenter)

        # Add label button to vertical box layout
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.button, alignment=Qt.AlignCenter)

    def on_button_click(self):
        # Update label
        self.label.setText(random.choice(self.hello))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
