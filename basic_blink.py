# Flash 1 color along the whole LED strip multiple times

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

def flash(color1, color2, iterations, delay)
    for i in range(iterations):
        pixels.fill(color1)
        pixels.show()
        time.sleep(delay)
        pixels.fill(color2)
        pixels.show()
        time.sleep(delay)


#Run Program

if __name__ == '__main__':

    try:

        while True:

#Flash red/white 10 times for 0.5 seconds each
            print ('Flash Red/White')
            flash(RED, WHITE, 10, .5)

# Flash Green/Off 5 times for 0.5 seconds each

    except KeyboardInterrupt:
        pixels.fill(OFF)
        pixels.show()


