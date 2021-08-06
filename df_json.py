'''
Descripttion: 
version: 
Author: Jin
Date: 2021-08-06 08:55:18
LastEditors: Jin
LastEditTime: 2021-08-06 09:38:42
'''
import json
from kafka.structs import RetryOptions
import pandas as pd
import test_kafka_producer as kp
import test_kafka_consumer as kc
'''
name: json转至df
msg: 
param {*} json
return {*}
'''
def json_to_df(json):
    df = pd.read_json(json,encoding="utf-8", orient='records')
    return df


'''
name: df转至json
msg: 
param {*} df
return {*}
'''
def df_to_json(df):
    json = df.to_json(orient="records",force_ascii=False)
    # json = df.to_json(orient="records",force_ascii=False)
    print(json)
    return json


if __name__ == '__main__':
    # 生成测试用的json
    obj="""[{"姓名": "张三",
        "住处": "天朝",
        "宠物": "koala",
        "兄弟": "李四"
        },{"姓名": "李四",
        "住处": "天朝",
        "宠物": "cat",
        "兄弟": "张三"}]"""
    with open("test.json","w",encoding="utf-8") as f:
        f.write(obj)
    # print(obj)
    
    tmp_df = json_to_df("test.json")

    tmp_json = df_to_json(tmp_df)
    print(tmp_json)

    # 测试发送JSON至kafka
    address = "192.168.51.93:9092"
    topic = 'test_topic'
    tiny_json = {'key1': 'value1'}
    kp.kafka_producer_json_srlz(address, topic, tmp_json)