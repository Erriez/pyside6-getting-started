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

from PySide6.QtWidgets import QApplication, QWidget, QSystemTrayIcon, QMenu, \
    QMessageBox, QSizePolicy, QPushButton, QCheckBox, QVBoxLayout
from PySide6.QtGui import Qt, QIcon, QAction
import sys


# https://doc.qt.io/qtforpython/PySide6/QtWidgets/QMessageBox.html
class ResizableMessageBox(QMessageBox):
    def __init__(self):
        QMessageBox.__init__(self)

        # Enable size grip on lower right corner
        self.setSizeGripEnabled(True)

    def event(self, e):
        # Undocumented: The only way of resizing a QMessageBox is from an event
        result = QMessageBox.event(self, e)

        # Set min/max sizes QMessageBox
        self.setMinimumSize(275, 125)
        self.setMaximumSize(500, 500)

        # https://doc.qt.io/qtforpython/PySide6/QtWidgets/QSizePolicy.html
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # Return event
        return result


class Window(QWidget):
    def __init__(self, system_tray):
        super().__init__()

        # Save system tray object
        self._system_tray = system_tray

        # Resize window
        self.resize(300, 150)

        # Set window title
        self.setWindowTitle('System Tray')

        # Create push button
        btn_show_info = QPushButton('Show info', self)
        btn_show_info.clicked.connect(self.on_btn_show_info)

        btn_show_warning = QPushButton('Show warning', self)
        btn_show_warning.setToolTip('Show <b>QSystemTrayIcon</b> warning message')
        btn_show_warning.resize(btn_show_warning.sizeHint())
        btn_show_warning.clicked.connect(self.on_btn_show_warning)

        btn_show_critical = QPushButton('Show critical', self)
        btn_show_critical.clicked.connect(self.on_btn_show_critical)

        self.chk_value = QCheckBox('Value')
        self.chk_value.setChecked(True)

        # Add widgets to window
        layout = QVBoxLayout(self)
        layout.addWidget(btn_show_info)
        layout.addWidget(btn_show_warning)
        layout.addWidget(btn_show_critical)
        layout.addWidget(self.chk_value)

    def showEvent(self, event):
        menu = self._system_tray.contextMenu()
        print(menu)

        is_checked = self.chk_value.isChecked()
        print(is_checked)

    def on_btn_show_info(self):
        # Show system tray popup with info icon
        self._system_tray.showMessage('Message Title',
                                      'Information.',
                                      icon=QSystemTrayIcon.MessageIcon.Information,
                                      msecs=5000)

    def on_btn_show_warning(self):
        # Show system tray popup
        self._system_tray.showMessage('Message Title',
                                      'Warning.',
                                      icon=QSystemTrayIcon.MessageIcon.Warning,
                                      msecs=5000)

    def on_btn_show_critical(self):
        # Show system tray popup
        self._system_tray.showMessage('Message Title',
                                      'Critical.',
                                      icon=QSystemTrayIcon.MessageIcon.Critical,
                                      msecs=5000)


class Application(QApplication):
    def __init__(self, args):
        super().__init__(args)

        self._menu = None
        self._system_tray = None
        self._window = None

        self.btn_show_hide = None
        self.btn_minimize = None
        self.btn_hello = None
        self.chk_option = None
        self.btn_quit = None

        # Keep application running when all windows are closed
        self.setQuitOnLastWindowClosed(False)
        # Set window icon
        self.setWindowIcon(QIcon("../images/web.png"))

        # Create tray menu
        self.create_menu()

        # Create system tray
        self.create_system_tray()

        # Create window widget
        self._window = Window(self._system_tray)

        # Application main loop
        sys.exit(self.exec())

    def create_menu(self):
        # Create the menu
        # The system tray icon does not take ownership of the menu. You must ensure
        # that it is deleted at the appropriate time by, for example, creating the
        # menu with a suitable parent object.
        self._menu = QMenu()

        # Create hello button
        self.btn_show_hide = QAction('Show')
        self.btn_show_hide.triggered.connect(self.on_btn_show)

        self.btn_minimize = QAction('Minimize')
        self.btn_minimize.triggered.connect(self.on_btn_minimize)

        self.btn_hello = QAction('Say hi!')
        self.btn_hello.triggered.connect(self.on_btn_hello)

        self.chk_option = QAction('Value')
        self.chk_option.setCheckable(True)
        self.chk_option.setChecked(True)
        self.chk_option.triggered.connect(self.on_checkbox_change)

        # Create quit button
        self.btn_quit = QAction('Quit')
        self.btn_quit.triggered.connect(QApplication.quit)

        # Add buttons to menu
        self._menu.addAction(self.btn_show_hide)
        self._menu.addAction(self.btn_minimize)
        self._menu.addAction(self.btn_hello)
        self._menu.addAction(self.chk_option)
        self._menu.addSeparator()
        self._menu.addAction(self.btn_quit)

    def create_system_tray(self):
        # Create system tray icon with menu
        # https://doc.qt.io/qtforpython/PySide6/QtWidgets/QSystemTrayIcon.html
        self._system_tray = QSystemTrayIcon()

        # Set system tray icon
        self._system_tray.setIcon(QIcon("../images/web.png"))

        # Make system tray icon with menu visible
        self._system_tray.setVisible(True)

        # Set system tray tooltip
        self._system_tray.setToolTip('PySide6 app')

        # Add the menu to the system tray
        self._system_tray.setContextMenu(self._menu)

        # Show system tray
        self._system_tray.show()

    def on_btn_show(self):
        # When the window is minimized on Ubuntu, it does not restore to normal
        # after calling show() or showNormal(). Workaround is to call hide()
        # first followed by showNormal().
        self._window.hide()
        self._window.showNormal()

    def on_btn_minimize(self):
        self._window.showMinimized()

    def on_checkbox_change(self, checked):
        self._window.chk_value.setChecked(checked)

    @staticmethod
    def on_btn_hello():
        # https://doc.qt.io/qtforpython/PySide6/QtWidgets/QMessageBox.html#PySide6.QtWidgets.PySide6.QtWidgets.QMessageBox.Icon
        icon = QMessageBox.Icon.Information
        title = 'System Tray'
        message = 'Hello world!'

        msgbox = ResizableMessageBox()
        msgbox.setIcon(icon)
        msgbox.setWindowTitle(title)
        msgbox.setText(message)
        # https://doc.qt.io/qtforpython/PySide6/QtWidgets/QMessageBox.html#PySide6.QtWidgets.PySide6.QtWidgets.QMessageBox.StandardButton
        msgbox.setStandardButtons(QMessageBox.StandardButton.Ok)

        msgbox.exec()


def main():
    # Create application
    Application(sys.argv)


if __name__ == '__main__':
    main()
