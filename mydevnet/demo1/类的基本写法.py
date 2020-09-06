

#小明今年18岁，身高1.75，每天早上跑完步，会去吃东西
#小美今年17岁，身高1.65，小美不跑步，小美喜欢吃东西
#定义类:类名怎么定义？使用class 来定义一个类
# class类名:类名- -般需要遵守大驼峰命名法，每一个单词的首字母都大写
# 1. class 《类名》:
# 2. class 《类名》（object）:
class Student (object): # 关注这个类有哪些属性和行为
    def __init__(self, name, age,height): #在__init__ 方法里 ，以参数的形式定特征
        self.name = name
        self.age = age
        self.height = height
    def run(self):
        print('正在跑步')
    def eat(self):
        print('吃东西')


#Student()会自动调用__init__放方法
#使用Student 创建了两个实例， S1， S2
#
s1 = Student('小明',18,1.76)
s2 = Student('xiaomeili', 19,1.80)

#根据逻辑，调用不同的行为
print(s1.name)
s1.run()
s1.eat()

s2.run()


