#!/usr/bin/env python
# coding: latin-1
# Autor:   Ingmar Stapel
# Date:   20170723
# Version:   1.0
# Homepage:   http://custom-build-robots.com
# This program messures the distance with a MaxBotix I2CXL MaxSonar
# ultrasonic sensor.

from smbus import SMBus
import time

# sensor default I2C address
address1 = 0x70

# variables
LOOP = 20
intervall = 0.5

for z in range(0x70, 0x77+1): # z = ze addresses
    print '========== curr_addr:',z,'=========='
    for x in range(0, LOOP):

	    try:
		    i2cbus = SMBus(0)
		    i2cbus.write_byte(z, 0x51)
		    time.sleep(0.1)
		    val = i2cbus.read_word_data(z, 0xe1)
		    print (val >> 8) & 0xff | (val & 0xff), 'cm'
	    except IOError, err:
		    print err
                    break
	    time.sleep(intervall)

