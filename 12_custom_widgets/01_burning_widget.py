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

from PySide6.QtWidgets import QApplication, QWidget, QSlider, QHBoxLayout, QVBoxLayout
from PySide6.QtCore import Qt, QObject, Signal
from PySide6.QtGui import QPainter, QFont, QColor, QPen
import sys


class Communicate(QObject):
    updateBW = Signal(int)


class BurningWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.setMinimumSize(1, 30)
        self.value = 75
        self.num = [75, 150, 225, 300, 375, 450, 525, 600, 675]

    def setValue(self, value):
        self.value = value

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.drawWidget(qp)
        qp.end()

    def drawWidget(self, qp):
        font = QFont('Serif', 7, QFont.Light)
        qp.setFont(font)

        size = self.size()
        w = size.width()
        h = size.height()

        step = int(round(w / 10.0))

        till = int(((w / 750.0) * self.value))
        full = int(((w / 750.0) * 700))

        if self.value >= 700:
            qp.setPen(QColor(255, 255, 255))
            qp.setBrush(QColor(255, 255, 184))
            qp.drawRect(0, 0, full, h)
            qp.setPen(QColor(255, 175, 175))
            qp.setBrush(QColor(255, 175, 175))
            qp.drawRect(full, 0, till - full, h)
        else:
            qp.setPen(QColor(255, 255, 255))
            qp.setBrush(QColor(255, 255, 184))
            qp.drawRect(0, 0, till, h)

        pen = QPen(QColor(20, 20, 20), 1, Qt.SolidLine)

        qp.setPen(pen)
        qp.setBrush(Qt.NoBrush)
        qp.drawRect(0, 0, w - 1, h - 1)

        j = 0

        for i in range(step, 10 * step, step):
            qp.drawLine(i, 0, i, 5)
            metrics = qp.fontMetrics()
            fw = metrics.horizontalAdvance(str(self.num[j]))
            qp.drawText(i - fw / 2, h / 2, str(self.num[j]))
            j = j + 1


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.resize(350, 200)
        self.setWindowTitle('Burning widget')

        slider = QSlider(Qt.Horizontal, self)
        slider.setFocusPolicy(Qt.NoFocus)
        slider.setRange(1, 750)
        slider.setValue(75)
        slider.setGeometry(30, 40, 150, 30)

        self.c = Communicate()
        self.burning = BurningWidget()
        self.c.updateBW[int].connect(self.burning.setValue)

        slider.valueChanged.connect(self.on_slider_change)
        hbox = QHBoxLayout()
        hbox.addWidget(self.burning)
        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        self.setLayout(vbox)

    def on_slider_change(self, value):
        self.c.updateBW.emit(value)
        self.burning.repaint()


def main():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
