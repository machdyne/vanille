blinky_vanille:
	mkdir -p output
	yosys -q -p "synth_ecp5 -top blinky -json output/blinky_vanille.json" rtl/blinky_vanille.v
	nextpnr-ecp5 --12k --package TQFP144 --lpf vanille_v2.lpf --json output/blinky_vanille.json --textcfg output/vanille_blinky_out.config
	ecppack -v --compress --freq 2.4 output/vanille_blinky_out.config --bit output/vanille.bit

prog:
	openFPGALoader -c dirtyJtag output/vanille.bit
