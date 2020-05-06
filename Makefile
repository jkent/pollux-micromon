ifndef BAREMETAL_PATH
$(err Not in a baremetal enabled shell)
endif

target := micromon.bin
srcdirs := src
cflags-y += -D_LF1000_BOOTLOADER -DCONFIG_MACH_LF_LF1000 -DCONFIG_CPU_SPEED_393216000 -DCONFIG_RAM_18MB -ffreestanding
include-y += src
ldscript-y = src/micromon.lds

include $(BAREMETAL_PATH)/tools/make/rules.mk
