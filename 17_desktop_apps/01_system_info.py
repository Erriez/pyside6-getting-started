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

from PySide6.QtWidgets import QApplication, QPushButton, QVBoxLayout,\
    QDialog, QFormLayout, QLineEdit
from PySide6.QtCore import qVersion
import os
import platform
import sys
from packaging import version

if sys.platform == 'linux':
    import distro


# https://doc.qt.io/qtforpython/PySide6/QtWidgets/QDialog.html
class Window(QDialog):
    def __init__(self):
        super().__init__()

        self.setMinimumSize(450, 250)
        self.setWindowTitle('System Info')

        form = QFormLayout()

        if sys.platform == 'linux':
            form.addRow('System:', QLineEdit(platform.system()))
            form.addRow('Machine:', QLineEdit(platform.machine()))
            form.addRow('Version:', QLineEdit(platform.version()))
            form.addRow('Distro:', QLineEdit(distro.name(pretty=True)))
            form.addRow('Name:', QLineEdit(distro.codename().capitalize()))
            form.addRow('Desktop', QLineEdit(os.environ.get('XDG_SESSION_TYPE').capitalize()))
        elif sys.platform == 'win32':
            form.addRow('OS:', QLineEdit('Windows'))

        qt_version = version.parse(str(qVersion()))
        form.addRow('PySide:', QLineEdit('v' + qt_version.base_version))

        button_quit = QPushButton('Quit')
        button_quit.clicked.connect(QApplication.quit)
        button_quit.resize(button_quit.sizeHint())

        # Add button to window
        layout = QVBoxLayout(self)
        layout.addLayout(form)
        layout.addWidget(button_quit)

        self.setLayout(layout)


def main():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
