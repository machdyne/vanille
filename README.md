# Vanille Computer

Vanille is an FPGA computer designed by Lone Dynamics Corporation.

![Vanille Computer](https://github.com/machdyne/vanille/blob/c7512943cbbb1073aff803d02f41e69563f15d20/vanille.png)

This repo will contain schematics, PCB layouts, pinouts, a 3D-printable case, example gateware and documentation.

Find more information on the [Vanille product page](https://machdyne.com/product/vanille-computer/).

## Programming Vanille

Vanille has a JTAG interface and ships with a [DFU bootloader](https://github.com/machdyne/tinydfu-bootloader) that allows the included flash [MMOD](https://machdyne.com/product/mmod) to be programmed over the USB-C port.

### DFU

The DFU bootloader is available for 5 seconds after power-on, issuing a DFU command during this period will stop the boot process until the DFU device is detached. If no command is received the boot process will continue and the user gateware will be loaded.

Install [dfu-util](http://dfu-util.sourceforge.net) (Debian/Ubuntu):

```
$ sudo apt install dfu-util
```

Update the user gateware on the flash MMOD:

```
$ sudo dfu-util -a 0 -D image.bit
```

Detach the DFU device and continue the boot process:

```
$ sudo dfu-util -a 0 -e
```

It is possible to update the bootloader itself using DFU but you shouldn't attempt this unless you have a JTAG programmer (or another method to program the MMOD) available, in case you need to restore the bootloader.

### JTAG

These examples assume you're using a "USB Blaster" JTAG cable, see the header pinout below. You will need to have [openFPGALoader](https://github.com/trabucayre/openFPGALoader) installed.

Program the configuration SRAM:

```
openFPGALoader -c usb-blaster image.bit
```

Program the flash MMOD:

```
openFPGALoader -f -c usb-blaster images/bootloader/tinydfu_vanille.bit
```

## Blinky 

Building the blinky example requires [Yosys](https://github.com/YosysHQ/yosys), [nextpnr-ecp5](https://github.com/YosysHQ/nextpnr) and [Project Trellis](https://github.com/YosysHQ/prjtrellis).

Assuming they are installed, you can simply type `make` to build the gateware, which will be written to output/blinky.bin. You can then use [openFPGALoader](https://github.com/trabucayre/openFPGALoader) or dfu-util to write the gateware to the device.

## Linux

See the [Kakao Linux](https://github.com/machdyne/kakao) repo for the latest instructions.

### Prebuilt Images

Prebuilt gateware capable of running Linux is available in the `images/v2` directory.

### Building Linux-capable Gateware

Please follow the setup instructions in the [linux-on-litex-vexriscv](https://github.com/litex-hub/linux-on-litex-vexriscv) repo and then:

1. Build the Linux-capable gateware:

```
$ cd linux-on-litex-vexriscv
$ ./make.py --board=vanille --dcache-size=64 --icache-size=64 --build
```

NOTE: This may fail, if so:

```
$ cd build/vanille/gateware
```

Edit `vanille.ys` and add the `-abc2` option as shown below:

```
synth_ecp5  -top vanille -abc2
```

Now run:

```
$ bash build_vanille.sh
```

2. Write the gateware to the MMOD using USB DFU:

```
$ sudo dfu-util -a 0 -D vanille.bit
```

3. Copy the device tree binary `../vanille.dtb` to a FAT-formatted MicroSD card.

## JTAG Header

The 3.3V JTAG header can be used to program the FPGA SRAM as well as the MMOD flash memory. It can also be used to provide power (5V) to the board.

```
1 2
3 4
5 6
```

| Pin | Signal |
| --- | ------ |
| 1 | TCK |
| 2 | TDI |
| 3 | TDO |
| 4 | TMS |
| 5 | 5V0 |
| 6 | GND |

## Board Revisions

| Revision | Notes |
| -------- | ----- |
| V0 | Initial prototype |
| V1 | Second prototype; fixes SRAM schematic error; adds LED |
| V2 | Initial production version; fixes another SRAM schematic error |

## License

The contents of this repo are released under the [Lone Dynamics Open License](LICENSE.md) with the following exceptions:

- The KiCad design files contain parts of the [kicad-pmod](https://github.com/mithro/kicad-pmod) library which is released under the [Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0.html).

- The KiCad design files may contain symbols and footprints released under other licenses; please contact us if we've failed to give proper attribution.

Note: You can use these designs for commercial purposes but we ask that instead of producing exact clones, that you either replace our trademarks and logos with your own or add your own next to ours.
