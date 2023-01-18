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

# Run application with commandline arguments:
#   -h or --help to show help
#   -v or --verbose to change verbose message in window

from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PySide6.QtCore import Qt, QCommandLineParser, QCommandLineOption
import sys


class Window(QWidget):
    def __init__(self, verbose=False):
        super().__init__()

        self.resize(300, 150)
        self.setWindowTitle('Commandline')

        if verbose:
            msg = 'Verbose enabled!'
        else:
            msg = 'Verbose not enabled.'

        self.text = QLabel(msg)
        self.text.setAlignment(Qt.AlignCenter)

        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.text)


def main():
    # Create application
    app = QApplication(sys.argv)

    # Create commandline parser
    parser = QCommandLineParser()

    # Set application description printed with -h or --help
    parser.setApplicationDescription("A PySide6 example application.")

    # Add help option -h / --help
    parser.addHelpOption()

    # Add verbose option -v / --verbose
    verbose = QCommandLineOption(['v', 'verbose'], 'Verbose option')
    parser.addOption(verbose)

    # Parse arguments
    parser.process(app)

    # Get verbose option
    verbose = parser.isSet(verbose)

    # Show window and with verbose option from commandline
    window = Window(verbose)
    window.show()

    # Main loop
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
