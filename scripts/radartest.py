from gpiozero import MotionSensor
from time import sleep
from gpiozero import OutputDevice
import datetime

radar = MotionSensor(11,pull_up=False)
ledring = OutputDevice(17)

def getTime():
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')


while True: 
    print("waiting for motion")
    radar.wait_for_motion()
    ledring.on()
    print(getTime() + " motion detected")
    sleep(5)
    ledring.off()