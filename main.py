from reusable.servo.code.servo import *
import random

INDEX_FINGER = 0
MIDDLE_FINGER = 1
RING_FINGER = 2
LITTLE_FINGER = 3
MAX_NUM_FINGERS = 4

def IndexFingerOpen(servo_object):
	servo_object.SetServoAngle(INDEX_FINGER, 20)

def IndexFingerClose(servo_object):
	servo_object.SetServoAngle(INDEX_FINGER, 120)
	
def MiddleFingerOpen(servo_object):
	servo_object.SetServoAngle(MIDDLE_FINGER, 0)

def MiddleFingerClose(servo_object):
	servo_object.SetServoAngle(MIDDLE_FINGER, 120)
	
def RingFingerOpen(servo_object):
	servo_object.SetServoAngle(RING_FINGER, 10)

def RingFingerClose(servo_object):
	servo_object.SetServoAngle(RING_FINGER, 60)
	
def LittleFingerOpen(servo_object):
	servo_object.SetServoAngle(LITTLE_FINGER, 50)

def LittleFingerClose(servo_object):
	servo_object.SetServoAngle(LITTLE_FINGER, 120)
	
def Paper(servo_object):
	print "Paper"
	IndexFingerOpen(servo_object)
	MiddleFingerOpen(servo_object)
	RingFingerOpen(servo_object)
	LittleFingerOpen(servo_object)

def Rock(servo_object):
	print "Rock"
	IndexFingerClose(servo_object)
	MiddleFingerClose(servo_object)
	RingFingerClose(servo_object)
	LittleFingerClose(servo_object)

def Scissor(servo_object):
	print "Scissor"
	IndexFingerOpen(servo_object)
	MiddleFingerOpen(servo_object)
	RingFingerClose(servo_object)
	LittleFingerClose(servo_object)
INDEX_FINGER = 0
MIDDLE_FINGER = 1
RING_FINGER = 2
LITTLE_FINGER = 3
def Throw(servo_object, move):
	if (move == 0):
		Rock(servo_object)
	elif (move == 1):
		Paper(servo_object)
	else:
		Scissor(servo_object)
		

print('Moving servo on channel 0, press Ctrl-C to quit...')
while True:
	servo = Servo()
	# Move servo on channel O between extremes.
	#options_list = [Rock, Paper, Scissor]
	#raw_input("Hit Enter to  Start...")
	
	random_move = random.randint(0,2)
	print random_move
	#options_list[random_throw](servo)
	Throw(servo, random_move)
	"""Scissor(servo)
	time.sleep(1)
	Paper(servo)"""
	time.sleep(5)
	"""if (random_move == 0):
		Paper(servo)
	elif (random_move == 1):
		Paper(servo)
	else:
		Scissor(servo)"""
