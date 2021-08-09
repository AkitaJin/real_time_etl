'''
Descripttion: 
version: 
Author: https://blog.csdn.net/yingtian648/article/details/102566971/
Date: 2021-08-09 11:02:21
LastEditors: Jin
LastEditTime: 2021-08-09 11:04:57
'''
#!/user/bin/python3
# -*- codeing:utf-8 -*-
# Time : 2019/8/8 16:44
# Author : LiuShiHua
# Desc :

import json
import paho.mqtt.client as mqtt
import time

#这里的HOST是错误的哈，需要写入你自己的HOST
#这里的HOST是错误的哈，需要写入你自己的HOST
#这里的HOST是错误的哈，需要写入你自己的HOST
HOST = "mqtt.qre.com.cn"
PORT = 1883
# # 同时订阅多个主题方式①使用#通配符
# # '#'号是通配符，订阅匹配#平级及子级主题的所有主题
# # 消息服务质量,0最多一次，1最少一次，2只一次
# subscribe_topic_running = "them/running/#"
# subscribe_topic_command = "them/gsensor/#"
# #同时订阅多个主题方式②订阅主题数组
# subscribe_topic_array = [("them/running/121", 0), ("them/command/121", 2)]
# subscribe_them_all = "them/#"
# publish_topic = "them/command/LNGNW8XLG9"
# 用户名
username = 'preiot'
# 密码
password = 'EnVyCAGYIzK22lEUXGvmEQEe4bVJmtll'
# 订阅主题
topic = "kafka/post/#"
# 客户端ID
CLIENT_ID = "aiit"

def on_connect(client, userdata, flags, rc):
    """
    链接mqtt成功、失败都会回调此函数
    :param client:
    :param userdata:
    :param flags:
    :param rc:0.成功 1.错误的协议版本 2.无效的 client ID  3.服务器不可用  4.错误的用户名或密码  5.无法验证
    :return:
     client.subscribe(subscribe_topic_array )  # 订阅多个主题
    """
    print("Connected with result code " + str(rc))
    client.subscribe(topic)  # 订阅消息


def on_message(client, userdata, msg):
    print("on_message 主题:" + msg.topic + " 消息:" + str(msg.payload.decode('utf-8')))


def on_running_message(client, userdata, msg):
    print("on_running_message 主题:" + msg.topic + " 消息:" + str(msg.payload.decode('utf-8')))


def on_command_message(client, userdata, msg):
    print("on_command_message 主题:" + msg.topic + " 消息:" + str(msg.payload.decode('utf-8')))


# 订阅回调
def on_subscribe(client, userdata, mid, granted_qos):
    print("On Subscribed: qos = %d" % granted_qos)


# 取消订阅回调
def on_unsubscribe(client, userdata, mid, granted_qos):
    print("On unSubscribed: qos = %d" % granted_qos)


# 发布消息回调
def on_publish(client, userdata, mid, granted_qos):
    print("On onPublish: qos = %d" % granted_qos)


# 断开链接回调
def on_disconnect(client, userdata, rc):
    print("Unexpected disconnection rc = " + rc)


# data = {
#     "type": 2,
#     "timestamp": time.time(),
#     "messageId": "9fcda359-89f5-4933-xxxx",
#     "command": "xx/recommend",
#     "data": {
#         "openId": "xxxx",
#         "appId": "XXX",
#         "recommendType": "temRecommend"
#     }
# }
# 注意：不要将以下内容放入if __name__="__main__"：中执行
# 注意：不要将以下内容放入if __name__="__main__"：中执行
# 注意：不要将以下内容放入if __name__="__main__"：中执行
# param = json.dumps(data)
client = mqtt.Client(CLIENT_ID)
client.username_pw_set(username, password)
client.on_connect = on_connect
client.on_message = on_message
"""
 如果要用通配符同时处理多个话题的消息，例如用 sensors/# 匹配 sensors/temperature 和 sensors/humidity 话题，
 可以用 message_callback_add() 设置回调函数：（如下）
 
 如果同时设置了 on_message() 和 message_callback_add() 回调函数，会首先寻找合适的 message_callback_add() 
 定义的话题过滤器，如果没有匹配，才会调用 on_message()
"""
# client.message_callback_add(topic, on_running_message)
# client.message_callback_add(topic, on_command_message)
client.on_subscribe = on_subscribe
client.on_unsubscribe = on_unsubscribe
client.on_publish = on_publish
client.on_disconnect = on_disconnect
client.connect(HOST, PORT, 60)
# client.publish(publish_topic, payload=param, qos=0)  # 发送消息
client.loop_forever()

