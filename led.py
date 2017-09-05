#Library imports
import Adafruit_BBIO.GPIO as GPIO	#GPIO Library
import time				#time Library (for delays)

#Constants
ONDELAY = 2.5
OFFDELAY = 1

#Setup
#->I/O Pin Configuration
GPIO.setup("USR0", GPIO.OUT)
GPIO.setup("USR1", GPIO.OUT)
GPIO.setup("USR2", GPIO.OUT)
GPIO.setup("USR3", GPIO.OUT)

#Execution
while True:
	#Turn ON LEDs
	GPIO.output("USR0", GPIO.HIGH)
	GPIO.output("USR1", GPIO.HIGH)
	GPIO.output("USR2", GPIO.HIGH)
	GPIO.output("USR3", GPIO.HIGH)
	#Delay
	time.sleep(ONDELAY)
	#Turn OFF LEDs
	GPIO.output("USR0", GPIO.LOW)
	GPIO.output("USR1", GPIO.LOW)
	GPIO.output("USR2", GPIO.LOW)
	GPIO.output("USR3", GPIO.LOW)
	#Delay
	time.sleep(OFFDELAY)
