from gpiozero import MotionSensor
from time import sleep

radar = MotionSensor(4,pull_up=False)

while True: 
    print("waiting for motion")
    radar.wait_for_motion()
    print("motion detected")
    sleep(1)