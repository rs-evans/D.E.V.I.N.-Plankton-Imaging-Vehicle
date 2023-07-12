# -*- coding: utf-8 -*-
# camera.py
# by Ryan Evans

import picamera2
from io import BytesIO
from time import sleep

camera = picamera2.Picamera2()
stream = BytesIO()

camera.start_preview()
sleep(2)

camera.capture(stream, 'jpeg')
