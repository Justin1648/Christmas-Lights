# Two color stripe moves from lower to upper number pixels

import time
import board
import neopixel
import random

# Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
# NeoPixels must be connected to D10, D12, D18 or D21 to work.

pixel_pin = board.D18

# The number of NeoPixels

num_pixels = 300

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!

ORDER = neopixel.RGB

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.2, 
    auto_write=False, pixel_order=ORDER)

# Preset color codes
RED = (0, 255, 0)
ORANGE = (79, 251, 20)
YELLOW = (255, 255, 50)
GREEN = (255, 0, 0)
BLUE = (0, 0, 255)
PURPLE = (0, 255, 255)
WHITE = (255, 255, 255)
OFF = (0, 0, 0)

def stripe6(color1, color2, color3, color4, color5, color6, window, iterations):
    for start in range(iterations):
        for window_start in range(0, num_pixels, window):
            for i in range(window):
                if (window * (1/6)) >= i:
                    color = color1
                elif (window * (2/6)) >= i > (window * (1 / 6)):
                    color = color6
                elif (window * (3/6)) >= i > (window * (2/6)):
                    color = color5
                elif (window * (4/6)) >= i > (window * (3/6)):
                    color = color4
                elif (window * (5/6)) >= i > (window * (4/6)):
                    color = color3
                else:
                    color = color2
                pixels[(start + window_start + i) % num_pixels] = color
            pixels.show()
            time.sleep(.001)

def sparkle(colorlist, iterations):
    for i in range(iterations):
        for j in range(int(num_pixels / 5)):
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

        #stripeChase Red/White (Color1, Color2, length of stripe, iterations)

            stripe6(RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE, 100, 100)

            pixels.fill(RED)
            pixels.show()
            time.sleep(1)

            pixels.fill(ORANGE)
            pixels.show()
            time.sleep(1)

            pixels.fill(YELLOW)
            pixels.show()
            time.sleep(1)

            pixels.fill(GREEN)
            pixels.show()
            time.sleep(1)

            pixels.fill(BLUE)
            pixels.show()
            time.sleep(1)

            pixels.fill(PURPLE)
            pixels.show()
            time.sleep(1)

            colorlist=[RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE]
            sparkle(colorlist, 100)

        #stripeChase Red/Green
#            print ('Red/Green stripe')
#            stripe3(RED, GREEN, WHITE, 30, 100)


    except KeyboardInterrupt:
        pixels.fill(OFF)
        pixels.show()


