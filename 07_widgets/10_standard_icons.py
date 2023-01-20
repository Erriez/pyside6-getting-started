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

from PySide6.QtWidgets import QApplication, QVBoxLayout, QGridLayout, QPushButton, QStyle, QWidget
from PySide6.QtGui import Qt
import sys

NUM_COLUMNS = 4


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Built-in Icons')

        # Create grid layout
        grid_layout = QGridLayout()

        # Get sorted list icon name strings
        icons = sorted([attr for attr in dir(QStyle.StandardPixmap) if attr.startswith("SP_")])

        # Loop through on all icon strings
        for icon_id, icon_name in enumerate(icons):
            # Get QStyle object from window
            style = self.style()

            # Get icon enum from icon name
            icon_enum = getattr(QStyle, icon_name)

            # Get standard icon
            icon = style.standardIcon(icon_enum)

            # Create push button with text icon name and set icon
            button = QPushButton(icon_name)
            button.setIcon(icon)

            # Add button to grid layout
            row = icon_id / NUM_COLUMNS
            column = icon_id % NUM_COLUMNS
            grid_layout.addWidget(button, row, column)

        # Create button with icon
        button_quit = QPushButton('Quit')
        button_quit.setFixedWidth(200)
        button_quit.setIcon(self.style().standardIcon(QStyle.SP_DialogOkButton))
        button_quit.clicked.connect(QApplication.quit)

        # Create vertical box layout
        vbox = QVBoxLayout()
        vbox.addLayout(grid_layout)
        vbox.addSpacing(50)
        vbox.addWidget(button_quit, alignment=Qt.AlignCenter)

        # Add layout to window
        self.setLayout(vbox)


def main():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
