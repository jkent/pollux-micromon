#!/usr/bin/env python3
#
#  Copyright (C) 2013-2020 Jeff Kent <jeff@jkent.net>
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

import sys
from micromon import *

# TODO: Integrate into the Micromon shell

def main():
    filename = sys.argv[1]

    load_address = 0x000000
    if len(sys.argv) > 2:
        load_address = int(sys.argv[2], 0)

    exec_address = load_address
    if len(sys.argv) > 3:
        exec_address = int(sys.argv[3], 0)

    target = Target()
    loader = Loader(target)
    core = Core(target)

    fp = open(filename, 'rb')
    data = fp.read()
    fp.close()

    assert core.mem_write(load_address, data)
    core.run(exec_address)

if __name__ == '__main__':
    main()
