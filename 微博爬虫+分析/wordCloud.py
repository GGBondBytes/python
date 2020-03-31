import jieba
from PIL import Image
from wordcloud import wordcloud
import matplotlib.pyplot as plt
import numpy as np
#英文词云
wc= wordcloud.WordCloud()
words=wc.generate("Choose a life of action, not one of ostentation.")
wc.to_file("./picture/英文词云.png")

#中文词云
wc= wordcloud.WordCloud("font_path='C:/Windows/Fonts/simhei.ttf")
text="今天是个好日子"
cut_text = jieba.cut(text)#分词
cuted=' '.join(cut_text)#词语之间加空格
words=wc.generate(cuted)
wc.to_file("./picture/中文词云.png")



##生成带形状的词云
text =open("./Data/微博评论数据女排20191230.csv",'r',encoding='UTF-8').read()
words_cuted = jieba.cut(text)
results = " ".join(words_cuted)
wc=wordcloud.WordCloud(mask=np.array(Image.open("./picture/china.jpg")),
                       font_path="C:\\Windows\\Fonts\\msyh.ttc",
                       background_color='white').generate(results)
# 显示词云
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.show()
wc.to_file("./picture/形状词云.png")