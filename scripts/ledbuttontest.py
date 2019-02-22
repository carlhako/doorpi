from time import sleep
from gpiozero import OutputDevice
from gpiozero import Button

ledring = OutputDevice(17)
bell = Button(4)

while 1:
    bell.wait_for_press()
    print("door bell pressed")
    ledring.on()
    sleep(2)
    ledring.off()
    
    