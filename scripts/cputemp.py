from gpiozero import LEDBarGraph, CPUTemperature
import paho.mqtt.client as mqtt

# Use minimums and maximums that are closer to "normal" usage so the
# bar graph is a bit more "lively"
cpu = CPUTemperature()

def on_connect(client, userdata, flags, rc):
	print("Connected with result code "+str(rc))
	client.publish("stat/doorpicputemp",cpu.temperature)
	
def on_publish(client,userdata,result):
	print("temp submitted")
	client.disconnect()

print(cpu.temperature)

client = mqtt.Client("doorpi_temp")
client.on_connect = on_connect
client.on_publish = on_publish
client.username_pw_set(username="carl",password="asdf")
client.connect("10.0.0.22", 1883, 60)
client.loop_forever()
