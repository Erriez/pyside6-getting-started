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

## PySide6 Documentation

- [Qt for Python](https://doc.qt.io/qtforpython/)
- [PySide6 Python module](https://pypi.org/project/PySide6/)
- [Qt Licensing](https://www.qt.io/licensing/)

## Installation Linux 

Run the following commands in a Linux terminal:

```bash
# Clone the sources (Make sure git is installed)
$ git clone https://github.com/Erriez/pyside6-getting-started.git

# Change directory to the sources
$ cd pyside6-getting-started

# Create a Python virtual environment
$ virtualenv venv

# Activate virtual environment (Prompt changes to venv)
$ . venv/bin/activate

# Install dependencies including PySide6
(venv) $ pip install -r requirements.txt
```

To run an example on Linux:

```bash
# Activate virtual environment
$ . venv/bin/activate

# Run an example
(venv) $ python 01_gettings_started/01_simple_example.py
```

## Installation Windows

* Download and install [Git](https://git-scm.com/download/win).
* Download and install [Python3](https://www.python.org/downloads/).  
  During installation, check: `Add Python to environment variables`. 
* Run the following commands in a Windows command prompt:  
  (`Winkey`+`R`, type: `cmd` followed by `Enter`)
  

```bat
# Clone the sources (Make sure git is installed)
> git clone https://github.com/Erriez/pyside6-getting-started.git

# Change directory to the sources
> cd pyside6-getting-started

# Install virtualenv (Make sure pip and Python are in the path)
> pip install virtualenv

# Create a Python virtual environment
> virtualenv venv

# Activate virtual environment (Prompt changes to venv)
> venv\Scripts\activate.bat

# Install dependencies including PySide6
(venv) > pip install -r requirements.txt
```

To run an example on Windows:

```bash
# Activate virtual environment
> venv\Scripts\activate.bat

# Run an example
(venv) > python 01_gettings_started\01_simple_example.py
```

## Versions and Platforms

Examples are tested with PySide v6.4.2 on Ubuntu 22.10 Wayland and Windows 10.
As Qt is platform independent, it may work on other systems like Raspberry Pi.
See section [Known issues](https://github.com/Erriez/pyside6-getting-started#known-issues) 
for platform specific issues.

**Note:** Developer [Erriez](https://github.com/Erriez/) does not support MAC.

## Known issues

- **Linux**: Moving the top window on (Ubuntu) Wayland with widget functions
  `move()` and `setGeometry()` are not supported by Qt / PySide6. This works on
  X11.
