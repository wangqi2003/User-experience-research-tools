import pandas as pd
import xlsxwriter    #调用模块

f = open('D:\\#王琦\\方太烟灶-文本分析\\情感词\\positive_ref.txt','r',encoding='utf-8')        #全

lines = f.readlines()      #把全部数据文件读到一个列表lines中


for line in lines:       #把lines中的数据逐行读取出来

    list1 = line.split('\n')   #处理逐行数据：，然后把处理后的行数据返回到list列表中
print(list1) 

m=open('D:\\#王琦\\方太烟灶-文本分析\\positive_pin\\posi_all_pin.txt','r',encoding='utf-8')        #部分best  fotile  haier  midea  robam  vatti

lines2 = m.readlines()      #把全部数据文件读到一个列表lines中

for line2 in lines2:       #把lines中的数据逐行读取出来
    
    list2 = line2.strip('\n').split(',')   #处理逐行数据：strip表示把头尾的'\n'去掉，split表示以空格来分割行数据，然后把处理后的行数据返回到list列表中


workbook = xlsxwriter.Workbook('D:\\#王琦\\方太烟灶-文本分析\\positive_pin\\posi_all_pin.xlsx')     #新建文件
 
sheet_all = workbook.add_worksheet('all_ci')             #新建sheet
 
sheet_part = workbook.add_worksheet('part_ci') 

bold = workbook.add_format({'bold': True})

new_list=list()

for i in range(len(lines2)):#63
    
    a,b=lines2[i].split(' ')
    name=a
    count=b
    #print(a,b)
    list_list=list()
    list_list.append(name)
    list_list.append(count)
    sheet_part.write(i,1,name)
    sheet_part.write(i,2,count)
    list_eve=list_list
    #print(list_eve)
    new_list.append(list_eve)
    #print(new_list[16])
    
new_list2=list()

for i in range(len(lines)):#63
    
    a=lines[i]
    name=a
    count=0
    #print(a,b)
    list_list=list()
    list_list.append(name)
    list_list.append(count)
    sheet_all.write(i,1,name)
    sheet_all.write(i,2,count)
    list_eve=list_list
    #print(list_eve)
    new_list2.append(list_eve)
#print(new_list2[16])

workbook.close()



