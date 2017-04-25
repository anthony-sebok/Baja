# D.A.S.H Project: A digital dashboard for vehicles

## Linux System
Made with a Raspberry Pi system that will host and run the files. Raspbian is recommended for best use.

## Software Requirements
* PHP server
* Python (included with Raspbian)
* Firefox or any web browser that can display full-screen

## Installation
* If using a 5 inch screen, you must install the appropriate driver given by the provider. The config.txt can be copied to your Linux's old config.txt to provide the correct resolution.
* Copy the UI folder to the following path:
``` /var/ ```
* Copy the contents of the web folder to the following path:
``` /var/www/html/ ```
* Modify your account's .profile 
``` 
#start temperature service
sudo modprobe w1-gpio
sudo modprobe w1-therm

#initiate UI
sudo python /var/ui/gasmon.py &
sudo python /var/ui/rpmmon.py &
sudo python /var/ui/gasreset.py &
sudo python /var/ui/tempmon.py &
firefox http://localhost/ui
```
A profile file is given in the repository if you have never modified your .profile before, just rename it from profile to .profile.
* For full-screen capability for Firefox, download the plug-in R-Kiosk

## Modifications
Vehicles are different and the UI may require variables to be tweaked for best results. If the maximum RPM exceeds 8000 RPM or the fuel is not 3.5L, then adjusting the max values in the index.html file of the web UI is needed in the JavaScript section of the file.
