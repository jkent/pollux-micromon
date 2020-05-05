cmake_minimum_required(VERSION 3.6)

project(micromon)

enable_language(C ASM)

add_executable(core.elf
    core/core.c
    core/crc32.c
    core/loader.c
    core/startup.S
    core/uart.c
)

include_directories(
    core/include
    include
)

add_definitions(
    -D_LF1000_BOOTLOADER
    -DCONFIG_MACH_LF_LF1000
    -DCONFIG_CPU_SPEED_393216000
    -DCONFIG_RAM_18MB
)

add_custom_command(OUTPUT ${CMAKE_CURRENT_BINARY_DIR}/core/core.lds
    MAIN_DEPENDENCY ${CMAKE_CURRENT_SOURCE_DIR}/core/core.lds.S
    COMMAND ${CMAKE_C_COMPILER} -I ${CMAKE_CURRENT_SOURCE_DIR}/core/include -E ${CMAKE_CURRENT_SOURCE_DIR}/core/core.lds.S -P -o core/core.lds VERBATIM
)
add_dependencies(core.elf linker-script)
add_custom_target(linker-script DEPENDS core/core.lds)
set_target_properties(core.elf PROPERTIES LINK_DEPENDS core/core.lds)
set(CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS} -T core/core.lds")

add_custom_command(TARGET core.elf POST_BUILD
    COMMAND arm-none-eabi-objcopy -S -I elf32-littlearm -O binary core.elf core.bin
)

add_custom_command(TARGET core.elf POST_BUILD
    COMMAND arm-none-eabi-objdump -d -m armv5te core.elf > core.dis
    COMMAND arm-none-eabi-size --format=berkeley core.elf
)

set_property(DIRECTORY PROPERTY ADDITIONAL_MAKE_CLEAN_FILES core.bin core.dis)