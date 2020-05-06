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

#include <asm/io.h>
#include <mach/alive.h>
#include <stddef.h>
#include "common.h"
#include "startup.h"
#include "uart.h"
#include "loader.h"
#include "core.h"

#define LOADER_SIGNATURE 0x6E6F4DE6

static void loader_latch_power(void);
static void loader_loop(void);
static void loader_load_rest(void);

enum loader_commands {
	loader_cmd_nop = 0,
	loader_cmd_go_main,
	loader_cmd_set_baudrate,
	loader_cmd_load_rest,
};

void loader(void)
{
	init_uart(NULL);
	loader_latch_power();
	put_u32(LOADER_SIGNATURE);
	loader_loop();
	main();

	/* Never return */
	while(1);	
}

static void loader_latch_power(void)
{
	writel(ALIVE_PWRGATEREG_NPOWERGATING, ALIVE_BASE + ALIVE_PWRGATEREG);
	writel(0, ALIVE_BASE + ALIVE_GPIORSTREG);
	writel(ALIVE_GPIO_VDDPWRONRST, ALIVE_BASE + ALIVE_GPIOSETREG);
	writel(0, ALIVE_BASE + ALIVE_GPIOSETREG);
	writel(0, ALIVE_BASE + ALIVE_PWRGATEREG);
}

static void loader_loop(void)
{
	u8 command;
	u32 baudrate;

	while (1) {
		command = getc();
		switch (command) {
		case loader_cmd_nop:
			break;

		case loader_cmd_go_main:
			return;

		case loader_cmd_set_baudrate:
			baudrate = get_u32();
			loader_set_baudrate(baudrate);
			break;

		case loader_cmd_load_rest:
			loader_load_rest();
			break;
		}
	}
}

void loader_set_baudrate(u32 baudrate)
{
	baudinfo_t *baudinfo = find_baudinfo(baudrate);
	if (baudinfo == NULL) {
		putc(REPLY_FAIL);
		return;
	}

	putc(REPLY_OK);
	init_uart(baudinfo);
	while (1) {
		if (getc() != '\x55')
			continue;
		if (getc() == '\xAA')
			break;
	}
	putc(REPLY_OK);
}

static void loader_load_rest(void)
{
	u32 *p;

	for (p = (u32 *)(MICROMON_START + 512); (u32)p < CORE_END; p++) {
		*p = get_u32();
	}
	putc(REPLY_OK);
}
