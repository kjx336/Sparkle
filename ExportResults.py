from Sparkle import Predict
from Sparkle.ClassLib.PersonalAnalysis import PersonalAnalysis
import matplotlib.pyplot as plt
def Export(PATH_Data,PATH_Model,to_cmd=True,to_txt=False,Filename="myResult"):
    a=Predict.QQget_res(PATH_Data,PATH_Model)
    if to_cmd == True:
        for x in a:
            print(x)
    if to_txt == True:
        s=""
        for x in a:
            s=s+x.__str__()+"\n"
        data = open(Filename+".txt", 'w')
        print(s, file=data)
        data.close()

    return a





if __name__ == "__main__":
    a = Export('C:/Users/kjx33/Desktop/7.txt',"E:\\myhub\\wechat_predicting\\Sparkle\\ModelLib\\train_model1.m")
    l = []
    for x in a:
        l.append(PersonalAnalysis(x,interval=30))
    for x in l:
        print(x.host)
        xL = []
        yL = []
        for y in x.timeanalysislist:
            print(y.Time,y.score)
            xL.append(y.Time)
            yL.append(y.score)
        plt.plot(xL, yL, marker='*', ms=10, label=x.host)
    plt.rcParams['font.sans-serif'] = ['KaiTi']  # 指定默认字体
    plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题
    plt.xlabel("日期")
    plt.ylabel("情感得分")
    plt.legend(loc="upper left")
    plt.savefig("7.png")
    plt.show()