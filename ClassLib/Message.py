import time
import re
class Message:
    def __init__(self, text, Time,host):
        self.score=0
        self.text = text
        self.Time = Time
        self.host = host
        self.Timer = int(time.mktime(time.strptime(self.Time, "%Y-%m-%d %H:%M:%S")))
        self.number = self.host
        if re.search('.*\((.*)\).*', self.host) != None:
            self.number = re.search('.*\((.*)\).*', self.host).group(1)
        if re.search('.*\<(.*)\>.*', self.host) != None:
            self.number = re.search('.*\<(.*)\>.*', self.host).group(1)
    def __str__(self):
        s = "time:" + self.Time + "host:" + self.host + "\ntext:" + self.host + "score:" + str(self.score)
        return s
    def get_score(self):
        return self.score
    def get_text(self):
        return self.text
    def get_Time(self):
        return self.Time
    def get_host(self):
        return self.host
    def get_Timer(self):
        return self.Timer
    def set_score(self,s):
        self.score=s

