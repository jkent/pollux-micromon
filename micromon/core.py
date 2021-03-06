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

from binascii import crc32
from .loader import Loader
from .log import Log
from time import sleep

COMMANDS = (
  'nop',
  'write_u8',
  'write_u16',
  'write_u32',
  'read_u8',
  'read_u16',
  'read_u32',
  'mem_write',
  'mem_read',
  'run',
  'run_kernel'
)

class Core:
    """python interface to the core, the base code running on the target"""
    def __init__(self, target):
        self._target = target

        if self._target.read_u32() != 0x4e4f4d75:
            raise Exception('Micromon signature invalid/missing')
        sleep(0.1)

    def write_u8(self, addr, data):
        self._target.write_u8(COMMANDS.index('write_u8'))
        self._target.write_u32(addr)
        self._target.write_u8(data)

    def write_u16(self, addr, data):
        self._target.write_u8(COMMANDS.index('write_u16'))
        self._target.write_u32(addr)
        self._target.write_u16(data)

    def write_u32(self, addr, data):
        self._target.write_u8(COMMANDS.index('write_u32'))
        self._target.write_u32(addr)
        self._target.write_u32(data)

    def read_u8(self, addr):
        self._target.write_u8(COMMANDS.index('read_u8'))
        self._target.write_u32(addr)
        return self._target.read_u8()

    def read_u16(self, addr):
        self._target.write_u8(COMMANDS.index('read_u16'))
        self._target.write_u32(addr)
        return self._target.read_u16()

    def read_u32(self, addr):
        self._target.write_u8(COMMANDS.index('read_u32'))
        self._target.write_u32(addr)
        return self._target.read_u32()

    def mem_write(self, addr, data):
        self._target.write_u8(COMMANDS.index('mem_write'))
        self._target.write_u32(addr)
        self._target.write_u32(len(data))
        self._write(data)
        remote_crc32 = self._target.read_u32()
        local_crc32 = crc32(data) & 0xFFFFFFFF
        crc_ok = (remote_crc32 == local_crc32)
        return crc_ok

    def mem_read(self, addr, size):
        self._target.write_u8(COMMANDS.index('mem_read'))
        self._target.write_u32(addr)
        self._target.write_u32(size)
        data = self._read(size)
        remote_crc32 = self._target.read_u32()
        local_crc32 = crc32(data) & 0xFFFFFFFF
        crc_ok = (remote_crc32 == local_crc32)
        return (data, crc_ok)

    def run(self, exec_at):
        self._target.write_u8(COMMANDS.index('run'))
        self._target.write_u32(exec_at)

    def run_kernel(self, exec_at, machine_type):
        self._target.write_u8(COMMANDS.index('run_kernel'))
        self._target.write_u32(exec_at)
        self._target.write_u32(machine_type)

    def _write(self, data):
        size = len(data)
        blocksize = 512
        blocks = (size + blocksize - 1) / blocksize
        block = 0

        log_entry = Log.info('Sending block %(block)d of %(blocks)d block(s)',
                             block=block, blocks=blocks)
        with log_entry:
            while block + 1 < blocks:
                log_entry.update(block=block + 1)
                offset = block * blocksize
                self._target.write(data[offset:offset+blocksize])
                block += 1

    def _read(self, size):
        data = ''
        blocksize = 512
        blocks = (size + blocksize - 1) / blocksize
        block = 0

        log_entry = Log.info('Receiving block %(block)d of %(blocks)d block(s)',
                             block=block, blocks=blocks)
        with log_entry:
            while block + 1 < blocks:
                log_entry.update(block=block + 1)
                offset = block * blocksize
                data_block = self._target.read(blocksize)
                if not data_block:
                    return None
                data += data_block
                block += 1

