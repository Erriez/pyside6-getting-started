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

from PySide6.QtWidgets import (QApplication, QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout)
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()

        # Set window size and title
        self.resize(400, 250)
        self.setWindowTitle("SpreadSheet example")

        # https://doc.qt.io/qtforpython/PySide6/QtWidgets/QTableWidget.html
        # Create table widget
        self.table = QTableWidget(6, 3)

        # Set column names
        self.table.setHorizontalHeaderLabels(["Name", "Age", "Gender"])

        # Fill table with data
        self.table.setItem(0, 0, QTableWidgetItem("Jan"))
        self.table.setItem(0, 1, QTableWidgetItem("53"))
        self.table.setItem(0, 2, QTableWidgetItem("Male"))

        self.table.setItem(1, 0, QTableWidgetItem("Henk"))
        self.table.setItem(1, 1, QTableWidgetItem("45"))
        self.table.setItem(1, 2, QTableWidgetItem("Male"))

        self.table.setItem(2, 0, QTableWidgetItem("Linda"))
        self.table.setItem(2, 1, QTableWidgetItem("18"))
        self.table.setItem(2, 2, QTableWidgetItem("Female"))

        self.table.setItem(3, 0, QTableWidgetItem("Kees"))
        self.table.setItem(3, 1, QTableWidgetItem("72"))
        self.table.setItem(3, 2, QTableWidgetItem("Male"))

        self.table.setItem(4, 0, QTableWidgetItem("Lotte"))
        self.table.setItem(4, 1, QTableWidgetItem("39"))
        self.table.setItem(4, 2, QTableWidgetItem("Female"))

        self.table.setItem(5, 0, QTableWidgetItem("Anne"))
        self.table.setItem(5, 1, QTableWidgetItem("28"))
        self.table.setItem(4, 2, QTableWidgetItem("Female"))

        # Add table to layout, add layout to widget
        self.vBox = QVBoxLayout()
        self.vBox.addWidget(self.table)
        self.setLayout(self.vBox)


def main():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
