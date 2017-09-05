#Lib import
import time
import Adafruit_BBIO.GPIO as GPIO

#Constants
BLINKONTIME = 1
BLINKOFFTIME = 2
ELOFF = 0
ELON = 1

#Variables
state =  ELOFF

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
print "State: ELOFF"
lastTime = time.clock()

#Execution
while True:
	if state == ELOFF:
		#Physical outputs state
		GPIO.output("USR0", GPIO.LOW)
		GPIO.output("USR1", GPIO.LOW)
		GPIO.output("USR2", GPIO.LOW)
		GPIO.output("USR3", GPIO.LOW)
		#Virtual vars state
		#Transitions questions
		if time.clock() - lastTime >= BLINKOFFTIME:
			print "State: ELON"
			state = ELON
			lastTime = time.clock()

	elif state == ELON:
                #Physical outputs state
                GPIO.output("USR0", GPIO.HIGH)
                GPIO.output("USR1", GPIO.HIGH)
                GPIO.output("USR2", GPIO.HIGH)
                GPIO.output("USR3", GPIO.HIGH)
                #Virtual vars state
                #Transitions questions
                if time.clock() - lastTime >= BLINKONTIME:
                        print "State: ELOFF"
                        state = ELOFF
                        lastTime = time.clock()

