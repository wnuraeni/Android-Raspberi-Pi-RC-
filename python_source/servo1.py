import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(7,GPIO.OUT)
#GPIO.setup(11,GPIO.OUT)

p = GPIO.PWM(7,50)
p.start(7.5)
#q = GPIO.PWM(11,50)
#q.start(11,8)
try:
	while True:
		GPIO.output(7,1)
		time.sleep(0.0015)
		GPIO.output(7,0)
		#GPIO.output(11,1)
		#time.sleep(0.0015)
		#GPIO.output(11,0)
		
		p.ChangeDutyCycle(0.5)
		time.sleep(1)
		p.ChangeDutyCycle(5.5)
		time.sleep(1)
		#q.ChangeDutyCycle(0.5)
		#time.sleep(1)
		#q.ChangeDutyCycle(5.5)
		#time.sleep(1)
		#p.ChangeDutyCycle(0.5)
		#time.sleep(1)
		
except KeyboardInterrupt:
	GPIO.cleanup()

