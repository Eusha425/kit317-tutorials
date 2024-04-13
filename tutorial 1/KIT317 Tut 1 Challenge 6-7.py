from sense_emu import SenseHat
import time

s=SenseHat()
while True:
    #challenge 6
    temp = s.get_temperature()
    pressure = s.get_pressure()
    humidity = s.get_humidity()
    
    message = str(temp)
    s.show_message(message,scroll_speed=0.000001,text_colour=[255,255,0],back_colour=[100,200,255]) #challenge 7

