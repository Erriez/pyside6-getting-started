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

from PySide6.QtWidgets import (QApplication, QWidget, QLabel, QGridLayout, QLineEdit, QHBoxLayout, QVBoxLayout,
                               QPushButton, QMessageBox)
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from pathlib import Path
import os
import sys


class Window(QWidget):
    USERNAME = "user"
    PASSWORD = "password"
    NUM_PASSWORD_RETRIES = 3

    def __init__(self):
        super().__init__()

        # Set default number of password retries
        self.password_retries = self.NUM_PASSWORD_RETRIES

        # Path to images
        path = Path(__file__).resolve().parent
        self.img_eye_red = QPixmap(os.path.join(path, '../images/eye_red.png'))
        self.img_eye_green = QPixmap(os.path.join(path, '../images/eye_green.png'))

        # Set window size and title
        self.setMinimumSize(250, 100)
        self.setWindowTitle('Login')
        self.setWindowFlags(Qt.WindowType.WindowCloseButtonHint)

        # Username
        self.label_username = QLabel('Username:')
        self.edit_username = QLineEdit()
        self.edit_username.setToolTip(f"Hint: use \"{self.USERNAME}\"")

        # Password
        self.label_password = QLabel('Password:')
        self.edit_password = QLineEdit(echoMode=QLineEdit.EchoMode.Password)
        self.edit_password.setToolTip(f"Hint: use \"{self.PASSWORD}\"")

        # Buttons
        self.button_show_password = QPushButton()
        self.button_show_password.setIcon(self.img_eye_green)
        self.button_cancel = QPushButton('Cancel')
        self.button_login = QPushButton('Log in')

        # Add username/password widgets to grid layout
        self.grid = QGridLayout()
        self.grid.addWidget(self.label_username, 0, 0)
        self.grid.addWidget(self.edit_username, 0, 1, 1, 2)

        self.grid.addWidget(self.label_password, 1, 0)
        self.grid.addWidget(self.edit_password, 1, 1)
        self.grid.addWidget(self.button_show_password, 1, 2)

        # Add cancel/login buttons to horizontal layout
        self.hbox = QHBoxLayout()
        self.hbox.addWidget(self.button_cancel)
        self.hbox.addWidget(self.button_login)

        # Add layouts to window widget
        self.vbox = QVBoxLayout()
        self.vbox.addLayout(self.grid)
        self.vbox.addStretch()
        self.vbox.addLayout(self.hbox)
        self.setLayout(self.vbox)

        # Add button events
        self.button_show_password.clicked.connect(self.on_toggle_show_password)
        self.button_login.clicked.connect(self.on_login)
        self.button_cancel.clicked.connect(self.close)

    def on_login(self):
        if not self.edit_username.text():
            QMessageBox().warning(self, "Login", "Please enter your username.", QMessageBox.Ok)
            return
        if not self.edit_password.text():
            QMessageBox().warning(self, "Login", "Please enter your password.", QMessageBox.Ok)
            return

        # WARNING: Username/password handling in plain text is for demonstration purposes only!
        if self.edit_username.text() == self.USERNAME and self.edit_password.text() == self.PASSWORD:
            QMessageBox().information(self, "Welcome", "Logged in!")
            self.close()
        else:
            msg = "Incorrect username or password. "
            if self.password_retries:
                msg += f"{self.password_retries} retries left."
            else:
                msg = "Login failed!"
            QMessageBox().warning(self, "Login", msg, QMessageBox.Ok)

            if self.password_retries <= 0:
                self.close()
            self.password_retries -= 1

    def on_toggle_show_password(self):
        # Toggle text visibility edit box and show password button icon
        if self.edit_password.echoMode() == QLineEdit.Normal:
            self.edit_password.setEchoMode(QLineEdit.Password)
            self.button_show_password.setIcon(self.img_eye_green)
        else:
            self.edit_password.setEchoMode(QLineEdit.Normal)
            self.button_show_password.setIcon(self.img_eye_red)

    def keyPressEvent(self, event):
        # Get keyboard key press event
        key = event.key()

        if key == Qt.Key_Escape:
            # Close window wen ESC key pressed
            self.close()
        elif key == Qt.Key_Return or key == Qt.Key_Enter:
            # Handle enter key depending on focus
            if self.edit_username.hasFocus():
                self.edit_password.setFocus()
            elif self.edit_password.hasFocus():
                self.button_login.click()
            elif self.button_login.hasFocus():
                self.button_login.click()
            elif self.button_cancel.hasFocus():
                self.close()

def main():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
