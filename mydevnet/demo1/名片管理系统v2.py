user_list = []


def add_info():
    # print（' 添加名片'）

    # 1.使用input语句，接收用户的输入

    name = input('请输入姓名:')

    # 4.用户输入完成以后，查看用户名是否存在

    for user in user_list:  # 4.1 遍历user list列表

        if user[' name '] == name:  # 如果发现列表里有相同的姓名

            print('此用户名已经被占用，请重新输入')  # 提示用户，姓名已经被占用了

            return  # 直接使用return结束整个函数

            # break #不需要再使用break

    tel = input('请输入手机号:')

    qq = input('请输入QQ号:')

    # 2.使用字典的形式将数据保存

    user_dict = {'name': name, 'tel': tel, 'qq': qq}

    # 3.把创建好的用户添加到用户列表里

    user_list.append(user_dict)

    print(user_list)


def is_available(num):
    if not num.isdigit():  # 如果序号不是数字
        return False
    num = int(num)
    if num < 0 or num > len(user_list) - 1:
        return False
    return True


def del_user():
    # print（利除名片 ）
    num = input('请输入要删除的序号:')  # 接收用户要删除的序号
    if not is_available(num):
        print('输入序号有误，请重新输入')
        return
    # 如果是数字，同时也在区间范围内，提示用户并删除
    num = int(num)
    answer = input('你确定要删除么？yes or no')
    if answer.lower() == 'yes':
        user_list.pop(num)
        # user_ list. remove（user_ list【num 】）
        # del user_ list 【 num 】


def modify_info():
    # print（'修改名片'）
    num = input('请输入要修改的序号:')
    if not is_available(num):
        print('输入序号有误，请重新输入')
        return
    user = user_list[int(num)]  # 根据用户输入的下标获取到數据
    print('你要修改的信息是: \nname:{name}， tel:{te1}， QQ:{qq}'.format(**user))
    new_name = input('请输入新的姓名:')
    new_tel = input('请输入新的手机号:')
    new_qq = input('请输入新QQ:')
    user['name'] = new_name
    user['tel'] = new_tel
    user['qq'] = new_qq


def query_info():
    # print（'查询名片' ）
    search_name = input(' 请输入要查询的名片姓名:')
    for user in user_list:
        if user[' name'] == search_name:
            print('查询到的信息如下: \nname: {name}， tel: {te1}， QQ: {qq}'.format(**user))
            break
    else:
        print('没有您要找的信息....')


def show_all():
    # print( '並ホ所有石片
    print('序号姓名   手机号    QQ')
    for i, user in enumerate(user_list):
        print(i, user[' name'].center(15), user['tel'].center(10), user['qq'].center(10))


def quit_system():
    answer = input('楽，祢硝定要退出幺?~~~~(ゝ_ < )~wm~(yes or no)')
    return answer.lower() == 'yes'


def start():
    while True:
        print("""
        名片管理系統V1.0
1:添加名片
2:刪除名片
3:修改名片
4:査洵名片
5:星示所有名片
6:退出系統
        """)
        operator = input('清輸入要迸行的操作(数字)')

        if operator == '1':
            add_info()
        elif operator == '2':
            del_user()
        elif operator == '3':
            modify_info()
        elif operator == '4':
            query_info()
        elif operator == '5':
            show_all()
        elif operator == '6':
            if quit_system():
                break
        else:
            print('输入有误，请重新输入......')


if __name__ == '__main__':
    start()
