import RPi.GPIO as GPIO
import time
import multiprocessing
import os

print 'distance measurement in progress'
TRIG1 = 14
ECHO1 = 15

TRIG2 = 2
ECHO2 = 3


            	
def mysensor(senname,TRIG,ECHO) :

    count = 0

    while count == 0 :
        
        print 'wait for sensor to settle'
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(TRIG,GPIO.OUT)
        GPIO.setup(ECHO,GPIO.IN)
        GPIO.output(TRIG, False)  
	time.sleep(0.2)
        GPIO.output(TRIG, True)
	time.sleep(0.00001)
        GPIO.output(TRIG, False)
           
	count = 1
        while GPIO.input(ECHO) == 0 :
            pulse_start = time.time()
		

        while GPIO.input(ECHO) == 1 :
            pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start

        distance = pulse_duration* 17150
        if 0<=distance<=20 :
            os.system('omxplayer Produce.wma')

        distance = round(distance, 2)
        
			
		
        print 'distance', senname,':', distance,'cm'
if __name__ == '__main__':
    jobs = []
    work1 = multiprocessing.Process(target=mysensor, args(1,TRIG1,ECHO1,))
    work2 = multiprocessing.Process(target=mysensor, args(1,TRIG2,ECHO2,))
    while 1 :
        work1.start()
	work2.start()

GPIO.cleanup()

