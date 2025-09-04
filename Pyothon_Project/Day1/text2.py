# 合法标识符
'''
    age = 25
    user_name = "Alice"
    _total = 100
    MAX_SIZE = 1024
    calculate_area()
    StudentInfo
    __private_var




def is_valid_identifier(name):
    try:
        exec(f"{name} = None")
        return True
    except:
        return False
    
def fristFunction():
    print("This is the first function")

print(is_valid_identifier("2var"))  # False
print(is_valid_identifier("var2"))  # True
fristFunction()

a = 20
if a==11:
    print("a is 11")
elif a==20:
    print("a is 20")
else:
    print("a is not 11 or 20")

str1 = "Hello, World!"
print(str1.lower())  # 输出字符串变小写
print(str1.upper())  # 输出字符串变大写

list1 = [1, 2, 3, 4, 5] 
list2 = [6, 7, 8.44, False, "d"] 
list3 = list1 + list2 
print(list3)  # 输出合并后的列表
for i in list3:
    if i==8.44:
        print(i)  # 输出列表中8.44的索引位置
        print(list3.index(i))  # 输出列表中8.44的索引位置

# for i in range(len(list3)):
#     print(list3[i])  # 输出列表中的元素

for index, value in enumerate(list3):
    if value == 8.44:
        print(index)  # 输出列表中8.44的索引位置

# indices = [index for index, value in enumerate(list3) if value == 8.44]
# print(indices)  # 输出列表中所有8.44的索引位置

# try:
#     index = list3.index(8.44)
#     print(index)  # 输出列表中8.44的索引位置
# except ValueError:
#     print("8.44 not found in the list")

# for index in range(len(list3)):
#     if list3[index] == 8.44:
#         print(index)  # 输出列表中8.44的索引位置




# 字典
# dict1 = {'name': 'Alice', 'age': 25, 'city': 'Beijing'} 
# print(dict1)  # 输出字典
# print(dict1['name'])  # 输出字典中name的值
# print(dict1.get('age'))  # 输出字典中age的值
# dict1['age'] = 26  # 修改字典中age的值
# print(dict1)  # 输出修改后的字典
# dict1.pop('city')  # 删除字典中city的值
# print(dict1)  # 输出删除city后的字典
# #清空字典
# dict1.clear()
# print(dict1)  # 输出清空后的字典
dict2 = {'name': 'Bob', 'age': 30, 3: 'Shanghai'} 
#遍历字典key和value
for key, value in dict2.items():
    print(key, value)  # 输出字典中key和value的值

#单独只是遍历字典的key
for key in dict2:
    print(key)  # 输出字典中key的值
#单独只是遍历字典的value
for value in dict2.values():
    print(value)  # 输出字典中value的值

# 元组
tuple1 = (1, 2, 3, 4, 5) 
print(tuple1)  # 输出元组
# tuple1[0] = 10  # 元组是不可变的，不能修改元组的值
# tuple1[1:3] = (10, 20)  # 元组是不可变的，不能修改元组的值
# print(tuple1)  # 输出修改后的元组
#遍历元组值和索引
for index, value in enumerate(tuple1):
    print(index, value)  # 输出元组中索引和值
# 元组和列表的区别
# 1. 元组是不可变的，不能修改元组的值
# 2. 元组是有序的，列表是无序的
# 3. 元组是不可变的，不能添加或删除元素，列表是可变的，可以添加或删除元素
# 4. 元组是小括号，列表是方括号
# 5. 元组只能存放一种数据类型，列表可以存放不同的数据类型
# 6. 元组的元素不能修改，列表的元素可以修改
# 7. 元组的元素不能删除，列表的元素可以删除

# 集合
set1 = {1, 2, 3, 4, 5} 
print(set1)  # 输出集合
set2 = {4, 5, 6, 7, 8} 
print(set1.union(set2))  # 输出两个集合的并集
print(set1.intersection(set2))  # 输出两个集合的交集
print(set1.difference(set2))  # 输出两个集合的差集
print(set1.symmetric_difference(set2))  # 输出两个集合的对称差集
set1.add(9)  # 添加元素到集合
print(set1)  # 输出添加后的集合
set1.remove(2)  # 删除集合中的元素
print(set1)  # 输出删除后的集合
set1.discard(3)  # 删除集合中的元素，如果元素不存在，不报错
print(set1)  # 输出删除后的集合
set1.clear()  # 清空集合queue
print(set1)  # 输出清空后的集合

# 列表推导式
# 列表推导式是一种创建列表的简洁方式，可以根据某种条件创建新的列表。
# 语法格式：
# new_list = [expression for item in iterable if condition]
# 1. expression：表达式，用于创建新元素。
# 2. item：可迭代对象中的元素。
# 3. iterable：可迭代对象，用于生成元素。
# 4. condition：可选，用于过滤元素。
# 5. new_list：新列表。

# 举例：
# 1. 取出列表中的偶数
# new_list = [num for num in [1, 2, 3, 4, 5] if num % 2 == 0]
# print(new_list)  # [2, 4]
# 2. 取出字典中的偶数
# dict1 = {'name': 'Alice', 'age': 25, 'city': 'Beijing'} 
# new_dict = {key: value for key, value in dict1.items() if value % 2 == 0}
# print(new_dict)  # {'age': 24}
# 3. 取出集合中的偶数
# set1 = {1, 2, 3, 4, 5} 
# new_set = {num for num in set1 if num % 2 == 0}
# print(new_set)  # {2, 4}

'''    

# names = ['Bob','Tom','alice','Jerry','Wendy','Smith']
# new_names = [name.upper()for name in names if len(name)>3]
# print(new_names)

# multiples = [i for i in range(30) if i % 3 == 0]
# print(multiples)


# listdemo = ['Goog','Runoo', 'Taobao']
# # 将列表中各字符串值为键，各字符串的长度为值，组成键值对
# newdict = {len(key):key for key in listdemo}
# print(newdict)

# 字典推导式
# 字典推导式是一种创建字典的简洁方式，可以根据某种条件创建新的字典。
# 语法格式：
# new_dict = {key_expression: value_expression for item in iterable if condition}
# 1. key_expression：表达式，用于创建新键。
# 2. value_expression：表达式，用于创建新值。
# 3. item：可迭代对象中的元素。
# 4. iterable：可迭代对象，用于生成元素。
# 5. condition：可选，用于过滤元素。
# 6. new_dict：新字典。



# list=[1,2,3,4]
# it = iter(list)    # 创建迭代器对象
# print (next(it))   # 输出迭代器的下一个元素
# print (next(it))   # 输出迭代器的下一个元素
# print (next(it))   # 输出迭代器的下一个元素
# print (next(it))   # 输出迭代器的下一个元素



#!/usr/bin/python3
 
# list=[1,2,3,4]
# it = iter(list)    # 创建迭代器对象
# for x in it:
#     print (x, end=" ")

# class MyNumbers:
#   def __iter__(self):
#     self.a = 1
#     return self
 
#   def __next__(self):
#     x = self.a
#     self.a += 1
#     return x
 
# myclass = MyNumbers()
# myiter = iter(myclass)
 
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))


# 同时打开多个文件
# with open('input.txt', 'r') as infile, open('output.txt', 'w') as outfile:
#     content = infile.read()
#     outfile.write(content.upper())
 
# import re
 
# print(re.search('www', 'www.runoob.com').span())  # 在起始位置匹配
# print(re.search('com', 'www.runoob.com').span())  # 不在起始位置匹配
# # (0, 3)
# # (11, 14)  起始位置为11 结束位置为13不包括14

 
import re
 
line = "Cats are smarter than dogs"
 
searchObj = re.search( r'(.*) are (.*?) .*', line, re.M|re.I)
 
if searchObj:
   print ("searchObj.group() : ", searchObj.group())
   print ("searchObj.group(1) : ", searchObj.group(1))
   print ("searchObj.group(2) : ", searchObj.group(2))
else:
   print ("Nothing found!!")