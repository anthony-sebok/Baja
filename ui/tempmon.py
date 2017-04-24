#!/bin/bash

import glob

def read_temp_raw():
	base_dir = '/sys/bus/w1/devices/'
	device_folder = glob.glob(base_dir + '28*')[0]
	device_file = device_folder + '/w1_slave'
	f = open(device_file, 'r')
	lines = f.read()
	f.close()
	return lines

try:
	while 1:
		data = read_temp_raw()
		tempData = data.split("\n")[1].split(" ")[9]
		temperature = float(tempData[2:])
		temp_c = temperature/1000.00
		temp_f = temp_c * 9.00 / 5.00 + 32.00
		
		#print(temp_c, temp_f)
		dataFile = open("/var/ui/data/data.temp", "w")
		print >> dataFile, temp_f
		dataFile.close()
except KeyboardInterrupt:
	GPIO.cleanup()
	print ("Program Exited Cleanly")
