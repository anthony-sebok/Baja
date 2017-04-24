#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

number = [0.25,0.50,0.75,1.00]

buttons = [18,22,12,16]

GPIO.setmode(GPIO.BOARD)

for i in range(4):
    GPIO.setup(buttons[i], GPIO.IN, pull_up_down = GPIO.PUD_UP)

try:
    while(True):
        for i in range(4):
            if GPIO.input(buttons[i]) == 0:
		print (number[i])
                f = open("/var/ui/data/data.gas", "w")
                print >> f, number[i]
                f.close()
		refill = open("/var/ui/data/refill.sig", "w")
		print >> refill, "signal"
		refill.close()
                time.sleep(0.2)
                pass
                
except KeyboardInterrupt:
    GPIO.cleanup()
