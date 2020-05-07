ifndef BAREMETAL_PATH
$(err Not in a baremetal enabled shell)
endif

target := micromon.bin
srcdirs := src
cflags-y += -ffreestanding
include-y += src

include $(BAREMETAL_PATH)/tools/make/rules.mk
