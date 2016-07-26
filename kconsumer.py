#!/usr/bin/python

from kafka import KafkaClient, SimpleConsumer
 

kafka_client = KafkaClient("mykafkaslave.example.com:6667")
consumer = SimpleConsumer(kafka_client, b"hello_group1_consumer", b"testkafka")
 
# We can also start at a specic offset
# consumer.seek(25, 0)
 
for message in consumer:
    print(message)


