#!/usr/bin/env python3
# print('hello','world')
# import os
# os.chmod('/tmp/zhuji',600)                     #修改了权限以及格式
# os.chmod('/tmp/zhuji',0O600)
# 100
# 0x100
# 20
# 0b10
# 20
# 0o20
#print('tom said'hello world"")
# words='hello world'
# print(words)
# woe = 'hello \n world'
# print(woe)
# word = '''1st 100
# 2nd 200
# 3rd 300'''
# print(word)
# lines = '''1st qian
# 2nd jian
# 3rd chao SB'''
# print(lines)
# py_str='python'
# len('py_str')
# py_str[0]
# str='pytho
# a = input("number: ")
# print(a)
# print(int(a)+10)
# print(a + str(10))
# print('helloe')
# adict = {'name':'大锤','age':18}
# print(adict['name'])
# print(adict['age'])
# 18 in adict
# 'age in adict'
# adict['sex'] = 'female'                   #不存在则创建
# adict['age'] = 20                         #存在则修改
#  print(adict)
# words='eelo\nharry\nnihao'
# if 'tom' in words:
#     print('yes')
# if 'tom' not in words:
#     print('not in')
# else:
#     print('tom in words')
# if -0.0:                    #任何值为0额数都是False,非0为True
#     print('ok')
# if -0.01:
#     print('0.01 is ok')
# if ' ':
#     print('space is true')
# if '':
#     print('空字符串是False')
# if not []:
#     print('空列表也是False')
# if not None:
#     print('
# import getpass                   #导入输入不显示的模块
# user=input('请输入用户名： ')
# password=getpass.getpass('请输入密码: ')
# if user=='bob' and password=='123456':
#     print('Login successful')
# else:
#     print('登陆失败')
# import random
# number = random.randint(1,100)
# print('number -> ',number)
# answer = int(input('请输入1-100的数字: '))
# if answer > number:
#     print('输大了')
# elif answer < number:
#     print('输小了')
# else :
#     print('猜对了')
# a=100
# b=80
# if a < b:
#     smaller = a
# else:
#     smaller = b
# print(smaller)
# #或者
# a=100
# b=80
# smaller = a if a > b else b
# print(smaller)
# num=int(input('请输入你的成绩: '))
# if num >= 90:
#     print('优秀')
# if num >= 80:
#     print('良好')
# if num >= 70:
#     print('一般')
# if num >= 60:
#     print('及格')
# else:
#     print('你要努力了')
# #或者
# score = int(input('请输入你的成绩哦: '))
# if 60 <= score < 70:
#     print('一般')
# if 70 <= score < 80:
#     print('良好')
# if 80 <= score < 90:
#     print('好')
# if 90 <= score < 100:
#     print('优秀')
# if score == 100:
#     print('牛皮')
# import random
# xitong = random.choice(['石头','剪刀','布'])
# print('xitong ->',xitong)
# chuquan = input('请输入你想猜啥: ')
# if xitong == '石头':
#     if chuquan == '石头':
#         print('平手')
#     if chuquan == '剪刀':
#         print('你输了')
#     if chuquan == '布':
#         print('你赢了')
# if xitong == '剪刀':
#     if chuquan == '剪刀':
#         print('平手')
#     if chuquan == '布':
#         print('你输了')
#     if chuquan == '石头':
#         print('你赢了')
# if xitong == '步':
#     if chuquan == '步':
#         print('平手')
#     if chuquan == '石头':
#         print('你输了')
#     if chuquan == '剪刀':
#         print('你赢了')
# import random
# win_list = (['剪刀','布'],['石头','剪刀'],['布','石头'])
# xuanze = (['石头','剪刀','布'])
# computer = random.choice(xuanze)
# player = input('请输入: "石头","剪刀","布"')
# print('计算机的选择:',computer ,'你的选择是:',player)
# if player == computer:
#     print('平手')
# elif (player,computer) in win_list:
#     print('你赢了')
# else :
#     print('你输了')
# import random
# win_list = (['剪刀','布'],['石头','剪刀'],['布','石头'])
# xuanze = (['剪刀','石头','布'])
# computer = random.choice(xuanze)
# prompt = '''(0) 剪刀
# (1) 石头
# (2) 布
# 请出拳(0/1/2): '''
# index = int(input(prompt))
# player = xuanze[index]
# if player == computer :
#     print('平手')
# elif [player,computer] in win_list:
#     print('你赢拉')
# else :
#     print('byebye')
# sum = 0
# count = 1
# while count <= 100 :
#     sum += count
#     count += 1
# print(sum)
# win_list = (['剪刀','布'],['石头','剪刀'],['布','石头'])
# xuanze = (['剪刀','石头','布'])
# computer = random.choice(xuanze)
# prompt = '''(0) 剪刀
# (1) 石头
# (2) 布
# 请出拳(0/1/2): '''
# index = int(input('(0/1/2)'))
# player = xuanze[index]
# if player == computer :
#     print('平手')
# elif [player,computer] in win_list:
#     print('你赢拉')
# else :
#     print('byebye')
# import random
# suiji = random.randint(1,100)
# running = True
# while  running :
#     shuzi = int(input('请输入1-100的数字: '))
#     if shuzi > suiji :
#         print('猜大了')
#     elif shuzi < suiji :
#         print('猜小了')
#     else :
#         print('猜对拉')
#         running = False
# import random
# cai = random.randint(1,100)
# while True:
#     shu = int(input('请输入1-100的数: '))
#     if shu > cai:
#         print('猜大了')
#     elif shu < cai:
#         print('猜小了')
#     else:
#         print('猜对拉')
#         break
# sum = 0
# count = 0
# while count <= 100:
#     sum += count
#     count +=1
# print(sum)
#偶数的相加案例：
# sum = 0
# count = 0
# while count <= 100:
#     count += 1
#     if count % 2 == 1:
#         continue
#     sum += count                     #!!!!注意格式错误
# print(sum)
# import random
# computer = random.randint(1,10)
# tries = 0
# while tries <3:
#     cai = int(input('请输入1-10的数: '))
#     if cai > computer:
#         print('\033[32;1m猜大了\033[0m')
#     elif cai < computer:
#         print('\033[32;1m猜小了！！\033[0m')
#     else:
#         print('\033[32;1m猜对啦!!\033[0m')
#         break
#     tries += 1
# else:
#     print('正确答案是: ',computer)
# a =123
# print (a)
# print(0b10)
# print(0o16)
# print(0x32)
# py='python'
# print(len(py))
# print(py[0])
# print(py[2])
# print(py[4:6])
# print(py[0:2])
# print(py[-1])
# py='python'
# print(py[-1])
# print(py[1:6])
# print(py[:5])
# print(py[1:])
# print(py[:])
# py='python'
# print(py[::2])
# print(py[1::2])
# print(py[::-2])
# py='python'
# # print(py*4)
# # 'py' in py                    #####True
# print(py+str(123))
# # print(int(py)+123)            ##报错转换不了
# list = (['hello','world','haha'])
# # print(list)
# # print(list[0])
# # print(list[2])
# listyuan = (['wo','shi','zui','pang','de'])
# print(listyuan[3])
# list[1] = 'nihao'
# print(list[1])
# listyuan[2] = 'haha'
# print(listyuan)
# haha = {'name': '大锤','age':18}
# print(18 in haha)                               ####False
# print('name' in haha)
# haha['sex']  = 'female'
# haha['age'] = 20
# print(haha)
# py='python'
# py[2] = 'o'                            ##报错  不能修改
# print(py)
# a = 100
# b = 80
# if a < b :
#     small = a
# else:
#     small = b
# print(b)
# a = 100
# b = 80
# small = a if a < b else b
# print(small)
# if 10:
#     print('yes')
# if "":
#     print('yes')
# else:
#     print('no')
# if 0:
#     print('yes')
# else:
#     print('no')
# num = int(input('输入的成绩： '))
# if num > 90:
#     print('优秀')
# elif num > 80:
#     print('良好')
# elif num > 70:
#     print('一般')
# elif num > 60:
#     print('及格')
# else:
#     print('羞羞害羞的羞')
# num = int(input('请输入你的数字: '))
# if 60 < num <= 70:
#     print('一般')
# elif 70 < num <= 80:
#     print('良好')
# elif 80 < num <= 90:
#     print('好')
# elif 90 < num <= 100:
#     print('很棒')
# else:
#     print('你要努力哦')
################石头剪刀布(单次机会)
# import random
# xuanze = (['石头','剪刀','布'])
# user = input('请输入（剪刀/石头/布）： ')
# computer = random.choice(xuanze)
# print('computer ->: ',computer)
# if computer == '石头':
#     if user == '石头':
#             print('平局')
#     if user == '剪刀':
#         print('你输了')
#     if user == '布' :
#         print('你赢了')
# elif computer == '剪刀':
#     if user == '剪刀':
#             print('平局')
#     if user == '石头':
#         print('你赢了')
#     if user == '布' :
#         print('你输了')
# elif computer == '布':
#     if user == '石头':
#             print('你输了')
#     if user == '剪刀':
#         print('你赢了')
#     if user == '布' :
#         print('平局')
# else:
#     print('请输入剪刀石头布')
# import random
# xuanze = (['石头','剪刀','布'])
# win_list = (['石头''剪刀'],['剪刀''布'],['布''石头'])
# prompt = '''(0) 石头
# (1) 剪刀
# (2) 布
# 请输入 (剪刀/石头/布): '''
# index = int(input(prompt))
# computer = random.choice(xuanze)
# user = xuanze[index]
# print('电脑出的是： ',computer)
# if [user == computer]:
#     print('平局')
# elif [user,computer] in win_list:
#     print('你赢了')
# else :
#     print('你输了')
# print('\033[32;1mhahahaha\033[0m')
# import random
# xuanze = (['石头','剪刀','布'])
# win_list = (['石头''剪刀'],['剪刀''布'],['布''石头'])
# tries = 0
# prompt = ''' (0) 石头
# (1) 剪刀
# (2) 布
# 请输入（0/1/2） '''
# computer = random.choice(xuanze)
# while tries <3 :
#     index = int(input(prompt))
#     user = xuanze[index]
#     print('电脑出的是: ', computer)
#     if user == computer:
#         print('菜鸡互啄')
#     elif [user,computer] in win_list:
#         print('你赢了')
#         break
#     else:
#         print('你输了')
#     tries += 1
# import random
# num = random.randint(1,10)
# tries = 0
# while tries < 6:
#     user = int(input('输入你猜的数字： '))
#     if user == num:
#         print('你对啦')
#         break
#     elif user > num:
#         print('猜大了')
#     else :
#         print('猜小了')
#     tries += 1
# else :
#     print('正确答案是： ',num)
# import random
# xuanze = ('石头','剪刀','布')
# win_list=(['石头','剪刀'],['剪刀','布'],['布','石头'])
# computer = random.choice(xuanze)
# prompt = ''' (0) 石头
# (1) 剪刀
# (2) 布
# 请输入（0/1/2）: '''
# tries = 0
# while tries < 2 :
#     index =int(input(prompt))
#     user = xuanze[index]
#     if user == computer :
#         print('平局')
#     elif [user,computer] in win_list:
#         print('猜对啦')
#         tries += 1
#         continue
#     else :
#         print('猜错拉')
#         tries += 1
# sum = 0
# count = 0
# # while count < 100 :
# #     sum += count
# #     count += 1
# # print(sum)
# while count <= 100 :
#     count += 1
#     if count % 2 == 1:
#         continue
#     else :
#         sum += count
# print(sum)
# sum = 0
# count = 0
# while count < 100 :
#     count +=1
#     if count % 2 == 1 :
#         sum += count
#     else :
#         continue
# print(sum)
# import random
# xuanze = (['石头','剪刀','布'])
# win_list = (['石头''剪刀'],['剪刀''布'],['布''石头'])
# prompt = '''(0) 石头
# (1) 剪刀
# (2) 布
# 请输入 (剪刀/石头/布): '''
# index = int(input(prompt))
# computer = random.choice(xuanze)
# user = xuanze[index]
# print('电脑出的是： ',computer)
# if [user == computer]:
#     print('平局')
# elif [user,computer] in win_list:
#     print('你赢了')
# else :
#     print('你输了')
# words = 'hello\nworld\ntom\njerry'
# if 'tom' in words:
#     print('yes')
# if 'jerry' in words :
#     print('yes')
# if 3:
#     print('ok')
# if 9:
#     print('yes')
# if '123':
#     print('no')
# if "":
#     print('haha')
# if not []:
#     print('xixi')
# if []:
#     print('haxi')
# if None:
#     print('这不是空')
# if not None:
#     print('这是空')
# import random
# number = random.randint(1,100)
# print('number -> ',number)
# answer = int(input('请输入1-100的数字: '))
# if answer > number:
#     print('输大了')
# elif answer < number:
#     print('输小了')
# else :
#     print('猜对了')




























