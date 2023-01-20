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

from PySide6.QtWidgets import QApplication, QLabel
from PySide6.QtCore import Qt
import os
import sys


def get_desktop_type():
    # Get desktop type
    if sys.platform == 'linux':
        desktop = os.environ.get('XDG_SESSION_TYPE', 'Unknown')
        desktop = desktop.capitalize()
        if desktop == 'Wayland':
            desktop += '\n\nMin/Max buttons may not work!'
    elif sys.platform == 'win32':
        desktop = 'Windows'
    else:
        desktop = 'Unknown'

    return desktop


def main():
    # Create application
    app = QApplication(sys.argv)

    # Create window from QLabel
    window = QLabel('Desktop: ' + get_desktop_type())
    # Resize window
    window.resize(300, 150)
    # Set window title
    window.setWindowTitle('Min/Max Buttons')
    # Align label center
    window.setAlignment(Qt.AlignCenter)

    # Remove minimize maximize button works on Windows 10 / Ubuntu X11, not
    # Ubuntu Wayland: https://bugreports.qt.io/browse/QTBUG-110448
    window.setWindowFlags(window.windowFlags() & Qt.CustomizeWindowHint)
    window.setWindowFlags(window.windowFlags() & ~Qt.WindowMinMaxButtonsHint)

    # Show window
    window.show()

    # Main loop
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
