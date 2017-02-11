#!/usr/bin/env python
import RPi.GPIO as GPIO
from time import sleep
import time, math

dist_meas = 0.00
km_per_hour = 0
rpm = 0
elapse = 0
sensor = 12
pulse = 0
start_timer = time.time()

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    GPIO.setup(sensor, GPIO.IN, GPIO.PUD_UP)
    GPIO.add_event_detect(sensor, GPIO.FALLING, callback=calculate_elapse, bouncetime=20)

def calculate_elapse(channel):
    global pulse,start_timer, elapse
    pulse+=1
    elapse = time.time() - start_timer
    if elapse > 13:
        elapse = 0
    start_timer = time.time()

def calculate_speed(r_cm):
    global pulse, elapse, rpm, dist_km, dist_meas, km_per_sec, km_per_hour
    if elapse!=0:
        rpm = 1/elapse*60
        circ_cm = (2*math.pi)*r_cm
        dist_km = circ_cm/100000
        km_per_sec = dist_km/elapse
        km_per_hour = km_per_sec*3600
        dist_meas = (dist_km*pulse)*1000
        return(km_per_hour)
    else:
        rpm = 0
        km_per_hour = 0

if __name__ == '__main__':
    setup()
    while True:
        calculate_speed(8)
        print('rpm:{0:.0f} KMH:{1:.1f} dist_meas:{2:.2f}m pulse:{3}       elapse_time:{4:.4f}'.format(rpm,km_per_hour,dist_meas,pulse,elapse))
        sleep(0.3)
