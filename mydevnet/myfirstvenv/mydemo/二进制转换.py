import re

while True:
    number = input("请输入一个二进制（按Q退出）：")
    pattern = re.compile(r'[^0,1]+')
    if number in {'q','Q'}:
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
            answer10+=int(number[i])*(2**(length-i-1))
        print('二进制转十六进制：', '%r-> 0x%x' % (int(number),answer10))
        print('二进制转八进制：', '%r-> 0o%o' % (int(number),answer10))
        print('二进制转十进制：', '%r -> %d' %(int(number),answer10))
