#!/usr/bin/env python3
#
#  Copyright (C) 2020 Jeff Kent <jeff@jkent.net>
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

def main():
    file = sys.argv[1]

    baud = 115200
    if len(sys.argv) > 2:
        baud = int(sys.argv[2])

    target = Target()
    loader = Loader(target, file)

    if target.read_u8() != 0x5A:
        raise Exception('Invalid handshake')
    target.write_u8(0xA5)

    target.set_baudrate(baud)

if __name__ == '__main__':
    main()
