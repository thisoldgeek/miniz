#!/bin/sh
# run installs with sudo!
apt-get update  
apt-get upgrade 
cp .distutils.cfg ~/.distutils.cfg
sudo apt-get install python3-pip
sudo pip3 install pi3d           
sudo apt-get install python3-pil
sudo apt-get install python3-setuptools 
sudo pip3 install  pylms
sudo apt-get install python3-numpy 
sudo pip3 install RPi.GPIO        

