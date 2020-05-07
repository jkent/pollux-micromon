ifndef BAREMETAL_PATH
$(err Not in a baremetal enabled shell)
endif
include $(BAREMETAL_PATH)/tools/make/rules.mk

target := micromon.bin

obj-y += main.o
obj-y += startup.o
