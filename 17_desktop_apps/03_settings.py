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

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QStatusBar,
    QDialog,
    QLabel,
    QPushButton,
    QLineEdit,
    QComboBox,
    QVBoxLayout,
    QGridLayout,
    QDialogButtonBox,
    QMessageBox
)
from PySide6.QtGui import QAction, QIcon
from PySide6.QtCore import Qt, QCoreApplication, QPoint, QSize, QSettings
import sys

# Default application defines
ORGANIZATION_NAME = "Erriez"
APPLICATION_NAME = "PySide6 Settings Example"


class Settings:
    """
    Class to convert settings between application and QSettings.
    Handle object types and default values.
    """
    _data = {
        "startup-count": {"value": None, "default": 1},
        "window-title": {"value": None, "default": APPLICATION_NAME},
        "window-state": {"value": None, "default": Qt.WindowState.WindowNoState},
        "window-size": {"value": None, "default": QSize(350, 200)},
        "window-position": {"value": None, "default": QPoint(100, 100)},
    }

    def __init__(self):
        self._deleted = False

        # Create QSettings object
        self._settings = QSettings()

        # Load settings
        self.load()

    def __del__(self):
        self.save()

    @property
    def path(self) -> str:
        # Return settings path
        return self._settings.fileName()

    def get(self, key):
        # Return a setting and set default value
        default_value = self._data[key]["default"]
        value = self._data[key]["value"]
        if type(value) != type(default_value):
            value = default_value
        return value

    def set(self, key: str, value):
        # Save new setting
        if key not in self._data:
            raise f"Setting \"{key}\" not defined"
        if type(value) != type(self._data[key]["default"]):
            raise f"Setting \"{key}\" invalid type"
        self._data[key]["value"] = value

    def remove_all(self):
        # Remove all settings
        self._settings.clear()
        self._deleted = True

    def print(self):
        # Print settings
        print(f"Settings \"{self._settings.fileName()}\":")
        for key in self._settings.allKeys():
            print(f"  {key}: {self._settings.value(key)}")

    def load(self):
        # Load settings
        for key in self._data.keys():
            self.set(key, self._settings.value(key, self._data[key]["default"]))

    def save(self):
        # Save settings when not deleted
        if not self._deleted:
            for key in self._data.keys():
                self._settings.setValue(key, self._data[key]["value"])
            # Save settings
            self._settings.sync()

class DialogSettings(QDialog):
    """
    Settings dialog window.
    """
    WINDOW_STATES = {
        "Normal": Qt.WindowState.WindowNoState,
        "Minimized": Qt.WindowState.WindowMinimized,
        "Maximized": Qt.WindowState.WindowMaximized,
    }

    def __init__(self, settings: Settings):
        super().__init__()

        # Store settings
        self.settings = settings

        # Set window title and icon
        self.setWindowTitle("Settings")
        self.setWindowIcon(QIcon.fromTheme(QIcon.ThemeIcon.DocumentProperties))

        # Add window title
        self.label_window_title = QLabel("Window title:")
        self.edit_window_title = QLineEdit(self.settings.get("window-title"))
        self.button_reset_window_title = QPushButton("Default")
        self.button_reset_window_title.clicked.connect(self.on_reset_window_title)

        # Default startup window state
        self.label_startup_window = QLabel("Startup state:")
        self.combobox_startup_window = QComboBox()
        self.combobox_startup_window.addItems(list(self.WINDOW_STATES.keys()))
        # Select default item in combobox
        for i, key in enumerate(self.WINDOW_STATES.keys()):
            if self.WINDOW_STATES.get(key) == self.settings.get("window-state"):
                self.combobox_startup_window.setCurrentIndex(i)
                break

        # Startup count
        self.label_startup_count = QLabel("Startup count:")
        self.label_startup_count_value = QLabel(str(self.settings.get("startup-count")))
        self.button_reset_startup_count = QPushButton("Reset")
        self.button_reset_startup_count.clicked.connect(self.on_reset_startup_count)

        # Settings path
        self.label_path = QLabel("Settings path:")
        self.label_path_value = QLabel(self.settings.path)

        # Button to remove all settings
        self.button_remove = QPushButton("Remove")
        self.button_remove.clicked.connect(self.on_button_remove)

        # Dialog buttons Ok and Cancel
        self.button_box = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok |
                                           QDialogButtonBox.StandardButton.Cancel |
                                           QDialogButtonBox.StandardButton.Apply)
        self.button_box.accepted.connect(self.on_accept)
        self.button_box.rejected.connect(self.reject)
        self.button_box.clicked.connect(self.on_button_box_click)

        # Add controls to grid layout
        self.grid = QGridLayout()
        self.grid.addWidget(self.label_startup_window, 0, 0)
        self.grid.addWidget(self.combobox_startup_window, 0, 1)
        self.grid.addWidget(self.label_window_title, 1, 0)
        self.grid.addWidget(self.edit_window_title, 1, 1)
        self.grid.addWidget(self.button_reset_window_title, 1, 2)
        self.grid.addWidget(self.label_startup_count, 2, 0)
        self.grid.addWidget(self.label_startup_count_value, 2, 1)
        self.grid.addWidget(self.button_reset_startup_count, 2, 2)
        self.grid.addWidget(self.label_path, 3, 0)
        self.grid.addWidget(self.label_path_value, 3, 1)
        self.grid.addWidget(self.button_remove, 3, 2)
        self.grid.setColumnStretch(1, 1)

        # Add grid and button box to vertical box layout
        self.vbox = QVBoxLayout()
        self.vbox.addLayout(self.grid)
        self.vbox.addStretch()
        self.vbox.addWidget(self.button_box)

        # Add vertical box layout to window
        self.setLayout(self.vbox)

    def on_button_remove(self):
        # Remove all settings
        self.settings.remove_all()

        # Exit application
        QMessageBox.information(self, "Settings", "Settings removed, closing application.")
        QCoreApplication.quit()

    def on_reset_window_title(self):
        self.edit_window_title.setText(APPLICATION_NAME)

    def on_reset_startup_count(self):
        self.settings.startup_count = 1
        self.label_startup_count_value.setText(str(self.settings.startup_count))

    def on_accept(self):
        # Handle OK button
        self._update()
        self.settings.save()
        self.accept()

    def on_button_box_click(self, button: QPushButton):
        # Handle Apply button
        role = self.button_box.buttonRole(button)
        if role == QDialogButtonBox.ApplyRole:
            self._update()
            self.settings.save()

    def _update(self):
        self.settings.set("window-title", self.edit_window_title.text())
        self.settings.set("window-state",
                          self.WINDOW_STATES.get(self.combobox_startup_window.currentText(),
                                                 Qt.WindowState.WindowNoState))

class MainWindow(QMainWindow):
    """
    Main application window with menubar, label and statusbar.
    """

    def __init__(self, settings: Settings):
        super().__init__()

        # Store settings
        self.settings = settings

        # Set window title, icon, state, size and position
        self.setWindowTitle(self.settings.get("window-title"))
        self.setWindowIcon(QIcon.fromTheme(QIcon.ThemeIcon.DocumentProperties))
        self.setWindowState(self.settings.get("window-state"))
        self.resize(self.settings.get("window-size"))
        self.move(self.settings.get("window-position"))

        # Create actions
        self.action_quit = QAction(QIcon.fromTheme(QIcon.ThemeIcon.ApplicationExit), '&Quit', self)
        self.action_quit.setShortcut('Ctrl+Q')
        self.action_quit.setStatusTip('Exit application')
        self.action_quit.triggered.connect(self.close)

        self.action_settings = QAction(QIcon.fromTheme(QIcon.ThemeIcon.DocumentProperties), '&Settings', self)
        self.action_settings.setShortcut('Ctrl+,')
        self.action_settings.setStatusTip('Application settings')
        self.action_settings.triggered.connect(self.on_settings)

        self.action_about = QAction(QIcon.fromTheme(QIcon.ThemeIcon.HelpAbout), '&Help', self)
        self.action_about.setShortcut('F1')
        self.action_about.setStatusTip('About')
        self.action_about.triggered.connect(self.on_about)

        # Create menubar
        self.menu = self.menuBar()

        self.menu_file = self.menu.addMenu("&File")
        self.menu_file.addAction(self.action_settings)
        self.menu_file.addSeparator()
        self.menu_file.addAction(self.action_quit)

        self.menu_help = self.menu.addMenu("&Help")
        self.menu_help.addAction(self.action_about)

        # Create widgets
        self.label = QLabel("Click File | Settings")
        self.label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(self.label)

        # Create statusbar
        self.setStatusBar(QStatusBar(self))

    def __del__(self):
        self.settings.set("window-position", self.pos())
        self.settings.set("window-size", self.size())

    def on_settings(self):
        dialog_settings = DialogSettings(self.settings)
        if dialog_settings.exec() == QDialog.Accepted:
            pass # Nothing to do

        # Update window title
        self.setWindowTitle(self.settings.get("window-title"))

    def on_about(self):
        QMessageBox.information(self, "About", APPLICATION_NAME)


def main():
    # Set organization and application names used by QSettings
    QCoreApplication.setOrganizationName(ORGANIZATION_NAME)
    QCoreApplication.setApplicationName(APPLICATION_NAME)

    # Load application settings
    settings = Settings()

    # Increment startup count
    startup_count = settings.get("startup-count")
    startup_count += 1
    settings.set("startup-count", startup_count)

    # Print settings
    settings.print()

    # Create application and pass settings
    app = QApplication(sys.argv)
    main_window = MainWindow(settings)
    main_window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
