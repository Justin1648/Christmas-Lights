# Simple test for NeoPixels on Raspberry Pi

import time
import board
import neopixel
import random

# Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
# NeoPixels must be connected to D10, D12, D18 or D21 to work.

pixel_pin = board.D18

# The number of NeoPixels

num_pixels = 600

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!

ORDER = neopixel.RGB

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.5, 
    auto_write=False, pixel_order=ORDER)

# Preset color codes
RED = (0, 255, 0)
ORANGE = (79, 251, 20)
YELLOW = (204, 204, 0)
GREEN = (255, 0, 0)
BLUE = (0, 0, 255)
PURPLE = (0, 128, 128)
DEEPSKYBLUE = (191, 0, 255)
SILVER = (192, 192, 192)
GREY = (128, 128, 128)
PINK = (51, 255, 153)
WHITE = (255, 255, 255)
MAROON = (0, 128, 0)
PGREEN = (240, 207, 204)
PPURPLE = (169, 204, 221)
CANDY = (188, 255, 217)
PBLUE = (206, 128, 225)
VIOLET = (130, 238, 238)
OFF = (0, 0, 0)



def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.

    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 85:
        r = int(pos * 3)
        g = int(255 - pos*3)
        b = 0
    elif pos < 170:
        pos -= 85
        r = int(255 - pos*3)
        g = 0
        b = int(pos*3)
    else:
        pos -= 170
        r = 0
        g = int(pos*3)
        b = int(255 - pos*3)
    return (r, g, b) if ORDER == neopixel.RGB or ORDER == neopixel.GRB else (r, g, b, 0)

def Rainbow(wait, iterations):
    for k in range(iterations):
        for j in range(255):
            for i in range(num_pixels):
                pixel_index = (i * 256 // num_pixels) + j
                pixels[i] = wheel(pixel_index & 255)
            pixels.show()
            time.sleep(wait)

def Wipe(color, wait):
    for i in range(num_pixels):
        pixels[i] = color
        time.sleep(wait) #time in seconds
        pixels.show()
    time.sleep(0.5)

def rWipe(color, wait):
    for i in range(num_pixels):
        pixels[(num_pixels-1-i)] = color
        time.sleep(wait)
        pixels.show()

def Wipe2(COLOR1, COLOR2, wait):
    for i in range(num_pixels):
        pixels[i] = COLOR1
        pixels[(num_pixels-1-i)] = COLOR2
        time.sleep(wait)
        pixels.show()

def Wipe4(COLOR1, COLOR2, COLOR3, COLOR4, wait):
    for i in range(num_pixels):
        a = i
        b = num_pixels-i-1
        if a <= b:
            pixels[a] = COLOR1
            pixels[b] = COLOR2
            time.sleep(wait)
            pixels.show()
        else:
            pixels[a] = COLOR3
            pixels[b] = COLOR4
            time.sleep(wait)
            pixels.show()

def Blink(color1, color2, iterations, delay):
    for i in range(iterations):
        pixels.fill(color1)
        pixels.show()
        time.sleep(delay)
        pixels.fill(color2)
        pixels.show()
        time.sleep(delay)

def Theater(color, color2, iterations):
    for j in range(iterations):
        for q in range(3):
            for i in range(0, num_pixels, 3):
                pixels[(i+q)] = color
                pixels[(i+q-1)] = color2
                pixels[(i+q-2)] = color2
            pixels.show()
            time.sleep(.05)

def Stripe(color1, color2, window, iterations):
    for start in range(iterations):
        for window_start in range(0, num_pixels, window):
            for i in range(window):
                color = color1

                if i >= window / 2:
                    color = color2
                pixels[(start + window_start + i) % num_pixels] = color
            pixels.show()
            time.sleep(.001)

def Stripe3(color1, color2, color3, window, iterations):
    for start in range(iterations):
        for window_start in range(0, num_pixels, window):
            for i in range(window):
                color = color1
                if i < window * (1 / 3):
                    color = color2
                elif i >= window * (2 / 3):
                    color = color3
                pixels[(start + window_start + i) % num_pixels] = color
            pixels.show()
            time.sleep(.001)

def Stripe6(color1, color2, color3, color4, color5, color6, window, iterations):
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

def Sparkle(colorlist, iterations):
    for i in range(iterations):
        for j in range(int(num_pixels / 10)):
            a = random.randint(0, num_pixels-1)
            color = random.choice(colorlist)
            pixels[a] = color
        pixels.show()
        time.sleep(0.05)
        pixels.fill(OFF)
        pixels.show()

def Dither(color, iterations, sleep):
    for i in range(iterations):
        for j in range(int(num_pixels / 25)):
            a = random.randint(0, num_pixels-1)
            pixels[a] = color
        pixels.show()
        time.sleep(0.05)
    pixels.fill(color)
    pixels.show()
    time.sleep(sleep)

def Fill(color):
    pixels.fill(color)
    pixels.show()
    time.sleep(1)

#Run Program

if __name__ == '__main__':

    try:

        while True:

    # Rainbow
#            rainbow(0.001, 5)

    # sparkle program
#            colorlist=[COLOR1, COLOR2, COLOR3]
#            print('Red/White/Blue Sparkle')
#            sparkle(colorlist, 100)

    # dither color change
#            dither(BLUE, 60, 10)

    # Wipe to  red
#            Wipe(RED, 0.01)
#            time.sleep(1)

    # Fill to white
#            pixels.fill(WHITE)
#            pixels.show()
#            time.sleep(1)

    # rWipe to green
#            rWipe(GREEN, 0.01)
#            time.sleep(1)

    #Flash red/white 10 times for 0.5 seconds each
#            blink(RED, WHITE, 10, .5)

    # stripe Red/White
#            stripe(RED, WHITE, 10, 100)

    # theater Red/Off
#            theaterChase(RED, OFF, 20)

#            Rainbow(.01, 2)

            Wipe(RED, .01)

            rWipe(WHITE, .01)

            Wipe(BLUE, .01)

            Wipe4(RED, WHITE, BLUE, BLUE, .01)

            Fill(RED)

            Fill(WHITE)

            Fill(BLUE)

            Stripe3(RED, WHITE, BLUE, 60, 100)

            Fill(OFF)

            Dither(RED, 60, 10)

            Dither(WHITE, 60, 10)

            Dither(BLUE, 60, 10)

            Fill(OFF)

            colorlist=[RED, WHITE, BLUE]
            Sparkle(colorlist, 100)



    # Turn off
#            print ('Turn Off')
            pixels.fill(OFF)
            pixels.show()
            time.sleep(5)

    except KeyboardInterrupt:
        print ('Exit Program')
        pixels.fill(OFF)
        pixels.show()

