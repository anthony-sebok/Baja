#!/usr/bin/python3
import RPi.GPIO as GPIO
from time import sleep
import time, math

dist_meas = 0.00
km_per_hour = 0
rpm = 0
elapse = 0
sensor = 12												#pin number sensor is plugged into
pulse = 0
start_timer = time.time()

def setup():											#Setting up GPIO
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    GPIO.setup(sensor, GPIO.IN, GPIO.PUD_UP)
    GPIO.add_event_detect(sensor, GPIO.FALLING, callback=calculate_elapse, bouncetime=20)	#callback calls function whenever magnet is detected and the bouncetime is the time the must elapse before the sensor can read another ping from the magnet ****This may need to be changed******

def calculate_elapse(channel): 			#callback function
    global pulse,start_timer, elapse
    pulse+=1											#adds one pulse whenever the magnet is detected
    elapse = time.time() - start_timer		#elapse time for every 1 complete rotation
    if elapse > 13:									#checks elapse if it goes too long it resets
        elapse = 0
    start_timer = time.time()					#resets the start time

def calculate_speed(r_cm):
    global pulse, elapse, rpm, dist_km, dist_meas, km_per_sec, km_per_hour
    if elapse!=0:										#avoid DivisionByZero error
        rpm = 1/elapse*60
        circ_cm = (2*math.pi)*r_cm				#calculate wheel circumference in CM
        dist_km = circ_cm/100000				#converts cm to km
        km_per_sec = dist_km/elapse			#calculate KM/sec
        km_per_hour = km_per_sec*3600	#calculate KM/hr
        dist_meas = (dist_km*pulse)*1000	#measures total distance traveled in meters
        return(km_per_hour)
    else:													#if elapse is 0 resets rpm and km_per_hr
        rpm = 0
        km_per_hour = 0

if __name__ == '__main__':
    setup()
    while True:
        calculate_speed(8)							#calls calculate_speed with wheel radius ****Will need to be change once actual radius is determined********
        print('rpm:{0:.0f} KMH:{1:.1f} dist_meas:{2:.2f}m pulse:{3}       elapse_time:{4:.4f}'.format(rpm,km_per_hour,dist_meas,pulse,elapse))
        sleep(0.3)
