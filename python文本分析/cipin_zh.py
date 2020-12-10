import jieba  #统计需要统计的词的频率  OR  统计除去不需要统计的词，剩余其他词的频率
import re
import chardet

def parse(text):
  text = re.sub(r'[^\w]', ' ' , text)
 #text = filter(None, text)
  jieba.load_userdict('D:\\#王琦\\方太烟灶-文本分析\\情感词\\positive_ref.txt')#自定义字典
  words = jieba.lcut(text,cut_all=True) #使用jieba.lcut()返回一个单词列表 评论数据

 #加载停用词
 #stopwords = [line.strip() for line in open('E:\\test\\ciyun_tu\\filter.txt',encoding='utf-8').readlines()]  #不需要统计频率的词组、组合

 #words_dict = {} #创建一个字典，用于生成单词，频率
 #for word in words:  
    #不在停用词表中  
  #if word not in stopwords:
   #if len(word) == 1:
    #continue
   #else:  
    #words_dict[word] = words_dict.get(word,0) + 1 #get不到word就创建word为下标的值0+1，如果get到了就在word的值上加1，然后更新字典
#以上注释为统计停用词以外的词频数量脚本

  textwords = [line.strip() for line in open('D:\\#王琦\\方太烟灶-文本分析\\情感词\\positive_ref.txt',encoding='utf-8').readlines()]  #需要统计频率的词组、组合
  print(textwords)
  word_dict={}#词频文件

  for i in words:
    #print(i)
    if i in textwords:
      word_dict[i] = word_dict.get(i,0) +1
      #print(word_dict)
  #words_dict = list(word_dict)
  #print(type(word_dict))
#以上为统计已有短语数量部分脚本，已有短语存储在count_words文件中


  words_dict_sorted = sorted(word_dict.items(), key=lambda kv:kv[1], reverse = True) 
  #print(words_dict_sorted)
  return words_dict_sorted

with open('D:\\#王琦\\方太烟灶-文本分析\\posi_all_comment.txt', 'r', encoding = 'utf-8',errors='ignore') as fin:#评论文件
  text = fin.read()
  print(text)
  #print(chardet.detect(text))
#stopwords = [line.strip() for line in open('G:\\test\\html\\cipin_analysis\\filter.txt',encoding='gb18030',errors='ignore').readlines()]  

word_and_freq = parse(text)

with open('D:\\#王琦\\方太烟灶-文本分析\\posi_all_pin.txt', 'w') as fout:
  for word, freq in word_and_freq:
    fout.write("{} {}\n".format(word, freq))