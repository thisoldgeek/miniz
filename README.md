# **miniz internet radio**
![miniz radio](https://github.com/thisoldgeek/miniz/blob/master/miniz_hackster_intro_photo.JPG "miniz Streaming Radio")
 

# *Acknowledgements:*
My grateful appreciation is extended to the following, without whom this project would never exist, 
and to various Makers and members of the Open Source community for their continued sharing and support.

Tinkernut, https://www.hackster.io/tinkernut/diy-vintage-spotify-radio-using-a-raspberry-pi-bc3322

gerrelt, http://www.gerrelt.nl/RaspberryPi/wordpress/tutorial-stand-alone-squeezebox-server-and-player-for-bbq/

Oliver Derks, pi3d clock, https://groups.google.com/forum/#!topic/pi3d/qls3MQbtLiA

Bob Rathbone, rotary encoders, http://www.bobrathbone.com/raspberrypi/Raspberry%20Rotary%20Encoders.pdf

jinglemansweep on github, pyLMS, https://github.com/jinglemansweep/PyLMS

pi3d written by Tim Skillman, Paddy Gaunt, Tom Ritchford Copyright © 2012 - 2017, https://github.com/tipam/pi3d

Adafruit, various but especially, https://learn.adafruit.com/running-opengl-based-games-and-emulators-on-adafruit-pitft-displays/pitft-setup

trendblog: Mark Knoll, running headless pi, http://trendblog.net/raspberry-pi-basic-headless-setup-without-cables/


## *Description:*
A mono radio that plays favorite Pandora channels, internet radio stations, podcasts, playlists and 
local music using Logitech Media System and SqueezeLite. 

In the as-built version of this project, I'm using the free downloadable Deco typefont from Nick Curtis, called "Dubba Dubba". If you like Nick's work, please contribute a few $$ at: http://www.1001fonts.com/search.html?search=dubba+dubba&x=10&y=6

See the posting at (future):
http://thisoldgeek.blogspot.com

hackster.io miniz


## *Required Hardware:*
* raspberry pi zero W
* Adafruit piTFT Plus 3.5in display
* Small Speaker (3 inch full-range)
* Adafruit mono i2s amp, product 3006
* Adafruit perma-proto bonnet, product 3203
* Pimoroni On-Off/SHIM, Adafruit product 3581
* 2x rotary encoders with on/off switch, Adafruit product 377
* Optional but highly recommended: right-angle micro-usb to barrel connector
* Miscellaneous screws, nuts, standoffs, 22AWG wire

## *Fabrication:*
* 3D print files in STL_files folder
* 3D printed case required; other 3d parts optional
* See docs folder for 3D print settings

## *Configuration:*
* Install python programs and run scripts. See tutorial at hackster.io/thisoldgeek

Change IP Address to the IP of your miniz
Change player_id to your player from LMS/Settings/Information MAC Address

If you'd like to add additional "radio stations"

Consult the miniz/docs file name miniZ_dial_frequency_map.png and change the /miniz/miniz.py program

*format below is degrees:fav_number

favs = {82:0,57:1,30:2,8:3,352:4,333:5}

## *Testing:*
Use miniz/test_rotary_switches.py to test the tune and volume rotary encoder wiring and functions
Pin numbers in test_rotary_switches.py are the same as in miniz.py

## *REQUIRED:*
Intentionally blank

## *More Information:*
See the build log at https://www.hackster.io/thisoldgeek/miniz-tiny-streaming-radio-based-on-classic-zenith-cube-cbbc3e
## *Update 11-19-2017:*
Initial install.
