**变量
python中的变量不需要声明
每个变量使用前必须赋值
变量赋值后才会被创建

2.多变量赋值
a = b = c = 1
a, b, c, = 1, 2, "noob"

3.标准数据类型
不可变
Number
String
Tuple
----------
可变
List
Set
Dictionary
类型判断
type(a)
instance(a, int)
?区别

------------------------
Number:
int float bool complex
del 删除 可删除多个
运算
5 + 4           加法
4.3 - 2         减法
3 * 7           乘法
2 / 4           浮点数除法
2 // 4          整数除法
17 % 3          取余
2 ** 5          乘方
------------------------
String:

str：= 'Runoob'

print(str)
print(str[0:-1])    #第一个到倒数第一个
print(str[0])       #输出字符串第一个字符
print(str[2:5])     #第三个到第五个
print(str[2:])      #第三个到最后一个
print(str * 2)      #字符串连续输出两个
print(str + "TEST") #连接字符串
-------------------------
List:
list_1 = ['sdf',123,2213,'123']
list_2 = [123, 'asdf']

print(list_1)       #输出完整列表
print(list_1[0])        #输出第一个元素
print(list_1[1:3])      #从第二个开始输出到第三个
print(list_1[2:])       #输出从第三个元素开始的所有元素
print(list_1 * 2)       #输出两次列表
print(list_1 + list_2)  #连接列表

>>> a = [1, 2, 3, 4, 5, 6]
>>> a[0] = 9
>>> a[2:5] = [13, 14, 15]
>>> a
[9, 2, 13, 14, 15, 6]
>>> a[2:5] = []   # 将对应的元素值设置为 []
>>> a
[9, 2, 6]

