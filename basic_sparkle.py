# Light 10% of pixels randomly using colors from colorlist for 0.05 seconds

import time
import board
import neopixel
import random

# Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
# NeoPixels must be connected to D10, D12, D18 or D21 to work.

pixel_pin = board.D18

# The number of NeoPixels

num_pixels = 300

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reverse$

ORDER = neopixel.RGB

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.2, 
    auto_write=False, pixel_order=ORDER)

# Preset color codes
RED = (0, 255, 0)
ORANGE = (79, 251, 20)
YELLOW = (255, 255, 0)
GREEN = (255, 0, 0)
BLUE = (0, 0, 255)
PURPLE = (0, 128, 128)
WHITE = (255, 255, 255)
OFF = (0, 0, 0)
DEEPSKYBLUE = (191, 0, 255)

def sparkle(colorlist, iterations):
    for i in range(iterations):
        for j in range(int(num_pixels / 10)):
            a = random.randint(0, num_pixels-1)
            color = random.choice(colorlist)
            pixels[a] = color
        pixels.show()
        time.sleep(0.05)
        pixels.fill(OFF)
        pixels.show()

#Run Program

if __name__ == '__main__':

    try:

        while True:

            colorlist=[WHITE, BLUE, DEEPSKYBLUE]
            print('Red/White/Blue Sparkle')
            sparkle(colorlist, 100)

    except KeyboardInterrupt:
        pixels.fill(OFF)
        pixels.show()




