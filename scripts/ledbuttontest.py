'''

2019-02-25 22:49:09.382472 -------------------------------
waiting for doorbell press
2019-02-26 08:25:25.260333 door bell pressed
ledToggle: 0
led ring on
publishing - on
2019-02-26 08:25:26.285726 Connected with result code 0
0
2019-02-26 08:25:26.292555 -------------------------------
waiting for doorbell press
2019-02-26 08:25:34.094656 door bell pressed
ledToggle: 0
led ring on
publishing - on
published message
led ring off
publishing - off
published message
0



'''

from time import sleep
from gpiozero import OutputDevice
from gpiozero import Button
import paho.mqtt.client as mqtt
import datetime

def getTime():
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')

ledring = OutputDevice(17)
bell = Button(4)
ledToggle = 0

def activateDoorBell():
    global ledToggle
    if ledToggle == 0:
        print("led ring on")
        ledring.on()
        print("publishing - on")
        client.publish("stat/doorbell","ON")
    elif ledToggle == 1:
        sleep(2)
        print("led ring off")
        ledring.off()
        print("publishing - off")
        client.publish("stat/doorbell","OFF")
    elif ledToggle == 2:
        ledToggle = 0
        print("waiting for doorbell press")

def doorBellPressed():
    global ledToggle
    ledToggle = 0
    print(getTime() + " door bell pressed -------------------------------")
    activateDoorBell()
    
def on_publish(client,userdata,result):
    global ledToggle
    print("published message")
    ledToggle += 1
    activateDoorBell()

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print(getTime() + " Connected with result code "+str(rc))


client = mqtt.Client("doorbell")
client.on_connect = on_connect
client.on_publish = on_publish
client.username_pw_set(username="carl",password="asdf")
client.connect("10.0.0.22", 1883, 60)

bell.when_pressed = doorBellPressed
print("waiting for doorbell press")
client.loop_forever()
