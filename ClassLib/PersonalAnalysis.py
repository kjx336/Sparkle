from Sparkle import Predict
import time
import math
class TimeAnalysis():
    def __init__(self,t):
        self.MessageList=[]
        self.score=None
        self.Timer=t
        self.Time=time.strftime("%Y--%m--%d",time.localtime(self.Timer))
    def Append(self, m):
        self.MessageList.append(m)
    def set_score(self):
        t = len(self.MessageList)
        s = 0
        for x in self.MessageList:
            s = s + x.score
        self.score = s / t

class PersonalAnalysis():
    def SortTime(self):
        for x in self.messageset.MessageList:
            x.Timer =(math.ceil(x.Timer/self.T))*self.T
    def Sort(self):
        for x in self.messageset.MessageList:
            flag=0
            if len(self.timeanalysislist)==0:
                Ls=TimeAnalysis(x.Timer)
                Ls.Append(x)
                self.timeanalysislist.append(Ls)
                continue
            for y in self.timeanalysislist:
                if y.Timer==x.Timer:
                    y.Append(x)
                    flag=1
                    break
            if flag==1:
                continue
            Ls = TimeAnalysis(x.Timer)
            Ls.Append(x)
            self.timeanalysislist.append(Ls)
        for x in self.timeanalysislist:
            x.set_score()

    def __init__(self,m,interval=1):
        self.T=interval*86400
        self.messageset=m
        self.SortTime()
        self.timeanalysislist=[]
        self.Sort()
        self.host=self.messageset.host

if __name__ == "__main__":
    a=Predict.QQget_res('C:/Users/kjx33/Desktop/fly.txt',"E:\\myhub\\wechat_predicting\\Sparkle\\ModelLib\\train_model1.m")
    l=[]
    for x in a:
        l.append(PersonalAnalysis(x))
    for x in l:
        print(x)





