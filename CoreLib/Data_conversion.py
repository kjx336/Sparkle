import re
from Sparkle.ClassLib import Message

def QQ(PATH):
    mid=[];a=0;res=[]
    with open(PATH, "r", encoding='utf-8') as f:
        for x in f.readlines():
            x = x.replace('\n', '')
            if (x != '================================================================' and x != '﻿消息记录（此消息记录为文本格式，不支持重新导入）' and x != ''):
                if (x != '\n'):
                    if (re.match('消息对象', x) == None and re.match('消息分组', x) == None and re.match('[图片]对方已成功接收了你发送的离线文件', x) == None and re.match('撤回了一条消息', x) == None and re.match('[图片]你已下载文件', x) == None):
                        mid.append(x)
                        a = a + 1
    for x in range(len(mid)):
        if (re.match(r'\d{4}-\d{1,2}-\d{1,2} \d{1,2}:\d{1,2}:\d{1,2}', mid[x]) != None):
            x1 = re.match(r'\d{4}-\d{1,2}-\d{1,2} \d{1,2}:\d{1,2}:\d{1,2}', mid[x]).group()
            x2 = mid[x][len(x1) + 1:]
            x3=""
            v=x+1
            if v<len(mid):
                while re.match(r'\d{4}-\d{1,2}-\d{1,2} \d{1,2}:\d{1,2}:\d{1,2}', mid[v]) == None:
                    x3=x3+ mid[v]
                    v=v+1
                    if v==len(mid):
                        break
            res.append(Message.Message(x3, x1, x2))
    return res
if __name__ == "__main__":
    get=QQ('C:/Users/kjx33/Desktop/jh21d.txt')
    for x in get:
        print(x.text)
