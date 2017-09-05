import Adafruit_BBIO.GPIO as GPIO
import time

ONDELAY = 2.5
OFFDELAY = 1

GPIO.setup("USR0", GPIO.OUT)
GPIO.setup("USR1", GPIO.OUT)
GPIO.setup("USR2", GPIO.OUT)
GPIO.setup("USR3", GPIO.OUT)

while True:
	GPIO.output("USR0", GPIO.HIGH)
	GPIO.output("USR1", GPIO.HIGH)
	GPIO.output("USR2", GPIO.HIGH)
	GPIO.output("USR3", GPIO.HIGH)
	time.sleep(ONDELAY)
	GPIO.output("USR0", GPIO.LOW)
	GPIO.output("USR1", GPIO.LOW)
	GPIO.output("USR2", GPIO.LOW)
	GPIO.output("USR3", GPIO.LOW)
	time.sleep(OFFDELAY)
