import re

while True:
    print('''

    ---------1. 十进制转换其他进制----------
    ---------2. 二进制转换其他进制----------
    ---------3. 八进制转换其他进制----------
    ---------4. 十六进制转换其他进制--------''')
    temp = input('选择需要进行的操作:')
    if int(temp) == 1:
        number = input("请输入一个整数（按Q退出）：")
        if number in {'q', 'Q'}:
            break
        elif not number.isdigit():
            print("输入有误，请重新输入：")
            continue
        else:
            number = int(number)
            print('十进制转十六进制：%d -> 0x%x' % (number, number))
            print('十进制转八进制：%d -> 0o%o' % (number, number))
            print('十进制转二进制：%d ->' % (number), bin(number))
    elif int(temp) == 2 :
        number = input("请输入一个二进制（按Q退出）：")
        pattern = re.compile(r'[^0,1]+')
        if number in {'q', 'Q'}:
            break
        elif not number.isdigit():
            print("输入有误，请重新输入：")
            continue

        elif re.search(pattern, number):
            print("输入有误，请重新输入：")
            continue
        else:
            answer10 = 0
            length = len(number)
            for i in range(length):
                answer10 += int(number[i]) * (2 ** (length - i - 1))
            print('二进制转十六进制：', '%r-> 0x%x' % (int(number), answer10))
            print('二进制转八进制：', '%r-> 0o%o' % (int(number), answer10))
            print('二进制转十进制：', '%r -> %d' % (int(number), answer10))
    elif int(temp) == 3:
        number = input("请输入一个八进制（按Q退出）：")
        pattern = re.compile(r'[^0,1,2,3,4,5,6,7,]+')
        if number in {'q', 'Q'}:
            break

        elif re.search(pattern, number):
            print("输入有误，请重新输入：")
            continue
        else:
            answer8 = int(number, 8)
            print('八进制转十进制：', oct(answer8), '-> %d' % (answer8))
            print('八进制转十六进制：', oct(answer8), '-> 0x%x' % (answer8))
            print('八进制转二进制：', oct(answer8), '->', bin(answer8))
    else :
        number = input("请输入一个十六进制（按Q退出）：")
        pattern = re.compile(r'[^0,1,2,3,4,5,6,7,8,9,a,b,c,d,e,f,A,B,C,D,E,F]+')
        if number in {'q', 'Q'}:
            break

        elif re.search(pattern, number):
            print("输入有误，请重新输入：")
            continue
        else:
            answer16 = int(number, 16)
            print('十六进制转十进制：', hex(answer16), '-> %d' % (answer16))
            print('十六进制转八进制：', hex(answer16), '-> 0o%o' % (answer16))
            print('十六进制转二进制：', hex(answer16), '->', bin(answer16))
