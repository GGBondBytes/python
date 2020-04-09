from snownlp import SnowNLP
text="今天分析毛不易的歌，太喜欢他的风格了"
s = SnowNLP(text)
print(s.sentiments)






import  numpy as np
from snownlp import SnowNLP
import matplotlib.pyplot as plt
f=open('./Data/mumachengshi.csv', 'r', encoding='utf-8')
list=f.readlines()
sentimentslist=[]
f.close()
for i in list:
    s=SnowNLP(i)
    print(s.sentiments)
    sentimentslist.append(s.sentiments)
plt.hist(sentimentslist,bins=np.arange(0,1,0.01),facecolor='b')
plt.xlabel('情绪指数')
plt.ylabel('分词数量')
plt.title('情感分析图')
plt.rcParams['font.sans-serif']=['SimHei'] #显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
plt.show()






from snownlp import SnowNLP
#获取情感分数
source = open("./Data/mumachengshi.csv","r",encoding='utf-8')
line = source.readlines()
sentimentslist = []
for i in line:
    s = SnowNLP(i)
    print(s.sentiments)
    sentimentslist.append(s.sentiments)

results = []
i = 0
while i<len(sentimentslist):
    results.append(sentimentslist[i]-0.5)
    i = i + 1

#可视化画图
import matplotlib.pyplot as plt
import numpy as np
plt.plot(np.arange(0, 47, 1), results, 'k-')
plt.xlabel('分词数量')
plt.ylabel('情绪指数')
plt.title('情感分析图')
plt.rcParams['font.sans-serif']=['SimHei'] #显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
plt.show()
