from Sparkle.CoreLib import Data_Cleaning
from Sparkle.ClassLib import Messageset
import re
def get_set(PATH):
    l = Data_Cleaning.QQcleaner(PATH)
    res=[]
    for x in l:
        if x.host=="" or re.search(r'.*系统消息.*', x.host) != None:
            continue
        T = []
        T.append(x)
        flag = 0
        for y in res:
            if y.number==x.number:
                flag=1
                y.Append(x)
                break
        if flag == 0:
            res.append(Messageset.MessageSet(T))
    return res
if __name__ == "__main__":
    a = get_set('C:/Users/kjx33/Desktop/7.txt')
    for x in a:
        print(x.host)
        if x.host=="遥梦幽兰":

            for y in x.MessageList:
                print(y.Timer)
