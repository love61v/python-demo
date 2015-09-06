'''
Created on 2015-8-20

@author: hubo
'''
#动物基本类
from enum import Enum
class Animal(object):
    
    def run(self):
        print("running...............")

# Dog 继承 Animal
class Dog(Animal):
    def run(self):
        print("dog is running")

# Cat 继承 Animal 
class Cat(Animal):
    def run(self):
        print("cat is running")


#多态
def run_twice(animal):
    animal.run()


dog  = Dog();
dog.run()

cat  = Cat();
cat.run()

a = list()
print("是否是实例",isinstance(dog, Animal))
print("是否是实例",isinstance(a, list))

run_twice(dog)

month = Enum("mon", ("jan","fe"))
for name in month.value():
    print(name)
    
