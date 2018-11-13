

import RPi.GPIO as GPIO
import time
import weight as w
while True:
    GPIO.setmode(GPIO.BCM)
    TRIGl = 23
    ECHOl = 24
    TRIGr = 22
    ECHOr = 27


    print "Distance measurement in progress"

    GPIO.setup(TRIGl,GPIO.OUT)
    GPIO.setup(ECHOl,GPIO.IN)
    GPIO.setup(TRIGr,GPIO.OUT)
    GPIO.setup(ECHOr,GPIO.IN)

    GPIO.output(TRIGl,False)
    GPIO.output(TRIGr,False)
    print " Sensors recalibrating, Please wait Chappar"
    time.sleep(2)

    print " Preparing to fire dual ultrasonic blasts!!"
    GPIO.output(TRIGl,True)
    time.sleep(0.00001)
    GPIO.output(TRIGl,False)
    
    
    print "left sensor range detection"
    
    while GPIO.input(ECHOl) == 0: 
        pulse_startl = time.time() 

    while GPIO.input(ECHOl) == 1:
        pulse_endl = time.time()


    print " calculating total time for transmission and reception"
    pulsel = pulse_endl - pulse_startl

    print "Calculating distance now  All most there!!"
    distance = pulsel* 17150
    distancel = round(distance,2)

    print " Here's the distance from the sensor in the left boi!! "
    print distancel,"cm"
    
    print " right sensor range detection"
    
    GPIO.output(TRIGr,True)
    time.sleep(0.00001)
    GPIO.output(TRIGr,False)

    while GPIO.input(ECHOr) == 0: 
        pulse_startr = time.time() 

    while GPIO.input(ECHOr) == 1:
        pulse_endr = time.time()


    print " calculating total time for transmission and reception"
    pulser = pulse_endr - pulse_startr

    print "Calculating distance now  All most there!!"
    distance = pulser* 17150
    distancer = round(distance,2)

    print " Here's the distance from the sensor in the right boi!! "
    print distancer,"cm"


    GPIO.cleanup()
    time.sleep(5)
    


