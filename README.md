nad-control
===========

Simple controls to switch NAD amplifiers on and off automatically via the rs-232 port. 

Prerequisites: 
- Python 3.0 (could easily be modified for Python 2)
- Pyserial (python-pyserial package in Arch Linux)

RS-232 cable from HTPC to serial RS-232 port at back of NAD amplifier. Tested on NAD C375BEE, but should work on most.

To get systemd to work:
1) copy nad.py to /usr/share/nad/nad.py (make sure it is executable by root, chmod 700 nad.py)
2) copy nad.service to /etc/systemd/system/nad.service
3) check it works, switch amp on / off with "systemctl start nad" and "systemctl stop nad" 
4) systemctl enable nad

I also set source to CD, speakers to A and disable speakers B. You can easily change that behaviour in nad.py.

NAD Documentation reference: http://nadelectronics.com/software#Protocol (NAD_M15HD_Protocol_Docs.zip)

Inspired by https://github.com/jaskorpe/nad_daemon which showed me this could work. 
But I didn't need an IP daemon since I only wanted to switch my amplifier on and off with my HTPC.

Some serial debugging tips:
1) make sure you have serial enabled in BIOS
2) check kernel is picking up serial port: /dev/ttyS0
3) If not check lsmod | grep 8250 => modprobe 8250 
4) if you're using USB to serial converter it will prob be /dev/ttyUSB0
