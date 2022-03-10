import RPi.GPIO as GPIO
import time
from gpiozero import LED
from time import sleep

led = LED(19)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
PIR_PIN =13
GPIO.setup(PIR_PIN, GPIO.IN)
'''
print('Starting up the PIR Module (click on STOP to exit)')
time.sleep(1)
print ('Ready')
'''
def get_reading():
  # time.sleep(1)
  if GPIO.input(PIR_PIN):
    #print('Motion Detected')
    #led.on()
    return 1
  else:
    #led.off()
    return 0
    #print ('Ready')
    