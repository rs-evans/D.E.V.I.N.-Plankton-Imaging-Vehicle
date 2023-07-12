# -*- coding: utf-8 -*-
# gpio_blink.py
# by Scott Kildall (www.kildall.com)
# LED is on pin 26, use a 270 Ohm resistor to ground

import RPi.GPIO as GPIO
import time

pin = 26
delay = 3 #seconds

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)

state = True

# endless loop, on/off for 1 second
while True:
	GPIO.output(pin,True)
	time.sleep(delay)
	GPIO.output(pin,False)
	time.sleep(delay)
