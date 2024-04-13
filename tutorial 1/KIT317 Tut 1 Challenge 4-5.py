from sense_emu import SenseHat
import time

s=SenseHat()
while True:
    #challenge 4
    temp = s.get_temperature()
    pressure = s.get_pressure()
    humidity = s.get_humidity()
    print(f"The Temperature is: {temp}\nThe Pressure is: {pressure}\nThe humidity is: {humidity}\n")
    
    #challenge 5
    if temp > 20:
        print("It is hot\n")
    else:
        print("It is cold\n")
        
    time.sleep(5)
    
    
