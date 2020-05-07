# vim: set ts=4 sw=4 expandtab
#
#  Copyright (C) 2011-2020 Jeff Kent <jakent@gmail.com>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
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

import micromon
from .config import Config
from .log import Log
import sys
import os
from binascii import crc32
from time import sleep

_loader_signature    = b'UART'

class Loader:
    def __init__(self, target):
        self._target = target

        powerup_delay = Config.get('target.powerup_delay')

        try:
            core = self._read_core()
            while True:
                self._target.set_baudrate(19200)

                self._target.set_uart_boot(True)
                if self._target.get_power_state():
                    self._target.reset()
                else:
                    print('Please power on the target')
                    while not self._target.get_power_state():
                        sleep(0.1)
                    self._target.purge_input()
                    sleep(powerup_delay)
                self._target.set_uart_boot(False)

                if self._init_core(core):
                    break
        except Exception as inst:
            Log.fatal(str(inst)).single()
            sys.exit(1)

    def _read_core(self):
        fp = open(micromon.CORE_BIN, 'rb')
        fp.seek(0, os.SEEK_END)
        size = fp.tell()
        fp.seek(0, os.SEEK_SET)

        core = fp.read(size)
        return core

    def _init_core(self, core):
        uart_boot_size = Config.get('monitor.uart_boot_size')

        if uart_boot_size in ['detect', '512']:
            if not self._write(core[:512]):
                return False
            if self._loader_signature():
                if not self._loader_512(core):
                    return False
            elif uart_boot_size == 'detect':
                if not self._write(core[512:16384]):
                    return False
                if self._loader_signature():
                    self._loader_16k()
                else:
                    raise Exception('Detect boot failed')
            else:
                raise Exception('512 boot failed')

        elif uart_boot_size == '16k':
            if not self._write(core[:16384]):
                return False
            if self._loader_signature():
                self._loader_16k()
            else:
                raise Exception('16k boot failed')

        return True

    def _loader_signature(self):
        response = self._target.read(4)
        if not response:
            return False

        if response == _loader_signature:
            return True
        else:
            raise Exception('Communication error occured')

    def _loader_512(self, core):
        self._set_baudrate()
        if not self._load_rest(core[512:]):
            return False
        return True

    def _loader_16k(self):
        self._set_baudrate()
        if not self._load_rest(16384, core[16384:]):
            return False
        return True

    def _set_baudrate(self):
        baudrate = Config.get('monitor.baudrate')
        baudrates = {
            19200: (11 << 16) | (39 << 4) | (1 << 1),
            38400: (5 << 16) | (39 << 4) | (1 << 1),
            57600: (3 << 16) | (39 << 4) | (1 << 1),
            115200: (1 << 16) | (39 << 4) | (1 << 1),
            230400: (7 << 16) | (4 << 4) | (1 << 1),
            460800: (3 << 16) | (4 << 4) | (1 << 1),
            614400: (2 << 16) | (4 << 4) | (1 << 1),
            921600: (1 << 16) | (4 << 4) | (1 << 1),
            1500000: (0 << 16) | (15 << 4) | (0 << 1),
        }
        baudinfo = baudrates[baudrate]

        with Log.debug('Setting target baudrate to %(baudrate)d',
                       baudrate=baudrate):
            self._target.write_u32(baudinfo)
            response = self._target.read_u8()
            if response:
                self._target.set_baudrate(baudrate)
            else:
                raise Exception('Changing baudrate failed')

            self._target.write_u16(0xAA55)
            response = self._target.read_u8()
            if not response:
                raise Exception('Changing baudrate failed')

    def _load_rest(self, data):
        self._target.write_u32(len(data))
        if not self._write(data):
            return False

        return True

    def _write(self, data):
        size = len(data)
        blocksize = 512
        blocks = (size + blocksize-1) / blocksize
        block = 0

        log_entry = Log.info('Sending block %(block)d of %(blocks)d block(s)',
                             block=block + 1, blocks=blocks)
        with log_entry:
            while block + 1 < blocks:
                log_entry.update(block=block + 1)
                if not self._target.get_power_state():
                    with Log.warning('Power lost'):
                        return False
                offset = block * blocksize
                self._target.write(data[offset:offset+blocksize])
                block += 1

        return True

