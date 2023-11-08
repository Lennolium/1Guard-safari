#!/usr/bin/env python3

"""
const.py: TODO: Headline...

TODO: Description...
"""

# Header.
__author__ = "Lennart Haack"
__email__ = "lennart-haack@mail.de"
__license__ = "GNU GPLv3"
__version__ = "0.0.1"
__date__ = "2023-11-07"
__status__ = "Prototype/Development/Production"

# Imports.
import os
import platform

# Constants.
CURRENT_PLATFORM = platform.uname()[0].upper()  # 'DARWIN' / 'LINUX' ...
APP_PATH = os.path.dirname(os.path.abspath(os.path.realpath(__file__)))
CONFIG_FILE = f"{APP_PATH}/logs/server.ini"
LOG_FILE = f"{APP_PATH}/logs/server.log"

# Database.