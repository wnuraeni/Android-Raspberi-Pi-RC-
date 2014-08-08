#!/usr/bin/python3
import socket
import RPi.GPIO as GPIO
import time

#=====socket listen
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '192.168.0.1'
port = 8081
server.bind((host,port))
server.listen(5)
print('Listening for a client...')
client,addr = server.accept()

#=====GPIO setup
GPIO.setmode(GPIO.BOARD) #GPIO dengan BOARD numbering system
GPIO.setup(7, GPIO.OUT) #set pin yang digunakan untuk output

p = GPIO.PWM(7,50) #set pulse-width-modulation PWM dengan #frekuensi 50 untuk pin 7
p.start(7.5) #mulai PWM dengan posisi netral : 7.5

print('Accepted connection from:', addr)
client.send(str.encode('welcome to my server!'))

while True:
 data = client.recv(1024)
 p.ChangeDutyCycle(7.5) #neutral position
 time.sleep(1)

 if(bytes.decode(data)== 'exit'):
  p.stop()
  GPIO.cleanup()
  break
 else:
  #kirim pesan balik ke client
  #msg = controller.process(bytes.decode(data))
  msg = (bytes.decode(data))
  print("Received data from client:",(msg))
  #client.send(str.encode(msg))
  client.send(msg)

  #mulai gerakkan servo
  if(msg == 'f5'):
   p.ChangeDutyCycle(12.5) #180 derajat
   time.sleep(1)
   #print("forward")
  elif(msg == 'r5'):
   p.ChangeDutyCycle(2.5) #0 derajat
   time.sleep(1)
   #print("reverse")
   
print('Ending the connection')
client.send(str.encode('exit'))
client.close()
