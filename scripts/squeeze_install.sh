#!/bin/sh
# original work by gerrelt
# http://www.gerrelt.nl/RaspberryPi/wordpress/tutorial-installing-squeezelite-player-on-raspbian/#Installing_Squeezelite
sudo apt-get install -y libflac-dev libfaad2 libmad0

#Create a squeezelite “work” directory and download squeezelite:

mkdir squeezelite
cd squeezelite
wget -O squeezelite-armv6hf.tar.gz http://www.gerrelt.nl/RaspberryPi/squeezelite_ralph/squeezelite-armv6hf.tar.gz
# for newest version see: https://sourceforge.net/projects/lmsclients/files/squeezelite/linux
tar -xvzf squeezelite-armv6hf.tar.gz
mv squeezelite squeezelite-armv6hf
sudo mv squeezelite-armv6hf /usr/bin
sudo chmod a+x /usr/bin/squeezelite-armv6hf

# cd to /home/pi/squeezelite not necessary - squeezelite under miniz/scripts
#cd /home/pi/squeezelite 
sudo wget http://www.gerrelt.nl/RaspberryPi/squeezelite_settings.sh
sudo mv squeezelite_settings.sh /usr/local/bin
sudo chmod a+x /usr/local/bin/squeezelite_settings.sh
 
sudo wget http://www.gerrelt.nl/RaspberryPi/squeezelitehf.sh
sudo mv squeezelitehf.sh /etc/init.d/squeezelite
sudo chmod a+x /etc/init.d/squeezelite
 
sudo wget http://www.gerrelt.nl/RaspberryPi/squeezelite.service
sudo mv squeezelite.service /etc/systemd/system
sudo systemctl enable squeezelite.service 
cd /home/pi
