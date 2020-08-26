#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


namelist = ['zhangsan', 'lisi', 'eason', 'lucy', 'songwa']
while True:

    name = input('输入您的名字:')
    if name.lower() not in namelist:
        namelist.append(name)
        print(namelist)

    else:
        print('用户名已经存在')




