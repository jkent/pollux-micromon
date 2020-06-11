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

REGS = (
    {'addr': 0xC0000000, 'name': 'DMA0SRCADDR', 'bits': 32, 'group': 'DMA'},
    {'addr': 0xC0000004, 'name': 'DMA0DSTADDR', 'bits': 32, 'group': 'DMA'},
    {'addr': 0xC0000008, 'name': 'DMA0LENGTH', 'bits': 16, 'group': 'DMA'},
    {'addr': 0xC000000A, 'name': 'DMA0REQID', 'bits': 16, 'group': 'DMA'},
    {'addr': 0xC000000C, 'name': 'DMA0MODE', 'bits': 16, 'group': 'DMA'},
    {'addr': 0xC0000010, 'name': 'DMA0BUFSRCADDR', 'bits': 32, 'group': 'DMA'},
    {'addr': 0xC0000014, 'name': 'DMA0BUFDSTADDR', 'bits': 32, 'group': 'DMA'},
    {'addr': 0xC0000018, 'name': 'DMA0BUFLENGTH', 'bits': 16, 'group': 'DMA'},
    {'addr': 0xC000001A, 'name': 'DMA0BUFREQID', 'bits': 16, 'group': 'DMA'},
    {'addr': 0xC000001C, 'name': 'DMA0BUFMODE', 'bits': 16, 'group': 'DMA'},
    {'addr': 0xC0000020, 'name': 'DMA0CMDWAIT', 'bits': 32, 'group': 'DMA'},
    {'addr': 0xC0000024, 'name': 'DMA0CMDSTOP', 'bits': 32, 'group': 'DMA'},
    {'addr': 0xC0000028, 'name': 'DMA0CMDBUSY', 'bits': 32, 'group': 'DMA'},
    {'addr': 0xC000002C, 'name': 'DMA0CMDSPACE', 'bits': 32, 'group': 'DMA'},

    {'addr': 0xC0000080, 'name': 'DMA1SRCADDR', 'bits': 32, 'group': 'DMA'},
    {'addr': 0xC0000084, 'name': 'DMA1DSTADDR', 'bits': 32, 'group': 'DMA'},
    {'addr': 0xC0000088, 'name': 'DMA1LENGTH', 'bits': 16, 'group': 'DMA'},
    {'addr': 0xC000008A, 'name': 'DMA1REQID', 'bits': 16, 'group': 'DMA'},
    {'addr': 0xC000008C, 'name': 'DMA1MODE', 'bits': 16, 'group': 'DMA'},
    {'addr': 0xC0000090, 'name': 'DMA1BUFSRCADDR', 'bits': 32, 'group': 'DMA'},
    {'addr': 0xC0000094, 'name': 'DMA1BUFDSTADDR', 'bits': 32, 'group': 'DMA'},
    {'addr': 0xC0000098, 'name': 'DMA1BUFLENGTH', 'bits': 16, 'group': 'DMA'},
    {'addr': 0xC000009A, 'name': 'DMA1BUFREQID', 'bits': 16, 'group': 'DMA'},
    {'addr': 0xC000009C, 'name': 'DMA1BUFMODE', 'bits': 16, 'group': 'DMA'},
    {'addr': 0xC00000A0, 'name': 'DMA1CMDWAIT', 'bits': 32, 'group': 'DMA'},
    {'addr': 0xC00000A4, 'name': 'DMA1CMDSTOP', 'bits': 32, 'group': 'DMA'},
    {'addr': 0xC00000A8, 'name': 'DMA1CMDBUSY', 'bits': 32, 'group': 'DMA'},
    {'addr': 0xC00000AC, 'name': 'DMA1CMDSPACE', 'bits': 32, 'group': 'DMA'},

    {'addr': 0xC0000100, 'name': 'DMA2SRCADDR', 'bits': 32, 'group': 'DMA'},
    {'addr': 0xC0000104, 'name': 'DMA2DSTADDR', 'bits': 32, 'group': 'DMA'},
    {'addr': 0xC0000108, 'name': 'DMA2LENGTH', 'bits': 16, 'group': 'DMA'},
    {'addr': 0xC000010A, 'name': 'DMA2REQID', 'bits': 16, 'group': 'DMA'},
    {'addr': 0xC000010C, 'name': 'DMA2MODE', 'bits': 16, 'group': 'DMA'},
    {'addr': 0xC0000110, 'name': 'DMA2BUFSRCADDR', 'bits': 32, 'group': 'DMA'},
    {'addr': 0xC0000114, 'name': 'DMA2BUFDSTADDR', 'bits': 32, 'group': 'DMA'},
    {'addr': 0xC0000118, 'name': 'DMA2BUFLENGTH', 'bits': 16, 'group': 'DMA'},
    {'addr': 0xC000011A, 'name': 'DMA2BUFREQID', 'bits': 16, 'group': 'DMA'},
    {'addr': 0xC000011C, 'name': 'DMA2BUFMODE', 'bits': 16, 'group': 'DMA'},
    {'addr': 0xC0000120, 'name': 'DMA2CMDWAIT', 'bits': 32, 'group': 'DMA'},
    {'addr': 0xC0000124, 'name': 'DMA2CMDSTOP', 'bits': 32, 'group': 'DMA'},
    {'addr': 0xC0000128, 'name': 'DMA2CMDBUSY', 'bits': 32, 'group': 'DMA'},
    {'addr': 0xC000012C, 'name': 'DMA2CMDSPACE', 'bits': 32, 'group': 'DMA'},

    {'addr': 0xC0000180, 'name': 'DMA3SRCADDR', 'bits': 32, 'group': 'DMA'},
    {'addr': 0xC0000184, 'name': 'DMA3DSTADDR', 'bits': 32, 'group': 'DMA'},
    {'addr': 0xC0000188, 'name': 'DMA3LENGTH', 'bits': 16, 'group': 'DMA'},
    {'addr': 0xC000018A, 'name': 'DMA3REQID', 'bits': 16, 'group': 'DMA'},
    {'addr': 0xC000018C, 'name': 'DMA3MODE', 'bits': 16, 'group': 'DMA'},
    {'addr': 0xC0000190, 'name': 'DMA3BUFSRCADDR', 'bits': 32, 'group': 'DMA'},
    {'addr': 0xC0000194, 'name': 'DMA3BUFDSTADDR', 'bits': 32, 'group': 'DMA'},
    {'addr': 0xC0000198, 'name': 'DMA3BUFLENGTH', 'bits': 16, 'group': 'DMA'},
    {'addr': 0xC000019A, 'name': 'DMA3BUFREQID', 'bits': 16, 'group': 'DMA'},
    {'addr': 0xC000019C, 'name': 'DMA3BUFMODE', 'bits': 16, 'group': 'DMA'},
    {'addr': 0xC00001A0, 'name': 'DMA3CMDWAIT', 'bits': 32, 'group': 'DMA'},
    {'addr': 0xC00001A4, 'name': 'DMA3CMDSTOP', 'bits': 32, 'group': 'DMA'},
    {'addr': 0xC00001A8, 'name': 'DMA3CMDBUSY', 'bits': 32, 'group': 'DMA'},
    {'addr': 0xC00001AC, 'name': 'DMA3CMDSPACE', 'bits': 32, 'group': 'DMA'},

    {'addr': 0xC0000200, 'name': 'DMA4SRCADDR', 'bits': 32, 'group': 'DMA'},
    {'addr': 0xC0000204, 'name': 'DMA4DSTADDR', 'bits': 32, 'group': 'DMA'},
    {'addr': 0xC0000208, 'name': 'DMA4LENGTH', 'bits': 16, 'group': 'DMA'},
    {'addr': 0xC000020A, 'name': 'DMA4REQID', 'bits': 16, 'group': 'DMA'},
    {'addr': 0xC000020C, 'name': 'DMA4MODE', 'bits': 16, 'group': 'DMA'},
    {'addr': 0xC0000210, 'name': 'DMA4BUFSRCADDR', 'bits': 32, 'group': 'DMA'},
    {'addr': 0xC0000214, 'name': 'DMA4BUFDSTADDR', 'bits': 32, 'group': 'DMA'},
    {'addr': 0xC0000218, 'name': 'DMA4BUFLENGTH', 'bits': 16, 'group': 'DMA'},
    {'addr': 0xC000021A, 'name': 'DMA4BUFREQID', 'bits': 16, 'group': 'DMA'},
    {'addr': 0xC000021C, 'name': 'DMA4BUFMODE', 'bits': 16, 'group': 'DMA'},
    {'addr': 0xC0000220, 'name': 'DMA4CMDWAIT', 'bits': 32, 'group': 'DMA'},
    {'addr': 0xC0000224, 'name': 'DMA4CMDSTOP', 'bits': 32, 'group': 'DMA'},
    {'addr': 0xC0000228, 'name': 'DMA4CMDBUSY', 'bits': 32, 'group': 'DMA'},
    {'addr': 0xC000022C, 'name': 'DMA4CMDSPACE', 'bits': 32, 'group': 'DMA'},

    {'addr': 0xC0000280, 'name': 'DMA5SRCADDR', 'bits': 32, 'group': 'DMA'},
    {'addr': 0xC0000284, 'name': 'DMA5DSTADDR', 'bits': 32, 'group': 'DMA'},
    {'addr': 0xC0000288, 'name': 'DMA5LENGTH', 'bits': 16, 'group': 'DMA'},
    {'addr': 0xC000028A, 'name': 'DMA5REQID', 'bits': 16, 'group': 'DMA'},
    {'addr': 0xC000028C, 'name': 'DMA5MODE', 'bits': 16, 'group': 'DMA'},
    {'addr': 0xC0000290, 'name': 'DMA5BUFSRCADDR', 'bits': 32, 'group': 'DMA'},
    {'addr': 0xC0000294, 'name': 'DMA5BUFDSTADDR', 'bits': 32, 'group': 'DMA'},
    {'addr': 0xC0000298, 'name': 'DMA5BUFLENGTH', 'bits': 16, 'group': 'DMA'},
    {'addr': 0xC000029A, 'name': 'DMA5BUFREQID', 'bits': 16, 'group': 'DMA'},
    {'addr': 0xC000029C, 'name': 'DMA5BUFMODE', 'bits': 16, 'group': 'DMA'},
    {'addr': 0xC00002A0, 'name': 'DMA5CMDWAIT', 'bits': 32, 'group': 'DMA'},
    {'addr': 0xC00002A4, 'name': 'DMA5CMDSTOP', 'bits': 32, 'group': 'DMA'},
    {'addr': 0xC00002A8, 'name': 'DMA5CMDBUSY', 'bits': 32, 'group': 'DMA'},
    {'addr': 0xC00002AC, 'name': 'DMA5CMDSPACE', 'bits': 32, 'group': 'DMA'},

    {'addr': 0xC0000300, 'name': 'DMA6SRCADDR', 'bits': 32, 'group': 'DMA'},
    {'addr': 0xC0000304, 'name': 'DMA6DSTADDR', 'bits': 32, 'group': 'DMA'},
    {'addr': 0xC0000308, 'name': 'DMA6LENGTH', 'bits': 16, 'group': 'DMA'},
    {'addr': 0xC000030A, 'name': 'DMA6REQID', 'bits': 16, 'group': 'DMA'},
    {'addr': 0xC000030C, 'name': 'DMA6MODE', 'bits': 16, 'group': 'DMA'},
    {'addr': 0xC0000310, 'name': 'DMA6BUFSRCADDR', 'bits': 32, 'group': 'DMA'},
    {'addr': 0xC0000314, 'name': 'DMA6BUFDSTADDR', 'bits': 32, 'group': 'DMA'},
    {'addr': 0xC0000318, 'name': 'DMA6BUFLENGTH', 'bits': 16, 'group': 'DMA'},
    {'addr': 0xC000031A, 'name': 'DMA6BUFREQID', 'bits': 16, 'group': 'DMA'},
    {'addr': 0xC000031C, 'name': 'DMA6BUFMODE', 'bits': 16, 'group': 'DMA'},
    {'addr': 0xC0000320, 'name': 'DMA6CMDWAIT', 'bits': 32, 'group': 'DMA'},
    {'addr': 0xC0000324, 'name': 'DMA6CMDSTOP', 'bits': 32, 'group': 'DMA'},
    {'addr': 0xC0000328, 'name': 'DMA6CMDBUSY', 'bits': 32, 'group': 'DMA'},
    {'addr': 0xC000032C, 'name': 'DMA6CMDSPACE', 'bits': 32, 'group': 'DMA'},

    {'addr': 0xC0000380, 'name': 'DMA7SRCADDR', 'bits': 32, 'group': 'DMA'},
    {'addr': 0xC0000384, 'name': 'DMA7DSTADDR', 'bits': 32, 'group': 'DMA'},
    {'addr': 0xC0000388, 'name': 'DMA7LENGTH', 'bits': 16, 'group': 'DMA'},
    {'addr': 0xC000038A, 'name': 'DMA7REQID', 'bits': 16, 'group': 'DMA'},
    {'addr': 0xC000038C, 'name': 'DMA7MODE', 'bits': 16, 'group': 'DMA'},
    {'addr': 0xC0000390, 'name': 'DMA7BUFSRCADDR', 'bits': 32, 'group': 'DMA'},
    {'addr': 0xC0000394, 'name': 'DMA7BUFDSTADDR', 'bits': 32, 'group': 'DMA'},
    {'addr': 0xC0000398, 'name': 'DMA7BUFLENGTH', 'bits': 16, 'group': 'DMA'},
    {'addr': 0xC000039A, 'name': 'DMA7BUFREQID', 'bits': 16, 'group': 'DMA'},
    {'addr': 0xC000039C, 'name': 'DMA7BUFMODE', 'bits': 16, 'group': 'DMA'},
    {'addr': 0xC00003A0, 'name': 'DMA7CMDWAIT', 'bits': 32, 'group': 'DMA'},
    {'addr': 0xC00003A4, 'name': 'DMA7CMDSTOP', 'bits': 32, 'group': 'DMA'},
    {'addr': 0xC00003A8, 'name': 'DMA7CMDBUSY', 'bits': 32, 'group': 'DMA'},
    {'addr': 0xC00003AC, 'name': 'DMA7CMDSPACE', 'bits': 32, 'group': 'DMA'},

    {'addr': 0xC000307C, 'name': 'DPC0HTOTAL', 'bits': 16, 'group': 'DPC'},
    {'addr': 0xC000307E, 'name': 'DPC0HSWIDTH', 'bits': 16, 'group': 'DPC'},
    {'addr': 0xC0003080, 'name': 'DPC0HASTART', 'bits': 16, 'group': 'DPC'},
    {'addr': 0xC0003082, 'name': 'DPC0HAEND', 'bits': 16, 'group': 'DPC'},
    {'addr': 0xC0003084, 'name': 'DPC0VTOTAL', 'bits': 16, 'group': 'DPC'},
    {'addr': 0xC0003086, 'name': 'DPC0VSWIDTH', 'bits': 16, 'group': 'DPC'},
    {'addr': 0xC0003088, 'name': 'DPC0VASTART', 'bits': 16, 'group': 'DPC'},
    {'addr': 0xC000308A, 'name': 'DPC0VAEND', 'bits': 16, 'group': 'DPC'},
    {'addr': 0xC000308C, 'name': 'DPC0CTRL0', 'bits': 16, 'group': 'DPC'},
    {'addr': 0xC000308E, 'name': 'DPC0CTRL1', 'bits': 16, 'group': 'DPC'},
    {'addr': 0xC0003090, 'name': 'DPC0EVTOTAL', 'bits': 16, 'group': 'DPC'},
    {'addr': 0xC0003092, 'name': 'DPC0EVSWIDTH', 'bits': 16, 'group': 'DPC'},
    {'addr': 0xC0003094, 'name': 'DPC0EVASTART', 'bits': 16, 'group': 'DPC'},
    {'addr': 0xC0003096, 'name': 'DPC0EVAEND', 'bits': 16, 'group': 'DPC'},
    {'addr': 0xC0003098, 'name': 'DPC0CTRL2', 'bits': 16, 'group': 'DPC'},
    {'addr': 0xC000309A, 'name': 'DPC0VSEOFFSET', 'bits': 16, 'group': 'DPC'},
    {'addr': 0xC000309C, 'name': 'DPC0VSSOFFSET', 'bits': 16, 'group': 'DPC'},
    {'addr': 0xC000309E, 'name': 'DPC0EVSEOFFSET', 'bits': 16, 'group': 'DPC'},
    {'addr': 0xC00030A0, 'name': 'DPC0EVSSOFFSET', 'bits': 16, 'group': 'DPC'},
    {'addr': 0xC00030A2, 'name': 'DPC0DELAY0', 'bits': 16, 'group': 'DPC'},
    {'addr': 0xC00030AA, 'name': 'DPRNUMGENCON0', 'bits': 16, 'group': 'DPC'},
    {'addr': 0xC00030AC, 'name': 'DPRNUMGENCON1', 'bits': 16, 'group': 'DPC'},
    {'addr': 0xC00030AE, 'name': 'DPRNUMGENCON2', 'bits': 16, 'group': 'DPC'},
    {'addr': 0xC00030B0, 'name': 'DPC0FDTADDR', 'bits': 16, 'group': 'DPC'},
    {'addr': 0xC00030B2, 'name': 'DPC0FRDITHERVALUE', 'bits': 16, 'group': 'DPC'},
    {'addr': 0xC00030B4, 'name': 'DPC0FGDITHERVALUE', 'bits': 16, 'group': 'DPC'},
    {'addr': 0xC00030B6, 'name': 'DPC0FBDITHERVALUE', 'bits': 16, 'group': 'DPC'},
    {'addr': 0xC00031C0, 'name': 'DPC0CLKENB', 'bits': 32, 'group': 'DPC'},
    {'addr': 0xC00031C4, 'name': 'DPC0CLKGEN0', 'bits': 32, 'group': 'DPC'},
    {'addr': 0xC00031C8, 'name': 'DPC0CLKGEN1', 'bits': 32, 'group': 'DPC'},
    {'addr': 0xC00034C2, 'name': 'VENCCTRLA', 'bits': 16, 'group': 'DPC'},
    {'addr': 0xC0003404, 'name': 'VENCCTRLB', 'bits': 16, 'group': 'DPC'},
    {'addr': 0xC0003408, 'name': 'VENCSCH', 'bits': 16, 'group': 'DPC'},
    {'addr': 0xC000340A, 'name': 'VENCHUE', 'bits': 16, 'group': 'DPC'},
    {'addr': 0xC000340C, 'name': 'VENSAT', 'bits': 16, 'group': 'DPC'},
    {'addr': 0xC000340E, 'name': 'VENCCRT', 'bits': 16, 'group': 'DPC'},
    {'addr': 0xC0003410, 'name': 'VENCBRT', 'bits': 16, 'group': 'DPC'},
    {'addr': 0xC0003412, 'name': 'VENCFSCADJH', 'bits': 16, 'group': 'DPC'},
    {'addr': 0xC0003414, 'name': 'VENCFSCADJL', 'bits': 16, 'group': 'DPC'},
    {'addr': 0xC0003420, 'name': 'VENCDACSEL', 'bits': 16, 'group': 'DPC'},
    {'addr': 0xC0003440, 'name': 'VENCICNTL', 'bits': 16, 'group': 'DPC'},
    {'addr': 0xC0003448, 'name': 'VENCHSVSO', 'bits': 16, 'group': 'DPC'},
    {'addr': 0xC000344A, 'name': 'VENCHSOS', 'bits': 16, 'group': 'DPC'},
    {'addr': 0xC000344C, 'name': 'VENCHSOE', 'bits': 16, 'group': 'DPC'},
    {'addr': 0xC000344E, 'name': 'VENCVSOS', 'bits': 16, 'group': 'DPC'},
    {'addr': 0xC0003450, 'name': 'VENCVSOE', 'bits': 16, 'group': 'DPC'},
    {'addr': 0xC000347C, 'name': 'DPC1HTOTAL', 'bits': 16, 'group': 'DPC'},
    {'addr': 0xC000347E, 'name': 'DPC1HSWIDTH', 'bits': 16, 'group': 'DPC'},
    {'addr': 0xC0003480, 'name': 'DPC1HASTART', 'bits': 16, 'group': 'DPC'},
    {'addr': 0xC0003482, 'name': 'DPC1HAEND', 'bits': 16, 'group': 'DPC'},
    {'addr': 0xC0003484, 'name': 'DPC1VTOTAL', 'bits': 16, 'group': 'DPC'},
    {'addr': 0xC0003486, 'name': 'DPC1VSWIDTH', 'bits': 16, 'group': 'DPC'},
    {'addr': 0xC0003488, 'name': 'DPC1VASTART', 'bits': 16, 'group': 'DPC'},
    {'addr': 0xC000348A, 'name': 'DPC1VAEND', 'bits': 16, 'group': 'DPC'},
    {'addr': 0xC000348C, 'name': 'DPC1CTRL0', 'bits': 16, 'group': 'DPC'},
    {'addr': 0xC000348E, 'name': 'DPC1CTRL1', 'bits': 16, 'group': 'DPC'},
    {'addr': 0xC0003490, 'name': 'DPC1EVTOTAL', 'bits': 16, 'group': 'DPC'},
    {'addr': 0xC0003492, 'name': 'DPC1EVSWIDTH', 'bits': 16, 'group': 'DPC'},
    {'addr': 0xC0003494, 'name': 'DPC1EVASTART', 'bits': 16, 'group': 'DPC'},
    {'addr': 0xC0003496, 'name': 'DPC1EVAEND', 'bits': 16, 'group': 'DPC'},
    {'addr': 0xC0003498, 'name': 'DPC1CTRL2', 'bits': 16, 'group': 'DPC'},
    {'addr': 0xC000349A, 'name': 'DPC1VSEOFFSET', 'bits': 16, 'group': 'DPC'},
    {'addr': 0xC000349C, 'name': 'DPC1VSSOFFSET', 'bits': 16, 'group': 'DPC'},
    {'addr': 0xC000349E, 'name': 'DPC1EVSEOFFSET', 'bits': 16, 'group': 'DPC'},
    {'addr': 0xC00034A0, 'name': 'DPC1EVSSOFFSET', 'bits': 16, 'group': 'DPC'},
    {'addr': 0xC00034A4, 'name': 'DPUPSCALECON0', 'bits': 16, 'group': 'DPC'},
    {'addr': 0xC00034A6, 'name': 'DPUPSCALECON1', 'bits': 16, 'group': 'DPC'},
    {'addr': 0xC00034A8, 'name': 'DPUPSCALECON2', 'bits': 16, 'group': 'DPC'},
    {'addr': 0xC00035C0, 'name': 'DPC1CLKENB', 'bits': 32, 'group': 'DPC'},
    {'addr': 0xC00035C4, 'name': 'DPC1CLKGEN0', 'bits': 32, 'group': 'DPC'},
    {'addr': 0xC00035C8, 'name': 'DPC1CLKGEN1', 'bits': 32, 'group': 'DPC'},

    {'addr': 0xC0004000, 'name': 'MLC0CONTROLT', 'bits': 32, 'group': 'MLC'},
    {'addr': 0xC0004004, 'name': 'MLC0SCREENSIZE', 'bits': 32, 'group': 'MLC'},
    {'addr': 0xC0004008, 'name': 'MLC0BGCOLOR', 'bits': 32, 'group': 'MLC'},
    {'addr': 0xC000400C, 'name': 'MLC0LEFTRIGHT0', 'bits': 32, 'group': 'MLC'},
    {'addr': 0xC0004010, 'name': 'MLC0TOPBOTTOM0', 'bits': 32, 'group': 'MLC'},
    {'addr': 0xC0004014, 'name': 'MLC0LEFTRIGHT0_0', 'bits': 32, 'group': 'MLC'},
    {'addr': 0xC0004018, 'name': 'MLC0TOPBOTTOM0_0', 'bits': 32, 'group': 'MLC'},
    {'addr': 0xC000401C, 'name': 'MLC0LEFTRIGHT0_1', 'bits': 32, 'group': 'MLC'},
    {'addr': 0xC0004020, 'name': 'MLC0TOPBOTTOM0_1', 'bits': 32, 'group': 'MLC'},
    {'addr': 0xC0004024, 'name': 'MLC0CONTROL0', 'bits': 32, 'group': 'MLC'},
    {'addr': 0xC0004028, 'name': 'MLC0HSTRIDE0', 'bits': 32, 'group': 'MLC'},
    {'addr': 0xC000402C, 'name': 'MLC0VSTRIDE0', 'bits': 32, 'group': 'MLC'},
    {'addr': 0xC0004030, 'name': 'MLC0TPCOLOR0', 'bits': 32, 'group': 'MLC'},
    {'addr': 0xC0004034, 'name': 'MLC0INVCOLOR0', 'bits': 32, 'group': 'MLC'},
    {'addr': 0xC0004038, 'name': 'MLC0ADDRESS0', 'bits': 32, 'group': 'MLC'},
    {'addr': 0xC000403C, 'name': 'MLC0PALETTE0', 'bits': 32, 'group': 'MLC'},
    {'addr': 0xC0004040, 'name': 'MLC0LEFTRIGHT1', 'bits': 32, 'group': 'MLC'},
    {'addr': 0xC0004044, 'name': 'MLC0TOPBOTTOM1', 'bits': 32, 'group': 'MLC'},
    {'addr': 0xC0004048, 'name': 'MLC0LEFTRIGHT1_0', 'bits': 32, 'group': 'MLC'},
    {'addr': 0xC000404C, 'name': 'MLC0TOPBOTTOM1_0', 'bits': 32, 'group': 'MLC'},
    {'addr': 0xC0004050, 'name': 'MLC0LEFTRIGHT1_1', 'bits': 32, 'group': 'MLC'},
    {'addr': 0xC0004054, 'name': 'MLC0TOPBOTTOM1_1', 'bits': 32, 'group': 'MLC'},
    {'addr': 0xC0004058, 'name': 'MLC0CONTROL1', 'bits': 32, 'group': 'MLC'},
    {'addr': 0xC000405C, 'name': 'MLC0HSTRIDE1', 'bits': 32, 'group': 'MLC'},
    {'addr': 0xC0004060, 'name': 'MLC0VSTRIDE1', 'bits': 32, 'group': 'MLC'},
    {'addr': 0xC0004064, 'name': 'MLC0TPCOLOR1', 'bits': 32, 'group': 'MLC'},
    {'addr': 0xC0004068, 'name': 'MLC0INVCOLOR1', 'bits': 32, 'group': 'MLC'},
    {'addr': 0xC000406C, 'name': 'MLC0ADDRESS1', 'bits': 32, 'group': 'MLC'},
    {'addr': 0xC0004070, 'name': 'MLC0PALETTE1', 'bits': 32, 'group': 'MLC'},
    {'addr': 0xC0004074, 'name': 'MLC0LEFTRIGHT2', 'bits': 32, 'group': 'MLC'},
    {'addr': 0xC0004078, 'name': 'MLC0TOPBOTTOM2', 'bits': 32, 'group': 'MLC'},
    {'addr': 0xC000407C, 'name': 'MLC0CONTROL2', 'bits': 32, 'group': 'MLC'},
    {'addr': 0xC0004080, 'name': 'MLC0VSTRIDE3', 'bits': 32, 'group': 'MLC'},
    {'addr': 0xC0004084, 'name': 'MLC0TPCOLOR3', 'bits': 32, 'group': 'MLC'},
    {'addr': 0xC000408C, 'name': 'MLC0ADDRESS3', 'bits': 32, 'group': 'MLC'},
    {'addr': 0xC0004090, 'name': 'MLC0ADDRESSCB', 'bits': 32, 'group': 'MLC'},
    {'addr': 0xC0004094, 'name': 'MLC0ADDRESSCR', 'bits': 32, 'group': 'MLC'},
    {'addr': 0xC0004098, 'name': 'MLC0VSTRIECB', 'bits': 32, 'group': 'MLC'},
    {'addr': 0xC000409C, 'name': 'MLC0VSTRIDECR', 'bits': 32, 'group': 'MLC'},
    {'addr': 0xC00040A0, 'name': 'MLC0HSCALE', 'bits': 32, 'group': 'MLC'},
    {'addr': 0xC00040A4, 'name': 'MLC0VSCALE', 'bits': 32, 'group': 'MLC'},
    {'addr': 0xC00040A8, 'name': 'MLC0LUENH', 'bits': 32, 'group': 'MLC'},
    {'addr': 0xC00040AC, 'name': 'MLC0CHENH0', 'bits': 32, 'group': 'MLC'},
    {'addr': 0xC00040B0, 'name': 'MLC0CHENH1', 'bits': 32, 'group': 'MLC'},
    {'addr': 0xC00040B4, 'name': 'MLC0CHENH2', 'bits': 32, 'group': 'MLC'},
    {'addr': 0xC00040B8, 'name': 'MLC0CHENH3', 'bits': 32, 'group': 'MLC'},
    {'addr': 0xC00043C0, 'name': 'MLC0CLKENB', 'bits': 32, 'group': 'MLC'},
    {'addr': 0xC0004400, 'name': 'MLC1CONTROLT', 'bits': 32, 'group': 'MLC'},
    {'addr': 0xC0004404, 'name': 'MLC1SCREENSIZE', 'bits': 32, 'group': 'MLC'},
    {'addr': 0xC0004408, 'name': 'MLC1BGCOLOR', 'bits': 32, 'group': 'MLC'},
    {'addr': 0xC000440C, 'name': 'MLC1LEFTRIGHT0', 'bits': 32, 'group': 'MLC'},
    {'addr': 0xC0004410, 'name': 'MLC1TOPBOTTOM0', 'bits': 32, 'group': 'MLC'},
    {'addr': 0xC0004414, 'name': 'MLC1LEFTRIGHT0_0', 'bits': 32, 'group': 'MLC'},
    {'addr': 0xC0004418, 'name': 'MLC1TOPBOTTOM0_0', 'bits': 32, 'group': 'MLC'},
    {'addr': 0xC000441C, 'name': 'MLC1LEFTRIGHT0_1', 'bits': 32, 'group': 'MLC'},
    {'addr': 0xC0004420, 'name': 'MLC1TOPBOTTOM0_1', 'bits': 32, 'group': 'MLC'},
    {'addr': 0xC0004424, 'name': 'MLC1CONTROL0', 'bits': 32, 'group': 'MLC'},
    {'addr': 0xC0004428, 'name': 'MLC1HSTRIDE0', 'bits': 32, 'group': 'MLC'},
    {'addr': 0xC000442C, 'name': 'MLC1VSTRIDE0', 'bits': 32, 'group': 'MLC'},
    {'addr': 0xC0004430, 'name': 'MLC1TPCOLOR0', 'bits': 32, 'group': 'MLC'},
    {'addr': 0xC0004434, 'name': 'MLC1INVCOLOR0', 'bits': 32, 'group': 'MLC'},
    {'addr': 0xC0004438, 'name': 'MLC1ADDRESS0', 'bits': 32, 'group': 'MLC'},
    {'addr': 0xC000443C, 'name': 'MLC1PALETTE0', 'bits': 32, 'group': 'MLC'},
    {'addr': 0xC0004440, 'name': 'MLC1LEFTRIGHT1', 'bits': 32, 'group': 'MLC'},
    {'addr': 0xC0004444, 'name': 'MLC1TOPBOTTOM1', 'bits': 32, 'group': 'MLC'},
    {'addr': 0xC0004448, 'name': 'MLC1LEFTRIGHT1_0', 'bits': 32, 'group': 'MLC'},
    {'addr': 0xC000444C, 'name': 'MLC1TOPBOTTOM1_0', 'bits': 32, 'group': 'MLC'},
    {'addr': 0xC0004450, 'name': 'MLC1LEFTRIGHT1_1', 'bits': 32, 'group': 'MLC'},
    {'addr': 0xC0004454, 'name': 'MLC1TOPBOTTOM1_1', 'bits': 32, 'group': 'MLC'},
    {'addr': 0xC0004458, 'name': 'MLC1CONTROL1', 'bits': 32, 'group': 'MLC'},
    {'addr': 0xC000445C, 'name': 'MLC1HSTRIDE1', 'bits': 32, 'group': 'MLC'},
    {'addr': 0xC0004460, 'name': 'MLC1VSTRIDE1', 'bits': 32, 'group': 'MLC'},
    {'addr': 0xC0004464, 'name': 'MLC1TPCOLOR1', 'bits': 32, 'group': 'MLC'},
    {'addr': 0xC0004468, 'name': 'MLC1INVCOLOR1', 'bits': 32, 'group': 'MLC'},
    {'addr': 0xC000446C, 'name': 'MLC1ADDRESS1', 'bits': 32, 'group': 'MLC'},
    {'addr': 0xC0004470, 'name': 'MLC1PALETTE1', 'bits': 32, 'group': 'MLC'},
    {'addr': 0xC0004474, 'name': 'MLC1LEFTRIGHT2', 'bits': 32, 'group': 'MLC'},
    {'addr': 0xC0004478, 'name': 'MLC1TOPBOTTOM2', 'bits': 32, 'group': 'MLC'},
    {'addr': 0xC000447C, 'name': 'MLC1CONTROL2', 'bits': 32, 'group': 'MLC'},
    {'addr': 0xC0004480, 'name': 'MLC1VSTRIDE3', 'bits': 32, 'group': 'MLC'},
    {'addr': 0xC0004484, 'name': 'MLC1TPCOLOR3', 'bits': 32, 'group': 'MLC'},
    {'addr': 0xC000448C, 'name': 'MLC1ADDRESS3', 'bits': 32, 'group': 'MLC'},
    {'addr': 0xC0004490, 'name': 'MLC1ADDRESSCB', 'bits': 32, 'group': 'MLC'},
    {'addr': 0xC0004494, 'name': 'MLC1ADDRESSCR', 'bits': 32, 'group': 'MLC'},
    {'addr': 0xC0004498, 'name': 'MLC1VSTRIECB', 'bits': 32, 'group': 'MLC'},
    {'addr': 0xC000449C, 'name': 'MLC1VSTRIDECR', 'bits': 32, 'group': 'MLC'},
    {'addr': 0xC00044A0, 'name': 'MLC1HSCALE', 'bits': 32, 'group': 'MLC'},
    {'addr': 0xC00044A4, 'name': 'MLC1VSCALE', 'bits': 32, 'group': 'MLC'},
    {'addr': 0xC00044A8, 'name': 'MLC1LUENH', 'bits': 32, 'group': 'MLC'},
    {'addr': 0xC00044AC, 'name': 'MLC1CHENH0', 'bits': 32, 'group': 'MLC'},
    {'addr': 0xC00044B0, 'name': 'MLC1CHENH1', 'bits': 32, 'group': 'MLC'},
    {'addr': 0xC00044B4, 'name': 'MLC1CHENH2', 'bits': 32, 'group': 'MLC'},
    {'addr': 0xC00044B8, 'name': 'MLC1CHENH3', 'bits': 32, 'group': 'MLC'},
    {'addr': 0xC00047C0, 'name': 'MLC1CLKENB', 'bits': 32, 'group': 'MLC'},

    {'addr': 0xC0005000, 'name': 'ADCCON', 'bits': 16, 'group': 'ADC'},
    {'addr': 0xC0005004, 'name': 'ADCDAT', 'bits': 16, 'group': 'ADC'},
    {'addr': 0xC0005008, 'name': 'ADCINTENB', 'bits': 16, 'group': 'ADC'},
    {'addr': 0xC000500C, 'name': 'ADCINTCLR', 'bits': 16, 'group': 'ADC'},
    {'addr': 0xC0005040, 'name': 'ADCCLKENB', 'bits': 32, 'group': 'ADC'},

    {'addr': 0xC000A000, 'name': 'GPIOAOUT', 'bits': 32, 'group': 'GPIO'},
    {'addr': 0xC000A004, 'name': 'GPIOAOUTENB', 'bits': 32, 'group': 'GPIO'},
    {'addr': 0xC000A008, 'name': 'GPIOADETMODE0', 'bits': 32, 'group': 'GPIO'},
    {'addr': 0xC000A00C, 'name': 'GPIOADETMODE1', 'bits': 32, 'group': 'GPIO'},
    {'addr': 0xC000A010, 'name': 'GPIOAINTENB', 'bits': 32, 'group': 'GPIO'},
    {'addr': 0xC000A014, 'name': 'GPIOADET', 'bits': 32, 'group': 'GPIO'},
    {'addr': 0xC000A018, 'name': 'GPIOAPAD', 'bits': 32, 'group': 'GPIO'},
    {'addr': 0xC000A01C, 'name': 'GPIOAPUENB', 'bits': 32, 'group': 'GPIO'},
    {'addr': 0xC000A020, 'name': 'GPIOAALTFN0', 'bits': 32, 'group': 'GPIO'},
    {'addr': 0xC000A024, 'name': 'GPIOAALTFN1', 'bits': 32, 'group': 'GPIO'},

    {'addr': 0xC000A040, 'name': 'GPIOBOUT', 'bits': 32, 'group': 'GPIO'},
    {'addr': 0xC000A044, 'name': 'GPIOBOUTENB', 'bits': 32, 'group': 'GPIO'},
    {'addr': 0xC000A048, 'name': 'GPIOBDETMODE0', 'bits': 32, 'group': 'GPIO'},
    {'addr': 0xC000A04C, 'name': 'GPIOBDETMODE1', 'bits': 32, 'group': 'GPIO'},
    {'addr': 0xC000A050, 'name': 'GPIOBINTENB', 'bits': 32, 'group': 'GPIO'},
    {'addr': 0xC000A054, 'name': 'GPIOBDET', 'bits': 32, 'group': 'GPIO'},
    {'addr': 0xC000A058, 'name': 'GPIOBPAD', 'bits': 32, 'group': 'GPIO'},
    {'addr': 0xC000A05C, 'name': 'GPIOBPUENB', 'bits': 32, 'group': 'GPIO'},
    {'addr': 0xC000A060, 'name': 'GPIOBALTFN0', 'bits': 32, 'group': 'GPIO'},
    {'addr': 0xC000A064, 'name': 'GPIOBALTFN1', 'bits': 32, 'group': 'GPIO'},

    {'addr': 0xC000A080, 'name': 'GPIOCOUT', 'bits': 32, 'group': 'GPIO'},
    {'addr': 0xC000A084, 'name': 'GPIOCOUTENB', 'bits': 32, 'group': 'GPIO'},
    {'addr': 0xC000A088, 'name': 'GPIOCDETMODE0', 'bits': 32, 'group': 'GPIO'},
    {'addr': 0xC000A08C, 'name': 'GPIOCDETMODE1', 'bits': 32, 'group': 'GPIO'},
    {'addr': 0xC000A090, 'name': 'GPIOCINTENB', 'bits': 32, 'group': 'GPIO'},
    {'addr': 0xC000A094, 'name': 'GPIOCDET', 'bits': 32, 'group': 'GPIO'},
    {'addr': 0xC000A098, 'name': 'GPIOCPAD', 'bits': 32, 'group': 'GPIO'},
    {'addr': 0xC000A09C, 'name': 'GPIOCPUENB', 'bits': 32, 'group': 'GPIO'},
    {'addr': 0xC000A0A0, 'name': 'GPIOCALTFN0', 'bits': 32, 'group': 'GPIO'},
    {'addr': 0xC000A0A4, 'name': 'GPIOCALTFN1', 'bits': 32, 'group': 'GPIO'},

    {'addr': 0xC000F000, 'name': 'CLKMODEREG', 'bits': 32, 'group': 'CLKPWR'},
    {'addr': 0xC000F004, 'name': 'PLLSETREG0', 'bits': 32, 'group': 'CLKPWR'},
    {'addr': 0xC000F008, 'name': 'PLLSETREG1', 'bits': 32, 'group': 'CLKPWR'},
    {'addr': 0xC000F040, 'name': 'GPIOWAKEUPENB', 'bits': 32, 'group': 'CLKPWR'},
    {'addr': 0xC000F044, 'name': 'RTCWAKEUPENB', 'bits': 32, 'group': 'CLKPWR'},
    {'addr': 0xC000F048, 'name': 'GPIOWAKEUPRISEENB', 'bits': 32, 'group': 'CLKPWR'},
    {'addr': 0xC000F04C, 'name': 'GPIOWAKEUPFALLENB', 'bits': 32, 'group': 'CLKPWR'},
    {'addr': 0xC000F050, 'name': 'GPIOPEND', 'bits': 32, 'group': 'CLKPWR'},
    {'addr': 0xC000F058, 'name': 'INTPENDSPAD', 'bits': 32, 'group': 'CLKPWR'},
    {'addr': 0xC000F05C, 'name': 'PWRRSTSTATUS', 'bits': 32, 'group': 'CLKPWR'},
    {'addr': 0xC000F060, 'name': 'INTENB', 'bits': 32, 'group': 'CLKPWR'},
    {'addr': 0xC000F07C, 'name': 'PWRMODE', 'bits': 32, 'group': 'CLKPWR'},
    {'addr': 0xC000F100, 'name': 'PADSTRENGTHGPIOAL', 'bits': 32, 'group': 'CLKPWR'},
    {'addr': 0xC000F104, 'name': 'PADSTRENGTHGPIOAH', 'bits': 32, 'group': 'CLKPWR'},
    {'addr': 0xC000F108, 'name': 'PADSTRENGTHGPIOBL', 'bits': 32, 'group': 'CLKPWR'},
    {'addr': 0xC000F10C, 'name': 'PADSTRENGTHGPIOBH', 'bits': 32, 'group': 'CLKPWR'},
    {'addr': 0xC000F110, 'name': 'PADSTRENGTHGPIOCL', 'bits': 32, 'group': 'CLKPWR'},
    {'addr': 0xC000F114, 'name': 'PADSTRENGTHGPIOCH', 'bits': 32, 'group': 'CLKPWR'},
    {'addr': 0xC000F118, 'name': 'PADSTRENGTHBUS', 'bits': 32, 'group': 'CLKPWR'},

    {'addr': 0xC0014800, 'name': 'MEMCFG', 'bits': 16, 'group': 'MCUA'},
    {'addr': 0xC0014802, 'name': 'MEMTIME0', 'bits': 16, 'group': 'MCUA'},
    {'addr': 0xC0014804, 'name': 'MEMTIME1', 'bits': 16, 'group': 'MCUA'},
    {'addr': 0xC0014808, 'name': 'MEMREFRESH', 'bits': 16, 'group': 'MCUA'},
    {'addr': 0xC001480A, 'name': 'MEMCONTROL', 'bits': 16, 'group': 'MCUA'},
    {'addr': 0xC001480C, 'name': 'MEMCLKDELAY', 'bits': 16, 'group': 'MCUA'},
    {'addr': 0xC001480E, 'name': 'MEMDQSOUTDELAY', 'bits': 16, 'group': 'MCUA'},
    {'addr': 0xC0014810, 'name': 'MEMDQSINDELAY', 'bits': 16, 'group': 'MCUA'},

    {'addr': 0xC0015800, 'name': 'MEMBW', 'bits': 32, 'group': 'MCUS'},
    {'addr': 0xC0015804, 'name': 'MEMTIMEACS', 'bits': 32, 'group': 'MCUS'},
    {'addr': 0xC0015808, 'name': 'MEMTIMECOS', 'bits': 32, 'group': 'MCUS'},
    {'addr': 0xC001580C, 'name': 'MEMTIMEACCL', 'bits': 32, 'group': 'MCUS'},
    {'addr': 0xC0015810, 'name': 'MEMTIMEACCH', 'bits': 32, 'group': 'MCUS'},
    {'addr': 0xC0015814, 'name': 'MEMTIMESACCL', 'bits': 32, 'group': 'MCUS'},
    {'addr': 0xC0015818, 'name': 'MEMTIMESACCH', 'bits': 32, 'group': 'MCUS'},
    {'addr': 0xC0015824, 'name': 'MEMTIMECOH', 'bits': 32, 'group': 'MCUS'},
    {'addr': 0xC0015828, 'name': 'MEMTIMECAH', 'bits': 32, 'group': 'MCUS'},
    {'addr': 0xC001582C, 'name': 'MEMBURSTL', 'bits': 32, 'group': 'MCUS'},
    {'addr': 0xC0015830, 'name': 'MEMBURSTH', 'bits': 32, 'group': 'MCUS'},
    {'addr': 0xC0015834, 'name': 'MEMWAIT', 'bits': 32, 'group': 'MCUS'},

    {'addr': 0xC0015874, 'name': 'NFCONTROL', 'bits': 32, 'group': 'NAND'},
    {'addr': 0xC0015878, 'name': 'NFECCL', 'bits': 32, 'group': 'NAND'},
    {'addr': 0xC001587C, 'name': 'NFECCH', 'bits': 32, 'group': 'NAND'},
    {'addr': 0xC0015880, 'name': 'NFORGECCL', 'bits': 32, 'group': 'NAND'},
    {'addr': 0xC0015884, 'name': 'NFORGECCH', 'bits': 32, 'group': 'NAND'},
    {'addr': 0xC0015888, 'name': 'NFCNT', 'bits': 32, 'group': 'NAND'},
    {'addr': 0xC001588C, 'name': 'NFECCSTATUS', 'bits': 32, 'group': 'NAND'},
    {'addr': 0xC0015890, 'name': 'NFSYNDRONE31', 'bits': 32, 'group': 'NAND'},
    {'addr': 0xC0015894, 'name': 'NFSYNDRONE75', 'bits': 32, 'group': 'NAND'},

    {'addr': 0xC0019000, 'name': 'ALIVEPWRGATEREG', 'bits': 32, 'group': 'ALIVE'},
    {'addr': 0xC0019004, 'name': 'ALIVEGPIORSTREG', 'bits': 32, 'group': 'ALIVE'},
    {'addr': 0xC0019008, 'name': 'ALIVEGPIOSETREG', 'bits': 32, 'group': 'ALIVE'},
    {'addr': 0xC001900C, 'name': 'ALIVEGPIOREADREG', 'bits': 32, 'group': 'ALIVE'},
    {'addr': 0xC0019010, 'name': 'ALIVESCRATCHRSTREG', 'bits': 32, 'group': 'ALIVE'},
    {'addr': 0xC0019014, 'name': 'ALIVESCRATCHSETREG', 'bits': 32, 'group': 'ALIVE'},
    {'addr': 0xC0019018, 'name': 'ALIVESCRATCHREADREG', 'bits': 32, 'group': 'ALIVE'},

    {'addr': 0xAC000000, 'name': 'NFDATA', 'bits': 32, 'group': 'NAND'},
    {'addr': 0xAC000010, 'name': 'NFCMD', 'bits': 16, 'group': 'NAND'},
    {'addr': 0xAC000018, 'name': 'NFADDR', 'bits': 16, 'group': 'NAND'},
)

class Registers:
    def __init__(self, core):
        self.core = core

    @classmethod
    def lookup(cls, reg): 
        if type(reg) == str:
            reg = reg.upper()
            if reg.startswith('0X'):
                reg = int(reg, 16)
                        
        if type(reg) == str:
            for r in REGS:
                if r['name'] == reg:
                    return r
        elif type(reg) == int:
            for r in REGS:
                if r['addr'] == reg:
                    return r
        raise Exception

    def read(self, r):
        if type(r) in [str, int]:
            r = Registers.lookup(r)
        if r['bits'] == 32:
            return self.core.read_u32(r['addr'])
        elif r['bits'] == 16:
            return self.core.read_u16(r['addr'])
        elif r['bits'] == 8:
            return self.core.read_u8(r['addr'])

    def write(self, r, value):
        if type(r) in [str, int]:
            r = Registers.lookup(r)
        if r['bits'] == 32:
            self.core.write_u32(r['addr'], value)
        elif r['bits'] == 16:
            self.core.write_u16(r['addr'], value)
        elif r['bits'] == 8:
            self.core.write_u8(r['addr'], value)

    def bit_set(self, r, bit):
        n = self.read(reg)
        n |= (1 << bit)
        self.write(reg, n)

    def bit_clear(self, r, bit):
        n = self.read(r)
        n &= ~(1 << bit)
        self.write(r, n)

