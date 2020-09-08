#open(file, mode='r', buffering=None, encoding=None, errors=None, newline=None, closefd=True):
#file :  用来指定打开文件的路径， 如果在同一个目录， 就是文件名。

#mode ： 打开文件的模式， r 默认只读

#encoding ： 打开文件的编码方式,在Windows 里面， 默认用gbk打开

import os

#1. 绝对的路径.

import OS
# print（os.name） # NT/posix
# windows系统里，文件夹之间使用\分隔.
# .在非windows系统里，文件夹之间使用/分隔.
# os.sep . I
#在Python的字符串里 ，\表示转义字符
# file = open（ 'C:\\Users \ \chris\ \Desktop\ \Python基础\ \Day13-文件操作\01 -代码\ \xxx. txt'）
# file = open（r'C: \Users \chris \Desktop \Python基础\Day13-文件操作01 -代码\xxx. txt'）
#file = open('C:/Users/ chris/Desktop/ Python基础/Day13-文件操作/01-代码/xxx. txt')   ----- 推荐


# 2.相对路径: 当前文件所在文件夹开始
#../ 表示上级文件夹
#./ 表示当前文件夹


#file = open('xxx.txt')


file = open('xx.txt', encoding='utf8')
file.close()


