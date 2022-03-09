import RPi.GPIO as GPIO
import time
from gpiozero import LED
from time import sleep

led = LED(19)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
PIR_PIN =21
GPIO.setup(PIR_PIN, GPIO.IN)

print('Starting up the PIR Module (click on STOP to exit)')
time.sleep(1)
print ('Ready')

while True:
  if GPIO.input(PIR_PIN):
    print('Motion Detected')
    led.on()
  else:
    led.off()
    print ('Ready')