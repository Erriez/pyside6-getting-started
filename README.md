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
- [02 Menu's and Toolbars](02_menus_toolbars/README.md)
- [03 Layout Management](03_layout_management/README.md)
- [04 Events and Signals](04_events_and_signals/README.md)
- [05 Dialogs](05_dialogs/README.md)
- [06 Widgets](06_widgets/README.md)
- [07 Widgets Specifics](07_widgets_specifics/README.md)
- [08 Wizard](08_wizard/README.md)
- [09 Drag and Drop](09_drag_and_drop/README.md)
- [10 Drawing](10_drawing/README.md)
- [11 Custom Widgets](11_custom_widgets/README.md)
- [12 Qt Creator](12_qt_creator/README.md)
- [13 Games](13_games/README.md)

## PySide6 Documentation

- [Qt for Python](https://doc.qt.io/qtforpython/)
- [PySide6 Python module](https://pypi.org/project/PySide6/)
- [Qt Licensing](https://www.qt.io/licensing/)

## Setup and Usage

- [Linux setup](SETUP_LINUX.md)
- [Windows setup](SETUP_WINDOWS.md)
- MAC setup: Not supported by developer [Erriez](https://github.com/Erriez/).

## Versions and Platforms

Examples are tested with PySide v6.4.2 on Ubuntu 22.10 Wayland and Windows 10.
As Qt is platform independent, it may work on other systems like Raspberry Pi.
See section [Known issues](https://github.com/Erriez/pyside6-getting-started#known-issues) 
for platform specific issues.

## Known issues

- **Linux**: Moving the top window on (Ubuntu) Wayland with widget functions
  `move()` and `setGeometry()` are not supported by Qt / PySide6. This works on
  X11.
