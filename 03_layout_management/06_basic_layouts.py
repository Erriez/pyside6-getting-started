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
# Sources:
#  - https://doc.qt.io/qtforpython-6/examples/example_widgets_layouts_basiclayouts.html
#  - https://github.com/Erriez/pyside6-getting-started
#

from PySide6.QtWidgets import (QApplication, QComboBox, QDialog,
                               QDialogButtonBox, QGridLayout, QGroupBox,
                               QFormLayout, QHBoxLayout, QLabel, QLineEdit,
                               QMenu, QMenuBar, QPushButton, QSpinBox,
                               QTextEdit, QVBoxLayout)
import sys


class Dialog(QDialog):
    num_grid_rows = 3
    num_buttons = 4

    def __init__(self):
        super().__init__()

        self.resize(600, 350)
        self.setWindowTitle("Basic Layouts")

        self.create_menu()
        self.create_horizontal_group_box()
        self.create_grid_group_box()
        self.create_form_group_box()

        big_editor = QTextEdit()
        big_editor.setPlainText("This widget takes up all the remaining space "
                                "in the top-level layout.")

        button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)

        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)

        main_layout = QVBoxLayout()
        main_layout.setMenuBar(self._menu_bar)
        main_layout.addWidget(self._horizontal_group_box)
        main_layout.addWidget(self._grid_group_box)
        main_layout.addWidget(self._form_group_box)
        main_layout.addWidget(big_editor)
        main_layout.addWidget(button_box)
        self.setLayout(main_layout)

    def create_menu(self):
        self._menu_bar = QMenuBar()

        self._file_menu = QMenu("&File", self)
        self._exit_action = self._file_menu.addAction("E&xit")
        self._menu_bar.addMenu(self._file_menu)

        self._exit_action.triggered.connect(self.accept)

    def create_horizontal_group_box(self):
        self._horizontal_group_box = QGroupBox("Horizontal layout")
        layout = QHBoxLayout()

        for i in range(Dialog.num_buttons):
            button = QPushButton(f"Button {i + 1}")
            layout.addWidget(button)

        self._horizontal_group_box.setLayout(layout)

    def create_grid_group_box(self):
        self._grid_group_box = QGroupBox("Grid layout")
        layout = QGridLayout()

        for i in range(Dialog.num_grid_rows):
            label = QLabel(f"Line {i + 1}:")
            line_edit = QLineEdit()
            layout.addWidget(label, i + 1, 0)
            layout.addWidget(line_edit, i + 1, 1)

        self._small_editor = QTextEdit()
        self._small_editor.setPlainText("This widget takes up about two thirds of the grid layout.")

        layout.addWidget(self._small_editor, 0, 2, 4, 1)

        layout.setColumnStretch(1, 10)
        layout.setColumnStretch(2, 20)
        self._grid_group_box.setLayout(layout)

    def create_form_group_box(self):
        self._form_group_box = QGroupBox("Form layout")
        layout = QFormLayout()
        layout.addRow(QLabel("LineEdit:"), QLineEdit("Enter your text here"))
        combobox = QComboBox()
        combobox.addItems(["Black", "White", "Red", "Blue", "Green"])
        layout.addRow(QLabel("ComboBox, long text:"), combobox)
        layout.addRow(QLabel("SpinBox:"), QSpinBox())
        self._form_group_box.setLayout(layout)


def main():
    app = QApplication(sys.argv)
    dialog = Dialog()
    dialog.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
