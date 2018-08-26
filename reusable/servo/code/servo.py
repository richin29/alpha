from __future__ import division
import time
import Adafruit_PCA9685

SERVO_BASE = 150  # Min pulse length out of 4096
SERVO_FACTOR = 2.5 # (600-SERVO_BASE)/180

class Servo():
	def __init__(self):
		# Initialise the PCA9685 using the default address (0x40).
		self.pwm = Adafruit_PCA9685.PCA9685()
		self.pwm.set_pwm_freq(60)

	def SetServoAngle(self, channel, angle):
		if angle >= 0 and angle <= 180:
			width = (int)(SERVO_BASE + (angle * SERVO_FACTOR))
			self.pwm.set_pwm(channel, 0, width)
