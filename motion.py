import os
import time
import RPi.GPIO as GPIO
import subprocess

GPIO.setmode(GPIO.BCM)
GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_UP)

isRan = False
isRan2 = False

rebootChange = False

while True:
	input_state = GPIO.input(15)
	if input_state == False and isRan == False:
		print('On')
		#time.sleep(180)
		os.system('sudo motion -c /home/pi/.motion/motion.conf &')
		time.sleep(2)
		rebootChange = True
		isRan = True
		isRan2 = False
	if input_state == True and isRan2 == False:
		print('off')
		time.sleep(2)
		if rebootChange == True:
			return_code = subprocess.call(['sudo', 'reboot'])
			time.sleep(2)
			rebootChange = False
			isRan = False
			isRan2 = True
