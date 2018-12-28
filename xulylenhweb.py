import paho.mqtt.client as mqtt
import webbrowser
import json
import requests

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
	print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
	client.subscribe("PC/openapp")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
	print(msg.topic+" "+str(msg.payload))
	app = msg.payload
	if app == "chrome":
		webbrowser.open('https://youtube.com')
	
	if app == "turn on light":
		
		url = 'https://minhthanhhome.duckdns.org/api/services/switch/turn_on?api_password=emilybro2018'
		payload = {'entity_id': 'switch.main_light_1'}
		headers = {'content-type': 'application/json'}
 
		r = requests.post(url, data=json.dumps(payload), headers=headers)
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set(username="vbddicrq",password="vmek8RI8criu")
client.connect("m12.cloudmqtt.com", 11189, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
