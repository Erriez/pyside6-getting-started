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

from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QMessageBox
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader

from pathlib import Path
import sys


class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Set window title
        self.setWindowTitle('Dynamic Form')

        # Create loader object
        loader = QUiLoader()

        # Set path Qt design file
        ui_path = Path(__file__).resolve().parent / "01_qt_creator_qwidget.ui"

        # Open and load .ui file read-only
        ui_file = QFile(ui_path)
        ui_file.open(QFile.ReadOnly)

        # Create dynamic widget from .ui file
        self.widget_dynamic = loader.load(ui_file)
        ui_file.close()

        # Add button click event
        self.widget_dynamic.btn_submit.clicked.connect(self.on_btn_submit)

        # Create vertical box layout
        vbox = QVBoxLayout()
        vbox.addWidget(self.widget_dynamic)

        # Set layout
        self.setLayout(vbox)

    def on_btn_submit(self):
        # Get variables from dynamic widget
        your_name = self.widget_dynamic.txt_name.text()
        your_comment = self.widget_dynamic.txt_comment.toPlainText()

        # Show information in message box
        QMessageBox.information(self,
                                'Submit',
                                'Your name: {}\nYour comment: {}'.format(your_name, your_comment))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
