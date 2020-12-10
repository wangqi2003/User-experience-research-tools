#设置颜色
# coding=UTF-8
import jieba
from imageio import imread
from wordcloud import WordCloud
import matplotlib.colors as colors 
import numpy as np # numpy数据处理库
from PIL import Image # 图像处理库

#mask=np.array(Image.open('xxx.jpg'))。其中from PIL import Image 
#mask = imread('D:\\#王琦\\方太烟灶-文本分析\\circle.png')#地球形
mask = np.array(Image.open('D:\\#王琦\\方太烟灶-文本分析\\circle.jpg')) # 定义词频背景

color=['#448ee4', '#49759c',  '#2976bb',  '#75bbfd',  '#0a437a',  '#276ab3',  '#2c6fbb',  '#056eee',  '#8ab8fe']#设置颜色 蓝色：'#448ee4', '#49759c',  '#2976bb',  '#75bbfd',  '#0a437a',  '#276ab3',  '#2c6fbb',  '#056eee',  '#8ab8fe',   红色： ,'#e50000',  '#bb3f3f',  '#840000',  '#db5856',  '#c44240',  '#c27e79',  '#ff796c',  '#fa4224',  '#29e8e'
colormap=colors.ListedColormap(color)#设置颜色

with open('D:\\#王琦\\方太烟灶-文本分析\\positive_pin\\posi_all_pin.txt',encoding='utf-8') as fp:    #D:\#王琦\方太烟灶-文本分析\positive_pin     D:\#王琦\方太烟灶-文本分析\negative_pin
    
    words = fp.read()  

 
wordshow = WordCloud(background_color='#FFFFFF',
                     width=800,
                     height=600,
                     max_words=200,
                     max_font_size=80,
                     prefer_horizontal=1,
                     relative_scaling=0.7,
                     colormap=colormap,
                     font_path="C:\\Program Files (x86)\\Microsoft Office\\root\\vfs\\Fonts\\private\\STSONG.TTF",    #用微软雅黑作为字体显示效果
                     mask = mask,             #转为词云形状
                      ).generate(words)
 
wordshow.to_file('D:\\#王琦\\方太烟灶-文本分析\\pictures\\all_posi_tu.png')  # 转换成图片  D:\#王琦\方太烟灶-文本分析\pictures
