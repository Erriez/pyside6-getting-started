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

import sys
from PySide6.QtCore import Qt, QAbstractTableModel, QModelIndex, QSize
from PySide6.QtWidgets import QApplication, QWidget, QTableView, QGridLayout, QHBoxLayout, QVBoxLayout, QSizePolicy


class CustomTableModel(QAbstractTableModel):
    def __init__(self, data: list):
        super(CustomTableModel, self).__init__()

        # Store data
        self._data = data

    def data(self, index, role=None):
        if role == Qt.DisplayRole:
            # Return cell value
            row = index.row()
            column = index.column()
            return self._data[row][column]

    def rowCount(self, parent=QModelIndex()):
        # Return number of rows
        return len(self._data)

    def columnCount(self, parent=QModelIndex()):
        # Return number of columns based on first row
        first_row = self._data[0]
        return len(first_row)

    def headerData(self, section, orientation, role):
        if role != Qt.DisplayRole:
            return None

        if orientation == Qt.Horizontal:
            return ("Column A", "Column B", "Column C")[section]
        else:
            return f"Row {section}"


class Window(QWidget):
    def __init__(self):
        super().__init__()

        # Set window title
        self.setWindowTitle('Table example')

        # Create table
        self.create_table()

        # Resize table to contents
        self.resize_table_to_contents()

    def create_table(self):
        self.table = QTableView()

        data = [
            [6, 8, 3],
            [5, 0, 4],
            [8, 5, 0],
            [2, 1, 2],
            [3, 6, 7],
            [7, 8, 1],
        ]

        self.model = CustomTableModel(data)
        self.table.setModel(self.model)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.table)
        self.setLayout(self.layout)

    def resize_table_to_contents(self):
        vh = self.table.verticalHeader()
        hh = self.table.horizontalHeader()
        size = QSize(hh.length(), vh.length())  # Get the length of the headers along each axis.
        size += QSize(vh.size().width(), hh.size().height())  # Add on the lengths from the *other* header
        size += QSize(20, 20)  # Extend further so scrollbars aren't shown.
        self.resize(size)


def main():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    app.exec()


if __name__ == '__main__':
    main()
