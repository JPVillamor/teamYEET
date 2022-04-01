from random import randint
# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

# Simple demo of the LSM9DS1 accelerometer, magnetometer, gyroscope.
# Will print the acceleration, magnetometer, and gyroscope values every second.
import time
import board
import adafruit_lsm9ds1

# Create sensor object, communicating over the board's default I2C bus
i2c = board.I2C()  # uses board.SCL and board.SDA
sensor = adafruit_lsm9ds1.LSM9DS1_I2C(i2c)

def get_temp():
    # sensor_value = randint(1,100)
    
    temp = sensor.temperature
    return temp
    
def get_acc(dimension):
    accx, accy, accz = sensor.acceleration
    
    if dimension == 'x':
        return round(accx, 3)
    elif dimension == 'y':
        return round(accy, 3)
    elif dimension == 'z':
        return round(accz, 3)
