

import random

while True:

    temp = input('你出啥（石头，剪刀，布）')

    computer = random.choice(range(1, 4))


    if computer == 1:
        computer = '石头'
        if temp == '石头':
            print('你：', temp , '电脑：',computer, '平手')
        elif temp == '剪刀':
            print('你：', temp, '电脑：', computer,'你输了')
        else:
            print('你：', temp, '电脑：', computer,'你赢了')

    elif computer == 2:
        computer = '剪刀'
        if temp == '石头':
            print('你：', temp, '电脑：', computer, '你赢了')
        elif temp == '剪刀':
            print('你：', temp, '电脑：', computer, '平手')
        else:
            print('你：', temp, '电脑：', computer, '你输了')

    else:
        computer = '布'
        if temp == '石头':
            print('你：', temp, '电脑：', computer, '你输了')
        elif temp == '剪刀':
            print('你：', temp, '电脑：', computer, '你赢了')
        else:
            print('你：', temp, '电脑：', computer, '平手')







