# Change the colors in a pixel strip in increasing numerical order.

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

# color:  color to change the pixel to.  wait: time between each pixel color change
def wipe(color, wait):
    for i in range(num_pixels):
        pixels[i] = color
        time.sleep(wait)
        pixels.show()

#Run Program

if __name__ == '__main__':

    try:

        while True:

        # ColorWipe tests
            print ('Green wipe')
            Wipe(GREEN,0.1) #Green wipe
    
            print ('Red wipe')
            Wipe(RED, 0.1) #Red wipe
    
            print ('White wipe')
            Wipe(WHITE, 0.1) #Blue wipe


    except KeyboardInterrupt:
        pixels.fill(OFF)
        pixels.show()


