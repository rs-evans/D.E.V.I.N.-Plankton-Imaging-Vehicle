# -*- coding: utf-8 -*-
# ESC.py
# by Ryan Evans

import pigpio
sudo pigpiod

# Connect ESC white wire to GPIO #27
ESC_pin = 27

# Create instance of the pi class
gpio = pigpio.pi()
gpio.set_mode(ESC_pin,pigpio.OUTPUT)

# Send 1500 ms to the ESC to initialize
gpio.set_servo_pulsewidth(ESC_pin,1500)

# Request input from user
print('1 is max forward, -1 is max reverse')
while True:
	duty = float(input('Enter duty cycle as a decimal between -1 and 1: '))
	pulse_width = 1500 + 400*duty
	gpio.set_servo_pulsewidth(ESC_pin,pulse_width)
	print('Selected Duty Cycle: ' + str(duty*100) + '%')
	print('Pulse Width Signal: ' + str(int(pulse_width)))

