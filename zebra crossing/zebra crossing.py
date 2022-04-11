# This code is for 6 zebra crossing for demonstration purposes written by John Holmes
# Date 10/4/22
# ---
# The code is written in MicroPpython
# And uses 2 libraries Machine, and utime
# machine gives us access to the GP input aand output pins on the Pi Pico
# utime gives us access to the sleep function
# ---
# Connections used for the demonstration are
# Bank 1 pins 0 & 1 
# bank 2 pins 2 & 3
# bank 3 pins 4 & 5
# bank 4 pins 6 & 7
# bank 5 pins 16 & 17
# bank 6 pins 26 & 27
# These pins on my board have built in LED's
# ---
# Hardware:
# 1. Cytron Maker Pi RP2040 (www.cytron.io/p-MAKER-PI-RP2040)
# - Any RP2040 boards should work too but you will have to add LEDS with resistors to make it work
# ---
# 
# Import the 2 library's
# from machine import Pin
# 
# import utime
# 
# Give meaning full variable names to the pins and set then up as outputs in this case
# head1 = Pin(0,Pin.OUT)
# head1a = Pin(21,Pin.OUT)

from machine import Pin
import utime

# Here we setup the GP pins as outputs and asign a variable name to each pin.
head1 = Pin(0,Pin.OUT)
head1a = Pin(1,Pin.OUT)
head2 = Pin(2,Pin.OUT)
head2a = Pin(3,Pin.OUT)
head3 = Pin(4,Pin.OUT)
head3a = Pin(5,Pin.OUT)
head4 = Pin(6,Pin.OUT)
head4a = Pin(7,Pin.OUT)
head5 = Pin(16,Pin.OUT)
head5a = Pin(17,Pin.OUT)
head6 = Pin(26,Pin.OUT)
head6a = Pin(27,Pin.OUT)

# Setup the forever loop this uses the built in libarary for turning the ouput in high or low.
# The pico runs through each line of code very quickly until it gets to the utime.sleep.
# Then the Pico will sleep for .5 of a second before starting up again.
# Once it gets to the last line in the program and completes that task it will return to the top
# line in the while loop. Hence runing until the Pico is powered down.

while True:
    head1.low()
    head1a.high()
    head2.low()
    head2a.high()
    head3.low()
    head3a.high()
    head4.low()
    head4a.high()
    head5.low()
    head5a.high()
    head6.low()
    head6a.high()
    utime.sleep(.5)
    
    head1.high()
    head1a.low()
    head2.high()
    head2a.low()
    head3.high()
    head3a.low()
    head4.high()
    head4a.low()
    head5.high()
    head5a.low()
    head6.high()
    head6a.low()
    utime.sleep(.5)
