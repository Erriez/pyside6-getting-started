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
- [15 Miscellaneous](15_misc/README.md)
- [16 Games](16_games/README.md)
- [17 Desktop Applications](17_desktop_apps/README.md)

## PySide6 Deployment

A separate PySide6 deployment project for Windows / Linux using Nuitka on
Github Actions is available 
[here](https://github.com/Erriez/pyside6-nuitka-deployment). 

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

Examples are tested with PySide 6.7.2 on Ubuntu 22.10 Wayland and
Windows 10/11.
As Qt is platform independent, it may work on other systems like Raspberry Pi.
See section [Known issues](https://github.com/Erriez/pyside6-getting-started#known-issues) 
for platform specific issues.

## Known Bugs and Issues

The following `Qt` / `PySide6` / `Qt Creator` bugs are reported and affects 
examples in this repository:

- [QTBUG-110119](https://bugreports.qt.io/browse/QTBUG-110119): Cannot move 
  window on Ubuntu Wayland.
  - Moving the top window on (Ubuntu) Wayland with widget functions `move()` and 
  `setGeometry()` are not supported by Qt / PySide6.
  - Window move works on X11 and Windows 10.
  - Other desktop GUI's such as TKinter are able to move the top window on 
    Wayland.
  - [QTBUG-86780](https://bugreports.qt.io/browse/QTBUG-86780): Documentation
    update requested.
- [QTBUG-110290](https://bugreports.qt.io/browse/QTBUG-110290): QWidget 
  `showNormal()` not working when window is minimized on Ubuntu X11 and Wayland.
- [QTBUG-110448](https://bugreports.qt.io/browse/QTBUG-110448): Cannot remove 
  window min/max buttons on Ubuntu Wayland.
- [QTCREATORBUG-25807](https://bugreports.qt.io/browse/QTCREATORBUG-25807):
  PySide6 generated class doesn't load UI file correctly with QtCreator.
- Example `13_qt_creator\01_qt_creator_qwidget.py` generates a warning:
  `Attribute Qt::AA_ShareOpenGLContexts must be set before QCoreApplication is created.`
  Unclear how to resolve this.
- Be aware that a large number of official
  [PySide6](https://doc.qt.io/qtforpython/) examples are currently outdated or 
  API documentation is incomplete or inconsistent.
