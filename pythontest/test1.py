#list练习
'''
L = [['Apple','Google','Microsoft'],['Java','Python','C++'],['Adam','Bart','Lisa']]
print(L[0][0])
print(L[1][1])
print(L[2][2])
'''
#条件判断
'''
print("请输入年龄：")
age = int(input())
if age >= 18:
    print('您的年龄是',age)
    print("成年")
else:
    print("未成年")
'''
#NMI指数
'''
小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：
低于18.5：过轻
18.5-25：正常
25-28：过重
28-32：肥胖
高于32：严重肥胖

print("请输入身高：")
height = float(input())
print("请输入体重")
weight = float(input())
s = weight/height
BMI = s*s
if BMI < 18.5:
    print("过轻")
elif BMI >= 18.5 and BMI < 25:
    print("正常")
elif BMI >= 25 and BMI < 28:
    print("过重")
elif BMI >=28 and BMI < 32:
    print("肥胖")
else:
    print("过度肥胖")
'''
#循环
'''
sum = 0
a = [1,2,3,4,5,6,7,8,9,10]
for x in a:
    sum = sum+x
print(sum)
'''
'''
sum = 0
for x in range(101):
    sum +=x
print(sum)
'''
'''
L = ['Nart','Lisa','Adam']
for x in L:
    print('Hello',x+'!')
'''
'''请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程 ax^2+bx+c=0ax 
2
 +bx+c=0 的两个解。

提示：

一元二次方程的求根公式为：

x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}x= 
2a
−b± 
b 
2
 −4ac
​
 
​
 

计算平方根可以调用math.sqrt()函数：'''
'''
import math

def quadratic(a,b,c):
    delta = math.sqrt(b*b-4*a*c)
    if delta >= 0:
        x1 = (-b + delta) / 2 * a
        x2 = (-b - delta) / 2 * a
        return x1,x2
    else:
        return "no answer"

print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
'''
'''
L = list(range(101))
print(L)
print(L[:11])
'''
'''''
# -*- coding: utf-8 -*-
def trim(s):
    if 0==len(s):
        return s

    while ' '==s[0]:
        s=s[1:]
        if 0==len(s):
            return s

    while ' '==s[-1]:
        s=s[:-1]
        if 0==len(s):
            return s

    return s
s1 = trim('hello   ')
print(s1)
'''
'''''
def findMinandMax(L):
    Max = -99
    Min = 99
    for key in L:
        if(key > Max):
            Max = key
        if key < Min:
            Min = key
    return (Min,Max)

L = [1,2,3,4,5,10]
l = findMinandMax(L)
print(l)
'''
'''''
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [x for x in L1 if isinstance(x,str)==True]
print(L2)
'''
'''
利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
'''
''''
def normalize(name):
    resukt = name[0].upper() + name[1:].lower()
    return resukt
L1 = ["adam", "LISA", "barT"]
L2 = list(map(normalize,L1))
print(L2)
'''
'''
Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：
'''
'''''
from functools import reduce
def sub(x,y):
    return x * y
L = [1,2,3,4,5]
def prod(sub ,L):
    return reduce(sub,L)
L2 = prod(sub,L)
print(L2)
'''
'''
利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
'''
'''
from functools import reduce
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def str2float(s):
    def fn(x,y):
        return x * 10 + y
    def char2float(s):
        return DIGITS[s]
    return reduce(fn,map(char2float,s))
s = str2float("12312")
print(s)
'''
'''''
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_name(t):
    return t[0]
L2 = sorted(L,key = by_name)
print(L2)
def by_sore(t):
    return t[1]
L3 = sorted(L,key = by_sore)
print(L3)
'''
'''''
def createCounter():
    i = [0]
    def counter():
        i[0] += 1
        return i[0]
    return counter
c = createCounter()
print(c())
print(c())
x = createCounter()
print(x())
'''
'''''
def is_odd(n):
    return n % 2 == 1

L = list(filter(is_odd, range(1, 20)))
print(L)

L1 = list(filter(lambda n : n % 2 == 1,range(1,20)))
print(L1)
'''
'''''
class student(object):
    def __init__(self,name, score):
        self.name = name
        self.score = score

s = student("里单反",77)
print(s.name)
'''
'''
把Student的gender属性改造为枚举类型，可以避免使用字符串：
'''
from enum import Enum,unique

class Gender(Enum):
    Male = 0
    Female = 1
class Student(object):
    def __init__(self,name,gender):
        self.name = name
        self.gender = gender
bar = Student('Bart',Gender.Male)
if bar.gender == Gender.Male:
    print('测试通过')
else:
    print('测试失败')