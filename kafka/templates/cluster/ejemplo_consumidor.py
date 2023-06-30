#Reemplazar direccion y "my-topic" segun corresponda
from kafka import KafkaConsumer
from json import loads
from time import sleep
consumer = KafkaConsumer(
    'my-topic',
    bootstrap_servers=['direccion:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True
)

for msg in consumer:
    print(msg)