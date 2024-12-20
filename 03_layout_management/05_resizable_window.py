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

from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QDialogButtonBox,
    QLabel,
    QLineEdit,
    QHBoxLayout,
    QVBoxLayout,
    QMessageBox
)
import sys


class Window(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Set window size and title
        self.setMinimumSize(300, 200)
        self.setWindowTitle("Resizable window")

        # Create label and line edit, then add to horizontal box layout
        self.labelName = QLabel("Your name:")
        self.editName = QLineEdit()
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.addWidget(self.labelName)
        self.horizontalLayout.addWidget(self.editName)

        # Create a dialog button box for OK and Cancel buttons
        self.buttonBox = QDialogButtonBox()
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel | QDialogButtonBox.StandardButton.Ok)

        # Connect OK and Cancel buttons to accept / reject slot
        self.buttonBox.accepted.connect(self.on_accept)
        self.buttonBox.rejected.connect(self.on_reject)

        # Add previously created layout and widgets to the dialog
        self.vboxLayout = QVBoxLayout(self)
        self.vboxLayout.addLayout(self.horizontalLayout)
        self.vboxLayout.addStretch()  # <- Stretch between layout on the top and OK/Cancel buttons at the bottom
        self.vboxLayout.addWidget(self.buttonBox)

    def on_accept(self):
        QMessageBox.information(self, "Dialog", f"Hello {self.editName.text()}!")

    def on_reject(self):
        QMessageBox.information(self, "Dialog", "Clicked cancel")


def main():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()