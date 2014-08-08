#!/usr/bin/env python

import RPi.GPIO as GPIO
from time import sleep
from time import time
import os
import Pyro.core
import Pyro.naming

class Movement(Pyro.core.ObjBase):
    # Movement constants
    SPEED = 100

    # Set up the GPIO
    def _setup(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(7,GPIO.OUT)
        GPIO.setup(13,GPIO.OUT)
        GPIO.setup(15,GPIO.OUT)
        GPIO.setup(18,GPIO.OUT)

        self.Motor1 = GPIO.PWM(7, 50) #kamera updown
	self.Motor4 = GPIO.PWM(18, 50) #kamera kanankiri
	self.pUpDown = 0;
	self.pLeftRight = 0;
        self.Motor2 = GPIO.PWM(13, 50) #majumundur
        self.Motor2.start(7.5)
        self.Motor3 = GPIO.PWM(15,50) #kanankiri
	self.Motor3.start(7.5)
        

    def __init__(self):
        Pyro.core.ObjBase.__init__(self)
        self._setup()

    def stop(self):        
        self.Motor2.ChangeDutyCycle(7.5)
	self.Motor3.ChangeDutyCycle(7.5)

#========= CAMERA MOVEMENT
    def camera_up(self, move_time):  
	self.pUpDown += 0.5     
	for i in range(3):
	 self.Motor1.start(self.pUpDown)
	 sleep(.1)
	self.Motor1.ChangeDutyCycle(0)

    def camera_down(self, move_time):  
	self.pUpDown -= 0.5     
	for i in range(3):
	 self.Motor1.ChangeDutyCycle(self.pUpDown)
	 sleep(.1)
	self.Motor1.ChangeDutyCycle(0)

    def camera_left(self, move_time):   
	self.pLeftRight += 0.5;    
	for i in range(3):
	 self.Motor4.ChangeDutyCycle(self.pLeftRight)
	 sleep(.1)
 	self.Motor4.ChangeDutyCycle(0)

    def camera_right(self, move_time):  
	self.pLeftRight -= 0.5;     
	for i in range(3):
	 self.Motor4.ChangeDutyCycle(self.pLeftRight)
	 sleep(.1)
	self.Motor4.ChangeDutyCycle(0)


#========== CAR MOVEMENT
    def forward(self, move_time):
        self.Motor2.ChangeDutyCycle(5.5)
        sleep(0.5)
	self.Motor2.ChangeDutyCycle(0)
        self.stop()
    def backward(self, move_time):
        self.Motor2.ChangeDutyCycle(10.5)
        sleep(0.5)
	self.Motor2.ChangeDutyCycle(0)
        self.stop()
    
    def left(self, move_time):
        self.Motor3.ChangeDutyCycle(2.5)
	sleep(move_time)
        self.stop()
    
    def right(self, move_time):
        self.Motor3.ChangeDutyCycle(12.5)
        sleep(move_time)
        self.stop()


if __name__ == "__main__":
    # Create a Pyro server and register our module with it
    Pyro.core.initServer()
    ns = Pyro.naming.NameServerLocator().getNS()
    daemon = Pyro.core.Daemon()
    daemon.useNameServer(ns)
    uri = daemon.connect(Movement(),"robotmovement")
    daemon.requestLoop()
