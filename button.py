
import os
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)


while True:
	input_state = GPIO.input(18)
	if input_state == False:
		os.system('omxplayer /home/pi/Downloads/dongdongdong.mp3')
