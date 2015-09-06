'''
Created on 2015-8-20

@author: admin
'''
class Student(object):
    
    def __init__(self,name,score):
        self.name = name
        self.score = score
        
    def showScore(self):
        print("我的分数: ",self.name, self.score)    
        
    def getScore(self):
        if self.score > 90:
            return "A"
        elif self.score > 60:
            return "B"
        else:
            return "C"
        
stu1 = Student("刘亦菲",99)            
stu2 = Student("张三",50)      

print("stu1 name=%s  : score=%d" % (stu1.name,stu1.score)) 
stu1.showScore() 

print("name=%s" %stu1.name,stu1.getScore())    
    
        