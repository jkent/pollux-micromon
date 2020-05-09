#
#  Copyright (C) 2011-2020 Jeff Kent <jeff@jkent.net>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License version 2 as
#  published by the Free Software Foundation.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#

import os
from os import path
import shutil
import subprocess
import sys

MICROMON_ROOT = path.normpath(path.join(path.dirname(path.abspath(__file__)), '..'))
DEFAULT_CONFIG_PATH = path.normpath(path.join(MICROMON_ROOT, 'micromon.default.cfg'))
CONFIG_PATH = path.normpath(path.join(MICROMON_ROOT, 'micromon.cfg'))
LOCAL_CONFIG_PATH = path.normpath(path.join(os.getcwd(), 'micromon.cfg'))
MICROMON_BIN = path.normpath(path.join(MICROMON_ROOT, 'build', 'micromon.bin'))

# need to iterate over path and see if we're in there currently
sys.path.append(MICROMON_ROOT)

if not path.exists(MICROMON_BIN):
    result = subprocess.check_call('make', cwd=MICROMON_ROOT)
    if result:
        sys.exit(result)

if path.exists(LOCAL_CONFIG_PATH):
    CONFIG_PATH = LOCAL_CONFIG_PATH

if not path.exists(CONFIG_PATH):
    shutil.copyfile(DEFAULT_CONFIG_PATH, CONFIG_PATH)

from .core import Core
from .target import Target
__all__ = ['Target', 'Core']

