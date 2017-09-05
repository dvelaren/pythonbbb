import time
import Adafruit_BBIO.PWM as PWM

PWM.start("USR0", 0)
PWM.start("USR1", 0)
PWM.start("USR2", 0)
PWM.start("USR3", 0)

while True:
	for i in range(0,100,1):
		PWM.set_duty_cycle("USR0", i)
		PWM.set_duty_cycle("USR1", i)
		PWM.set_duty_cycle("USR2", i)
		PWM.set_duty_cycle("USR3", i)
		time.sleep(.02)
