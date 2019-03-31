import sys
sys.path.insert(0,"build/lib.linux-armv7l-2.7/")

import VL53L1X
from time import sleep
import time
import RPi.GPIO as GPIO

SHUTX_PIN_1 = 20
SHUTX_PIN_2 = 16
SHUTX_PIN_3 = 21


def get_and_print_measurement():
    # Start ranging, 1 = Short Range, 2 = Medium Range, 3 = Long Range
    start = time.time()
    tof.start_ranging(3)
    distance_in_mm = tof.get_distance()
    print("sensor on pin: %d\tvalue: %d\ttime: %f" % (pin, distance_in_mm,time.time()-start))
    #sleep(1)
    tof.stop_ranging()

def toggle_pin(pin):
    if pin == SHUTX_PIN_3:
        new_pin = SHUTX_PIN_1
    elif pin == SHUTX_PIN_2:
        new_pin = SHUTX_PIN_3
    else:
        new_pin = SHUTX_PIN_2
    return new_pin

GPIO.setwarnings(False)

# Setup GPIO for shutdown pins on each VL53L0X
GPIO.setmode(GPIO.BCM)
GPIO.setup(SHUTX_PIN_1, GPIO.OUT)
GPIO.setup(SHUTX_PIN_2, GPIO.OUT)
GPIO.setup(SHUTX_PIN_3, GPIO.OUT)

# Set all shutdown pins low to turn off each VL53L0X
GPIO.output(SHUTX_PIN_1, GPIO.LOW)
GPIO.output(SHUTX_PIN_2, GPIO.LOW)
GPIO.output(SHUTX_PIN_3, GPIO.LOW)
#sleep(1)

# Start with first sensor
pin = SHUTX_PIN_1
GPIO.output(pin, GPIO.HIGH)

# Initialise the i2c bus and configure the sensor
tof = VL53L1X.VL53L1X()
print("Python: Initialized")
tof.open()
print("Python: Opened")
GPIO.output(pin, GPIO.LOW)

while True:
    pin = toggle_pin(pin)
    GPIO.output(pin, GPIO.HIGH)
    get_and_print_measurement()
    GPIO.output(pin, GPIO.LOW)
    #sleep(0.05)
