# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox

# Important:
# You need to run the following command to convert .ui to .py files:
#     pyside6-uic qt_creator_mainwindow.ui -o qt_creator_mainwindow.py
#     pyside6-uic qt_creator_dialog.ui -o qt_creator_dialog.py
from qt_creator_mainwindow import Ui_MainWindow
from qt_creator_dialog import Ui_Dialog

class Dialog(Ui_Dialog, QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.buttonShowDialog.clicked.connect(self.on_show_dialog)

    def on_show_dialog(self, s):
        dialog = Dialog(self)
        if dialog.exec() == QDialog.Accepted:
            QMessageBox.information(self, "Dialog", f"Hello {dialog.editName.text()}!")
        else:
            QMessageBox.information(self, "Dialog", "Clicked cancel")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
