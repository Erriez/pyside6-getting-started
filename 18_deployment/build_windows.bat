virtualenv venv
call .\venv\Scripts\activate.bat
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m nuitka --onefile --plugin-enable=pyside6 --include-data-dir=./data/=data --windows-console-mode=disable --windows-icon-from-ico=data/app.png 01_deployment.py
"C:\Program Files (x86)\NSIS\makensis.exe" windows_installer.nsi