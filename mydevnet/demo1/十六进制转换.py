import re

while True:
    number = input("请输入一个十六进制（按Q退出）：")
    pattern = re.compile(r'[^0,1,2,3,4,5,6,7,8,9,a,b,c,d,e,f,A,B,C,D,E,F]+')
    if number in {'q','Q'}:
        break

    elif re.search(pattern, number):
        print("输入有误，请重新输入：")
        continue
    else:
        answer16 = int(number , 16)
        print('十六进制转十进制：', hex(answer16), '-> %d' % (answer16))
        print('十六进制转八进制：', hex(answer16), '-> 0o%o' % (answer16))
        print('十六进制转二进制：', hex(answer16), '->' ,bin(answer16))
