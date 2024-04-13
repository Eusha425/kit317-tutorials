from sense_emu import SenseHat
s = SenseHat()
w = (255,255,255)
b = (0,0,0)
#challenge 8
tick = [
b, b, b, b, b, b, b, w,
b, b, b, b, b, b, w, b,
b, b, b, b, b, w, b, b,
w, b, b, b, w, b, b, b,
b, w, b, w, b, b, b, b,
b, b, w, b, b, b, b, b,
b, b, b, b, b, b, b, b,
b, b, b, b, b, b, b, b,
]



cross = [
w, b, b, b, b, b, b, w,
b, w, b, b, b, b, w, b,
b, b, w, b, b, w, b, b,
b, b, b, w, w, b, b, b,
b, b, b, w, w, b, b, b,
b, b, w, b, b, w, b, b,
b, w, b, b, b, b, w, b,
w, b, b, b, b, b, b, w,
]

#challenge 9
while True:
    temp = s.get_temperature()

    if temp > 20:
        s.set_pixels(tick)
        
    else:
        s.set_pixels(cross)

    

    
    

