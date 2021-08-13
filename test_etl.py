'''
Descripttion: MQTT调用的伪脚本
version: 
Author: Jin
Date: 2021-08-11 10:47:40
LastEditors: Jin
LastEditTime: 2021-08-11 13:39:08
'''
import time
import datetime

def main(msg):
    print("——————————————————————————来自调用的伪代码——————————————————————————")
    print(msg)
    # t1 = datetime.datetime.now()
    # time.sleep(2)
    # t2 = datetime.datetime.now()
    # print((t2-t1)>datetime.timedelta(seconds=1))

if __name__ == '__main__':
    main('111')