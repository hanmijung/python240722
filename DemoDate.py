# DemoDate.py

from datetime import *

print(dir())
d1=date(2024,5,1)
print(d1)

d2=date.today()
print(d2)



d3=datetime.now()
print(d3)

d4=timedelta(days=100)
print(d2+d4)

#문자열 가공
nowDate=date(2024,7,1).strftime("%Y/%m/%d")
print(nowDate)

import random

print(random.random())
print(random.random())

print([random.randrange(20) for i in range(10)])
print([random.randrange(50) for i in range(10)])


print(random.sample(range(20),10))
print(random.sample(range(20),10))

#로또번호
print(random.sample(range(45),5))