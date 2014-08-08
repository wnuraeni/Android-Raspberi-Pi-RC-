import time
import RPi.GPIO as GPIO
import Pyro.core

movement  = Pyro.core.getProxyForURI("PYRONAME://robotmovement");
#movement.right(100)


GPIO.setmode(GPIO.BOARD)

GPIO_TRIGGER = 23
GPIO_ECHO = 24

print "Ultrasonic Measurement"

GPIO.setup(GPIO_TRIGGER, GPIO.OUT) #Trigger
GPIO.setup(GPIO_ECHO, GPIO.IN) #Echo

    

GPIO.output(GPIO_TRIGGER, False)
time.sleep(0.5)

GPIO.output(GPIO_TRIGGER,True)
time.sleep(0.00001)
GPIO.output(GPIO_TRIGGER,False)
#start = time.time()
while GPIO.input(GPIO_ECHO)==0:
 start = time.time()

while GPIO.input(GPIO_ECHO)==1:
 stop = time.time()

elapsed = stop-start

distance = elapsed * 34000
distance = distance / 2

if distance < 10:
	movement.netral(0)

print "Distance : %.1f" % distance

GPIO.cleanup()
