'''
Descripttion: 
version: 
Author: Jin
Date: 2021-08-04 14:08:46
LastEditors: Jin
LastEditTime: 2021-08-05 11:05:34
'''
from kafka import KafkaProducer
import json

'''
name: 
msg: 创建kafka生产者。
param {*} address
param {*} topic
return {*}
'''
def kafka_producer_string(address, topic):
    producer = KafkaProducer(bootstrap_servers=[address])
    print('create a KafkaProducer succesfully')
    
    for i in range(3):
        msg = b"msg%d" % i
        producer.send(topic, msg)

    producer.close()
    print('dump to kafka succesfully')

if __name__ == '__main__':
    address = "192.168.51.93:9092"
    topic = 'test_topic'
    group = 'test_group'
    kafka_producer_string(address, topic)
