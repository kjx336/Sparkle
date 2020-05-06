from Sparkle.CoreLib import Data_conversion
import re
def QQcleaner(PATH):
    get = Data_conversion.QQ(PATH)
    m1=[]
    for x in get:
        x.text = x.text.replace("[图片]", "")
        x.text = x.text.replace("[表情]", "")
        x.text = x.text.replace("[闪照]请使用新版手机QQ查看闪照。", "")
        x.text = x.text.replace("[发起投票]", "")
        x.text = x.text.replace("[QQ红包]请使用新版手机QQ查收红包。", "")
        x.text = x.text.replace("[群签到]请使用新版QQ进行查看。", "")
        if re.search(r'.*@(.*) .*',x.text)!=None:
            re_re=re.search(r'.*@(.*) .*',x.text).group()
            for a in re_re:
                x.text = x.text.replace(a, "")
        if re.search(r'.* 参加了投票 .*', x.text) != None or re.search(r'.*撤回了一条消息.*', x.text) != None or re.search(r'.*邀请.*加入了本群。', x.text) != None or re.search(r'.*领取了.*的红包。', x.text) != None:
            x.text=""
        if x.text!="" :
            m1.append(x)
    return m1
if __name__ == "__main__":
    a = QQcleaner('C:/Users/kjx33/Desktop/7.txt')
    for x in a:
        print(x.text)
