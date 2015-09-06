'''
Created on 2015-8-20

@author: admin
'''
class Person(object):
    
    def __init__(self,name,age):
        self.__name = name
        self.__age = age
        
    def setName(self,name):
        self.__name = name
    
    def getName(self):
        return self.__name
    
    def setAge(self,age):
        self.__age = age
    
    def getAge(self):
        return self.__age
    
    
person = Person("李四",20)
print(person.getAge(),person.getName())