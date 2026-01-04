## 🐞 Debug with Visual Studio Code

- `[Debug with free VSCode]` (On Windows and Linux desktops)

---

# Developing PySide6 with Visual Studio Code

- Download and install **Visual Studio Code**:  
  [https://code.visualstudio.com/](https://code.visualstudio.com/)

- Install the following VSCode extensions:
  - **Python** (Microsoft)
  - **Pylance** (Microsoft)
  - **Qt for Python** (optional, for syntax highlighting)
  - **Debugger for Python** (bundled with Python extension)

---

### 1. Open the project in VSCode

- Start VSCode and select **File -> Open Folder...**
- Open the `pyside6-getting-started` folder.

*(screenshot placeholder)*  
`![VSCode open](screenshots/VSCode01.png)`

---

### 2. Create or select a Python virtual environment

When opening a Python file, VSCode will prompt you to select a Python interpreter.

- Click **Select Python Interpreter** in the status bar
  or open the command palette (**Ctrl+Shift+P**) and run:

```
Python: Select Interpreter
```

*(screenshot placeholder)*  
`![VSCode interpreter](screenshots/VSCode02.png)`

Choose one of:

- An existing virtual environment  
- Or create a new one:

```
python -m venv .venv
```

VSCode will automatically activate it.

---

### 3. Install PySide6 inside the environment

Open a terminal inside VSCode:

```
pip install PySide6
```

Wait until installation completes.

---

### 4. Configure debugging

VSCode automatically detects Python scripts, but you can create a debug configuration:

- Open **Run and Debug** (Ctrl+Shift+D)
- Click **Create a launch.json file**
- Choose **Python: Current File**

This generates:

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Current File",
            "type": "python",
            "request": "launch",
            "program": "${file}",
            "console": "integratedTerminal"
        }
    ]
}
```

*(screenshot placeholder)*  
`![VSCode debug config](screenshots/VSCode03.png)`

---

### 5. Set breakpoints and start debugging

- Open any `.py` file from the **Explorer** panel
- Click in the left margin to set a breakpoint
- Press **F5** or click the green **Run** icon

*(screenshot placeholder)*  
`![VSCode debug](screenshots/VSCode04.png)`

---

### 6. Step through the code

Use the standard VSCode debug keys:

- **F10** – Step over  
- **F11** – Step into  
- **Shift+F11** – Step out  
- **F5** – Continue  

*(screenshot placeholder)*  
`![VSCode stepping](screenshots/VSCode05.png)`
