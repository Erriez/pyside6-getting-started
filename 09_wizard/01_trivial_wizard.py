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

from PySide6.QtWidgets import QApplication, QFormLayout, QLabel, QLineEdit, QVBoxLayout, QWizardPage, QWizard
import sys


def create_intro_page():
    page = QWizardPage()
    page.setTitle("Introduction")

    label = QLabel("This wizard will help you register your copy of Super Product Two.")
    label.setWordWrap(True)

    layout = QVBoxLayout(page)
    layout.addWidget(label)

    return page


def create_registration_page():
    page = QWizardPage()
    page.setTitle("Registration")
    page.setSubTitle("Please fill both fields.")

    layout = QFormLayout(page)
    layout.addRow("Name:", QLineEdit())
    layout.addRow("Email address:", QLineEdit())

    return page


def create_conclusion_page():
    page = QWizardPage()
    page.setTitle("Conclusion")

    label = QLabel("You are now successfully registered. Have a nice day!")
    label.setWordWrap(True)

    layout = QVBoxLayout(page)
    layout.addWidget(label)

    return page


def main():
    QApplication(sys.argv)

    wizard = QWizard()
    wizard.addPage(create_intro_page())
    wizard.addPage(create_registration_page())
    wizard.addPage(create_conclusion_page())

    wizard.setWindowTitle("Trivial Wizard")
    wizard.show()

    sys.exit(wizard.exec())


if __name__ == '__main__':
    main()
