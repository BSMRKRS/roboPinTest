import RoboPiLib as RPL

RPL.RoboPiInit("/dev/ttyAMA0",115200)
import sys
import time

sensor_pin_1 = 16
sensor_pin_2 = 17
RPL.pinMode(sensor_pin_1, RPL.INPUT)
RPL.pinMode(sensor_pin_2, RPL.INPUT)

ticks = 100000
ticksDone = 0

mtrLeft = [0, -1]
mtrRight = [1, 1]

outputLog = ["---"]

def clearText():
	print("\033c")

def allStop():
	RPL.servoWrite(0, 1500)
	RPL.servoWrite(1, 1500)
	RPL.servoWrite(0, 0)
	RPL.servoWrite(1, 0)

def motorMove(mot1, mot2):
	mtrLeftMove = float(1500 + ((float(mtrLeft[1]) * (float(mot1) / 100) * 500)))
	mtrRightMove = float(1500 + ((float(mtrRight[1]) * (float(mot2) / 100) * 500)))
	RPL.servoWrite(mtrLeft[0], int(mtrLeftMove))
	RPL.servoWrite(mtrRight[0], int(mtrRightMove))
	print("MotorLeft Moved: " + str(mtrLeftMove) + ", MotorRight Moved: " + str(mtrRightMove))
	print("Left Throttle: " + str(mot1) + "%, Right Throttle: " + str(mot2))
