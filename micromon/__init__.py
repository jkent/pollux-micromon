from os import path
import shutil
import subprocess
import sys

MICROMON_ROOT = path.normpath(path.join(path.dirname(path.abspath(__file__)), '..'))
DEFAULT_CONFIG_PATH = path.normpath(path.join(MICROMON_ROOT, 'micromon.default.cfg'))
CONFIG_PATH = path.normpath(path.join(MICROMON_ROOT, 'micromon.cfg'))
MICROMON_BIN = path.normpath(path.join(MICROMON_ROOT, 'build', 'micromon.bin'))

# need to iterate over path and see if we're in there currently
sys.path.append(MICROMON_ROOT)

if not path.exists(MICROMON_BIN):
    result = subprocess.check_call('make', cwd=MICROMON_ROOT)
    if result:
        sys.exit(result)

if not path.exists(CONFIG_PATH):
    shutil.copyfile(DEFAULT_CONFIG_PATH, CONFIG_PATH)

from .core import Core
from .target import Target
__all__ = ['Target', 'Core']

