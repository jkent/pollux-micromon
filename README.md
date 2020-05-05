Micromon
========

Micromon is a tool for the POLLUX VR3520F and LF1000 System On a Chip (SoC) platform.

It is loaded using UART0, and has the capability of loading very fast if the hardware is configured for 512-byte boot mode.  It also has features to detect if the target has power and assert reset and uart boot modes if your hardware supports it.

Getting started
---------------

```sh
sudo apt-get install gcc-arm-none-eabi
mkdir build
cd build
cmake -DCMAKE_TOOLCHAIN_FILE=toolchain.cmake ..
make
cd ..
```

Configure your target in `micromon.cfg`.


Now, with your target turned on and setup for UART boot mode: 

```sh
./shell.py
```

You may have to hold the power switch in the ON position until micromon takes control of the target.

To turn off your device,
```
power off
```

The bootstrap.py and boot_kernel.py scripts let you load and execute other binaries from micromon.

Have fun!