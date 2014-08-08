import Rpi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)

frequencyHertz = 50
pwm = GPIO.PWM(11, frequenyHertz)

leftPosition = 0.75
rightPosition = 2.5
middlePosition = (rightPosition - leftPosition) / 2 + leftPosition

position = [leftPosition, middlePosition, rightPosition, middlePosition]
msPerCycle = 1000 / frequencyHertz

for i in range(2):
	for position in positionList:
		dutyCuclePercentage = position * 100 / msPerCycle
		print "Position: " + str(position)
		print "Duty Cycle: " + str(dutyCyclePercentage) + "%"
		print ""
		pwm.start(dutyCyclePercentage)
		time.sleep(.5)

pwm.stop()
GPIO.cleanup()
