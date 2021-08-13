'''
Descripttion: 
version: 
Author: Jin
Date: 2021-08-11 14:36:11
LastEditors: Jin
LastEditTime: 2021-08-12 14:39:00
'''
import requests
import pandas as pd

url = 'http://10.0.102.47:8003/api/algorithm/start/95'
df_input = pd.DataFrame([1,2,3])
df_tensor = pd.DataFrame([2,3,4])

data = {
    'path1' : '12312.xlsx',
    'path2' : df_tensor
}
response = requests.post(url=url,data=data).json()
print(response)

