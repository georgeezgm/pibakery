#!/user/bin/python
 
#Needs the LED0 (OK light) to be uncoupled from the mmc0 trigger using:
# echo none >/sys/class/LEDs/led0/trigger prior to start
 
import RPi.GPIO as GPIO
from time import sleep
 
# Needs to be BCM. GPIOBOARD lets you address GPIO ports by peripheral
# connector pin number, and the LED GPIO isn't on the connector
GPIO.setmode(GPIO.BCM)
 
#disable warning about channel in use
GPIO.setwarnings(False)
 
# set up GPIO output channel
GPIO.setup(16, GPIO.OUT)
# write the Brecon VOR details to the screen
print "The Brecon VOR is 117.45 BCN _.../_._./_."
print "Now watch the LED!"

sleep(3)
 
# Flash the Brecon Morse pattern
 
# OK
# --- -.-
GPIO.output(16, GPIO.LOW) #da
sleep(1)
GPIO.output(16, GPIO.HIGH)
sleep(1)
GPIO.output(16, GPIO.LOW) #da
sleep(1)
GPIO.output(16, GPIO.HIGH)
sleep(1)
GPIO.output(16, GPIO.LOW) #da
sleep(1)
GPIO.output(16, GPIO.HIGH)
sleep(1)
GPIO.output(16, GPIO.LOW) #dah
sleep(2)
GPIO.output(16, GPIO.HIGH)
sleep(1)
GPIO.output(16, GPIO.LOW) #da
sleep(1)
GPIO.output(16, GPIO.HIGH)
sleep(1)
GPIO.output(16, GPIO.LOW) #d
sleep(0.5)
GPIO.output(16, GPIO.HIGH)
sleep(1)
GPIO.output(16, GPIO.LOW) #da
sleep(1)
GPIO.output(16, GPIO.HIGH)
#next letter
sleep(3)
 