'''
Descripttion: 
version: 
Author: Jin
Date: 2021-08-06 10:38:30
LastEditors: Jin
LastEditTime: 2021-08-06 11:10:05
'''
import datetime
import socket, sys
import paho.mqtt.client as mqtt

# 服务器地址
strBroker = "tcp://mqtt.qre.com.cn"
# 通信端口
port = 1883
# 用户名
username = 'preiot'
# 密码
password = 'EnVyCAGYIzK22lEUXGvmEQEe4bVJmtll'
# 订阅主题名
topic = 'topic'

#======================================================
def on_connect(mqttc, obj, rc):
    print("OnConnetc, rc: "+str(rc))
 
def on_publish(mqttc, obj, mid):
    print("OnPublish, mid: "+str(mid))
 
def on_subscribe(mqttc, obj, mid, granted_qos):
    print("Subscribed: "+str(mid)+" "+str(granted_qos))
 
def on_log(mqttc, obj, level, string):
    print("Log:"+string)
 
def on_message(mqttc, obj, msg):
    curtime = datetime.datetime.now()
    strcurtime = curtime.strftime("%Y-%m-%d %H:%M:%S")
    print(strcurtime + ": " + msg.topic+" "+str(msg.qos)+" "+str(msg.payload))
    on_exec(str(msg.payload))
 
def on_exec(strcmd):
    print("Exec:",strcmd)

#=====================================================
if __name__ == '__main__':
    mqttc = mqtt.Client("test")
    mqttc.on_message = on_message
    mqttc.on_connect = on_connect
    mqttc.on_publish = on_publish
    mqttc.on_subscribe = on_subscribe
    mqttc.on_log = on_log
 
    # 设置账号密码
    mqttc.username_pw_set(username, password=password)

    mqttc.connect(strBroker, port, 60)
    mqttc.subscribe(topic, 0)
    mqttc.loop_forever()