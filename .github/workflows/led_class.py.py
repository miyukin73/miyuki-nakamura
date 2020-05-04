#led_class.py
import RPI.GPIO as GPIO

class Led(object):
    def_init_(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(25,GPIO.OUT)
   
    def led_on(self):
        GPIO.output(25, GPIO.HIGH)
        
    def led_off(self):
        GPIO.output(25, GPIO.LOW)
    
    def cleanup(self):
        GPIO.cleanup()
