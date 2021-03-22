import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
IR=40
GPIO.setup(IR, GPIO.IN)
while True:
    a=GPIO.input(IR)
    print (a)
    time.sleep(1)
    if a==0:
        print("Object is detected")
        time.sleep(1)
    else:
        print("Object is not detected")
        
