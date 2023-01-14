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
# This example creates a Qt core application without a GUI and quits after 3
# seconds.
#

# Import PySide6 modules
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QTimer

# Import Python system module
import sys


# Main function
def main():
    # Print message on a terminal
    print('Waiting to quit application...')

    # Create QApplication object
    # https://doc.qt.io/qtforpython/PySide6/QtWidgets/QApplication.html
    app = QApplication([])

    # Close application after 3 seconds
    # https://doc.qt.io/qtforpython-6/PySide6/QtCore/QTimer.html
    QTimer.singleShot(3000, app.quit)

    # Qt application loop runs until application is quit.
    # Exit code 0 (success) is returned to the console on application quit.
    # Exit codes other than 0 are returned when an error occurred.
    sys.exit(app.exec())


# Python code starts here
if __name__ == "__main__":
    main()
