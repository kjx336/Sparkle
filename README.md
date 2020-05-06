# Sparkle(星火)情感分析平台
***break the silence and light up the darkness***

您快速、简洁、开放、自由的中文社交媒体情感分析助理

## 简介：

Sparkle(星火)情感分析平台是一个基于sklearn/jieba的Python情感分析框架。其功能强大的接口可以高效应用于社交媒体情感分析中，开放的模型训练功能可以让您快速训练属于您自己的模型并使用。

得益于其封装完善的接口，它可以对直接导出的QQ历史记录进行一键化处理，分发给情感分析中枢，依据不同的模型以完成具体的功能。您还可以将其与功能强大的itchat包共同使用，对微信消息进行实时的情感分析

在不同语境下，您可以调用我们封装完善的模型训练接口，一键化训练您自己的模型并使用

除了拥有情感分析的作用，Sparkle(星火)还提供了多项一键化丰富实用的工具和输出方式，您使用简单的几行代码就可以完成大量的操作

Sparkle(星火)在其底层使用一组强大的正则表达式提取QQ历史记录中的时间、名称和消息并进行标准化、脱敏等处理。在模型训练与预测方面，Sparkle(星火)调用了sklearn/jieba两个开放库。前者是一个强大的机器学习库，后者是一个广泛应用的中文分词库

需要注意的是，Sparkle(星火)使用的python为python3版本，jieba为0.41版本，sklearn内的numpy为1.16.4版本。若您测试本文档中的样例（如使用matplotlib）出现报错的现象，请您尝试提升/降低您已安装的其他库的版本。我们也会在样例前说明确定兼容的版本号，建议您将各版本号与我们的样例保持一致，以免出现不可预期的错误。
## 安装：

### Sparkle(星火)
您在克隆本 Git 仓库后，即可完成安装

### jieba

您可以前往[jieba的github地址](https://github.com/fxsjy/jieba),根据其使用教程安装jieba。

### sklearn

您可以前往[sklearn 中文文档](http://www.scikitlearn.com.cn),根据其安装指南安装sklearn。

### QQ电脑版

您可以前往[I'm QQ - 每一天,乐在沟通](https://im.qq.com/download),挑选您合适的电脑端QQ版本进行安装。
## 开始使用：

在您将一切安装成功并就绪后，您就已经做好了使用Sparkle(星火)完成一个最小样例的准备

### 您的第一个情感分析样例:

```
from Sparkle import Predict
if __name__ == "__main__":
    text="好的"
    result=Predict.ret(text)
    print(result)

    text = ["可以","不行"]
    result = Predict.ret(text)
    print(result)

>>1
>>[1 0]
```
其中，
>` if __name__ == "__main__":`

语句块的前三行代码将依次执行：
* 设定一个被测试的文本
* 调用Predict.ret方法，进行情感分析并返回一个预测值
* 打印这个预测值

如您所见，在后三行中，基于ret方法的健壮性，该方法可以自动判定您传入的文本是一个字符串还是列表，并将返回值做相应调整

> 提示：若您打印出的返回值为None，请您手动改变第四行、第八行中可选参数PATH_Model的绝对路径值。譬如您的Sparkle安装在了E:\\myhub\\wechat_predicting文件夹下，您只需要将这两行改为：
```
result = Predict.ret(text, PATH_Model="E:\\myhub\\wechat_predicting\\Sparkle\\ModelLib\\train_model1.m")
```
程序就可以照常运作并输出结果了。

### 现在开始使用Sparkle(星火)（*样例2*）:

Sparkle(星火)的强大之处在于，它可以对直接导出的QQ历史记录文件进行一键分析。下面的实例将让您简单了解这项功能

首先，您需要进入QQ电脑版中“消息管理”模块，选择您要分析的聊天（可以是多人的群，也可以是一对一的聊天），右键点击“导出消息记录”，将“保存类型”设置为“文本文件”，即txt文件，选择路径和名称后，点击保存

之后你需要在新的py文件中输入以下代码：
```
from Sparkle import ExportResults
if __name__ == "__main__":
    a = ExportResults.Export('C:/Users/kjx33/Desktop/7.txt',"E:\\myhub\\wechat_predicting\\Sparkle\\ModelLib\\train_model1.m")

>>host: 用户1
>>messagelist: 336  score: 0.6815476190476191
>>host: 用户2
>>messagelist: 456  score: 0.5701754385964912
```
这样，您本组聊天中所有用户的情感分析得分就会显示出来了。


### 使用Sparkle(星火)监测情感波动(*样例3*):

Sparkle(星火)精心设计的算法可以帮助您在上一个样例的基础上，监测用户的情感波动。您可以使用强大的python绘图工具matplotlib配合Sparkle(星火)进行使用

> 提示：以下样例中，matplotlib版本号为：3.0.3。我们建议您使用pip install matplotlib==3.0.3命令将您的matplotlib设定为与我们相同的版本，以免使您的程序出现预期之外的错误

```
from Sparkle import ExportResults
from Sparkle.ClassLib.PersonalAnalysis import PersonalAnalysis
import matplotlib.pyplot as plt
if __name__ == "__main__":
    a = ExportResults.Export('C:/Users/kjx33/Desktop/7.txt',"E:\\myhub\\wechat_predicting\\Sparkle\\ModelLib\\train_model1.m") #此处需修改您的文件和模型路径
    l = []
    for x in a:
        l.append(PersonalAnalysis(x, interval=30))
    for x in l:
        print(x.host)
        xL = []
        yL = []
        for y in x.timeanalysislist:
            print(y.Time, y.score)
            xL.append(y.Time)
            yL.append(y.score)
        plt.plot(xL, yL, marker='*', ms=10, label=x.host)
    plt.xticks(rotation=45) # x轴标签倾斜45度避免重叠
    plt.rcParams['font.sans-serif'] = ['KaiTi']  # 指定字体为楷体
    plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题
    plt.xlabel("日期")
    plt.ylabel("情感得分")
    plt.legend(loc="upper left")
    plt.savefig("7.png") # 此处需指定图像保存的名称，不保存可以省略
    plt.show()

>>host: 用户1
>>messagelist: 336  score: 0.6815476190476191
>>host: 用户2
>>messagelist: 456  score: 0.5701754385964912
>>用户1
>>2019--11--10 0.5769230769230769
>>2019--12--10 0.75
>>2020--01--09 0.6578947368421053
>>2020--02--08 0.6666666666666666
>>2020--03--09 0.7205882352941176
>>2020--04--08 0.6730769230769231
>>2020--05--08 0.7333333333333333
>>用户2
>>2019--11--10 0.75
>>2019--12--10 0.6842105263157895
>>2020--01--09 0.5869565217391305
>>2020--02--08 0.5
>>2020--03--09 0.5714285714285714
>>2020--04--08 0.5503875968992248
>>2020--05--08 0.4861111111111111
```
到这里一切OK的话，您应该收到了由matplotlib为您绘制的分时情感波动图。这一张图的出现意味着您至此已经熟悉了解了Sparkle(星火)最基本、最核心的操作，可以开始使用Sparkle(星火)完成更优秀的工作！

## 刚刚发生了什么？

在上一节，您已经成功完成了一次基本的情感分析并获得了结果。您是否在疑惑，这项工作是如何完成的呢？在这一节，我将以样例3为例，为您初步解释Sparkle(星火)的工作流程。

### 从QQ历史记录到MessageSet实例

当您指定了一项QQ历史记录路径后，Sparkle(星火)的最底层代码就会开始运作。经过数组正则表达式后，您的QQ历史记录会经过数据标准化、数据清洗、数据脱敏的过程，最终会形成大量Message对象实例，并根据发送方名称的不同转变为多组MessageSet实例。

### 从MessageSet实例到预测结果

当数组MessageSet对象被传入Predict.QQget_res后，该方法会逐Message调用Predict.ret方法，使用指定模型为各Message的情感得分进行赋值。随后会逐个调用MessageSet.set_score方法，计算这个MessageSet的平均情感得分。

### 从MessageSet到PersonalAnalysis

如果您需要得到详细的分时分析报告而不是一个笼统的平均值，您只需要将各MessageSet传入PersonalAnalysis类并指定分时时长interval，PersonalAnalysis强劲的构造函数会自动帮您将一个MessageSet依据您指定的interval转化为多个分时的TimeAnalysis实例，并形成一个完整的PersonalAnalysis实例返回。这样，您就获得了一份完整的PersonalAnalysis报告。您可以像样例3一样通过matplotlib进行可视化处理，方便您进行分析。

至此，您已经大概了解了Sparkle(星火)的工作原理和工作流程。下面我将为您具体介绍Sparkle(星火)内定义的各种类与方法，帮助您实现一些更棒的功能！

## Sparkle(星火)中类的属性与方法

在这一节中，我将详细为您介绍Sparkle(星火)中定义的四个类的属性与方法。这些类被定义在ClassLib中，您可以在该文件夹下找到他们。
*注：PersonalAnalysis类和TimeAnalysis类均定义在PersonalAnalysis文件中*

### Message类

Message类是Sparkle(星火)中最基础的类，描述的是一条单个的消息。它包括了了一条消息的发送人全称、发送人识别码、时间、时间戳、正文文本、情感得分等多项属性。

属性名称  | 类型| 介绍
------------- | -------------| -------------
host  | String| 发送人全称
number  | String| 发送人识别码。在一对一聊天中和host相同；在群聊中为发送人的QQ号
Time  | String| 时间，为"%Y-%m-%d %H:%M:%S"格式
Timer  | int| 时间戳
text  | String| 正文文本
score  | int| 情感得分，取值为0或1

| 方法名称 | 介绍                    |
| ------------- | ------------------------------ |
| `__init__(self, text, Time,host)`      | 构造函数，传入正文内容、时间和发送人       |
| `__str__(self)`   | 返回属性值，内含时间、发送人、正文和情感得分    |
| `set_score(self,s)`   | **传入设置该正文的情感分析值**     |

### MessageSet类

MessageSet类是Message类的扩展。它是某一个用户的所有Message的集合。

属性名称  | 类型| 介绍
------------- | -------------| -------------
host  | String| 发送人全称
number  | String| 发送人识别码。在一对一聊天中和host相同；在群聊中为发送人的QQ号
MessageList  | list| list容器，内含的一组与host对应的Message
score  | float| 情感得分，取值为0至1之间的小数。**在调用之前需要使用set_score(self)方法初始化**

| 方法名称 | 介绍                    |
| ------------- | ------------------------------ |
| `__init__(self,messagelist)`      | 构造函数，传入messagelist以初始化host、number、MessageSet       |
| `__str__(self)`   | 返回属性值，内含发送人、MessageSet长度和平均情感得分    |
| ` Append(self,message)`   | 向本MessageSet中的MessageList追加一条Message     |
| `set_score(self)`   | **遍历MessageSet，根据平均得分设置score**     |

### TimeAnalysis类与PersonalAnalysis类

TimeAnalysis类和PersonalAnalysis类是为解决分时分析而构造的。TimeAnalysis类描述的是某一个用户在某一时段所有Message的集合。PersonalAnalysis类是某一用户全体TimeAnalysis实例的集合

首先为您介绍TimeAnalysis类

属性名称  | 类型| 介绍
------------- | -------------| -------------
Time  | String| 时间，为"%Y-%m-%d %H:%M:%S"格式
Timer  | int| 时间戳
MessageList  | list| list容器，内含的一组相同host的Message
score  | float| 情感得分，取值为0至1之间的小数。**在调用之前需要使用set_score(self)方法初始化**

| 方法名称 | 介绍                    |
| ------------- | ------------------------------ |
| `__init__(self,t)`      | 构造函数，传入时间戳以初始化       |
| ` Append(self,message)`   | 向本MessageList中追加一条Message     |
| `set_score(self)`   | **遍历MessageList，根据平均得分设置score**     |

最后为您介绍PersonalAnalysis类

属性名称  | 类型| 介绍
------------- | -------------| -------------
host  | String| 发送人全称
T  | int| 分时参数，PersonalAnalysis类用这个参数控制分时跨度大小
MessageSet  | MessageSet| 对应host的MessageSet
timeanalysislist  | list| list容器，内含一组与本PersonalAnalysis实例的host参数相同的TimeAnalysis实例

| 方法名称 | 介绍                    |
| ------------- | ------------------------------ |
| `__init__(self,m,interval=1)`      | 构造函数，传入一个MessageSet实例m和分时跨度值interval（单位为：日，默认为一日）以初始化这个PersonalAnalysis       |

## Sparkle(星火)API列表

### Predict.ret(text,PATH_Model):
**说明**

ret函数可以帮助您对某一个中文语句用您指定的模型进行情感分析

**参数**

字段名  | 数据类型| 默认值| 说明
------------- | -------------| -------------| -------------
text  | String| -| 您想要进行情感判断的一个字符串
PATH_Model  | String| -| 您想要使用的模型的绝对路径
**响应数据**

字段名  | 数据类型| 说明
------------- | -------------| -------------
tl  | int| 判定的返回值，为1或0

### Predict.QQget_res(PATH_Data,PATH_Model):
**说明**

QQget_res函数可以帮助您对某一个已导出的QQ聊天记录用您指定的模型进行情感分析

**参数**

字段名  | 数据类型| 默认值| 说明
------------- | -------------| -------------| -------------
PATH_Data  | String| -| 您想要进行情感判断的QQ历史记录的绝对路径
PATH_Model  | String| -| 您想要使用的模型的绝对路径
**响应数据**

字段名  | 数据类型| 说明
------------- | -------------| -------------
me  | list| 一个由一组MessageSet组成的列表

### ExportResult.Export(PATH_Data,PATH_Model,to_cmd=True,to_txt=False,Filename="myResult"):
**说明**

ExportResult.Export函数可以帮助您对某一个已导出的QQ聊天记录用您指定的模型进行情感分析并快速导出

**参数**

字段名  | 数据类型| 默认值| 说明
------------- | -------------| -------------| -------------
PATH_Data  | String| -| 您想要进行情感判断的QQ历史记录的绝对路径
PATH_Model  | String| -| 您想要使用的模型的绝对路径
to_cmd  | String| True| 当值为True时，将向命令行输出情感判断结果
to_txt  | String| False| 当值为True时，将向一个txt文件输出情感判断结果
Filename  | String|"myResult"| 当`to_txt`字段为True时，此字段将决定输出文件的文件名。您也可以在此定义您需要的绝对路径

**响应数据**

字段名  | 数据类型| 说明
------------- | -------------| -------------
a  | list| 一个由一组MessageSet组成的列表，与ExportResult.Export方法返回的相同

### Data_Standardization.get_set(PATH_Data):
**说明**

Data_Standardization.get_set参数可以帮助您将一个您指定路径的QQ历史记录转化为一个包含一组MessageSet的列表并返回

**参数**

字段名  | 数据类型| 默认值| 说明
------------- | -------------| -------------| -------------
PATH_Data  | String| -| 您想要进行情感判断的QQ历史记录的绝对路径

**响应数据**

字段名  | 数据类型| 说明
------------- | -------------| -------------
res  | list| 一个由一组MessageSet组成的列表，**其score值还未被初始化**

## 下一步做什么？

在前面的章节中，您已经掌握了Sparkle(星火)的具体操作方法，可以编写更为完整的程序了。

您可以将Sparkle(星火)与itchat联合使用，完成对微信聊天的实时情感监控

您也可以将Sparkle(星火)与酷Q联合使用，完成对QQ聊天的实时情感监控

您也可以将Sparkle(星火)嵌入您的爬虫，分析大众点评、微博等社交软件的情感走势

## 作者附：

There is a sparkle in your eyes。

在过去的数年，我国抑郁症患者人数持续增长。现如今，有权威组织预测我国抑郁症患者人数已经接近9000万。如果不加干预，在未来的数年之内，我国抑郁症患者人数可能破亿。更有报告指出，我国大学生群体中，抑郁症患病率接近29%。

Sparkle(星火)开发的初衷之一，是完成一款易于上手的社交媒体情感分析包，使心理工作者/学生工作者可以快速搭建一款职工/大学生心理安全检测系统。在浩如烟海的社交网络中，寻找那些需要被关注的人，为心理工作者/学生工作者提供预警线与干预线。打破痛苦的沉寂，提供一星温暖的光明
。
根据与一些心理专家的交流，我们在此提供一些建议：

预警线：当使用系统自带模型train_model1分析出某一成员在60天内情感分析值均低于0.5，判定该成员的心情长时间不佳，有转向轻度抑郁症的风险，请心理工作者/学生工作者留意这名成员平时的行为举止。若观察该成员平时的行为举止符合轻度抑郁症的特征，请心理工作者/学生工作者进行干预。

干预线：当使用系统自带模型train_model1分析出某一成员在14天内情感分析值均低于0.35，判定该成员的心情短时间内出现明显低落，有已经成为轻度抑郁症的可能。请心理工作者/学生工作者留意这名成员平时的行为举止，在必要时进行干预。

不过，在社交网络中寻找需要关注的群体，帮助其倾诉，并帮助缓解抑郁问题，对于抑郁症人群来说也可以算是Sparkle(闪耀)了。

愿世间充满爱，愿每个人都能关注抑郁症群体。

***Sparkle,break the silence and light up the darkness***
<br>*Signed-off-by: 遥梦幽兰kzx <kjx336@163.com>*