#!/bin/bash
echo "Starting gas monitor..."
sudo python /var/ui/gasmon.py &
echo "Starting gas gauge reset..."
sudo python /var/ui/gasreset.py &
echo "Starting rpm monitor..."
sudo python /var/ui/rpmmon.py &
echo "Starting temp monitor..."
sudo python /var/ui/tempmon.py &
echo "Start web browser"
firefox http://localhost/ui
