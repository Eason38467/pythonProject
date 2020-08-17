import re

while True:
    number = input("请输入一个八进制（按Q退出）：")
    pattern = re.compile(r'[^0,1,2,3,4,5,6,7,]+')
    if number in {'q','Q'}:
        break

    elif re.search(pattern, number):
        print("输入有误，请重新输入：")
        continue
    else:
        answer8 = int(number,8)
        print('十六进制转十进制：', oct(answer8), '-> %d' % (answer8))
        print('十六进制转十六进制：', oct(answer8), '-> 0x%x' % (answer8))
        print('十六进制转二进制：', oct(answer8), '->' ,bin(answer8))
