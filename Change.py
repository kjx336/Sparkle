import re
from aip import AipNlp
import time
import pandas as pd
from Sparkle.CoreLib import Data_Standardization
import math
APP_ID = '18287614'
API_KEY = 'DE2RorqXKSggNtucNo7G3d9z'
SECRET_KEY = 'aEVuMIH9dw6mLuD6DD9FD5V8ANp2GIYY'
client = AipNlp(APP_ID, API_KEY, SECRET_KEY)
a= Data_Standardization.get_set("C:/Users/kjx33/Desktop/myg.txt")
for x in a:
    print(x.host)
m=[]
for x in a:
    for y in x.MessageList:
        m.append(y.text)

print(len(m))
m=list(set(m))
f=len(m)
print(f)
f=f/100000
f=math.ceil(f)
m=m[::f]
result=[]
message=[]
dataf=pd.DataFrame({'message':message,'result':result})
dataf.to_csv('C:/Users/kjx33/Desktop/Alltoresult.csv',mode = 'a',encoding='gbk',index =False)
result.append(1)
message.append("呵呵")
Total=0
for x in m:
    if ((Total % 100) == 0):
        print(Total)
    try:
        reply = client.sentimentClassify(x)
        res=reply['items'][0]['positive_prob']
        message[0]=x
        result[0]=res
        time.sleep(0.5)
        dataf = pd.DataFrame({'message':message, 'result': result})
        dataf.to_csv('C:/Users/kjx33/Desktop/Alltoresult.csv', mode='a', encoding='gbk', index=False, header=None)
        Total=Total+1
    except:
        print(x, "无法解析")
        time.sleep(0.5)
print("总数为：")
print(Total)