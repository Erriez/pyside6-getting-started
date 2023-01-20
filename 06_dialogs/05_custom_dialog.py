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

from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout,\
    QDialog, QFormLayout, QLineEdit, QDialogButtonBox, QMessageBox, QSpinBox
from PySide6.QtCore import Qt
import sys


# https://doc.qt.io/qtforpython/PySide6/QtWidgets/QDialog.html
class CustomDialog(QDialog):
    def __init__(self, parent=None, title='', name='', age=0):
        super().__init__(parent)

        # Resize window
        self.setMinimumWidth(300)
        self.setWindowTitle(title)

        # Create name text box
        self.txt_name = QLineEdit(name)
        self.txt_name.setMaxLength(20)

        # Create age spinbox
        self.spin_age = QSpinBox()
        self.spin_age.setMinimum(0)
        self.spin_age.setMaximum(100)
        self.spin_age.setValue(age)

        # Add text boxes to form layout
        self.form = QFormLayout()
        self.form.addRow('Name: ', self.txt_name)
        self.form.addRow('Age:', self.spin_age)

        # Create dialog Ok and Cancel buttons
        dialog_buttons = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok |
                                          QDialogButtonBox.StandardButton.Cancel)
        dialog_buttons.accepted.connect(self.accept)
        dialog_buttons.rejected.connect(self.reject)

        # Add form and dialog buttons to vertical box layout
        vbox = QVBoxLayout()
        vbox.addLayout(self.form)
        vbox.addWidget(dialog_buttons)

        # Add vertical layout to window
        self.setLayout(vbox)

    def get_name(self):
        # Return text from textbox
        return self.txt_name.text()

    def get_age(self):
        # Return age from spinbox
        return self.spin_age.value()


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.custom_dialog_modeless = None
        self.name = ''
        self.age = 0

        # Set minimum window size
        self.setMinimumSize(150, 100)
        self.setWindowTitle('Custom dialog')

        self.setWindowFlags(self.windowFlags() & Qt.CustomizeWindowHint)
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowMinMaxButtonsHint)

        # Create push buttons
        show_dialog_model = QPushButton('Model dialog', self)
        show_dialog_model.clicked.connect(self.dialog_model_show)
        show_dialog_model.setFixedWidth(130)
        show_dialog_modeless = QPushButton('Modeless dialog', self)
        show_dialog_modeless.clicked.connect(self.dialog_modeless_show)
        show_dialog_modeless.setFixedWidth(130)

        # Add button to window
        hbox = QHBoxLayout()
        hbox.addWidget(show_dialog_model)
        hbox.addWidget(show_dialog_modeless)

        # Create quit button
        dialog_buttons = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok)
        dialog_buttons.button(QDialogButtonBox.StandardButton.Ok).setText('Quit')
        dialog_buttons.accepted.connect(QApplication.quit)

        # Add model buttons and quit button to layout
        vbox = QVBoxLayout()
        vbox.addLayout(hbox)
        vbox.addWidget(dialog_buttons)

        # Add layout to window
        self.setLayout(vbox)

    def dialog_model_show(self):
        # Create custom model dialog
        custom_dialog_model = CustomDialog(parent=self,
                                           title='Custom Model Dialog',
                                           name=self.name,
                                           age=self.age)

        # Wait until True (Ok / accepted) or False (Cancel / rejected) clicked
        if custom_dialog_model.exec():
            # Get results from dialog
            self.name = custom_dialog_model.get_name()
            self.age = custom_dialog_model.get_age()
            self.show_results(name=self.name, age=self.age)

    def dialog_modeless_show(self):
        # Create custom modeless dialog
        if not self.custom_dialog_modeless:
            self.custom_dialog_modeless = CustomDialog(parent=self,
                                                       title='Custom Modeless Dialog',
                                                       name=self.name,
                                                       age=self.age)
            self.custom_dialog_modeless.accepted.connect(self.dialog_modeless_close)
            self.custom_dialog_modeless.rejected.connect(self.dialog_modeless_reject)

            # Show modeless dialog (show() returns immediately)
            self.custom_dialog_modeless.show()

    def dialog_modeless_close(self):
        # Get results from dialog
        self.name = self.custom_dialog_modeless.get_name()
        self.age = self.custom_dialog_modeless.get_age()
        self.show_results(name=self.name, age=self.age)

        # Destroy object
        self.custom_dialog_modeless = None

    def dialog_modeless_reject(self):
        # Destroy object
        self.custom_dialog_modeless = None

    def show_results(self, name, age):
        # Show results in information message box
        QMessageBox.information(self,
                                'Result',
                                "Hi {}! \nYou are {} years old.".format(name, age),
                                QMessageBox.StandardButton.Ok)


def main():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
