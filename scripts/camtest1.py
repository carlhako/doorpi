# https://github.com/iizukanao/picam
from picamera import PiCamera
from time import sleep
from gpiozero import MotionSensor
import datetime

def getTime():
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    
camera = PiCamera()
radar = MotionSensor(4,pull_up=False)

camera.resolution = (1920, 1080)
camera.framerate = 25

storageLoc = '/doorpi/capture/'
#storageLoc = '/home/pi/stills/'

while True: 
    print("waiting for motion")
    radar.wait_for_motion()
    print("motion detected")
    videoFilename = storageLoc + 'vid ' + getTime() + '.h264'
    camera.start_recording(videoFilename)
    print("started recording to " + videoFilename)

    for i in range(5):
        sleep(1)
        stillFilename = storageLoc + 'still ' + getTime() + '.jpg'
        camera.capture(stillFilename)
        print(stillFilename)

    camera.stop_recording()
