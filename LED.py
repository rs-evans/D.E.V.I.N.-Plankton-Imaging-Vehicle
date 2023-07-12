# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT
# https://learn.adafruit.com/neopixels-on-raspberry-pi/python-usage

import board
import neopixel
import time

# Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
# NeoPixels must be connected to D10, D12, D18 or D21 to work.
# Sound must be disabled to use GPIO18 AND 12. This can be done in /boot/config.txt by changing 
# "dtparam=audio=on" to "dtparam=audio=off" and rebooting.
pixel_pin = board.D12

# The number of NeoPixels
# This is for a 12-LED ring light
num_pixels = 12

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.RGBW

# bpp=4 because this is an RGBW ring light (dedicated white pixel)
pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, bpp=4, brightness=1, auto_write=False, pixel_order=ORDER
)

def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 85:
        r = int(pos * 3)
        g = int(255 - pos * 3)
        b = 0
    elif pos < 170:
        pos -= 85
        r = int(255 - pos * 3)
        g = 0
        b = int(pos * 3)
    else:
        pos -= 170
        r = 0
        g = int(pos * 3)
        b = int(255 - pos * 3)
    return (r, g, b) if ORDER in (neopixel.RGB, neopixel.GRB) else (r, g, b, 0)


def rainbow_cycle(wait):
    for j in range(255):
        for i in range(num_pixels):
            pixel_index = (i * 256 // num_pixels) + j
            pixels[i] = wheel(pixel_index & 255)
        pixels.show()
        time.sleep(wait)

while True:
    user = input("Turn LED on or off: ")

    if user == "on":
        pixels.fill((0, 0, 0, 255))
        pixels.show()
    elif user == "off":
        pixels.fill((0, 0, 0, 0))
        pixels.show()
    elif user == "max":
        pixels.fill((255, 255, 255, 255))
        pixels.show()
    elif user == "disco":
        while True:
            rainbow_cycle(0.001)  # rainbow cycle with 1ms delay per step
    else:
        print('Enter "on" or "off" only')