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

from PySide6.QtWidgets import QApplication, QWidget, QSystemTrayIcon, QMenu, \
    QMessageBox, QSizePolicy, QPushButton, QHBoxLayout
from PySide6.QtGui import QIcon, QAction
from pathlib import Path
import os
import sys


def main():
    app = QApplication(sys.argv)

    # Keep application running when all windows are closed
    app.setQuitOnLastWindowClosed(False)
    # Set window icon
    path = Path(__file__).resolve().parent
    app.setWindowIcon(QIcon(os.path.join(path, "../images/web.png")))

    # Create the menu
    # The system tray icon does not take ownership of the menu. You must ensure
    # that it is deleted at the appropriate time by, for example, creating the
    # menu with a suitable parent object.
    menu = QMenu()

    # Create quit button
    btn_quit = QAction('Quit')
    btn_quit.triggered.connect(QApplication.quit)

    # Add buttons to menu
    menu.addAction(btn_quit)

    # Create system tray icon with menu
    # https://doc.qt.io/qtforpython/PySide6/QtWidgets/QSystemTrayIcon.html
    system_tray = QSystemTrayIcon()

    # Set system tray icon
    system_tray.setIcon(QIcon(os.path.join(path, "../images/web.png")))

    # Make system tray icon with menu visible
    system_tray.setVisible(True)

    # Add the menu to the system tray
    system_tray.setContextMenu(menu)

    # Show system tray
    system_tray.show()

    # Application main loop
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
