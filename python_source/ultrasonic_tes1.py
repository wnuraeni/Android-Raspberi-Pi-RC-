import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD);

GPIO.setup(23,GPIO.OUT);
GPIO.setup(24,GPIO.IN);

GPIO.output(23,GPIO.LOW)
time.sleep(0.5)

#GPIO.output(23,True)
#time.sleep(0.01)
#GPIO.output(23,False)
i=0
signalon = 0
signaloff = 0
#GPIO.output(23,True)

while True:
	GPIO.output(23,True)
	time.sleep(0.00001)
	GPIO.output(23,False)
	while GPIO.input(24) == 0:
		
		signaloff = time.time()
		#print "off",signaloff
	while GPIO.input(24) == 1:
		
		signalon = time.time()
		#print "on",signalon

#	print signalon - signaloff
	t = signalon - signaloff; #ms
	s =  t*58.2
	if (s > 1):
		print t*58.2 ,"cm"
#	time.sleep(0.5)
