# Installation Linux 

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
