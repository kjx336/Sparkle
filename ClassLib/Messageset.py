class MessageSet():
    def __init__(self,messagelist):
        self.score = 0
        self.MessageList = messagelist
        self.host=self.MessageList[0].host
        self.number=self.MessageList[0].number
    def __str__(self):
        return "host: " + self.host + "\nmessagelist: " + str(len(self.MessageList)) + "  score: " + str(self.score)
    def Append(self,message):
        self.MessageList.append(message)
    def set_score(self):
        t=len(self.MessageList)
        s=0
        for y in self.MessageList:
            s=s+y.score
        self.score=s/t
    def get_score(self):
        return self.score
