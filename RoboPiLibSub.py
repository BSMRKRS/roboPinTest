import sys
import time

INPUT = 0

def servoWrite(x, y):
	print("RoboPiLib failed to initialize. Motor " + str(x) + " would be moving: " + str(y))

def pinMode(x, y):
	print("RoboPiLIb failed to initialize. Digital Sensor " + str(x) + " would be getting input: " + str(y))

def digitalRead(x):
	print("RoboPiLIb failed to initialize. Ateempting to read sensor: " + str(x))
	return(1)
	
def analogRead(x):
	print("RoboPiLIb failed to initialize. Ateempting to read sensor: " + str(x))
	return(1)
	
def RoboPiInit(x, y):
	print("RoboPiLIb failed to initialize.")