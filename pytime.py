#Lib import
import time
import Adafruit_BBIO.GPIO as GPIO

#Constants
BLINKONTIME = 1
BLINKOFFTIME = 2

#Setup
#->I/O config
GPIO.setup("USR0", GPIO.OUT)
GPIO.setup("USR1", GPIO.OUT)
GPIO.setup("USR2", GPIO.OUT)
GPIO.setup("USR3", GPIO.OUT)
#->I/O cleaning
GPIO.output("USR0", GPIO.LOW)
GPIO.output("USR1", GPIO.LOW)
GPIO.output("USR2", GPIO.LOW)
GPIO.output("USR3", GPIO.LOW)
#Refresh last time
lastTime = time.clock()

#Execution
while True:
	print time.clock() - lastTime
	if time.clock() - lastTime <= BLINKONTIME:
		GPIO.output("USR0", GPIO.HIGH)
		GPIO.output("USR1", GPIO.HIGH)
                GPIO.output("USR2", GPIO.HIGH)
                GPIO.output("USR3", GPIO.HIGH)
	elif  time.clock() - lastTime > BLINKONTIME and time.clock() - lastTime < BLINKOFFTIME:
                GPIO.output("USR0", GPIO.LOW)
                GPIO.output("USR1", GPIO.LOW)
                GPIO.output("USR2", GPIO.LOW)
                GPIO.output("USR3", GPIO.LOW)
	else:
		lastTime = time.clock()
