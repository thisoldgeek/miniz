#!/bin/sh
# run with sudo!
apt-get update  # To get the latest package lists
apt-get upgrade
apt-get install python3-pip     #takes a while!
pip3 install pi3d           # will not print any text on screen for a while! 
apt-get install python3-pil
apt-get install python3-setuptools 
easy_install3 pylms
apt-get install python3-numpy 
pip3 install RPi.GPIO        # this is Stretch Lite! Fewer packages installed

