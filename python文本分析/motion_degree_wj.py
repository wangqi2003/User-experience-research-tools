import pandas as pd
import numpy as np

#读取原始正向评论信息（excel文件要先去除换行符等，clean公式）
data=pd.read_excel(u'D:/05-工作/伊飒尔/海尔大数据项目/data/VIOMI_positive.xlsx')
#读取维度-语料文件
data_positive_words=pd.read_excel(u'D:/05-工作/伊飒尔/海尔大数据项目/data/positive-维度.xlsx')
# print(data_positive_words.head())

list0=[]
list_words=[]
list_num=[]
#读取分好的词频文件
for line in open(u'D:/05-工作/伊飒尔/海尔大数据项目/data/VIOMI_positive_pin.txt'):
    list=line.strip("\n").split(" ")
    list_words.append(list[0])
    # print(list_words)
    list_num.append(list[1])
list_words=list_words[1:]
# print(len(list_words))


dict={}
new1=[]
new=[]
new2=[]

#汇总每条语料的情感度
for word in list_words:
    new1 = []
    new = []
    # print(word)
    for i in range(len(data)):
        # print(len(data))
        if word in data["评论内容"][i]:
            #统计分词在句子中出现频次
            n = data["评论内容"][i].count(word)
            # print(data["评论内容"][i])
            # print(data["正向情感评分"][i])
            dict[word]=data["正向情感评分"][i]*n
            new.append(dict.get(word))
            new1=sum(new)
        else:
            pass
    new2.append(new1)

#合并语料、语料频次、语料总情感度
out_data=pd.DataFrame(
    [new2,
    list_num[1:],
    list_words]
)

out_data=out_data.T
out_data.columns=["情感度汇总","频次","描述"]
out_data["频次"]=out_data["频次"].astype(int)

#每条语料的平均情感度
out_data["情感度"]=out_data["情感度汇总"]/out_data["频次"]
# print(out_data)

#合并语料和维度文件，增加每条语料对应的维度信息
result_data=pd.merge(out_data,data_positive_words,how="left",on="描述")
#文件输出
result_data.to_csv(u"D:/05-工作/伊飒尔/海尔大数据项目/data/VIOMI_positive_emotion.csv",encoding="utf_8_sig")

