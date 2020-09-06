Namecard = []

flag = True


count = 1

while flag:

    print("-" * 20)
    print("名片管理系统 V1.0".center(20, ' '))
    print('1: 添加新名片')
    print('2: 删除名片')
    print('3: 修改名片')
    print('4: 查询名片')
    print('5: 显示所有名片')
    print('6: 退出系统')
    print("-" * 20)

    options = input('请输入您需要进行操作的序号：')
    if options.isdigit():
        if int(options) == 1:
            if count == 1:
                name = input('请输入您的姓名：')
                phonenumber = input('请输入您的手机号：')
                qqnumber = input('请输入您的qq号：')

                Namecard.append({'name': name, 'phonenumber': phonenumber, 'qqnumber': qqnumber})
                count = count +1
            else:
                name = input('请输入您的姓名：')
                for x in Namecard:

                    if x["name"] == name:
                        print('该姓名已经存在，请重新输入')
                        break

                else:
                    phonenumber = input('请输入您的手机号：')
                    qqnumber = input('请输入您的qq号：')

                    Namecard.append({'name': name, 'phonenumber': phonenumber, 'qqnumber': qqnumber})


            for n in Namecard:
                print(
                    f"Seq:{Namecard.index(n)+1}, Name:{n['name']}, Phone Number:{n['phonenumber']}, QQ Number:{n['qqnumber']}")

        elif int(options) == 2:
            delopetion = input('请输入您要删除的条目（姓名或者序号）：')
            if delopetion.isdigit():
                Namecard.pop(int(delopetion)-1)
            else:
                for n in Namecard:
                    if n['name'] == delopetion:
                        Namecard.pop(Namecard.index(n))

            for n in Namecard:
                print(
                    f"Seq:{Namecard.index(n)+1}, Name:{n['name']}, Phone Number:{n['phonenumber']}, QQ Number:{n['qqnumber']}")



        elif int(options) == 3:
            modifyoption = input('请输入您要修改的条目（姓名或者序号）：')
            if modifyoption.isdigit():
                for n in Namecard:
                    if Namecard.index(n)+1 == int(modifyoption):
                        n["name"] = input('请输入新的姓名：')
                        n['phonenumber'] = input('请输入新的手机号：')
                        n['qqnumber'] = input('请输入新的QQ号：')
            else:
                for n in Namecard:
                    if n['name'] == modifyoption:
                        n["name"] = input('请输入新的姓名：')
                        n['phonenumber'] = input('请输入新的手机号：')
                        n['qqnumber'] = input('请输入新的QQ号：')

            for n in Namecard:
                print(
                    f"Seq:{Namecard.index(n) + 1}, Name:{n['name']}, Phone Number:{n['phonenumber']}, QQ Number:{n['qqnumber']}")

        elif int(options) == 4:
            findname = input('请输入您要寻找的条目（姓名）：')
            for n in Namecard:
                if n['name'] == findname:
                    print(f"Seq:{Namecard.index(n) + 1}, Name:{n['name']}, Phone Number:{n['phonenumber']}, QQ Number:{n['qqnumber']}")

        elif int(options) == 5:
            print('序号'.ljust(1, ' '), end='')
            print('姓名'.center(10, ' '), end='')
            print('手机号码'.center(10, ' '), end='')
            print('QQ号码'.center(15, ' '))
            for n in Namecard:
                print(' ', Namecard.index(n) + 1, end='')
                print(n['name'].center(10, ' '), end='')
                print(n['phonenumber'].center(10, ' '), end='')
                print(n['qqnumber'].center(15, ' '))
        else:
            option = input('您确定退出么？（Y/N）').upper()
            if option == 'Y':
                flag = False

    else:
        print('您输入有误，请重新输入')
