/*
 * Copyright (C) 2011-2020 Jeff Kent <jakent@gmail.com>
 *
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
 */

#ifndef __CRC32_H__
#define __CRC32_H__

#include <asm/types.h>

#define CRC32_POLYNOMIAL 0x04C11DB7

void init_crc32_table(void);
u32 crc32(u32 crc, const u8 data);

#endif /* __CRC32_H__ */
