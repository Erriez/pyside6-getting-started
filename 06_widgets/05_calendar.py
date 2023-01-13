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

from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QCalendarWidget, QLabel
import sys


class Window(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle('Calendar')

        # https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QCalendarWidget.html
        calendar = QCalendarWidget(self)
        calendar.setGridVisible(True)
        calendar.clicked.connect(self.show_date)
        calendar.setVerticalHeaderFormat(QCalendarWidget.ISOWeekNumbers)

        self.lbl_date = QLabel(self)
        self.lbl_date.setText(calendar.selectedDate().toString())

        layout = QVBoxLayout()
        layout.addWidget(calendar)
        layout.addWidget(self.lbl_date)
        self.setLayout(layout)

    def show_date(self, date):
        self.lbl_date.setText('Selected: ' + date.toString())


def main():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
