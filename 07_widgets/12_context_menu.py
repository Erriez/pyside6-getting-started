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

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QMenu, QLabel, QMessageBox
from PySide6.QtGui import QFont
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()

        # Resize window and set window title
        self.resize(300, 200)
        self.setWindowTitle("Context menu")

        # Create label
        self.label = QLabel("Right mouse click here...")
        font = QFont("Arial", 14)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet(f"color: red;")

        # Add label to layout and window
        self.vbox = QVBoxLayout(self)
        self.vbox.addWidget(self.label)

        # Create context menu
        self.context_menu = QMenu(self)

        # Create context submenu's
        self.submenu_colors = QMenu("Color")
        self.submenu_window = QMenu("Window")

        # Add actions to color submenu and connect to one grouped triggered event
        self.action_color = self.submenu_colors.addAction("Red")
        self.action_color = self.submenu_colors.addAction("Yellow")
        self.action_color = self.submenu_colors.addAction("Green")
        self.submenu_colors.triggered.connect(self.on_action_color)

        # Add actions to window submenu
        self.action_normal = self.submenu_window.addAction("Normal")
        self.action_normal.triggered.connect(self.on_action_normal)
        self.action_minimize = self.submenu_window.addAction("Minimize")
        self.action_minimize.triggered.connect(self.on_action_minimize)
        self.action_maximize = self.submenu_window.addAction("Maximize")
        self.action_maximize.triggered.connect(self.on_action_maximize)

        # Add action to menu
        self.action_hello_world = self.context_menu.addAction("Show message")
        self.action_hello_world.triggered.connect(self.on_action_hello_world)

        # Add checkable action to menu
        self.action_checked_item = self.context_menu.addAction("Checked item")
        self.action_checked_item.setCheckable(True)
        self.action_checked_item.triggered.connect(self.on_action_checked)

        # Add separators and submenu's to menu
        self.action_sep1 = self.context_menu.addSeparator()
        self.context_menu.addMenu(self.submenu_colors)
        self.context_menu.addMenu(self.submenu_window)
        self.action_sep2 = self.context_menu.addSeparator()

        # Add action to menu
        self.action_quit = self.context_menu.addAction("Quit")
        self.action_quit.triggered.connect(self.on_action_quit)

    def contextMenuEvent(self, event):
        # Show the context menu
        self.context_menu.exec(event.globalPos())

    def on_action_hello_world(self):
        QMessageBox.information(self, "Context Menu", "Hello world from QMenu!")

    def on_action_checked(self, checked: bool):
        QMessageBox.information(self, "Context Menu", f"Checked: {checked}")

    def on_action_color(self, action):
        QMessageBox.information(self, "Color Submenu", f"Selected color: {action.text()}")

    def on_action_normal(self):
        self.showNormal()

    def on_action_minimize(self):
        self.showMinimized()

    def on_action_maximize(self):
        self.showMaximized()

    def on_action_quit(self):
        self.close()


def main():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
