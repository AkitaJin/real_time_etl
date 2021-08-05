'''
Descripttion: 
version: 
Author: Jin
Date: 2021-08-04 14:08:46
LastEditors: Jin
LastEditTime: 2021-08-05 11:05:47
'''
from kafka import KafkaConsumer, KafkaProducer
import json


'''
name: 
msg: 创建kafka消费者。注意注明api_version和group_id
param {*} address
param {*} topic
param {*} group
return {*}
'''
def kafka_consumer(address, topic, group):
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
    print('receive from kafka completely')


if __name__ == '__main__':
    address = "192.168.51.93:9092"
    topic = 'test_topic'
    group = 'test_group'
    kafka_consumer(address, topic, group)