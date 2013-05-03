#!/usr/bin/python

import serial
import getopt
import sys
import time

def usage(): 
	print('''
Usage: nad [OPTION]... [COMMAND]...

Simple NAD Amplifier Serial RS-232 on/off controller

Optional argument:
  -p, --port                 rs-232 port, default /dev/ttyS0
  
Manadatory commands: on / off

Examples:
  ./nad on
  ./nad off
  ./nad --port=/dev/ttyUSB0 off

Can be used with systemd/init script to switch NAD amplifier on/off when switching pc on/off.
''') 

class Nad:
	serial_port = None

	def __init__(self, port):
		self.serial_port = serial.Serial(port, 115200, timeout=5)

	def close(self):
		self.serial_port.close

	def send(self,cmd):
		# Send command twice, seems to miss if first time sometimes :/ ... no harm.
		self.serial_port.write(bytes("\r"+cmd+"\r",'utf-8')) 
		self.serial_port.write(bytes("\r"+cmd+"\r",'utf-8'))
		time.sleep(0.5) 

def main(argv):
	try:
		opts, args = getopt.getopt(argv, "h", ["help", "port="])
	except getopt.GetoptError:
		usage()
		sys.exit()
 
	port = '/dev/ttyS0'
	source = "".join(args)
	if (source=="" and opts==[]):
		usage()
		sys.exit()

	for opt, arg in opts:
		if opt in ("-h", "--help"):
			usage()
			sys.exit()
		elif opt in ("-p", "--port"):
			port = arg
			print(port)
	
	if source in ("on"):
		nad = Nad(port)
		nad.send("Main.Power=On")
		nad.send("Main.Source=CD")
		nad.send("Main.SpeakerA=On")
		nad.send("Main.SpeakerB=Off")
		nad.send("Main.Mute=Off")
		nad.close

	if source in ("off"):
		nad = Nad(port)
		nad.send("Main.Power=Off")
		nad.close

	sys.exit()

if __name__ == "__main__":
	main(sys.argv[1:])

