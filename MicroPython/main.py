"""
Created by: Mr. Coxall
Created on: Sep 2020
This module is a Micro:bit MicroPython program that detects distance with sonar and lights up LEDs.
"""

from microbit import *
from machine import time_pulse_us
import neopixel


# variables
neopixel_strip = neopixel.NeoPixel(pin16, 8)

# choose pins
trig = pin1
echo = pin2

display.clear
display.show(Image.PACMAN)
sleep(1000)

# neopixels clean up
neopixel_strip[0] = (0, 0, 0)
neopixel_strip[1] = (0, 0, 0)
neopixel_strip[2] = (0, 0, 0)
neopixel_strip[3] = (0, 0, 0)
print(neopixel_strip[0])
print(neopixel_strip[1])
print(neopixel_strip[2])
print(neopixel_strip[3])
neopixel_strip.show()

# setup
trig.write_digital(0)
echo.read_digital()

while True:
    # output for sonar
    trig.write_digital(1)
    trig.write_digital(0)

    # Measure the echo pulse
    micros = time_pulse_us(echo, 1)
    t_echo = micros / 1000000

    # calculate distance to cm
    dist_cm = (t_echo / 2) * 34300
    display.scroll(str(int(dist_cm)))

    # if distance < 10cm then neopixels light up red
    if dist_cm < 10:
        neopixel_strip[0] = (255, 0, 0)
        neopixel_strip[1] = (255, 0, 0)
        neopixel_strip[2] = (255, 0, 0)
        neopixel_strip[3] = (255, 0, 0)
        print(neopixel_strip[0])
        print(neopixel_strip[1])
        print(neopixel_strip[2])
        print(neopixel_strip[3])
        neopixel_strip.show()
        sleep(1000)
        display.show(Image.PACMAN)

    # if distance >= 10cm then neopixels light up green
    else:
        neopixel_strip[0] = (0, 255, 0)
        neopixel_strip[1] = (0, 255, 0)
        neopixel_strip[2] = (0, 255, 0)
        neopixel_strip[3] = (0, 255, 0)
        print(neopixel_strip[0])
        print(neopixel_strip[1])
        print(neopixel_strip[2])
        print(neopixel_strip[3])
        neopixel_strip.show()
        sleep(1000)
        display.show(Image.PACMAN)
