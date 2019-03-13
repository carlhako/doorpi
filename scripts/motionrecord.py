# https://github.com/iizukanao/picam
import paho.mqtt.client as mqtt
import datetime
from gpiozero import MotionSensor
from picamera import PiCamera
from time import sleep

from gpiozero import OutputDevice
ledring = OutputDevice(17)

doorbellmotionTopic = 'stat/doorbellmotion'

def getTime():
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    
camera = PiCamera()
radar = MotionSensor(24,pull_up=False)

camera.resolution = (1920, 1080)
camera.framerate = 25

storageLoc = '/doorpi/capture/'
#storageLoc = '/home/pi/stills/'

while True: 
    print("waiting for motion")
    radar.wait_for_motion()
    print("motion detected")
    ledring.on()
    videoFilename = storageLoc + 'vid ' + getTime() + '.h264'
    camera.start_recording(videoFilename)
    print("started recording to " + videoFilename)

    for i in range(5):
        stillFilename = storageLoc + 'still ' + getTime() + '.jpg'
        camera.capture(stillFilename)
        print(stillFilename)
        sleep(1)

    camera.stop_recording()
    ledring.off()
