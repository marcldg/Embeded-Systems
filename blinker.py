import RPi.GPIO as GPIO
import time

first = True

if(first):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(11, GPIO.OUT)
    first = False

try:
    while 1:

        GPIO.output(11, GPIO.HIGH)
        time.sleep(0.25)
        GPIO.output(11, GPIO.LOW)
        time.sleep(0.25)
except KeyboardInterrupt:
        GPIO.cleanup()