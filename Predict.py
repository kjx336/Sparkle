from sklearn.externals import joblib
import jieba
from Sparkle.CoreLib import Data_Standardization


class FormatError(Exception):
    def __init__(self):
        print("Format Error,please try again.")

def ret(text,PATH_Model):
    try:
        if not isinstance(text, str) and not isinstance(text, list):
            raise FormatError
        if isinstance(text, str):
            str_cut = []
            str_cut.append(" ".join(jieba.cut(text)))
            clf = joblib.load(PATH_Model)
            tl = clf.predict(str_cut)[0]
            return tl
        if isinstance(text, list):
            str_cut = []
            for x in text:
                str_cut.append(" ".join(jieba.cut(x)))
            clf = joblib.load(PATH_Model)
            tl = clf.predict(str_cut)
            return tl
    except:
        pass

def QQget_res(PATH_Data,PATH_Model):
    me= Data_Standardization.get_set(PATH_Data)
    for x in me:
        for y in x.MessageList:
            r=ret(y.text,PATH_Model)
            y.score=r
    for x in me:
        x.set_score()
    return me



if __name__ == "__main__":
    a=QQget_res('C:/Users/kjx33/Desktop/7.txt',"E:\\myhub\\wechat_predicting\\Sparkle\\ModelLib\\train_model1.m")
    for x in a:
        print(x)


