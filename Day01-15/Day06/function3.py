"""

Python的内置函数
	- 数学相关: abs / divmod / pow / round / min / max / sum
	- 序列相关: len / range / next / filter / map / sorted / slice / reversed
	- 类型转换: chr / ord / str / bool / int / float / complex / bin / oct / hex
	- 数据结构: dict / list / set / tuple
	- 其他函数: all / any / id / input / open / print / type

Version: 0.1
Author: 骆昊
Date: 2018-03-05

"""


def myfilter(mystr):
	return len(mystr) == 6


# help()
print(chr(0x9a86)) #chr()  range（256）返回一个对应的字符
print(hex(ord('骆'))) 

#ord() 返回字符的十进制整数
#hex() 函数用于将10进制整数转换成16进制，以字符串形式表示

print(abs(-1.2345))
print(round(-1.2345)) # 返回浮点数的四舍五入值
print(round(1.555))
print(pow(1.2345, 5))
fruits = ['orange', 'peach', 'durian', 'watermelon']
print(fruits[slice(1, 3)]) #slice切片
# fruits2 = list(filter(myfilter, fruits))
fruits2 = tuple(filter(myfilter, fruits))
print(fruits)
print(fruits2)

"""

filter(function, iterable)
filter()函数用于过滤序列，过滤掉不符合条件的元素，返回由符合条件元素组成的新列表

# 过滤出列表中所有的基数
def is_odd(n):
    return n % 2 == 1
 
newlist = filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(newlist)

"""

"""

list()函数将元组转化成列表


aTuple = (123, 'xyz', 'zara', 'abc');
aList = list(aTuple)
 
print "列表元素 : ", aList


输出：列表元素 :  [123, 'xyz', 'zara', 'abc']

"""