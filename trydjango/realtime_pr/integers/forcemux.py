"""
Pinouts
=======
Function    FX29    
Ground      Black    
Power (5V)  Red     
SDA         White     
SCL         Yellow   
"""
import time
import board
import busio
from adafruit_bus_device.i2c_device import I2CDevice

import adafruit_tca9548a

i2c = board.I2C()  # uses board.SCL and board.SDA

tca = adafruit_tca9548a.TCA9548A(i2c)
#tsl1 = adafruit_tsl2591.TSL2591(tca[0])


# Initialize Counters
StaleCount = 0
ValidCount = 0
FaultCount = 0

# Constants
FX29LoadRange  = 50    # Load Range for Force Sensor
FX29ZeroForce  = 0   # 0% Force Sensor Reading (Count)
FX29FullForce  = 15000  # 100% Force Sensor Reading (Count)

#IO variables
Command = bytearray(1)
F1Result  = bytearray(2)

#device = I2CDevice(i2c, 0x28)
force1 = I2CDevice(tca[0], 0x28)
force2 = I2CDevice(tca[1], 0x28)
force3 = I2CDevice(tca[6], 0x28)
force4 = I2CDevice(tca[7], 0x28)
f1name = 'force1'
f2name = 'force2'
f3name = 'force3'
f4name = 'force4'

force_out1 = float(0)
force_out2 = float(0)
force_out3 = float(0)
force_out4 = float(0)

def function(force1, output):
    global force_out1
    global force_out2
    global force_out3
    global force_out4
    global StaleCount
    global ValidCount
    global FaultCount
    while True:
        try:
                # read command was used to retrieve a sensor reading
                force1.readinto(F1Result)

                # Handle Status information
                Status = ( F1Result[0] & 0xC0 ) >> 6
                if ( Status == 0 ) :
                    ValidCount = ValidCount + 1
                elif (Status == 2 ) :
                    StaleCount = StaleCount + 1
                elif (Status == 3 ) :
                    FaultCount = FaultCount + 1

                # Combine the two bytes of data after masking the Status bits into a single value
                Measurement = (( F1Result[0] & 0x3F ) << 8 | ( F1Result[1] & 0xFF ) )              # Reading from Device
                # Convert to lb without removing offset (FX29ZeroForce) from the Measurement.
                # Correct translation would be:
                # Force_lb = ((Measurement - FX29ZeroForce) * FX29LoadRange ) / (FX29FullForce - FX29ZeroForce)
                Force_lb    = Measurement * FX29LoadRange / (FX29FullForce - FX29ZeroForce)    # Converted to Pounds (lb)

                # Convert to grams
                Force_grm   = Force_lb * 453.59237                                             # Converted to grams  (g)

                # Remove decimals prior to reporting reading
                Force_Send  = int(Force_grm)                                                   # Reported Force (grams, no fraction)

                #initiate next measurement
                force1.readinto(Command)

                # Report Force
                # print(fname + ' ' + str(Force_lb))
                
                if output == 1:
                    force_out1 = Force_lb
                elif output == 2:
                    force_out2 = Force_lb
                elif output == 3:
                    force_out3 = Force_lb
                elif output == 4:
                    force_out4 = Force_lb

                # Target a refresh rate of 100Hz
                time.sleep(.01)

                # Debug
                #print(FaultCount, StaleCount, ValidCount, Force_Send, Force_lb, Force_grm)
                break;
        except:
                # Handle IO exception by waiting it out
                time.sleep(0.010)
                #print("Exception")

'''
while True:
    time.sleep(1)
      
    with force1:
        function(force1, 1)
    with force2:
        function(force2, f2name)
    with force3:
        function(force3, f3name)
    with force4:
        function(force4, f4name)
'''