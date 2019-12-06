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

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.2, 
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
        time.sleep(wait)
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
                
            

#Run Program

if __name__ == '__main__':

    try:

        while True:

        #theaterChase Red/off
            print ('Red/off theater')
            theaterChase(RED, OFF, 20)

        #theaterChase Red/Green
            print ('Red/Green theater')
            theaterChase(RED, GREEN, 20)


    except KeyboardInterrupt:
        colorWipe((0, 0, 0), .01)


