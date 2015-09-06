'''
Created on 2015-8-21

@author: admin
'''
from idlelib.IOBinding import encoding
from fileinput import close


# 读取文件
path = "d:/aa.txt"
with open(path, mode='r', closefd=True) as f:
    for line in f.readlines():
        print(line.strip())

f.close()
        
        
# 写文件
destPath = "d:/bb.txt"
with open(destPath, mode='w',encoding='utf-8', closefd=True) as fos:
    for i in range(1,10):
        fos.write("你好: %s"%i)
        
    
        
        
