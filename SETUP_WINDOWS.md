# Installation Windows

* Download and install [Git](https://git-scm.com/download/win).
* Download and install [Python3](https://www.python.org/downloads/).  
  During installation, check: `Add Python to environment variables`. 
* Run the following commands in a Windows command prompt:  
  (`Winkey`+`R`, type: `cmd` followed by `Enter`)
  

```
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

```
# Activate virtual environment
> venv\Scripts\activate.bat

# Run an example
(venv) > python 01_gettings_started\01_simple_example.py
```
