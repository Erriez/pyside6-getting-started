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

from PySide6.QtWidgets import QApplication, QWidget, QFrame, QSplitter, QStyleFactory, QLabel, QHBoxLayout
from PySide6.QtCore import Qt
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.resize(300, 300)
        self.setWindowTitle('QSplitter')

        # Create 3 frames
        top_left_frame = QFrame(self)
        top_left_frame.setFrameShape(QFrame.StyledPanel)

        top_right_frame = QFrame(self)
        top_right_frame.setFrameShape(QFrame.StyledPanel)

        bottom_frame = QFrame(self)
        bottom_frame.setFrameShape(QFrame.StyledPanel)

        # Add label to center of each frame
        top_left_label = QLabel('Top left')
        top_left_label.setAlignment(Qt.AlignCenter)
        top_left_hbox = QHBoxLayout()
        top_left_hbox.addWidget(top_left_label)
        top_left_frame.setLayout(top_left_hbox)

        top_right_label = QLabel('Top right')
        top_right_label.setAlignment(Qt.AlignCenter)
        top_right_hbox = QHBoxLayout()
        top_right_hbox.addWidget(top_right_label)
        top_right_frame.setLayout(top_right_hbox)

        bottom_label = QLabel('Bottom')
        bottom_label.setAlignment(Qt.AlignCenter)
        bottom_hbox = QHBoxLayout()
        bottom_hbox.addWidget(bottom_label)
        bottom_frame.setLayout(bottom_hbox)

        # Add frames to splitter
        # https://doc.qt.io/qtforpython/PySide6/QtWidgets/QSplitter.html
        splitter1 = QSplitter(Qt.Horizontal)
        splitter1.addWidget(top_left_frame)
        splitter1.addWidget(top_right_frame)

        splitter2 = QSplitter(Qt.Vertical)
        splitter2.addWidget(splitter1)
        splitter2.addWidget(bottom_frame)

        # Add splitter to window
        hbox = QHBoxLayout(self)
        hbox.addWidget(splitter2)
        self.setLayout(hbox)
        QApplication.setStyle(QStyleFactory.create('Cleanlooks'))


def main():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
