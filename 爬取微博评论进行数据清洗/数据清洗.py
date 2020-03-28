# 此函数作用是对初始语料进行分词处理后，作为训练模型的语料
import re


def cut_txt(old_file):
    import jieba
    global cut_file     # 分词之后保存的文件名
    cut_file = old_file + '_cut1.csv'

    try:
        fi = open(old_file, 'r', encoding='utf-8')
    except BaseException as e:  # 因BaseException是所有错误的基类，用它可以获得所有错误类型
        print(Exception, ":", e)    # 追踪错误详细信息

    text0 = fi.read()  # 获取文本内容
    text1 = re.sub("@([\s\S]*?):", "", text0)  # 去除@ ...：
    text2 = re.sub("\[([\S\s]*?)\]", "",text1)  # [...]：
    text3 = re.sub("@([\s\S]*?)", "", text2)  # 去除@...
    text4 = re.sub("[\.\!\/_,$%^*(+\"\']+|[+——！，。？、~@#￥%……&*（）]+", "", text3)  # 去除标点及特殊符号
    text5 = re.sub("[^\u4e00-\u9fa5]", "", text4)  # 去除所有非汉字内容（英文数字）
    new_text = jieba.cut(text5, cut_all=False)  # 精确模式
    str_out = ''.join(new_text)
    fo = open(cut_file, 'w', encoding='utf-8')
    fo.write(str_out)
if __name__ == '__main__':
    cut_txt('./Data/微博评论数据.csv')