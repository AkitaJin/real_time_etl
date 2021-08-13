'''
Descripttion: 
version: 
Author: Jin
Date: 2021-08-06 10:38:30
LastEditors: Jin
LastEditTime: 2021-08-11 13:44:46
'''
import datetime
import paho.mqtt.client as mqtt
import test_etl
# import time

# 服务器地址
strBroker = "mqtt.qre.com.cn"
# 通信端口
port = 1883
# 用户名
username = 'preiot'
# 密码
password = 'EnVyCAGYIzK22lEUXGvmEQEe4bVJmtll'
# 订阅主题
topic = "/kafka/post/+"
# 客户端ID，需要修改成对应的client_id
client_id = "aiit_test_1"
# 最后传输时间
last_deliver_time = datetime.datetime.now()
# 消息暂存
msg_list = []

#======================================================
def on_connect(mqttc, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    # mqttc.subscribe("data/receive")         # 订阅消息
 
def on_publish(mqttc, obj, mid):
    print("OnPublish, mid: "+str(mid))
 
def on_subscribe(mqttc, obj, mid, granted_qos):
    print("Subscribed: "+str(mid)+" "+str(granted_qos))
 
def on_log(mqttc, obj, level, string):
    print("Log:"+string)


'''
name: on_message
msg: 判断是否满足发送的时间间隔，再将数据传入另一个函数。
传入对象是时间间隔内收到的消息组成的数组。
param {*} mqttc
param {*} obj
param {*} msg
return {*}
'''
def on_message(mqttc, obj, msg):
    curtime = datetime.datetime.now()
    strcurtime = curtime.strftime("%Y-%m-%d %H:%M:%S")
    # print("时间：" + strcurtime+ "， 主题:" + msg.topic+"， 消息"+str(msg.payload.decode("utf-8")))
    global last_deliver_time, msg_list
    print('curtime: ', curtime)
    if curtime - last_deliver_time > datetime.timedelta(seconds=10):
        test_etl.main(msg_list)
        msg_list = []
        last_deliver_time = curtime
        print('满足发送时间间隔，消息已发送')
    else:
        msg_list.append(str(msg.payload.decode("utf-8")))
        print('未满足发送时间间隔')
    
def on_exec(strcmd):
    print("Exec:",strcmd)

#=====================================================
if __name__ == '__main__':
    mqttc = mqtt.Client(client_id)
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