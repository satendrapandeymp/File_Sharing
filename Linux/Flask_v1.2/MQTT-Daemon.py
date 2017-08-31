import os, time
import paho.mqtt.client as mqtt

# For connection with mosquitto
server = "localhost"
port = 1883
vhost = "yourvhost"
username = "username"
password = "password"
topic = "share/"

# For subscribing our topic on connect
def onConnect(client, userdata, rc):    
    client.subscribe([(topic, 1)]) 

def onMessage(client, userdata, message): 
	print message

	# Run another script
	os.system("python main.py")

while True:
    try:
        client = mqtt.Client(client_id="", clean_session=True, userdata=None, protocol="MQTTv31")
        client.username_pw_set(vhost + ":" + username, password)
        client.on_connect = onConnect
        client.on_message = onMessage
        client.connect(server, port, keepalive=60, bind_address="12")
        client.loop_forever()  
    except Exception, e:
        print "Exception handled, reconnecting...\nDetail:\n%s" % e
	time.sleep(5)
	print e
