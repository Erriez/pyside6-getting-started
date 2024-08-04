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

from PySide6.QtWidgets import QApplication, QWidget, QDial, QLabel, QSizePolicy, QVBoxLayout
import sys


class Window(QWidget):
    dial_min = 0
    dial_max = 100

    def __init__(self):
        super().__init__()

        # Resize window
        self.resize(250, 200)
        # Set window title
        self.setWindowTitle('Dial')

        # https://doc.qt.io/qtforpython/PySide6/QtWidgets/QDial.html
        self.dial = QDial()
        self.dial.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.dial.setNotchesVisible(True)
        self.dial.setRange(self.dial_min, self.dial_max)
        self.dial.setValue(0)
        self.dial.valueChanged.connect(self.dial_value_changed)

        # Create label
        self.label = QLabel()

        vbox = QVBoxLayout()
        vbox.addWidget(self.dial)
        vbox.addWidget(self.label)

        # Add layout to window
        self.setLayout(vbox)

        # Update label value
        self.dial_value_changed()

    def dial_value_changed(self):
        # Display value
        self.label.setText('Value: {}'.format(self.dial.value()))


def main():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
