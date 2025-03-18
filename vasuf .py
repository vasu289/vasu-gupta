import paho.mqtt.client as mqtt
import json
import couchdb                                                                                                                                           # type: ignore
from datetime import datetime

couchdb_url = "http://vasu:Vasugupta7814@127.0.0.1:5984/"  
couch = couchdb.Server(couchdb_url)
db_name = "gyro_data"

if db_name not in couch:
    db = couch.create(db_name)
else:
    db = couch[db_name]
MQTT_BROKER = "f5d507c5a52e4e8387fc4179d556160a.s1.eu.hivemq.cloud"
MQTT_PORT = 8883
MQTT_TOPIC = "sensor/gyroscope"
MQTT_USERNAME = "vasugupta" 
MQTT_PASSWORD = "Vasugupta78140"

def on_message(client, userdata, msg):
    try:
        payload = json.loads(msg.payload.decode())
        payload["timestamp"] = datetime.utcnow().isoformat()  # Add timestamp
        
        db.save(payload)
        print(f"Stored in CouchDB: {payload}")
    except Exception as e:
        print("Error:", e)

mqtt_client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
mqtt_client.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)
mqtt_client.tls_set()
mqtt_client.on_message = on_message
mqtt_client.connect(MQTT_BROKER, MQTT_PORT, keepalive=60)
mqtt_client.subscribe(MQTT_TOPIC)

print(f"Connected to MQTT broker {MQTT_BROKER}, listening for topic: {MQTT_TOPIC}")
mqtt_client.loop_forever()