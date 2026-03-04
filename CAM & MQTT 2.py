import paho.mqtt.client as mqtt

subscribe = "masukankata"

def on_message(client, userdata, msg):
    data = str(msg.payload.decode())
    print("Pesan diterima:", data)

client = mqtt.Client()
client.on_message = on_message
server = "mqtt-dashboard.com"
client.connect(server, 1883)
client.subscribe(subscribe)

client.loop_forever()