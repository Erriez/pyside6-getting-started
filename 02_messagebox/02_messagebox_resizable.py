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

from PySide6.QtWidgets import QApplication, QWidget, QMessageBox, QSizePolicy, \
    QPushButton, QVBoxLayout
import sys


# https://doc.qt.io/qtforpython/PySide6/QtWidgets/QMessageBox.html
class ResizableMessageBox(QMessageBox):
    def __init__(self, parent=None):
        QMessageBox.__init__(self)

        # Store parent
        self.parent = parent

        # Enable size grip on lower right corner
        self.setSizeGripEnabled(True)

    def event(self, e):
        # Undocumented: The only way of resizing a QMessageBox is from an event
        result = QMessageBox.event(self, e)

        # Set min/max sizes QMessageBox
        self.setMinimumSize(275, 125)
        self.setMaximumSize(500, 500)

        # https://doc.qt.io/qtforpython/PySide6/QtWidgets/QSizePolicy.html
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # Show dialog on center of parent window
        if self.parent:
            geo = self.geometry()
            geo.moveCenter(self.parent.geometry().center())
            self.setGeometry(geo)

        # Return event
        return result


class Window(QWidget):
    def __init__(self):
        super().__init__()

        # Resize window
        self.resize(350, 200)

        # Set window title
        self.setWindowTitle('Messagebox Resizable')

        # Create button
        self.button = QPushButton("Show messagebox")
        self.button.clicked.connect(self.on_button_click)

        # Add button to window
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.button)

    def on_button_click(self):
        # https://doc.qt.io/qtforpython/PySide6/QtWidgets/QMessageBox.html#PySide6.QtWidgets.PySide6.QtWidgets.QMessageBox.Icon
        icon = QMessageBox.Icon.Information
        title = 'Messagebox'
        message = 'This is a resizable messagebox!\nNext line with information.'

        # Create resizable messagebox and show centered on window
        msgbox = ResizableMessageBox(self)
        msgbox.setIcon(icon)
        msgbox.setWindowTitle(title)
        msgbox.setText(message)
        # https://doc.qt.io/qtforpython/PySide6/QtWidgets/QMessageBox.html#PySide6.QtWidgets.PySide6.QtWidgets.QMessageBox.StandardButton
        msgbox.setStandardButtons(QMessageBox.StandardButton.Ok)
        msgbox.exec()


def main():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
