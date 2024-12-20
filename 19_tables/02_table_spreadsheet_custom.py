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

from PySide6.QtWidgets import (QApplication, QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout, QLabel)
from PySide6.QtGui import QFont, QBrush, QColor, QPixmap
from PySide6.QtCore import Qt, QSize
from pathlib import Path
import os
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()

        # Path to find images directory
        self.path = Path(__file__).resolve().parent

        # Set window size and title
        self.resize(400, 250)
        self.setWindowTitle("SpreadSheet example")

        # https://doc.qt.io/qtforpython/PySide6/QtWidgets/QTableWidget.html
        # Create table widget
        self.table = QTableWidget(6, 3)

        # Set column names
        self.table.setHorizontalHeaderLabels(["Name", "Age", "Gender"])
        self.table.horizontalHeader().setStyleSheet(f"background-color: lightblue;")
        self.table.verticalHeader().setStyleSheet(f"background-color: lightgreen;")

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

        # ---------------------------
        # Set cell with different font and colors
        font = QFont("Arial", 14)                       # Create font with size
        font.setBold(True)                              # Make font bold

        item_name = QTableWidgetItem("Anne")
        item_name.setFont(font)                              # Set cell font
        item_name.setTextAlignment(Qt.AlignCenter)           # Set cell text alignment
        item_name.setForeground(QBrush(QColor(Qt.yellow)))   # Set cell foreground color
        item_name.setBackground(QBrush(QColor(Qt.red)))      # Set cell background color
        item_name.setFlags(item_name.flags() ^ Qt.ItemIsEditable) # Disable cell editing

        # Create table cell picture
        self.label_widget = QLabel()
        self.label_widget.setPixmap(
            QPixmap(os.path.join(self.path, '../images/web.png')).scaled(QSize(20, 20), Qt.KeepAspectRatio))

        # Add data to table row
        self.table.setItem(5, 0, item_name)
        self.table.setItem(5, 1, QTableWidgetItem("28"))
        self.table.setCellWidget(5, 2, self.label_widget)
        # ---------------------------

        # Set table column width
        self.table.setColumnWidth(0, 150)

        # Make table sortable by clicking on the header
        self.table.setSortingEnabled(True)

        # Add table to layout, add layout to widget
        self.vBox = QVBoxLayout()
        self.vBox.addWidget(self.table)
        self.setLayout(self.vBox)

        # Add signals
        self.table.cellClicked.connect(self.on_cell_click)
        self.table.itemChanged.connect(self.on_item_changed)
        self.table.itemSelectionChanged.connect(self.on_item_selection_changed)

    def on_cell_click(self, row, column):
        print(f"Clicked {row} {column}")

    def on_item_changed(self, item):
        print(f"Item {item.row(), item.column()} changed to {item.text()}")

    def on_item_selection_changed(self):
        print(f"Item selection changed {self.table.currentRow(), self.table.currentColumn()}")


def main():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
