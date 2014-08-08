#!/usr/bin/env python

import RPi.GPIO as GPIO
from time import sleep
from time import time
from UltraSonic import UltraSonic
import os
import Pyro.core
import Pyro.naming

class Movement(Pyro.core.ObjBase):
    # Movement constants
    #SPEED = 200

    # Set up the GPIO
    #ultra_run = False;
	
    def _setup(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(7,GPIO.OUT)
        GPIO.setup(13,GPIO.OUT)
        GPIO.setup(15,GPIO.OUT)
        GPIO.setup(18,GPIO.OUT)
	GPIO.setup(23, GPIO.OUT)
	GPIO.setup(24, GPIO.IN)
        
	self.ultra_run = False;
        self.Motor1 = GPIO.PWM(7, 50) #kamera updown
        
        self.Motor2 = GPIO.PWM(13, 50) #majumundur
        
        self.Motor3 = GPIO.PWM(15,50) #kanankiri
	
        self.Motor4 = GPIO.PWM(18, 50) #kamera kanankiri
	

    def __init__(self):
        Pyro.core.ObjBase.__init__(self)
        self._setup()

    
#========= CAMERA MOVEMENT
    def camera_up(self, move_time):       
	for i in range(3):
		self.Motor1.start(2.5)
		sleep(.05)
	self.Motor1.ChangeDutyCycle(0)
    def camera_down(self, move_time):       
	for i in range(3):
		self.Motor1.start(11.5)
		sleep(.05)
	self.Motor1.ChangeDutyCycle(0)
    def camera_left(self, move_time):      
	for i in range(3):
		self.Motor4.start(4.5)
		sleep(.05)
	self.Motor4.ChangeDutyCycle(0)
    def camera_right(self, move_time):       
	for i in range(3):
		self.Motor4.start(10.5)
		sleep(.05)
	self.Motor4.ChangeDutyCycle(0)
    def camera_center(self, move_time):
	for i in range(3):
		self.Motor4.start(7.5)
		sleep(.05)
	self.Motor4.ChangeDutyCycle(0)	


#========== CAR MOVEMENT
    def forward(self, move_time):
        #self.Motor2.ChangeDutyCycle(5.5)
        #sleep(.05)
	#self.Motor2.ChangeDutyCycle(0)
        #self.stop()
	for i in range(3):
		self.Motor2.start(8.5)
		sleep(.05)
	self.Motor2.ChangeDutyCycle(0)
    def backward(self, move_time):
        #self.Motor2.ChangeDutyCycle(10.5)
        #sleep(.05)
	#self.Motor2.ChangeDutyCycle(0)
        #self.stop()
	for i in range(3):
		self.Motor2.start(3.5)
		sleep(.05)
	self.Motor2.ChangeDutyCycle(0)
    def berhenti(self, move_time):
	for i in range(3):
		self.Motor2.start(7.5)
		sleep(.05)
	self.Motor2.ChangeDutyCycle(0)	
	
    def left(self, move_time):
        #self.Motor3.ChangeDutyCycle(12.5)
	#sleep(move_time)
        #self.stop()
	for i in range(3):
		self.Motor3.start(12.5)
		sleep(.05)
	self.Motor3.ChangeDutyCycle(0)
    
    def right(self, move_time):
        #self.Motor3.ChangeDutyCycle(2.5)
        #sleep(move_time)
        #self.stop()
	for i in range(3):
		self.Motor3.start(2.5)
		sleep(.05)
	self.Motor3.ChangeDutyCycle(0)
    def netral(self, move_time):
	for i in range(3):
		self.Motor3.start(7.5)
		sleep(.05)
	self.Motor3.ChangeDutyCycle(0)

#================UltraSonic Movement	
    def ultrasonic_start(self,move_time):
	self.s = UltraSonic(0)
	self.s.start_thread()
	self.s.start()
    def ultrasonic_stop(self,move_time):
	self.s.stop()
	self.s.join()
	self.s = UltraSonic(0)
	self.s.stop()
	del self.s	
	     
if __name__ == "__main__":
    # Create a Pyro server and register our module with it
    Pyro.core.initServer()
    ns = Pyro.naming.NameServerLocator().getNS()
    daemon = Pyro.core.Daemon()
    daemon.useNameServer(ns)
    uri = daemon.connect(Movement(),"robotmovement")
    daemon.requestLoop()
