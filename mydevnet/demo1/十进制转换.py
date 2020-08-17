while True:
    number = input("请输入一个整数（按Q退出）：")
    if number in {'q','Q'}:
        break
    elif not number.isdigit():
        print("输入有误，请重新输入：")
        continue
    else:
        number = int(number)
        print('十进制转十六进制：%d -> 0x%x'%(number,number))
        print('十进制转八进制：%d -> 0o%o' % (number, number))
        print('十进制转二进制：%d ->' % (number), bin(number))
