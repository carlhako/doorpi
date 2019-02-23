from time import sleep
from gpiozero import OutputDevice
from gpiozero import Button
import paho.mqtt.client as mqtt


ledring = OutputDevice(17)
bell = Button(4)

def waitForDoorBellPress():
    print("waiting for doorbell press")
    bell.wait_for_press()
    print("door bell pressed")
    client.publish("stat/doorbell","pressed")


def on_publish(client,userdata,result):
    print("data published \n")
    ledring.on()
    sleep(2)
    ledring.off()
    waitForDoorBellPress()


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    waitForDoorBellPress()

client = mqtt.Client("doorbell")
client.on_connect = on_connect
client.on_publish = on_publish
client.username_pw_set(username="carl",password="asdf")
client.connect("10.0.0.22", 1883, 60)
print("asdf")
client.loop_forever()
