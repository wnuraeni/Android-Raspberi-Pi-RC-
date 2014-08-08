import RPi.GPIO as GPIO
import time
#io.setmode(io.BCM)

#in1_pin=7
#in2_pin=17

#io.setup(in1_pin,io.OUT)
#io.setup(in2_pin,io.OUT)

def set(property, value):
 GPIO.setmode(GPIO.BOARD)
 GPIO.setup(7,GPIO.OUT)

 p = GPIO.PWM(7,50)
 p.start(7.5)

# try:
  #f = open("/sys/class/rpi-pwm/pwm0/"+property,'w')
  #f.write(value)
  #f.close()
 #except:
  #print("Error writing to:" + property+"value: "+value)

#set("delayed","0")
#set("mode","pwm")
#set("frequency","500")
#set("active","1")

def clockwise():
 GPIO.setmode(GPIO.BOARD)
 GPIO.setup(7,GPIO.OUT)
 p = GPIO.PWM(7,50)
 p.start(7.5)
 p.ChangeDutyCycle(5.5)
 time.sleep(1)
 p.ChangeDutyCycle(20.5)
 time.sleep(1)
 GPIO.output(7,1)
 time.sleep(0.0015)
 GPIO.output(7,0)
 #io.output(in1_pin, True)
 #io.output(in2_pin, False)
 
def counter_clockwise():
 GPIO.setmode(GPIO.BOARD)
 GPIO.setup(7,GPIO.OUT)
 p = GPIO.PWM(7,50)
 p.start(7.5)
 p.ChangeDutyCycle(5.5)
 time.sleep(1)
 p.ChangeDutyCycle(20.5)
 time.sleep(1)
 GPIO.output(7,1)
 time.sleep(0.0015)
 GPIO.output(7,0)
 #io.output(in1_pin, False)
 #io.output(in2_pin, True)

#clockwise()

#while True:
 #cmd = raw_input("Command, f/r 0..9, E.g f5 :")
 #direction = cmd[0]
 #if direction == "f":
  #clockwise()
 #else:
  #counter_clockwise()
 #speed = int(cmd[1])*11
 #set("duty",str(speed))

