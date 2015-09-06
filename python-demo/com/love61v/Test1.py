'''
Created on 2015-8-18

@author: admin
''' 
from builtins import abs
from _functools import reduce
from _ast import Str
import sys
import os

num = 2
if num == 2:
    print('粉粉是个猪头')
else:
    print('粉粉是个猪猪')
    
    
def power(num, index):
    sums = 1
    while index > 0:
        index = index -1
        sums= sums * num        
    return sums

arg1 = 5
arg2 = 2
print("调用: power(%d , %d) 结果是: "%(arg1,arg2),  power(arg1,arg2))
print("呵呵: 结果=%d" %power(5,2))


arr = []
n = 1
while n < 10:
    arr.append(n)
    n = n +2
    
print("数组: ", arr)
print("取前4个元素:", arr[0:3])
print("取最后一个: ", arr[-1])
print("切: ",arr[:3])
print("双冒号: ", arr[::2])


print("遍历数组: ")
for ele in arr:
    print(ele)
    
print("遍历数组及下标:")
for index,value in enumerate(arr):
    print("数组 : index=%d value=%d " %(index,value))
    
print("遍历map 的key: ")
myMap = {"name": "张三","age": 23, "sex": "M"}
for key in myMap:
    print("map的key=>",key)
    
print("遍历map 的value:")
for value in myMap.values():
    print("map的value=>",value)
    
print("遍历map的key value")
for k,v in myMap.items():
    print("遍历map的key value ==> ","key=", k, " value=", v)
    

#x = 100 
#if isinstance(x, str) is True:
#    print("ok")
#else:
#    print("no")
    
print("================================")
def add(x,y,funs):
    return funs(x) + funs(y)

print("调用add方法结果: " , add(2,-9,abs))

def getMax(x,y,h):
    return h(x,y)

print("调用getMax方法结果: " , getMax(2,-9,max))


def calc(x):
    return x * x

r = map(calc,[1,2,3,4])
print(list(r))


def res(x,y):
    return x +y 

r = reduce(res,[1,3,4,5,6])
print("reduce结果: ",r)


print("排序:",sorted([1,3,4,-22,99,-2],key=abs))

print(sys.path)


print(os.name)


    

