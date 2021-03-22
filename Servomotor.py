from RPi.GPIO import *
from time import *
setmode(BOARD)
setwarnings(False)
setup(3,OUT)
pwm=PWM(3,50)#3 is the special board pin used for pulse width modulation, 50 is frequency
pwm.start(0)#preseting the serevo motor to 0degree
def SetAngle(angle):
    duty = (angle/18) + 2
    output(3,True)
    pwm.ChangeDutyCycle(duty)
    sleep(1)
    output(3,False)
    pwm.ChangeDutyCycle(0)
while True:
    for i in range(0,90,10):
        SetAngle(i)
        sleep(1)

    #SetAngle(360)
pwm.stop()
cleanup();
