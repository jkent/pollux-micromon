/* vim: set ts=4 sw=4 noexpandtab
 *
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

#include <asm/types.h>
#include <baremetal/crc32.h>
#include <baremetal/linker.h>
#include <driver/lowlevel_uart.h>

static void mem_write(void);
static void mem_read(void);
static void write_u8();
static void write_u16();
static void write_u32();
static void read_u8();
static void read_u16();
static void read_u32();
static void run(u32 exec_at);
static void run_kernel(u32 exec_at, u32 machine_type);

enum cmd_commands {
	cmd_nop = 0,
	cmd_write_u8,
	cmd_write_u16,
	cmd_write_u32,
	cmd_read_u8,
	cmd_read_u16,
	cmd_read_u32,
	cmd_mem_write,
	cmd_mem_read,
	cmd_run,
	cmd_run_kernel,
	END_OF_COMMANDS
};

int main(void)
{
	init_crc32_table();

	/* signal we are here */
	lowlevel_write_u8(1);

	while (1) {
		u8 command = lowlevel_read_u8();
		switch (command) {
		case cmd_nop:
			break;

		case cmd_write_u8:
			write_u8();
			break;

		case cmd_write_u16:
			write_u16();
			break;

		case cmd_write_u32:
			write_u32();
			break;

		case cmd_read_u8:
			read_u8();
			break;

		case cmd_read_u16:
			read_u16();
			break;

		case cmd_read_u32:
			read_u32();
			break;

		case cmd_mem_write:
			mem_write();
			break;

		case cmd_mem_read:
			mem_read();
			break;

		case cmd_run:
			run(lowlevel_read_u32());
			break;

		case cmd_run_kernel:
			run_kernel(lowlevel_read_u32(), lowlevel_read_u32());
			break;
		}
	}

	return 0;
}

static void read_u8(void)
{
	u8 *addr = (u8 *)lowlevel_read_u32();
	lowlevel_write_u8(*addr);
}

static void read_u16(void)
{
	u16 *addr = (u16 *)lowlevel_read_u32();
	lowlevel_write_u16(*addr);
}

static void read_u32(void)
{
	u32 *addr = (u32 *)lowlevel_read_u32();
	lowlevel_write_u32(*addr);
}

static void write_u8(void)
{
	u8 *addr = (u8 *)lowlevel_read_u32();
	*addr = lowlevel_read_u8();
}

static void write_u16(void)
{
	u16 *addr = (u16 *)lowlevel_read_u32();
	*addr = lowlevel_read_u16();
}

static void write_u32(void)
{
	u32 *addr = (u32 *)lowlevel_read_u32();
	*addr = lowlevel_read_u32();
}

static void mem_write(void)
{
	u8 *addr, *p;
	u32 size;
	u32 crc = 0;

	addr = (u8 *)lowlevel_read_u32();
	size = lowlevel_read_u32();

	p = addr;
	while ((u32)addr + size > (u32)p) {
		*p = lowlevel_read_u8();
		crc = crc32(crc, *p);
		p++;
	}
	lowlevel_write_u32(crc);
}

static void mem_read(void)
{
	u8 *addr, *p;
	u32 size;
	u32 crc = 0;

	addr = (u8 *)lowlevel_read_u32();
	size = lowlevel_read_u32();

	p = addr;
	while ((u32)addr + size > (u32)p) {
		lowlevel_write_u8(*p);
		crc = crc32(crc, *p);
		p++;
	}
	lowlevel_write_u32(crc);
}

static void run(u32 exec_at)
{
	((void(*)())exec_at)();
}

static void run_kernel(u32 exec_at, u32 machine_type)
{
	void (*kernel)(int zero, int arch, u32 params);
	u32 param_at = (u32)-1;

	kernel = (void (*)(int, int, u32))exec_at;
	kernel(0, machine_type, param_at);
}
