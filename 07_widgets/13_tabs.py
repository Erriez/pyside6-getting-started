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

from PySide6.QtWidgets import (QApplication, QWidget, QLabel, QComboBox, QTabWidget, QCheckBox, QGridLayout,
                               QVBoxLayout, QMenu, QMessageBox, QInputDialog)
from PySide6.QtGui import QPixmap, QCursor
from PySide6.QtCore import Qt, QPoint
from pathlib import Path
import os
import sys


class TabPlaylist(QWidget):
    def __init__(self, title: str):
        super().__init__()

        # Variables
        self._favorite = False

        # Add a label to tab
        self.label = QLabel(f"This is tab \"{title}\"")
        self.label.setAlignment(Qt.AlignCenter)

        # Add label to widget
        self.hbox = QVBoxLayout()
        self.hbox.addWidget(self.label)
        self.setLayout(self.hbox)

    def toggle_favorite(self):
        self._favorite ^= True

    def get_favorite(self):
        return self._favorite


class TabSettings(QWidget):
    def __init__(self, tabs: QTabWidget):
        super().__init__()

        # Store tabs widget
        self.tabs = tabs

        # Add a label to tab
        self.label = QLabel(f"This is the \"Settings\" tab with it's own controls.\nSettings tab cannot be closed.")
        self.label.setAlignment(Qt.AlignCenter)

        # Create widgets
        self.label_tab_dir = QLabel("Tab direction:")
        self.combo_tab_dir = QComboBox()
        self.combo_tab_dir.addItems(["North (default)", "South", "West", "East"])
        self.combo_tab_dir.currentTextChanged.connect(self.on_combo_select)

        self.label_tabs_close_button = QLabel("Tabs close button:")
        self.check_tabs_close_button = QCheckBox()
        self.check_tabs_close_button.setChecked(self.tabs.tabsClosable())
        self.check_tabs_close_button.checkStateChanged.connect(self.on_tabs_close_button_change)

        self.label_tabs_movable = QLabel("Tabs movable:")
        self.check_tabs_movable = QCheckBox()
        self.check_tabs_movable.setChecked(self.tabs.isMovable())
        self.check_tabs_movable.checkStateChanged.connect(self.on_tabs_movable_change)

        # Add widgets to layout
        self.box = QGridLayout()
        self.box.addWidget(self.label_tab_dir, 0, 0)
        self.box.addWidget(self.combo_tab_dir, 0, 1)

        self.box.addWidget(self.label_tabs_close_button, 1, 0)
        self.box.addWidget(self.check_tabs_close_button, 1, 1)

        self.box.addWidget(self.label_tabs_movable, 2, 0)
        self.box.addWidget(self.check_tabs_movable, 2, 1)

        self.box.setColumnStretch(1, 1)
        self.box.addWidget(self.label, 3, 0, 1, 2)

        self.setLayout(self.box)

    def on_combo_select(self, text: str):
        if "North" in text:
            self.tabs.setTabPosition(QTabWidget.North)
        elif "South" in text:
            self.tabs.setTabPosition(QTabWidget.South)
        elif "West" in text:
            self.tabs.setTabPosition(QTabWidget.West)
        elif "East" in text:
            self.tabs.setTabPosition(QTabWidget.East)

    def on_tabs_close_button_change(self, state: Qt.CheckState):
        if state == Qt.Checked:
            self.tabs.setTabsClosable(True)
        else:
            self.tabs.setTabsClosable(False)

    def on_tabs_movable_change(self, state: Qt.CheckState):
        if state == Qt.Checked:
            self.tabs.setMovable(True)
        else:
            self.tabs.setMovable(False)


class Window(QWidget):
    def __init__(self):
        super().__init__()

        # Variables
        self.playlists = 0
        self.last_tab_context_menu = -1

        # Load icons
        self.path = Path(__file__).resolve().parent
        self.playlist_icon = QPixmap(os.path.join(self.path, '../images/playlist.png'))
        self.star_icon = QPixmap(os.path.join(self.path, '../images/star_yellow.png'))
        self.gear_icon = QPixmap(os.path.join(self.path, '../images/gear.png'))

        # Set window size and title
        self.resize(500, 300)
        self.setWindowTitle('Pyside6 Tabs Example by Erriez')
        self.setWindowIcon(self.playlist_icon)

        # Create tab widget
        # https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QTabWidget.html
        self.tabs = QTabWidget()

        # Set tabs properties before creating settings tab
        self.tabs.setTabPosition(QTabWidget.North)
        self.tabs.setTabsClosable(True)
        self.tabs.setMovable(True)

        # Create and add playlist tabs
        for i in range(0, 3):
            self.playlists += 1
            tab_title = f"Playlist {self.playlists}"
            self.tabs.addTab(TabPlaylist(tab_title), self.playlist_icon, tab_title)

        # Created and add settings tab
        self.tab_settings = TabSettings(tabs=self.tabs)
        self.tabs.addTab(self.tab_settings, self.gear_icon, "Settings")

        # Set slots
        self.tabs.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tabs.tabBar().currentChanged.connect(self.on_tab_current_changed)
        self.tabs.tabBar().tabBarClicked.connect(self.on_tab_bar_click)
        self.tabs.tabBar().tabBarDoubleClicked.connect(self.on_tab_bar_double_click)
        self.tabs.tabBar().tabCloseRequested.connect(self.on_tab_close_requested)
        self.tabs.tabBar().tabMoved.connect(self.on_tab_moved)
        self.tabs.customContextMenuRequested.connect(self.on_custom_context_menu_request)

        # Create context menu
        self.context_menu = QMenu()
        self.action_tab_create = self.context_menu.addAction("Create")
        self.action_tab_create.triggered.connect(self.on_action_tab_create)
        self.action_tab_rename = self.context_menu.addAction("Rename")
        self.action_tab_rename.triggered.connect(self.on_action_tab_rename)
        self.action_tab_close = self.context_menu.addAction("Close")
        self.action_tab_close.triggered.connect(self.on_action_tab_close)
        self.context_menu.addSeparator()
        self.action_tab_close_all = self.context_menu.addAction("Close all")
        self.action_tab_close_all.triggered.connect(self.on_action_tab_close_all)

        # Add tab widget to layout
        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.tabs)
        self.setLayout(self.vbox)

    def on_tab_current_changed(self, tab_index: int):
        print(f"Tab current change: {tab_index}")

    def on_tab_bar_click(self, tab_index: int):
        print(f"Tab bar click: {tab_index}")

    def on_tab_bar_double_click(self, tab_index: int):
        print(f"Tab bar double click: {tab_index}")

        # Get tab widget
        widget = self.tabs.widget(tab_index)

        # Check if widget is a TabPlaylist
        if isinstance(widget, TabPlaylist):
            # Toggle and get favorite to set corresponding tab icon
            widget.toggle_favorite()
            if widget.get_favorite():
                self.tabs.tabBar().setTabIcon(tab_index, self.star_icon)
            else:
                self.tabs.tabBar().setTabIcon(tab_index, self.playlist_icon)

    def on_tab_close_requested(self, tab_index: int):
        print(f"Tab close request: {tab_index}")
        if self.tabs.tabBar().tabText(tab_index) == "Settings":
            QMessageBox.warning(self, "Tab close", "Cannot close settings tab.")
            return

        print(f"Removing tab at index {tab_index}")
        self.tabs.removeTab(tab_index)

    def on_tab_moved(self, tab_index: int):
        print(f"Tab moved: {tab_index}")

    def on_custom_context_menu_request(self, point: QPoint):
        print(f"Context menu request ({point.x()},{point.y()})")

        # Convert mouse click in tab bar to tab index
        tab_index = self.tabs.tabBar().tabAt(point)
        if tab_index < 0:
            return

        # Store tab index opened context menu
        self.last_tab_context_menu = tab_index

        # Get selected tab text
        is_settings_tab = False
        if self.tabs.tabBar().tabText(tab_index) == "Settings":
            is_settings_tab = True

        # Enable close menu on playlist tabs and disable on last settings tab
        if is_settings_tab:
            self.action_tab_rename.setDisabled(True)
            self.action_tab_close.setDisabled(True)
        else:
            self.action_tab_rename.setDisabled(False)
            self.action_tab_close.setDisabled(False)

        # Enable close all menu when playlist tabs available
        if self.tabs.count() <= 1:
            self.action_tab_close_all.setDisabled(True)
        else:
            self.action_tab_close_all.setDisabled(False)

        # Show context menu
        self.context_menu.popup(QCursor.pos())

    def on_action_tab_create(self):
        # Set tab index
        tab_insert_index = 0
        if self.last_tab_context_menu >= 0:
            tab_insert_index = self.last_tab_context_menu

        # Set tab title
        self.playlists += 1
        tab_title = f"Playlist {self.playlists}"

        # Insert new tab
        print(f"Inserting tab \"{tab_title}\"at index {tab_insert_index}")
        self.tabs.insertTab(tab_insert_index, TabPlaylist(tab_title), self.playlist_icon, tab_title)

    def on_action_tab_rename(self):
        print(f"Renaming tab at index {self.last_tab_context_menu}")
        tab_text, ok = QInputDialog.getText(self, 'Rename tab', 'Enter a new tab title:')
        if ok:
            self.tabs.tabBar().setTabText(self.last_tab_context_menu, str(tab_text))

    def on_action_tab_close(self):
        print(f"Removing tab at index {self.last_tab_context_menu}")
        self.tabs.removeTab(self.last_tab_context_menu)

    def on_action_tab_close_all(self):
        # Close all tabs except settings tab
        while self.tabs.count() > 1:
            for tab_index in range(0, self.tabs.count()):
                if self.tabs.tabBar().tabText(tab_index) != "Settings":
                    print(f"Removing tab at index {self.last_tab_context_menu}")
                    self.tabs.removeTab(tab_index)
                    # After removing a tab, index and count changes and should restart from index 0
                    break


def main():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
