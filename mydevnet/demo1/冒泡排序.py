#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
#冒泡排序思想： 一个数字与他相邻的下一个数字进行比较运算，如果前一个大于后一个，交换顺序。


a = [1,2,3,4,5,6,7,4,5,23,42,423,523,4,324,234,24,234,23,423,42,34,234,23]

i=0
count = 0

#每一趟比较次数可以优化。
#第一趟比较，j=0 多比较了 0次
#第二趟比较，j=1， 多比较了1次
#第三次比较，j=2，多比较了2次

while i < len(a)-1:
    #在每一趟中加入一个flag，来进行趟数的优化
    flag = True
    n = 0
    while n < len(a) -1-i:
        count += 1
        if a[n] > a[n +1]:
            flag = False  #产生交换时， flag 被改为false
            a[n],a[n+1] = a[n+1],a[n]
        n +=1
    if flag:
        break
    i+=1

print(a)
print(count)









