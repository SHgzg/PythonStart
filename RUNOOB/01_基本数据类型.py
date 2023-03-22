num_init = 123
num_flo = 1.23
#为避免数据丢失自动转换较高的数据类型
# int + flo = flo (隐式转换)
num_new = num_init + num_flo
# print(num_new,type(num_new))
# >> 124.23 <class 'float'>

num_str = '456'
# int + str = !error
# 字符串和整数做算数运算没有隐式转换，需要显示转换
num_new = num_init + num_str
print(num_new,type(num_new))
# >>---------------------------------------------------------------------------
# TypeError                                 Traceback (most recent call last)
# Cell In[5], line 3
#       1 num_str = '456'
#       2 # int + str = !error
# ----> 3 num_new = num_init + num_str
#       4 print(num_new,type(num_new))

# TypeError: unsupported operand type(s) for +: 'int' and 'str'


# 显式类型转换
# int(x) x转换为整数
# float(x) x转换为浮点数
# str(x) x转换为字符串
# complex([real [,imag]]) 转换为复数
# repr(x) x转换为表达式
# eval(str) 用来计算在字符串中的有效Python表达式，！！并返回一个对象 
# tuple(s) 将序列s转换为一个元组
# list(s) 将序列s转换为一个列表
# set(x) 将x转换为一个可变集合
# dict(d) 创建一个字典，d必须是一个 (key,value) 【元组】 序列
# frozenset(s) 创建一个不可变集合
# chr(x) 将一个 【整数】 转换为字符串
# ord(x) 将一个字符串转换为它的整数数值
# hex(x) 将一个整数转换为一个十六进制字符串
# oct(x) 将一个整数转换为一个八进制字符串

num_new= 1
print(type(num_new))
# >> <class 'int'>
eval('type(num_new)')
# >> int