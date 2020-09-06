#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


while True:
    num = int(input('请输入一个整数：'))

    pri = True

    for x in range(2, num):
        if num % x == 0:
            pri = False
            break

    if pri % num > 1:
        print('zhishu')
    else:
        print('heshu')



