import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(23, GPIO.IN)

while True:
    if GPIO.input(23) == 1: #scheinbar ist 1 in meiner schaltung AUS
         #Ausschalten
        GPIO.output(22, GPIO.LOW)

    else:
        #Einschalten
        GPIO.output(22, GPIO.HIGH)
        
#for i in range(5):
 #   GPIO.output(22, GPIO.HIGH)
  #  time.sleep(0.5)
   # GPIO.output(22, GPIO.LOW)
    #time.sleep(0.5)