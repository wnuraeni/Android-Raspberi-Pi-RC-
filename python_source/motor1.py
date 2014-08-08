import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(7,GPIO.OUT)
#GPIO.setup(11,GPIO.OUT)

#p = GPIO.PWM(7,50)
#p.start(7.5)
#q = GPIO.PWM(11,50)
#q.start(11,8)

def clockwise():
 i=0
 p = GPIO.PWM(7,50)
 p.start(7.5)
 #while (i<10):
 GPIO.output(7,1)
 time.sleep(0.0015)
 GPIO.output(7,0)
 p.ChangeDutyCycle(5.5)
 time.sleep(1)
 # p.ChangeDutyCycle(20.5)
  #time.sleep(1)
  #i+=1

def counter_clockwise():
 i=0
 p2 = GPIO.PWM(7,50)
 p2.start(7.5)
 #while (i<10):
 GPIO.output(7,0)
 time.sleep(0.0015)
 GPIO.output(7,1)
 # p.ChangeDutyCycle(5.5)
  #time.sleep(1)
 p2.ChangeDutyCycle(20.5)
 time.sleep(1)
  #i+=1
try:
	while True:
		cmd = raw_input("Command, f/r 0..9, E.g f5 :")
		direction = cmd[0]
		if direction == "f":
		 clockwise()
		else:
		 counter_clockwise()
		speed = int(cmd[1])*11
		#GPIO.output(7,1)
		#time.sleep(0.0015)
		#GPIO.output(7,0)
		#GPIO.output(11,1)
		#time.sleep(0.0015)
		#GPIO.output(11,0)
		
		#p.ChangeDutyCycle(0.5)
		#time.sleep(1)
		#p.ChangeDutyCycle(5.5)
		#time.sleep(1)
		#q.ChangeDutyCycle(0.5)
		#time.sleep(1)
		#q.ChangeDutyCycle(5.5)
		#time.sleep(1)
		#p.ChangeDutyCycle(0.5)
		#time.sleep(1)
		
except KeyboardInterrupt:
	GPIO.cleanup()

