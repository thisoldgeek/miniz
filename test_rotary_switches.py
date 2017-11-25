#!/usr/bin/env python
#
# Raspberry Pi Rotary Test Encoder Class
# $Id: test_rotary_switches.py,v 1.4 2014/01/31 14:06:26 bob Exp $
#
# Author : Bob Rathbone
# Site   : http://www.bobrathbone.com
#
# This class uses standard rotary encoder with push switch
#

import sys
import time
from rotary_class import RotaryEncoder




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


# This is the event callback routine to handle left knob events
def tune_knob_event(event):
	handle_event(event,"Tune knob")	
	return

# This is the event callback routine to handle right knob events
def vol_knob_event(event):
	handle_event(event,"Volume knob")	
	return

# This is the event callback routine to handle events
def handle_event(event, name):
	if event == RotaryEncoder.CLOCKWISE:
		print (name, "Clockwise event =", RotaryEncoder.CLOCKWISE)
	elif event == RotaryEncoder.ANTICLOCKWISE:
		print (name, "Anticlockwise event =", RotaryEncoder.BUTTONDOWN)
	elif event == RotaryEncoder.BUTTONDOWN:
		print (name, "Button down event =", RotaryEncoder.BUTTONDOWN)
	elif event == RotaryEncoder.BUTTONUP:
		print (name, "Button up event =", RotaryEncoder.BUTTONUP)
	return

# Define the left and right knobs
tuneknob = RotaryEncoder(TUNE_A,TUNE_B,TUNE_BUTTON,tune_knob_event)
volknob = RotaryEncoder(VOLUME_A,VOLUME_B,VOLUME_BUTTON,vol_knob_event)

# Wait for events
while True:
	time.sleep(0.5)

# End of program

