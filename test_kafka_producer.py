'''
Descripttion: 
version: 
Author: Jin
Date: 2021-08-04 14:08:46
LastEditors: Jin
LastEditTime: 2021-08-05 10:47:04
'''
from kafka import KafkaConsumer, KafkaProducer
import json

def kafka_consumer(address,topic, group):
    consumer = KafkaConsumer(
        topic
        ,bootstrap_servers=[address]
        ,api_version=(0, 10, 1)
        ,group_id='test_group'
        ,auto_offset_reset='earliest'
    )
    # print(consumer.topics)
    print('create a KafkaConsumer succesfully')
    
    for message in consumer:
        print ("%s:%d:%d: key=%s value=%s" % (message.topic, 
        message.partition, message.offset, message.key, message.value))
        print(1)
    print('receive from kafka succesfully')

def kafka_producer_string(address, topic):
    producer = KafkaProducer(bootstrap_servers=[address])
    print('create a KafkaProducer succesfully')
    
    for i in range(3):
        # msg = "msg%d" % i
        # producer.send(topic, msg)
        producer.send(topic, b"hello world")

    producer.close()
    print('dump to kafka succesfully')


if __name__ == '__main__':
    address = "192.168.51.93:9092"
    topic = 'test_topic'
    group = 'test_group'
    # kafka_producer_string(address, topic)
    kafka_consumer(address, topic, group)