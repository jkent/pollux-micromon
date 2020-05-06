OUTPUT_FORMAT("elf32-littlearm", "elf32-littlearm", "elf32-littlearm")
OUTPUT_ARCH(arm)
ENTRY(_start)
SECTIONS
{
 . = 0x0;
 . = ALIGN(4);
 .startup : { */core/startup.*(.text .rodata .data) }
 . += (1024 * 1024 * 31);
 . = ALIGN(4);
 .text : AT(ADDR(.startup) + SIZEOF(.startup))
 {
  */core/loader.*(.text .rodata .data)
  */core/uart.*(.text .rodata .data)
  *(.text)
 }
 . = ALIGN(4);
 .rodata : { *(.rodata) }
 . = ALIGN(4);
 .data : { *(.data) }
 . = ((((1024 * 1024 * 31) + (1024 * 1024 * 1)) - (1024 * 64)) - (1024 * 48));
 . = ALIGN(4);
 __bss_start__ = .;
 .bss : { *(.bss) }
 __bss_end__ = .;
 . = (((1024 * 1024 * 31) + (1024 * 1024 * 1)) - (1024 * 64));
 . = ALIGN(4);
 __stack_end__ = .;
 . = ((1024 * 1024 * 31) + (1024 * 1024 * 1));
 . = ALIGN(4);
 __stack_start__ = .;
 /DISCARD/ : { *(.glue_7 .glue_7t .vfp11_veneer .v4_bx) }
}
