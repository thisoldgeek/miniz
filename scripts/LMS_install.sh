#!/bin/sh
# the following is the original work of gerrelt
# http://www.gerrelt.nl/RaspberryPi/wordpress/tutorial-stand-alone-squeezebox-server-and-player-for-bbq/
# install some libs
sudo apt-get install -y libsox-fmt-all libflac-dev libfaad2 libmad0
# get the latest nightly build (from downloads.slimdevices.com):
wget -O logitechmediaserver_arm.deb $(wget -q -O - "http://www.mysqueezebox.com/update/?version=7.9.1&revision=1&geturl=1&os=debarm")
sudo dpkg -i logitechmediaserver_arm.deb
