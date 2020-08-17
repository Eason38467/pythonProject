print("=========欢迎进入狗狗年龄对比系统===========")

control = 'N'

while control == 'N':
    try:
        age = int(input("请输入您家狗狗的年龄："))
        age = float(age)
        if age < 0 :
            print("您在逗我？")
        elif age == 1:
            print("相当于人类14岁")
        elif age == 2:
            print("相当于人类22岁")
        else:
            human = 22 + (age - 2 )* 5
            print("相当于人类：", human)

    except ValueError:
        print("输入不合法，请输入有效年龄")
    print("")
    temp = input("退出(Y/N)?")
    control = temp.upper()

    print("")

input("点击enter退出")