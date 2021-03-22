import time
from RPi.GPIO import *
setmode(BOARD)
setup(38, OUT)
setup(40, OUT)
output(38, False)
output(40, False)
for i in range(1,10):
    if i%2==0:
        output(40, True)
        time.sleep(2)
        output(40, False)
    if i%2!=0:
        output(38, True)
        time.sleep(2)
        output(38, False)
output(38, False)
output(40, False)
