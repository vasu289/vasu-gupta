import paho.mqtt.client as mqtt
import pymongo
import json
import urllib.parse

username = urllib.parse.quote_plus("vasu")
password = urllib.parse.quote_plus("Vasugupta78140") 

MONGO_URI = f"mongodb+srv://{username}:{password}@cluster0.sea91.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
mongo_client = pymongo.MongoClient(MONGO_URI)
db = mongo_client["sensor_data"]
collection = db["gyroscope"]

MQTT_BROKER = "f5d507c5a52e4e8387fc4179d556160a.s1.eu.hivemq.cloud"
MQTT_PORT = 8883  
MQTT_TOPIC = "sensor/gyroscope"
MQTT_USER = "vasugupta"
MQTT_PASSWORD = "Vasugupta78140"

def on_message(client, userdata, message):
    try:
        data = json.loads(message.payload.decode())
        print("Received Data:", data)

        collection.insert_one(data)
        print("Data saved to MongoDB Atlas.")

    except Exception as e:
        print("Error:", e)

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)  
client.username_pw_set(MQTT_USER, MQTT_PASSWORD)
client.tls_set() 

client.on_message = on_message
client.connect(MQTT_BROKER, MQTT_PORT, 60)
client.subscribe(MQTT_TOPIC)

print("Listening for MQTT messages...")
client.loop_forever()
