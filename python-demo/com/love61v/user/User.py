'''
Created on 2015-8-20

@author: admin
'''
from com.love61v.user import Person
 

class User(Person):
    
    def show(self):
        print(self.getName())
        
user = User("张三人",34)
print(user.show())
 