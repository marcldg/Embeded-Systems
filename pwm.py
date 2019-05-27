import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

led = 4
GPIO.setup(led, GPIO.OUT)

trig = 23
echo = 25
GPIO.setup(trig, GPIO.OUT)
GPIO.setup(echo,GPIO.IN)
GPIO.output(trig, False)

def checkdist():
    GPIO.output(trig, True)
    time.sleep(0.00001)
    GPIO.output(trig, False)
    t1 = time.time()
    t2 = time.time()
    while GPIO.input(echo) == 0:
        t1 = time.time()
    while GPIO.input(echo) == 1:
        t2 = time.time()
    distance = (t2-t1)*34300/2
    return distance


pwm = GPIO.PWM(led, 80)

pwm.start(0)
try:
    while True:
        distance = checkdist()
        print("distance = %.1f cm" % distance)
        time.sleep(1)
        if   45<checkdist()<50:
            pwm.ChangeDutyCycle(10)
        elif 40<checkdist()<45:
            pwm.ChangeDutyCycle(20)
        elif 35<checkdist()<40:
            pwm.ChangeDutyCycle(30)
        elif 30<checkdist()<35:
            pwm.ChangeDutyCycle(40)
        elif 25<checkdist()<30:
            pwm.ChangeDutyCycle(60)
        elif 20<checkdist()<25:
            pwm.ChangeDutyCycle(70)
        elif 15<checkdist()<20:
            pwm.ChangeDutyCycle(80)
        elif 10<checkdist()<15:
            pwm.ChangeDutyCycle(90)
        elif 5<checkdist()<10:
            pwm.ChangeDutyCycle(100)
        else:
            pwm.ChangeDutyCycle(0)
except KeyboardInterrupt:
	pass

pwm.stop()

GPIO.cleanup()