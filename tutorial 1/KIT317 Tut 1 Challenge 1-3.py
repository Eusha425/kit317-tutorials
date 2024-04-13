from sense_emu import SenseHat
import time
#challenge 1

s=SenseHat()
while True:
    s.set_pixel(3,4,0,190,255) #challenge 1 different colour & challenge 3 different LED blink
    time.sleep(0.1) # challenge 2 different rateof blinking
    s.set_pixel(3,4,0,0,0) 
    time.sleep(0.1)