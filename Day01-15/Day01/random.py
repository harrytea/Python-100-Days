'''
random.py
'''

import random

print(random.randint(1, 10))  #产生1到10的一个整数型随机数
print(random.random())  #产生0-1之间的随机浮点数
print(random.uniform(1.1, 5.4))  #产生1.1到5.5之间的随机浮点数，区间可以不是整数
print(random.choice("tomorrow"))  #从序列中随机选取一个元素
print(random.randrange(1, 100, 2))  #生成从1-100之间间隔为2的随机整数

a = [1, 3, 5, 6, 7]
random.shuffle(a)  #将a的元素顺序打乱
print(a)