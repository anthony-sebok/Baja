#!/bin/bash

sudo rm /var/ui/data/data.rpm
sudo touch /var/ui/data/data.rpm

echo "Starting gas monitor..."
sudo python /var/ui/gasmon.py &
echo "Starting gas gauge reset..."
sudo python /var/ui/gasreset.py &
echo "Starting rpm monitor..."
sudo python /var/ui/rpmmon.py &
echo "Starting temp monitor..."
sudo python /var/ui/tempmon.py &
echo "Start web browser"
firefox -private  http://localhost/ui
