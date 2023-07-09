from time import sleep
from kafka import KafkaConsumer
from json import loads, JSONDecodeError
from pymongo import MongoClient


consumer = KafkaConsumer(
    'macrohard',
    bootstrap_servers=['144.22.52.73:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    value_deserializer=lambda x: x.decode('utf-8')
)


# Establecer conexión con la base de datos
client = MongoClient('144.22.44.98', 8008)

# Obtener una referencia a la base de datos
db = client['RED']

# Obtener una referencia a una colección
collection = db['PARADEROS']


for msg in consumer:
    try:
        json_data = loads(msg.value)
        inserted_document = collection.insert_one(json_data)
    except:
        print("Error: Invalid JSON message")
