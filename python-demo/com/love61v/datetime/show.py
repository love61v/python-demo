'''
Created on 2015-8-25

@author: admin
'''
from _datetime import datetime

now = datetime.now()
print(now)

print(type(now))

print(now.strftime("%Y-%m-%d %H:%M:%S"))
