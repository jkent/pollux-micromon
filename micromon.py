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

from cmd import Cmd
import sys
from time import sleep
from micromon import *
from micromon.registers import REGS, Registers

def print_value(value, bits):
    value_bin = bin(value)[2:].zfill(bits)
    value_bin = ' '.join((value_bin[i:i+4] for i in range(0, bits, 4))).rjust(39)
    value_hex = ('0x%0.*X' % (bits // 4, value)).rjust(10)
    print('%s      %s' % (value_hex, value_bin.rjust(14 - len(value_bin))))

class CommandParser(Cmd):
    def __init__(self):
        Cmd.__init__(self)
        self.prompt = '> '
        self.target = None
    
    def preloop(self):
        self.target = Target()
        self.loader = Loader(self.target)
        self.core = Core(self.target)
        self.regs = Registers(self.core)
        self.do_power('on')

    def emptyline(self):
        pass

    def read(self, s, bits):
        l = s.split()
        if len(l) != 1:
            print('*** Invalid number of arguments')
            return

        upper = (1 << 32) - 1
        try:
            addr = int(l[0], 0)
        except:
            try:
                r = Registers.lookup(l[0])
                if r['bits'] != bits:
                    regbits = r['bits']
                    print(f'Note: Register is {regbits} bits')
                addr = r['addr']
            except:
                print('*** Register is unknown')
                return

        if addr < 0 or addr > upper:
            print(f'*** Address must be an integer in the range of 0 to {upper}')
            return

        if bits == 8:
            value = self.core.read_u8(addr)
        elif bits == 16:
            value = self.core.read_u16(addr)
        elif bits == 32:
            value = self.core.read_u32(addr)
        else:
            print('*** Invalid number of bits')
            return

        if value is None:    
            print('*** Error reading')
            return

        print_value(value, bits)

    def write(self, s, bits):
        l = s.split()
        if len(l) != 2:
            print('*** Invalid number of arguments')
            return
        
        upper = (1 << 32) - 1
        try:
            addr = int(l[0], 0)
        except:
            try:
                r = Registers.lookup(l[0])
                if r['bits'] != bits:
                    regbits = r['bits']
                    print(f'Note: Register is {regbits} bits')
                addr = r['addr']
            except:
                print('*** Register is unknown')
                return

        if addr < 0 or addr > upper:
            print(f'*** Address must be an integer in the range of 0 to {upper}')
            return
        
        upper = (1 << bits) - 1
        try:
            value = int(l[1], 0)
            assert value >= 0 and value <= upper
        except:
            print(f'*** Value must be an integer in the range of 0 to {upper}')
            return

        if bits == 8:
            self.core.write_u8(addr, value)
        elif bits == 16:
            self.core.write_u16(addr, value)
        elif bits == 32:
            self.core.write_u32(addr, value)
        else:
            print('*** Invalid number of bits')
            return

    def do_readb(self, s):
        """readb address

        Read a u8 value from memory.
        """
        self.read(s, 8)

    def do_readw(self, s):
        """readw address

        Read a u16 value from memory.
        """
        self.read(s, 16)

    def do_readl(self, s):
        """readl address

        Read a u32 value from memory.
        """
        self.read(s, 32)

    def do_writeb(self, s):
        """writeb address value

        Write a u8 value to memory.
        """
        self.write(self, s, 8)

    def do_writew(self, s):
        """writew address value

        Write a u16 value to memory.
        """
        self.write(self, s, 16)

    def do_writel(self, s):
        """writel address value

        Write a u32 value to memory.
        """
        self.write(self, s, 32)

    def do_reglist(self, s):
        """reglist [[group]]

        List registers grouped by function.
        """
        group = None
        l = s.split()
        if len(l) == 1:
            group = l[0].upper()
        elif len(l) > 2:
            print('*** Invalid number of arugments')
            return

        groups = []
        regs = {}

        for r in REGS:
            r_group = r['group'].upper()
            if r_group.upper() not in groups:
                groups.append(r_group)
                regs[r_group] = []
            regs[r_group].append(r)

        if group is None:
            print('')
            self.print_topics('Register groups', groups, 15, 80)
        else:
            if group in groups:
                print('')
                for r in regs[group]:
                    print(('0x%08X      %-24s' % (r['addr'], r['name'])))
                print('')
            else:
                print('*** Unknown register group')
                return

    # TODO:
    #def do_reginfo(self, s):
    #    """reginfo [regname]
    #
    #    Provide detailed information on a register.
    #    """

    def do_memtoggle(self, s):
        """memtoggle [addr] [bits] [mask]"""
        l = s.split()
        if len(l) != 3:
            print('*** Invalid number of arguments')
            return

        addr = None
        bits = None
        value = None
        try:
            addr = int(l[0],16)
            bits = int(l[1])
            mask = int(l[2],16)
            assert bits in [8, 16, 32]
        except:
            print('*** Bad values')
            return

        if bits == 8:
            read = lambda addr: self.core.read_u8(addr)
            write = lambda addr, value: self.core.write_u8(addr, value)
        elif bits == 16:
            read = lambda addr: self.core.read_u16(addr)
            write = lambda addr, value: self.core.write_u16(addr, value)
        elif bits == 32:
            read = lambda addr: self.core.read_u32(addr)
            write = lambda addr, value: self.core.write_u32(addr, value)

        orig = read(addr)
        value = orig

        print('Press any key to stop...')
        while not getkey():
            value ^= mask
            write(addr, value)
            sleep(0.05)

        write(addr, orig)

    def do_adc(self, s):
        """adc [channel]"""

        l = s.split()
        if len(l) != 1:
            print('*** Invalid number of arguments')
            return

        try:
            channel = int(l[0])
            assert channel in range(0,8)
        except:
            print('*** Invalid channel')
            return

        def init():
            self.regs.write('ADCCLKENB', 1 << 3)
            self.regs.write('ADCCON', 0)
            adccon = 126 << 6
            self.regs.write('ADCCON', adccon)
            adccon |= 1 << 14
            self.regs.write('ADCCON', adccon)

        def read(channel):
            adccon = self.regs.read('ADCCON') & ~(0x7 << 3)
            adccon |= (1 << 0) | (channel << 3)
            self.regs.write('ADCCON', adccon)

            while (self.regs.read('ADCCON') & 0x1):
                pass

            value = self.regs.read('ADCDAT') & 0x3FF
            return value

        def shutdown():
            self.regs.write('ADCCON', 0)
            self.regs.write('ADCCLKENB', 0)

        init()
        value = read(channel)
        print(value)
        shutdown()

    def do_power(self, s):
        """power [on|off]

        Changes the ALIVEGPIO VDDPWRON bit.
        """
        if s.lower() in ['1', 'on']:
            self.regs.write('ALIVEPWRGATEREG', 1)
            self.regs.write('ALIVEGPIORSTREG', 0)
            self.regs.write('ALIVEGPIOSETREG', 0x80)
            self.regs.write('ALIVEGPIOSETREG', 0)
            self.regs.write('ALIVEPWRGATEREG', 0)
        elif s.lower() in ['0', 'off']:
            self.regs.write('ALIVEPWRGATEREG', 1)
            self.regs.write('ALIVEGPIOSETREG', 0)
            self.regs.write('ALIVEGPIORSTREG', 0x80)
            self.regs.write('ALIVEGPIORSTREG', 0)
            self.regs.write('ALIVEPWRGATEREG', 0)
            return True
        else:
            print((self.do_power.__doc__))

    def do_EOF(self, s):
        """EOF

        Powers off target and exits.
        """
        self.do_power('off')
        print()
        return True

    def do_quit(self, s):
        """quit

        Exit the program.
        """
        return True
    do_q = do_quit
    
if __name__ == '__main__':
    print('\nMicromon Shell 1.0\n')

    cp = CommandParser()
    cp.cmdloop('Type \'help\' for assistance.')
