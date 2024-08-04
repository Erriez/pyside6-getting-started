#!/usr/bin/bash -e

APP_EXE=pyside6_deployment_example
APP_LICENSE=LICENSE
APP_UNINSTALL=uninstall.sh
APP_ICO=pyside6_deployment_example.png
APP_SHORTCUT=${APP_EXE}.desktop
APP_DEVELOPER=erriez

EXE_PATH=$HOME/.local/bin/${APP_DEVELOPER}/${APP_EXE}
ICON_PATH=$HOME/.local/share/icons
SHORTCUT_PATH=$HOME/.local/share/applications

DST_EXE_FILE=${EXE_PATH}/${APP_EXE}
DST_LICENSE_FILE=${EXE_PATH}/${APP_LICENSE}
DST_UNINSTALL_FILE=${EXE_PATH}/${APP_UNINSTALL}
DST_ICON_FILE=${ICON_PATH}/${APP_ICO}
DST_SHORTCUT_FILE=${SHORTCUT_PATH}/${APP_SHORTCUT}

# Start installation
echo "Installing ${APP_EXE}..."

# Create directories
mkdir -p "${EXE_PATH}"
mkdir -p "${ICON_PATH}"
mkdir -p "${SHORTCUT_PATH}"

# Copy files
cp "${APP_EXE}" "${DST_EXE_FILE}"
cp "${APP_LICENSE}" "${DST_LICENSE_FILE}"
cp "${APP_UNINSTALL}" "${DST_UNINSTALL_FILE}"
cp "${APP_ICO}" "${DST_ICON_FILE}"
cp "${APP_SHORTCUT}" "${DST_SHORTCUT_FILE}"

# Make executable
chmod +x "${DST_EXE_FILE}"
chmod +x "${DST_UNINSTALL_FILE}"
chmod +x "${DST_SHORTCUT_FILE}"

# Replace Icon= and Exec= with absolute path in .desktop shortcut
sed -i "s|Icon=|Icon=${DST_ICON_FILE}|g" "${DST_SHORTCUT_FILE}"
sed -i "s|Exec=|Exec=${DST_EXE_FILE} %f|g" "${DST_SHORTCUT_FILE}"

echo "Application installed in: ${EXE_PATH}"
echo "Run uninstall.sh in the install directory to uninstall."
echo "Installation completed"
