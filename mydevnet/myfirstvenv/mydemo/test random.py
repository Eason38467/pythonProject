import random

a = 0
keys = 'Y'

while keys == 'Y':

    while True:

        x = random.choice(range(100))
        y = random.choice(range(100))
        a = a + 1
        if x > y:
            print(x , '>', y)
        elif x < y:
            print(x , '<', y)
        else:
            print('x=y=' , x, 'total cal ', a, 'time')
            break
    temp = input('继续?(Y/N)')
    keys = temp.upper()


print(input('按任意键退出'))

