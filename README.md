# Qt PySide6 Getting Started

This repository contains simple examples to start with Qt PySide6 for educational purposes.
Examples are tested with v6.4.2.

- [Getting Started Sources](https://github.com/Erriez/pyside6-getting-started)

## PySide6 Documentation

- [Qt for Python](https://doc.qt.io/qtforpython/)

## Installation

```bash
# Create a Python virtual environment
$ virtualenv venv

# Activate virtual environment
$ . venv/bin/activate

# Install dependencies
$ pip install -r requirements.txt
```

## Run a Getting Started Example

```bash
# Activate virtual environment
$ . venv/bin/activate

# Run an example
$ python 01_gettings_started/01_simple_example.py
```

## Known issues

- Moving the top window on Wayland with widget functions `move()` and 
 `setGeometry()` is supported by Qt / PySide6.
