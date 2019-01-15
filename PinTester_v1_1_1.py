import sys
import time
import os
try:
	import RoboPiLib as RPL
	RPL.RoboPiInit("dev/ttyAMA0",115200)
except:
	import RoboPiLibSub as RPL
	print("ROBOPILIB HAS FAILED TO INITIALIZE! Loading substitute...")
	time.sleep(2)

#DEFINITIONS================================================================================
#LOOP BOOLEANS------------------------------------------------------------------------------
#These determine what parts of the program loop run
l1 = True
l1_1 = False
l1_2 = False
#-------------------------------------------------------------------------------------------
#STRINGS------------------------------------------------------------------------------------
l1s1 = "-----===PIN_DIAGNOSTICS===-----"
l1s2 = "v0.0.1"
l1s3 = "---"
l1s4 = "0 - Exit"
l1s5 = "1 - Test ALL pins"
l1s6 = "2 - Test a specific pin"

l1_1s1 = "---=FULL PIN TEST=---"
l1_1s2 = "Testing motors by attempting a full speed move for one second each."
l1_1s3 = "Testing sensors by displaying output for five seconds each."

l1_2s1 = "---=INDIVIDUAL PIN TESTING=---"
l1_2s2 = "---"
l1_2s3 = "0 - Back"
l1_2s4 = "1 - Test Motor"
l1_2s5 = "2 - Test Digital Sensor"
l1_2s6 = "3 - Test Analog Sensor"
l1_2s7 = "Enter a pin number: "
#-------------------------------------------------------------------------------------------
#PIN ARRAYS---------------------------------------------------------------------------------
pinArrayMotor = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
pinArraySensorset1 = [16, 17, 18, 19, 20, 21, 22, 23]
pinArraySensorset2 = [0, 1, 2, 3, 4, 5, 6, 7]
#-------------------------------------------------------------------------------------------
#===========================================================================================

#FUNCTIONS==================================================================================
#DISPLAY FUNCTIONS--------------------------------------------------------------------------
def displayTextClear():
	#os.system('clear') #Uses built-in OS function to clear the display
	os.system('cls' if os.name == 'nt' else 'clear')
#-------------------------------------------------------------------------------------------
#INPUT FUNCTIONS----------------------------------------------------------------------------
def checkInt(inptInt):
    try:
        int(inptInt)
        return True
    except ValueError:
        return False
#-------------------------------------------------------------------------------------------
#PIN CHECK FUNCTIONS------------------------------------------------------------------------
def checkPinsMotor():
	x = 0
	while (x < len(pinArrayMotor)):
		RPL.servoWrite(pinArrayMotor[x], 2000)
		print("Moving motor " + str(pinArrayMotor[x]) + "... ")
		time.sleep(1)
		RPL.servoWrite(pinArrayMotor[x], 1500)
		RPL.servoWrite(pinArrayMotor[x], 0)
		print("Done with motor " +str(pinArrayMotor[x]) + ".")
		x += 1
	print("Motor testing completed!")

def checkPinsDigital():
	x = 0
	global multiplier
	multiplier = 1
	if (os.name != 'nt'):
		multiplier = 1000
	while (x < len(pinArraySensorset1)):
		RPL.pinMode(pinArraySensorset1[x], RPL.INPUT)
		initialTime = float(time.clock() * multiplier)
		while (float(time.clock() * multiplier) < (initialTime + 4)):
			displayTextClear()
			print ("Pin " + str(pinArraySensorset1[x]) + " output: " + str(RPL.digitalRead(pinArraySensorset1[x])))
			time.sleep(0.2)
		x += 1
	print("Digital sensor testing complete!")

def checkPinsAnalog():
	x = 0
	global multiplier
	while (x < len(pinArraySensorset2)):
		initialTime = float(time.clock() * multiplier)
		while(float(time.clock() * multiplier) < (initialTime + 4)):
			displayTextClear()
			print("Pin " + str(pinArraySensorset2[x]) + " output: " + str(RPL.analogRead(pinArraySensorset2[x])))
			time.sleep(0.2)
		x += 1
	print("Analog sensor testing complete!")

def checkPin(x, y):
	global multiplier
	if (y == 0):
		RPL.servoWrite(x, 2000)
		print("Moving motor " + str(x) + "... ")
		time.sleep(1)
		RPL.servoWrite(x, 1500)
		RPL.servoWrite(x, 0)
		print("Done with motor " +str(x) + ".")
		x += 1
		print("Motor testing completed!")
	if (y == 1):
		RPL.pinMode(pinArraySensorset1[x], RPL.INPUT)
		initialTime = float(time.clock() * multiplier)
		while (float(time.clock() * multiplier) < (initialTime + 4)):
			displayTextClear()
			print ("Pin " + str(pinArraySensorset1[x]) + " output: " + str(RPL.digitalRead(pinArraySensorset1[x])))
			time.sleep(0.2)
		print("Digital sensor testing complete!")
	if (y == 2):
		initialTime = float(time.clock() * multiplier)
		while(float(time.clock() * multiplier) < (initialTime + 4)):
			displayTextClear()
			print("Pin " + str(pinArraySensorset2[x]) + " output: " + str(RPL.analogRead(pinArraySensorset2[x])))
			time.sleep(0.2)
		print("Analog sensor testing complete!")

def checkIfGivenIsGood(x, y):
	z = 0
	if (y == 0):
		while (z < len(pinArrayMotor)):
			if (x == pinArrayMotor[z]):
				return True
			z += 1
		return False
	if (y == 1):
		while (z < len(pinArraySensorset1)):
			if (x == pinArraySensorset1[z]):
				return True
			z += 1
		return False
	if (y == 2):
		while (z < len(pinArraySensorset2)):
			if (x == pinArraySensorset2[z]):
				return True
			z += 1
		return False
#-------------------------------------------------------------------------------------------
#===========================================================================================

#PROGRAM====================================================================================
#Loop 1-------------------------------------------------------------------------------------
while (l1 == True):
	displayTextClear()
	print(l1s1)
	print(l1s2)
	print(l1s3)
	print(l1s4)
	print(l1s5)
	print(l1s6)
	i1 = raw_input("")
	if (checkInt(i1) == True):
		i1 = int(i1)
	if (i1 == 0):
		l1 = False
		l1_1 = False
		l1_2 = False
	elif (i1 == 1):
		l1_1 = True
	elif (i1 == 2):
		l1_2 = True
	else:
		displayTextClear()
		print("Invalid command. Please enter a correct command...")
		time.sleep(0.75)
#-------------------------------------------------------------------------------------------
#Loop 1_1-----------------------------------------------------------------------------------
	while (l1_1 == True):
		displayTextClear()
		print(l1_1s1)
		print(l1s3)
		time.sleep(0.25)
		print(l1_1s2)
		checkPinsMotor()
		time.sleep(0.25)
		print(l1_1s3)
		checkPinsDigital()
		time.sleep(0.25)
		print(l1_1s3)
		checkPinsAnalog()

		time.sleep(0.5)
		print("Repeat?")
		print("0 - No")
		print("1 - Yes")
		i2 = raw_input("")
		if checkInt(i2) == True:
			i2 = int(i2)
		if i2 == 0:
			l1_1 = False
#-------------------------------------------------------------------------------------------
#Loop 1_2-----------------------------------------------------------------------------------
	while (l1_2 == True):
		displayTextClear()
		print(l1_2s1)
		print(l1_2s2)
		print(l1_2s3)
		print(l1_2s4)
		print(l1_2s5)
		print(l1_2s6)
		i2 = raw_input("")
		if (checkInt(i2) == True):
			i2 = int(i2)

		h = 0
		step2 = False

		if (i2 == 0):
			l1_2 = False
		elif (i2 == 1):
			h = 0
			step2 = True
		elif (i2 == 2):
			h = 1
			step2 = True
		elif (i2 == 3):
			h = 2
			step2 = True
		else:
			displayTextClear()
			print("Invalid command. Please enter a correct command...")
			time.sleep(0.75)
			step2 = False

		if (l1_2 != False and step2 == True):
			print(l1_2s7)
			i3 = raw_input("")
			if (checkInt(i3) == True):
				i3 = int(i3)
			else:
				displayTextClear()
				print("Invalid command. Please enter a correct command...")
				time.sleep(0.75)
				step2 = False
			if (checkIfGivenIsGood(i3, h) == True):
				checkPin(i3, h)
				time.sleep(0.5)
				print("Repeat?")
				print("0 - No")
				print("1 - Yes")
				i4 = raw_input("")
				if checkInt(i4) == True:
					i4 = int(i4)
				if i4 == 0:
					step2 = False
					l1_2 = False
				elif i4 == 1:
					step2 = False
				else:
					displayTextClear()
					print("Invalid command. Please enter a correct command...")
					time.sleep(0.75)
					step2 = False
			else:
				step2 = False
				print("That pin/device combination does not exist. Please try again.")
				time.sleep(0.80)

#-------------------------------------------------------------------------------------------
#===========================================================================================
