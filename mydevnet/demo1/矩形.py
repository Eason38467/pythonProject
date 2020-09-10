#设计两个类:
# -一个点类，属性包括x ， y坐标。
#一-个Rectangle类（矩形） ，属性有左上角和右下角的坐标，
#方法:1.计算矩形的面积；2. 判断点是否在矩形内
#实例化一个点对象，一个正方形对象，输出矩形的面积，输出点是否在矩形内

import random

class Point(object):
    def __init__(self, x:int,y:int):
        self.x = x
        self.y = y


class Rectangle(object):
    def __init__(self, top:tuple,bottom:tuple):
        self.top = top
        self.bottom = bottom

    def area(self):
        long = self.bottom[0]-self.top[0]
        weith = self.top[1] - self.bottom[1]
        return long * weith

P1 = Point(random.randint(1,10),random.randint(1,10))
R1= Rectangle((3,7), (4, 5))

print((P1.x,P1.y))
if R1.top[0]<= P1.x <= R1.bottom[0] and R1.bottom[1]<= P1.y <= R1.top[1]:
    print(f"输入的矩形面积为：{R1.area()}, 点位置在矩部")
else:
    print(f"输入的矩形面积为：{R1.area()}, 点位置不在矩形内部")