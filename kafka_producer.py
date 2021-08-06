'''
Descripttion: 
version: 
Author: Jin
Date: 2021-08-04 14:08:46
LastEditors: Jin
LastEditTime: 2021-08-06 09:43:39
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
import json  

def kafka_producer_string(address, topic,msg):
    producer = KafkaProducer(bootstrap_servers=[address])
    print('create a KafkaProducer succesfully')
    
    for i in range(3):
        msg = b"msg%d" % i
        producer.send(topic, msg)

    producer.close()
    print('dump to kafka succesfully')


def kafka_producer_json_srlz(address, topic, msg):
    producer = KafkaProducer(
        bootstrap_servers=[address]
        ,value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )
    print('create a KafkaProducer succesfully')

    producer.send(topic, msg)

    producer.close()
    print('dump to kafka succesfully')

if __name__ == '__main__':
    address = "192.168.51.93:9092"
    topic = 'test_topic'
    group = 'test_group'
    kafka_producer_string(address, topic)
