#!/usr/bin/env python

import RPi.GPIO as GPIO
import time, sys, os.path

FLOW_SENSOR = 11
global fuelPercent
global fuelPassed
fuelPercent= 0.0
fuelPassed = 0.0

#Load previous gas data
old = open('/var/ui/data/data.gas', 'r')
fuelPercent= old.read().rstrip()
fuelPassed = 3.5 - (3.5 * float(fuelPercent))
print "Loading old percentage: ", fuelPercent
print "Passed: ", fuelPassed, "L"
old.close()

GPIO.setmode(GPIO.BOARD)
GPIO.setup(FLOW_SENSOR, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

def pulse(channel):
   global fuelPercent
   global fuelPassed
   fuelPassed = fuelPassed + 0.00105669
   fuelPercent= 1 - (fuelPassed / 3.5)
   print "[gasmon] signal: ", fuelPassed, "L", fuelPercent, "% remain"

GPIO.add_event_detect(FLOW_SENSOR, GPIO.RISING, callback=pulse)



while True:
    try:
	#Check for refill signal
	if (os.path.isfile("/var/ui/data/refill.sig")):
		refill = open('/var/ui/data/data.gas', 'r')
		fuelPercent= refill.read().rstrip()
		fuelPassed = 3.5 - (3.5 * float(fuelPercent))
		refill.close()
		os.remove("/var/ui/data/refill.sig")
	print "Current fuel: ", fuelPercent
	#Write data
	f = open('/var/ui/data/data.gas', 'w')
	print >> f, fuelPercent
	f.close()
	#print "wrote", fuelPercent
        time.sleep(1)
    except KeyboardInterrupt:
        print '\nInterrupted, ending process'
        GPIO.cleanup()
        sys.exit()
