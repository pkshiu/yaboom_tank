import RPi.GPIO as GPIO
import time
import signal
import atexit

atexit.register(GPIO.cleanup)

# This is the sonar servo
servopin=23

# this is camera horizontal servo
servopin=11

# this is camera vertical servo
# THIS IS NOT WORKING
servopin=9

#The servo rotates to the specified angle
def servo_appointed_detection(pos):
    for i in range(18):
        pwm_servo.ChangeDutyCycle(2.5 + 10 * pos/180)    

def test_servo():
    servo_appointed_detection(0)
    time.sleep(2)
    servo_appointed_detection(90)
    time.sleep(2)
    servo_appointed_detection(160)
    time.sleep(2)
    servo_appointed_detection(90)
    time.sleep(2)

GPIO.setmode(GPIO.BCM)
GPIO.setup(servopin,GPIO.OUT,initial=False)
pwm_servo=GPIO.PWM(servopin,50)
pwm_servo.start(0)
time.sleep(2)
test_servo()
GPIO.cleanup()
exit(0)

while(True):
    for i in range(0,180,10):
        pwm_servo.ChangeDutyCycle(12.5-5*i/360)
        time.sleep(1)
    for i in  range(0,180,10):
        pwm_servo.ChangeDutyCycle(7.5-5*i/360)
        time.sleep(1)
