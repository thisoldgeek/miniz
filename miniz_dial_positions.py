#!/usr/bin/python3

# use this program to map the radio dial to the degrees of a circle
# favorites are played when the radio needle passes over the associated degree
# this mapping occurs in dictionary named 'favs' below

import pi3d
import time
from time import sleep
from rotary_class import RotaryEncoder
# Works as of 03-03-2017 03:57PM
# Added refinements to dial: numbers, inner dial, bezel for magic eye
# 03-09-2017 05:58PM
# rot2 = -60 equals "2 o'clock" on the dial
# rot2 = 0 equals "12 o'clock" on the dial
# rot2 = 30  equals "11 o'clock" on the dial
# Thus you could have 12 radio stations/presets at 30 degree intervals around the dial

#DISPLAY = pi3d.Display.create(w=999, h=999, samples=4)
# use_pygame=True, with no w,h,x,y values yields drawing surface full screen no borders

DISPLAY = pi3d.Display.create(use_pygame=True, samples=4)
DISPLAY.set_background(0,0,0,1) #r,g,b and alpha
shader = pi3d.Shader("uv_flat")
CAMERA = pi3d.Camera(is_3d=False)

# colors
gold=(233,215,127) # RGB Values
white=(255,255,255)
black=(0,0,0)
blue=(0,0,255)

myFont = pi3d.Font("/home/pi/miniz/fonts/DubbaDubbaNF.ttf", white, font_size = 30)   #load ttf font and set the font color to blue

# Radio Dial Sprites
needle = pi3d.ImageSprite("/home/pi/miniz/textures/needle.png", shader,  w=64.0,  h=288.0,  x=0.0, y=-30.0, z=4.0)

# dial below was named miniZ_Full_simple_dial_v2_metal_ring.png in dev
backgr = pi3d.ImageSprite("/home/pi/miniz/textures/dial.png",  shader,  w=320.0,  h=320.0,  x=0.0, y=-30.0, z=6.0) 


# Define GPIO inputs for Tuning/Menu Select
PIN_A = 13	# Pin xx CW / Dial UP
PIN_B = 12	# Pin xx CCW / Dial Down
BUTTON = 6	# Pin x  Switch 

degrees =  80
prev_station = 0
station_cmd = 'favorites playlist play item_id:'
increment = 1
eye_rot = 0
needle_rot =  degrees
favs = {0:0,30:1,60:2,90:3,120:4,150:5}

# This is the event callback routine to handle events
def switch_event(event):
	global degrees
	global increment
	global needle_rot
	global prev_station
	global station_req

	if event == RotaryEncoder.CLOCKWISE:
           print("Clockwise")
           degrees = degrees - increment
	elif event == RotaryEncoder.ANTICLOCKWISE:
           print("Anticlockwise")
           degrees = degrees + increment
	#elif event == RotaryEncoder.BUTTONDOWN:
         #  print("Button down")
	#elif event == RotaryEncoder.BUTTONUP:
        #   print("Button up")
	#if degrees % 30 == 0:   # if a 30 degree increment
        #    prev_station = degrees
        #   tune_fav = station_cmd + str(favs[degrees]) # format station play request
        #    sq.request(tune_fav)
	if event == RotaryEncoder.CLOCKWISE:
		if degrees <= 0:
		    degrees = 360

	if event == RotaryEncoder.ANTICLOCKWISE:
	 	if degrees > 360:
		    degrees = 0
	print(degrees)
	needle_rot = degrees
	sleep(.2)
	return

# Define the switch
rswitch = RotaryEncoder(PIN_A,PIN_B,BUTTON,switch_event)


while DISPLAY.loop_running():
  needle.rotateToZ(needle_rot)
  needle.draw()
  backgr.draw()
  frequency = pi3d.String(camera=CAMERA, is_3d=False, font=myFont, string=str(needle_rot),  x=0, y=-90.0, z=1.0)
  frequency.set_shader(shader)
  frequency.draw()
  sleep(.05)
