import time
import RPi.GPIO as GPIO
import Pyro.core

movement  = Pyro.core.getProxyForURI("PYRONAME://robotmovement");
#movement.right(100)


GPIO.setmode(GPIO.BOARD)

#GPIO_TRIGGER = 23;
#GPIO_ECHO = 24;
#GPIO_TRIGGER = 21;
#GPIO_ECHO = 22
#print "Ultrasonic Measurement"

#GPIO.setup(21, GPIO.OUT)
#GPIO.setup(22, GPIO.IN)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(5, GPIO.IN)
GPIO.setup(23, GPIO.OUT) #Trigger
GPIO.setup(24, GPIO.IN) #Echo ultra1


GPIO.output(3, False)
GPIO.output(23, False)
time.sleep(0.5)
#GPIO.output(21, False)
#time.sleep(0.5)

while True:
#	GPIO.output(GPIO_TRIGGER, False)
#	time.sleep(0.5)

	GPIO.output(23,True)
	GPIO.output(3,True)
#	GPIO.output(21,True)
	time.sleep(0.00001)
#	time.sleep(0.01)
	GPIO.output(23,False)
	GPIO.output(3,False)
#	GPIO.output(21,False)
	start = time.time()

#	GPIO.output(21,True)
#	time.sleep(0.00001)
#	GPIO.output(21,False)
#	start = time.time()

	while GPIO.input(5)==0:
#		 print "input 24"
		 start = time.time()
	while GPIO.input(5)==1:
#		 print "stop 24"
		 stop = time.time()
	while GPIO.input(24)==0:
#		 print "start 22"
		 start2 = time.time()
	while GPIO.input(24)==1:
#		 print "stop 22"
		 stop2 = time.time()

	elapsed  = stop - start
	elapsed2 = stop2 - start2
	
	distance = elapsed * 34000
	distance = distance / 2

	distance2 = elapsed2 * 34000
	distance2 = distance2/2

	if distance < 10:
		 movement.netral(0)

	if distance2 < 10 :
         	 movement.netral(0)

	if distance > 10:	
		print "distance : %.1f" % distance

	if distance > 10:
		print "distance2 : %.1f" % distance2
GPIO.cleanup()

