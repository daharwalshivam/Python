import paho.mqtt.client as mqttClient
import time

def on_connect(client,userdata,flags,rc):
    if rc == 0:
        print("connected to broker")
        global Connected
        Connected = True
    else:
        print("connection failed")

Connected = False

broker_address = "enter broker address here"
port = 12345
user = "user name"
password = "password here"

client = mqttClient.Client("topic name")
client.username_pw_set(user,password=password)
client.on_connect = on_connect
client.connect( broker_address,port=port)
client.loop_start()
while Connected != True:
    time.sleep(0.1)
try:
    while True:

        value = raw_input('enter the message')
        client.publish("topic name as per MQTT",value)

except KeyboardInterrupt:

    client.disconnect()
    client.loop_stop()
