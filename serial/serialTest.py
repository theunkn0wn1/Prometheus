#####
# Author: TheUnkn0wn1
# Function: Establish Serial comms between Pi and RoboClaw
###

import serial #Common pySerial library
import RPi.GPIO as gpio #renaming because I hate caps...

port = "/dev/ttyAMA0"
tx = 8 	#Red wire
rx = 10	#purple
try:
	ser = serial.Serial(port,38400,timeout=5)
except Exception as error:
	print("An error occured executing the serial connection attempt")
	print(type(error))
	print(error)
