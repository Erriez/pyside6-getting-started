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

from PySide6.QtWidgets import QApplication, QWidget, QCheckBox
from PySide6.QtCore import Qt
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.resize(250, 150)
        self.setWindowTitle('QCheckBox')

        # https://doc.qt.io/qtforpython/PySide6/QtWidgets/QCheckBox.html
        checkbox = QCheckBox('Show title', self)
        checkbox.move(20, 20)
        checkbox.toggle()
        checkbox.setTristate(True)
        checkbox.stateChanged.connect(self.on_checkbox_change)

    def on_checkbox_change(self, state):
        # https://forum.qt.io/topic/142047/pyside6-qcheckbox-statechanged-generates-state-event-int-instead-of-qt-checkstate/4
        state = Qt.CheckState(state)
        if state == Qt.CheckState.Unchecked:
            self.setWindowTitle('Unchecked')
        elif state == Qt.PartiallyChecked:
            self.setWindowTitle('PartiallyChecked')
        elif state == Qt.Checked:
            self.setWindowTitle('Checked')
        else:
            self.setWindowTitle('UNKNOWN')


def main():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
