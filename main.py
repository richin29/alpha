from reusable.servo.code.servo import *

print('Moving servo on channel 0, press Ctrl-C to quit...')
while True:
	servo1 = Servo()
    # Move servo on channel O between extremes.
	servo1.SetServoAngle(0, 0)
	time.sleep(1)
	servo1.SetServoAngle(0, 180)
	time.sleep(1)
