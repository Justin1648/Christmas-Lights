# Simple test for NeoPixels on Raspberry Pi

import time
import board
import neopixel

# Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
# NeoPixels must be connected to D10, D12, D18 or D21 to work.

pixel_pin = board.D18

# The number of NeoPixels

num_pixels = 150

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!

ORDER = neopixel.RGB

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.5, 
    auto_write=False, pixel_order=ORDER)

# Preset color codes
RED = (0, 255, 0)
GREEN = (255, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
OFF = (0, 0, 0)

def colorWipe(color, wait):
    for i in range(num_pixels):
        pixels[i] = color
        time.sleep(wait) #time in seconds
        pixels.show()
    time.sleep(0.5)

def theaterChase(color, color2, iterations):
    for j in range(iterations):
        for q in range(3):
            for i in range(0, num_pixels, 3):
                pixels[(i+q)] = color
                pixels[(i+q-1)] = color2
                pixels[(i+q-2)] = color2
            pixels.show()
            time.sleep(.05)

def stripeChase(color1, color2, window, iterations):
    for start in range(iterations):
        for window_start in range(0, num_pixels, window):
            for i in range(window):
                color = color1

                if i >= window / 2:
                    color = color2
                pixels[(start + window_start + i) % num_pixels] = color
            pixels.show()
            time.sleep(.001)


#Run Program

if __name__ == '__main__':

    try:

        while True:

    # colorWipe to  red
            print ('colorWipe Red')
            colorWipe(RED, 0.01)
            time.sleep(1)

    # Fill to white
            print ('Fill White')
            pixels.fill(WHITE)
            pixels.show()
            time.sleep(1)

    # colorWipe off
            print ('colorWipe Off')
            colorWipe(OFF, 0.01)

    # colorWipe to green
            print ('colorWipe Green')
            colorWipe(GREEN, 0.01)
            time.sleep(1)

    # Fill all white
            print ('Fill White')
            pixels.fill(WHITE)
            pixels.show()
            time.sleep(1)

    # colorWipe to Red
            print ('colorWipe Red')
            colorWipe(RED, 0.01)
            time.sleep(1)

    # stripeChase Red/White
            print ('Red/White stripe')
            stripeChase(RED, WHITE, 10, 100)

    # theaterChase Red/Off
            print ('theaterChase Red/Off')
            theaterChase(RED, OFF, 20)

    # Red Fill
            print ('Fill Red')
            pixels.fill(RED)
            pixels.show()
            time.sleep(1)

    # stripeChase Red/Green
            print ('Red/Green stripe')
            stripeChase(RED, GREEN, 10, 100)

    # theaterChase Green/Off
            print ('theaterChase Green/Off')
            theaterChase(GREEN, OFF, 20)

    # Green Fill
            print ('Fill green')
            pixels.fill(GREEN)
            pixels.show()
            time.sleep(1)

    # stripeChase Green/White
            print ('Green/White stripeChase')
            stripeChase(GREEN, WHITE, 10, 100)

    # theaterChase White/Off
            print ('theaterChase White/Off')
            theaterChase(WHITE, OFF, 20)

    # White Fill
            print ('Fill White')
            pixels.fill(WHITE)
            pixels.show()
            time.sleep(1)

    # Turn off
            print ('Turn Off')
            colorWipe(OFF, .01)
            time.sleep(5)

    except KeyboardInterrupt:
        print ('Exit Program')
        colorWipe((0, 0, 0), .01)


