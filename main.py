#Python code !!!!
#Import your stufff !!!!!
from codrone_edu.drone import *

drone = Drone()

color_data = drone.get_color_data
height = drone.get_height()

drone.pair()
drone.set_controller_LED(0, 0, 255, 100)



while True:
    time.sleep(0.1)
    if drone.s_pressed():
        print(color_data)
    break

while True:
    time.sleep(0.1)
    if drone.h_pressed():
        print(height)
    break
