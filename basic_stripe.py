# Two color stripe moves from lower to upper number pixels

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

def stripe(color1, color2, window, iterations):
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

        #stripeChase Red/White (Color1, Color2, length of stripe, iterations)
            print ('Red/White stripe')
            stripe(RED, WHITE, 20, 20)

        #stripeChase Red/Green
            print ('Red/Green stripe')
            stripe(RED, GREEN, 20, 20)


    except KeyboardInterrupt:
        pixels.fill(OFF)
        pixels.show()


