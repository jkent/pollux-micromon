# vim: set ts=4 sw=4 expandtab
#
#  Copyright (C) 2011-2020 Jeff Kent <jeff@jkent.net>
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

from .config import Config
from .log import Log
from serial import Serial
from time import sleep
from struct import Struct
import sys

u8 = Struct('<B')
u16 = Struct('<H')
u32 = Struct('<L')

class Target:
    """abstraction for direct serial communication to the target"""
    def __init__(self):
        serial_port = Config.get('target.serial_port')
        data_timeout = Config.get('target.data_timeout')

        with Log.debug('Opening serial port'):
            try:
                self.sp = Serial(serial_port, 19200, timeout=data_timeout)
            except:
                Log.fatal('Unable to open %(port)s', port=serial_port).single()
                sys.exit(1)
            self.sp.flushOutput()
            self.sp.flushInput()

    def _set_pin(self, pin, state):
        if pin == 'rts':
            self.sp.rts = state
        elif pin == '!rts':
            self.sp.rts = not state
        elif pin == 'dtr':
            self.sp.dtr = state
        elif pin == '!dtr':
            self.sp.dtr = not state

    def _get_pin(self, pin):
        if pin == 'cts':
            return self.sp.cts
        elif pin == '!cts':
            return not self.sp.cts
        elif pin == 'dsr':
            return self.sp.dsr
        elif pin == '!dsr':
            return not self.sp.dsr
        elif pin == 'cd':
            return self.sp.cd
        elif pin == '!cd':
            return not self.sp.cd
        elif pin == 'ri':
            return self.sp.ri
        elif pin == '!ri':
            return not self.sp.ri

    def set_baudrate(self, baudrate):
        with Log.debug('Setting local baudrate to %(baudrate)s',
                       baudrate=baudrate):
            self.sp.flushOutput()
            self.sp.flushInput()
            self.sp.baudrate = baudrate

    def purge_input(self):
        self.sp.flushInput()

    def reset(self):
        reset_pin = Config.get('target.reset_pin')
        reset_delay = Config.get('target.reset_delay')

        if reset_pin != 'none':
            with Log.info('Resetting target'):
                self._set_pin(reset_pin, True)
                self._set_pin(reset_pin, False)
                sleep(reset_delay)

    def set_uart_boot(self, state):
        uart_boot_pin = Config.get('target.uart_boot_pin')

        if uart_boot_pin != 'none':
            with Log.debug('Setting uart boot state to %(state)s',
                           state=str(bool(state))):
                self._set_pin(uart_boot_pin, state)

    def get_power_state(self):
        power_detect_pin = Config.get('target.power_detect_pin')

        if power_detect_pin != 'none':
            return self._get_pin(power_detect_pin)
        else:
            return True

    def write(self, data):
        self.sp.write(data)
        self.sp.flush()

    def read(self, bytes):
        data = self.sp.read(bytes)
        return data

    def _write_struct(self, data, t):
        data = t.pack(data)
        self.sp.write(data)

    def _read_struct(self, t):
        data = self.sp.read(t.size)
        if not data or len(data) != t.size:
            return None
        return t.unpack(data)[0]

    def write_u8(self, n):
        self._write_struct(n, u8)

    def write_u16(self, n):
        self._write_struct(n, u16)

    def write_u32(self, n):
        self._write_struct(n, u32)

    def read_u8(self):
        return self._read_struct(u8)

    def read_u16(self):
        return self._read_struct(u16)

    def read_u32(self):
        return self._read_struct(u32)
