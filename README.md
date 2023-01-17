# Qt PySide6 Getting Started

This repository contains simple getting started examples to develop Qt
applications in Python using PySide6. It is intended for educational purposes
and self study:

- Basic Python knowledge recommended.
- No experiences with Qt or PySide required.
- A computer to run / test the examples.

## PySide6 Introduction

PySide6 is the official `Qt for Python` module, which provides access to the
complete Qt 6.0+ framework. It is available under both Open Source 
(LGPLv3/GPLv2) and commercial license. Using PyPi (PIP) is the recommended
installation source.

## PySide6 Examples

- [00 Qt Core](00_qt_core/README.md)
- [01 Getting Started](01_gettings_started/README.md)
- [02 Messagebox](02_messagebox/README.md)
- [03 Layout Management](03_layout_management/README.md)
- [04 Menu's and Toolbars](04_menus_toolbars/README.md)
- [05 Events and Signals](05_events_and_signals/README.md)
- [06 Dialogs](06_dialogs/README.md)
- [07 Widgets](07_widgets/README.md)
- [08 Widgets Specifics](08_widgets_specifics/README.md)
- [09 Wizard](09_wizard/README.md)
- [10 Drag and Drop](10_drag_and_drop/README.md)
- [11 Drawing](11_drawing/README.md)
- [12 Custom Widgets](12_custom_widgets/README.md)
- [13 Qt Creator](13_qt_creator/README.md)
- [14 System tray](14_system_tray/README.md)
- [15 Games](15_games/README.md)

## PySide6 Documentation

- [Qt for Python](https://doc.qt.io/qtforpython/)
- [PySide6 Python module](https://pypi.org/project/PySide6/)
- [Qt Licensing](https://www.qt.io/licensing/)

## Setup and Usage

- [Linux setup](SETUP_LINUX.md)
- [Windows setup](SETUP_WINDOWS.md)
- MAC setup: Not supported by developer [Erriez](https://github.com/Erriez/).

## Debug with PyCharm

- [Debug with free PyCharm](SETUP_PyCharm.md) (On Windows and Linux desktops)

## Versions and Platforms

Examples are tested with PySide v6.4.2 on Ubuntu 22.10 Wayland and Windows 10.
As Qt is platform independent, it may work on other systems like Raspberry Pi.
See section [Known issues](https://github.com/Erriez/pyside6-getting-started#known-issues) 
for platform specific issues.

## Known issues

- **Linux**: Moving the top window on (Ubuntu) Wayland with widget functions
  `move()` and `setGeometry()` are not supported by Qt / PySide6. This works on
  X11.
