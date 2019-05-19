import RPi.GPIO as GPIO
import time

#Definition of  pin 
IN1 = 20
IN2 = 21
IN3 = 19
IN4 = 26
ENA = 16
ENB = 13

#Definition of button
key = 8

#Definition of ultrasonic module pin
EchoPin = 0
TrigPin = 1

#Definition of servo pin
ServoPin = 23

#Set the GPIO port to BCM encoding mode.
GPIO.setmode(GPIO.BCM)

#Ignore warning information
GPIO.setwarnings(False)

#Motor pins are initialized into output mode
#Key pin is initialized into input mode
#Ultrasonic pin initialization
def init():
    global pwm_servo
    GPIO.setup(key,GPIO.IN)
    GPIO.setup(ServoPin, GPIO.OUT)
    GPIO.setup(EchoPin,GPIO.IN)
    GPIO.setup(TrigPin,GPIO.OUT)
    
    pwm_servo = GPIO.PWM(ServoPin, 50)
    pwm_servo.start(0)


#Button detection
def key_scan():
    while GPIO.input(key):
         pass
    while not GPIO.input(key):
         time.sleep(0.01)
         if not GPIO.input(key):
             time.sleep(0.01)
         while not GPIO.input(key):
             pass
                
#Ultrasonic function
def distance_test():
    GPIO.output(TrigPin,GPIO.HIGH)
    time.sleep(0.000015)
    GPIO.output(TrigPin,GPIO.LOW)
    while not GPIO.input(EchoPin):
        pass
    t1 = time.time()
    while GPIO.input(EchoPin):
        pass
    t2 = time.time()
    print("distance is %d " % (((t2 - t1)* 340 / 2) * 100))
    time.sleep(0.01)
    return ((t2 - t1)* 340 / 2) * 100
    
#The servo rotates to the specified angle
def servo_appointed_detection(pos):
    for i in range(18):
        pwm_servo.ChangeDutyCycle(2.5 + 10 * pos/180)    


time.sleep(2)

#The try/except statement is used to detect errors in the try block.
#the except statement catches the exception information and processes it.
try:
    init()
    # key_scan()
    servo_appointed_detection(0)
    distance_test()
    time.sleep(2)
    servo_appointed_detection(90)
    distance_test()
    time.sleep(2)
    servo_appointed_detection(160)
    distance_test()
    time.sleep(2)
    servo_appointed_detection(90)
    distance_test()
    time.sleep(2)
       
except KeyboardInterrupt:
    pass

GPIO.cleanup()
