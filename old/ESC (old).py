# -*- coding: utf-8 -*-
# ESC.py
# by Ryan Evans

from gpiozero import Servo
#import RPi.GPIO as GPIO
import time

ESC_pin = 3

initial_value = None
min_pulse_width = 1100e-6 #microseconds
max_pulse_width = 1900e-6 #microseconds
frame_width = 1/400 #1/Hz

servo = Servo(ESC_pin,initial_value,min_pulse_width,max_pulse_width,frame_width)

print('1 is max forward, -1 is max reverse')
while True:
	servo.value = float(input('Enter duty cycle as a decimal between -1 and 1: '))
	print('Selected Duty Cycle: ' + str(servo.value*100) + '%')
	print('Pulse Width Signal: ' + str(int(servo.pulse_width*1e6)))

