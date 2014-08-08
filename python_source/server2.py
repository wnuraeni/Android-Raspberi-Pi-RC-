#!/usr/bin/python3
import socket
import sys
sys.path.append('/usr/lib/python3/dist-packages')
import RPi.GPIO as GPIO
import time

#====socket listen
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host=''
port = 5150
server.bind((host,port))
server.listen(5)
print('Listening for a client...')
client,addr = server.accept()

#=====GPIO setup
GPIO.setmode(GPIO.BOARD) #GPIO dengan BOARD numbering system
GPIO.setup(7, GPIO.OUT)  #set pin yg digunakan untuk output
#GPIO.setup(3, GPIO.OUT)

p = GPIO.PWM(7,50)	#set pulse-width-modulation PWM dengan #frekuensi 50 untuk pin 7
#q = GPIO.PWM(3,50)
p.start(7.5) #mulai PWM dengan posisi netral : 7.5
#q.start(3.5)

print('Accepted connection from:', addr)
client.send(str.encode('Welcome to my server!'))

while True:
 data = client.recv(1024)
 p.ChangeDutyCycle(7.5) #neutral position
 time.sleep(1)
 #q.ChangeDutyCycle(3.5)
 #time.sleep(1) 
 

 if(bytes.decode(data)=='exit'):
  p.stop()
  #q.stop()
  GPIO.cleanup()
  break 
 else:
  #kirim pesan balik ke client
  msg = (bytes.decode(data))
  print("Received data from client:", msg)
  client.send((msg))

  #mulai gerakkan servo
  if(msg == "f5"):
   p.ChangeDutyCycle(9.5) #180 derajat
   time.sleep(1)
   #print("forward")
  elif(msg == "r5"):
   p.ChangeDutyCycle(5.5) #0 derajat
   time.sleep(1)
   #print("reverse")
  #elif(msg == "q5"):
   #q.ChangeDutyCycle(12.5)
   #time.sleep(1)
   #print("right")
  #elif(msg == "w5"):
   #q.ChangeDutyCycle(2.5)
   #time.sleep(1)
   #print("left")
print('Ending the connection')
client.send(str.encode('exit'))
client.close()
