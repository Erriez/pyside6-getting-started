#
# MIT License
#
# Copyright (c) 2023-2024 Erriez
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
# Source: https://github.com/Erriez/pyside6-getting-started
#

from PySide6.QtCore import qVersion
from packaging import version
import sys

# Minimum tested version
PYSIDE_MINIMUM_VERSION = '6.4.2'


def main():
    # Get minimum PySide version
    pyside_version = version.parse(str(qVersion()))

    # Compare PySide version with minimum version
    if pyside_version < version.parse(PYSIDE_MINIMUM_VERSION):
        print('WARNING: PySide v{} not tested!'.format(pyside_version.base_version))
        print('Minimum tested version: v{}'.format(PYSIDE_MINIMUM_VERSION))
        sys.exit(2)

    # Print PySide version
    print('PySide{}: v{}'.format(pyside_version.major, pyside_version.base_version))


if __name__ == '__main__':
    main()
