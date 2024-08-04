#!/usr/bin/bash -e

SCRIPT_PATH=$(dirname -- "${BASH_SOURCE[0]}")
OUTPUT_FILENAME=pyside6_deployment_example

virtualenv venv
. venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m nuitka --onefile --plugin-enable=pyside6 --include-data-dir=./data/=data --windows-console-mode=disable --windows-icon-from-ico=data/app.png --output-filename=${OUTPUT_FILENAME} 01_deployment.py

INSTALLER_DIR=${SCRIPT_PATH}/linux_installer
LICENSE_FILE=${INSTALLER_DIR}/LICENSE
OUTPUT_FILE="pyside6_deployment_example.deb"
LABEL="Erriez PySide6 Deployment Example"

cp "${OUTPUT_FILENAME}" "${INSTALLER_DIR}/${OUTPUT_FILENAME}"

echo "Creating Linux installer"
makeself --sha256 --license "${LICENSE_FILE}" "${INSTALLER_DIR}" "${OUTPUT_FILE}" "${LABEL}" ./install.sh

echo "Created installer:"
./"${OUTPUT_FILE}" --check
./"${OUTPUT_FILE}" --info
./"${OUTPUT_FILE}" --list

