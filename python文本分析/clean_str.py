import re
import openpyxl


 
def find_chinese(file):
    pattern = re.compile(r'[^\u4e00-\u9fa5]')
    chinese = re.sub(pattern, '', file)
    print(chinese)
 
#def find_unchinese(file):
    #pattern = re.compile(r'[\u4e00-\u9fa5]')
    #unchinese = re.sub(pattern,"",file)
    #print(unchinese)
 
 



if __name__ == "__main__":
    line = excel
    print("原文：")
    
    print("保留中文：")
    find_chinese(line)

