import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
IR=40
led=38
bz=37
GPIO.setup(IR, GPIO.IN)
GPIO.setup(led, GPIO.OUT)
GPIO.setup(bz, GPIO.OUT)
while True:
    a=GPIO.input(IR)
    print (a)
    if a==1:
        print("Object is detected")
        GPIO.output(led,True)
        GPIO.output(bz,True)
    else:
        print("Object is not detected")
        GPIO.output(led,False)
        GPIO.output(bz,False)
        
