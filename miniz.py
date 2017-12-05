#!/usr/bin/python3

import pi3d
import time
import os
from PIL import Image, ImageDraw
from time import sleep
from rotary_class import RotaryEncoder
from pylms.server import Server
from pylms.player import Player
import textwrap

#sc = Server(hostname="192.168.0.211", port=9090, username="user", password="password")
hostIP = "192.168.0.211"	# Change to the IP Address of your Logitech Media Server (LMS)
sc = Server(hostname=hostIP, port=9090)	# used for volume and play/pause
scNP = Server(hostname=hostIP, port=9090)	# used only to get Now Playing cover.jpg

sleep(60)     # allow time for LMS to start, otherwise get ConnectionError 111
sc.connect()
scNP.connect()
# insert MAC address here from LMS/Settings/Information
player_id ="b8:27:eb:93:bb:81"    # miniz Player
sq = sc.get_player(player_id)
sqNP = scNP.get_player(player_id)  # UGLY KLUDGE! Avoids conflict with volume routine which caused bad refresh on album cover.jpg

DISPLAY = pi3d.Display.create(use_pygame=True, samples=4)
DISPLAY.set_background(0,0,0,1) #r,g,b and alpha
shader = pi3d.Shader("uv_flat")
CAMERA = pi3d.Camera(is_3d=False)

# Radio Dial Sprites
radio_needle = pi3d.ImageSprite("/home/pi/miniz/textures/needle.png", shader,  w=64.0,  h=288.0,  x=0.0, y=-30.0, z=4.0)

# dial below was named miniZ_Full_simple_dial_v2_metal_ring.png in dev
radio_dial = pi3d.ImageSprite("/home/pi/miniz/textures/dial.png",  shader,  w=320.0,  h=320.0,  x=0.0, y=-30.0, z=6.0) 

# Clock Face Sprites
clock_face = pi3d.ImageSprite("/home/pi/miniz/textures/clock_face.png",  shader,  w=320.0,  h=320.0,  x=0.0, y=-30.0, z=6.0)
clock_hour = pi3d.ImageSprite("/home/pi/miniz/textures/clock_hour_hand.png", shader,  w=32.0,  h=176.0,  x=0.0, y=-30.0, z=4.0)
clock_min  = pi3d.ImageSprite("/home/pi/miniz/textures/clock_minute_hand.png", shader,  w=16.0,  h=156.0,  x=0.0, y=-30.0, z=4.0)

global myFont
# colors
gold=(233,215,127) # RGB Values
white=(1,1,1)
black=(0,0,0)
blue=(0,0,255)

myFont = pi3d.Font("/home/pi/miniz/fonts/DubbaDubbaNF.ttf", gold, font_size = 30)   #load ttf font and set the font color to gold


# Define GPIO inputs for Tuning/Menu Select
TUNE_A = 13	# Pin xx CW / Dial UP
TUNE_B = 12	# Pin xx CCW / Dial Down
TUNE_BUTTON = 6	# Pin x  Switch 

# Define GPIO inputs for Volume 
VOLUME_A = 27
VOLUME_B = 23
# VOLUME Button is used on Pimoroni On Off SHIM 
# Defined here to complete callback; not used in routine
VOLUME_BUTTON = 4

degrees =  57
prev_degrees = 0
station_cmd = 'favorites playlist play item_id:'
increment = 1
screen_num = 1
radio_needle_rot = degrees
start_time = time.time()
curr_album  = None
prev_album = curr_album
# format below is degrees:fav_number
# see separate guide to LMS for setting up favorites in https://github.com/thisoldgeek/miniz
favs = {82:0,57:1,30:2,8:3,352:4,333:5}

# This is the event callback routine to handle tune knob events
def tune_knob_event(event):
 handle_tune_event(event)

 return

# This is the event callback routine to handle volume knob events
def volume_knob_event(event):
 handle_volume_event(event) 

 return

# This is the event callback routine to handle dial tune events
def handle_tune_event(event):
	global degrees
	global increment
	global radio_needle_rot
	global prev_station
	global station_req
	global start_time    # Start timer for BUTTONDOWN Event
	global buttonTime    # Variable holds how long button was held down

	if event == RotaryEncoder.CLOCKWISE:
           #print("Clockwise")
           degrees = degrees - increment
	elif event == RotaryEncoder.ANTICLOCKWISE:
           #print("Anticlockwise")
           degrees = degrees + increment
	elif event == RotaryEncoder.BUTTONDOWN:
         #  print("Button down")
		start_time = time.time()
	elif event == RotaryEncoder.BUTTONUP:
		#print("Button up")
		buttonTime = time.time() - start_time # How long was the button down?
		handle_tune_button(buttonTime)

	valid_sta = favs.get(degrees)

	if valid_sta is not None:
            prev_degrees = degrees
            tune_fav = station_cmd + str(favs[degrees]) # format station play request
            sq.request(tune_fav)

	if event == RotaryEncoder.CLOCKWISE:
		if degrees <= 0:
		    degrees = 360

	if event == RotaryEncoder.ANTICLOCKWISE:
	 	if degrees > 360:
		    degrees = 0
	#print(degrees)
	radio_needle_rot = degrees
	sleep(.1)

	return

# Action to take based on how long tune button is pressed
def handle_tune_button(buttonVal):
	global screen_num	# Current screen to display

	if  .1 <= buttonVal < 2:	# Count to 2 and release button
		sq.toggle()	# toggle pause/play
	elif 2 <= buttonVal < 4:	# Count to 4 and release button
		DISPLAY.clear()
		if   screen_num  == 1:
			screen_num = 2	#show clock
		elif screen_num == 2:
			screen_num = 3	# Show cover art
		elif screen_num == 3:
			screen_num = 1  # Back to beginning, show the radio dial
	elif 4 <= buttonVal < 8:	# Count to 8 and release button
		print ("REALLY Long Push!")
		os.system("systemctl restart squeezelite")	# Do this if sound is distorted; player will resume play on restart

	return

# This is the event callback routine to handle volume events
def handle_volume_event(event):

	if event == RotaryEncoder.CLOCKWISE:
 		sq.volume_up()
	elif event == RotaryEncoder.ANTICLOCKWISE:
 		sq.volume_down()
	# The button on volume is connected to GPIO 4 via Pimoroni On Off SHIM
	sleep(.25)

	return

# Define the switches
tune_knob = RotaryEncoder(TUNE_A,TUNE_B,TUNE_BUTTON, tune_knob_event)
volume_knob = RotaryEncoder(VOLUME_A, VOLUME_B, VOLUME_BUTTON, volume_knob_event)

# draw the sprites depending on screen_num passed from main
# this MUST be called from the Main Thread/Main while loop
def draw_sprites(mode):
	global prev_album
	global curr_album
	global curr_track
	global curr_artist
	global artist_track
	global cover_art
	global track

	if mode == 1:	# draw the radio dial sprites
		radio_needle.rotateToZ(radio_needle_rot)
		radio_needle.draw()
		radio_dial.draw()
	elif mode == 2:	# draw the clock
		minutes= time.localtime(time.time()).tm_min
		hours = time.localtime(time.time()).tm_hour
		clock_min.rotateToZ(360-(minutes*6-1))
		clock_hour.rotateToZ(360-hours*30-minutes*0.5)
		clock_face.draw()
		clock_min.draw()
		clock_hour.draw()
	elif mode == 3:	#  Get Album Cover Art
		curr_album = sqNP.get_track_album() # Sometimes 'volume' or blank will be returned in curr_album 	BUG!
		if  curr_album != prev_album:
			prev_album = curr_album
			curr_track = sqNP.get_track_title()
			curr_artist = sqNP.get_track_artist()
			format_track = textwrap.wrap(curr_track, width=20)

			fret = os.system("wget -O /home/pi/miniz/textures/cover.jpg http://"+hostIP+":9000/music/current/cover.jpg?player="+player_id)

			if fret == 0:	# fret contains return code from wget; sometimes you get a 404, "Not Found" on cover.jpg
				im = Image.open("/home/pi/miniz/textures/cover.jpg")
				tex = pi3d.Texture(im)
				cover_art = pi3d.ImageSprite(tex, shader, w=320, h=320, x=0.0, y=-30.0, z=6.0)
				cover_art.draw()
				artist = pi3d.String(camera=CAMERA, is_3d=False, font=myFont, string=curr_artist,  x=0, y=-30, z=1.0)
				artist.set_shader(shader)
				artist.draw()
				track = pi3d.String(camera=CAMERA, is_3d=False, font=myFont, string=curr_track,  x=0, y=-80, z=1.0)
				track.set_shader(shader)
				track.draw()
			else:
				im = Image.open("/home/pi/miniz/textures/default_cover.png")
				tex = pi3d.Texture(im)
				cover_art = pi3d.ImageSprite(tex, shader, w=320, h=320, x=0.0, y=-30.0, z=6.0)
				cover_art.draw()
				artist = pi3d.String(camera=CAMERA, is_3d=False, font=myFont, string=curr_artist,  x=0, y=-30, z=1.0)
				artist.set_shader(shader)
				artist.draw()
				track = pi3d.String(camera=CAMERA, is_3d=False, font=myFont, string=curr_track,  x=0, y=-80, z=1.0)
				track.set_shader(shader)
				track.draw()
		elif curr_album ==  prev_album:
			cover_art.draw()
			track.draw()

	return


while DISPLAY.loop_running():
  draw_sprites(screen_num)
  sleep(.2)
