import threading
import time
import RPi.GPIO as GPIO
import Pyro.core

class UltraSonic(threading.Thread):

	def __init__(self,counter):
		threading.Thread.__init__(self)
		self.movement = Pyro.core.getProxyForURI("PYRONAME://robotmovement");
		GPIO.setmode(GPIO.BOARD)

		#GPIO.setup(3, GPIO.OUT)#trigger
		#GPIO.setup(5, GPIO.IN)#echo
		GPIO.setup(11, GPIO.OUT)#trigger
		GPIO.setup(12, GPIO.IN)#echo
		#GPIO.setup(21, GPIO.OUT)#trigger
		#GPIO.setup(22, GPIO.IN)#echo
		GPIO.setup(23, GPIO.OUT)#trigger
		GPIO.setup(24, GPIO.IN)#echo

	def start_thread(self):
		self.counter = True
	def stop(self):
		self.counter=False
	def run(self):
		#GPIO.output(3, False)
		GPIO.output(11, False)
		#GPIO.output(21, False)
		GPIO.output(23, False)
		#time.sleep(0.5)

		while self.counter:
#			print "loop"
# 	        GPIO.output(3,True)
#       	time.sleep(0.00001)
#	        GPIO.output(3,False)
#       	start = time.time()

#         	while GPIO.input(5)==0:
#               	start = time.time()
#	        while GPIO.input(5)==1:
#               	stop = time.time()

#         	elapsed = stop - start
#         	distance = elapsed * 34000
#         	distance = distance/2


#	        if distance < 10 :
#       	        movement.right(0)

#        	print "Distance : %.if" % distance

		        GPIO.output(23,True)
	         	time.sleep(0.00001)
		        GPIO.output(23,False)
	        	start2 = time.time()

		        while GPIO.input(24)==0:
	        	       start2 = time.time()
		        while GPIO.input(24)==1:
	        	       stop2 = time.time()

		        elapsed2 = stop2 - start2

	         	distance2 = elapsed2 * 34000
	         	distance2 = distance2/2

		        if distance2 < 100 :
	                	self.movement.berhenti(0)
	         	if distance2 < 10 :
	                	self.movement.backward(0)
	                	self.movement.berhenti(0)

	         	print "Distance2 : %.if" % distance2
		  	#GPIO.output(21,True)
	         	#time.sleep(0.00001)
	         	#GPIO.output(21,False)
	         	#start3 = time.time()

	         	#while GPIO.input(22)==0:
	                #	start3 = time.time()
	         	#while GPIO.input(22)==1:
	                #	stop3 = time.time()

	         	#elapsed3 = stop3 - start3

	         	#distance3 = elapsed3 * 34000
	         	#distance3 = distance3/2

	         	#if distance3 < 100 :
	                #	self.movement.berhenti(0)
	         	#if distance3 < 10:
	                #	self.movement.forward(0)
	  		#	self.movement.berhenti(0)

	         	#print "Distance3 : %.if" % distance3

	         	GPIO.output(11,True)
	         	time.sleep(0.00001)
	         	GPIO.output(11,False)
	         	start4 = time.time()

	         	while GPIO.input(12)==0:
	                	start4 = time.time()
	         	while GPIO.input(12)==1:
	                	stop4 = time.time()

	         	elapsed4 = stop4 - start4

	         	distance4 = elapsed4 * 34000
		 	distance4 = distance4/2

	         	if distance4 < 10 :
	                	self.movement.left(0)

	         	print "Distance4 : %.if" % distance4

