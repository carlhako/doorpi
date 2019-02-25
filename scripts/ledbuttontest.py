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
        waitForDoorBellPress()

def waitForDoorBellPress():
    print(ledToggle)
    print(getTime() + " -------------------------------")
    print("waiting for doorbell press")
    bell.wait_for_press()
    print("door bell pressed")
    print("ledToggle: " + str(ledToggle))
    activateDoorBell()
    
def on_publish(client,userdata,result):
    global ledToggle
    print("published message")
    ledToggle += 1
    activateDoorBell()

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    #if waitingForDoorbellPress == 0:
    waitForDoorBellPress()

client = mqtt.Client("doorbell")
client.on_connect = on_connect
client.on_publish = on_publish
client.username_pw_set(username="carl",password="asdf")
client.connect("10.0.0.22", 1883, 60)
client.loop_forever()
