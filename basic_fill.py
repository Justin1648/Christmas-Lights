# Change the color of the entire strip at one time

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

# Run program

if __name__ == '__main__':

    try:

        while True:

   # Fill all green
            print ('Fill Green')
            pixels.fill(GREEN)
            pixels.show()
            time.sleep(1)

    # Fill all red
            print ('Fill Red')
            pixels.fill(RED)
            pixels.show()
            time.sleep(1)

    # Fill all blue
            print ('Fill Blue')
            pixels.fill(BLUE)
            pixels.show()
            time.sleep(1)

    # Fill all white
            print ('Fill White')
            pixels.fill(WHITE)
            pixels.show()
            time.sleep(1)


    except KeyboardInterrupt:
        pixels.fill(OFF)
        pixels.show()


