# 面向对象的编程有三大特性： 封装， 继承，多态
# 封装：函数是对语句的封装；类是对函数和变量的封装
# 继承：类和类之间为人手动的建立父子关系。 父类的属性和方法， 子类可以使用
# 多态： 是一种技巧，可以提高代码的灵活度

# 继承：如下面， 多个类中存在多个相同的方法， 所以可以认为继承。  例如， Animal作为父类（基类）， Dog和Student 作为子类（派生类）

class Animal(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sleep(self):
        print(self.name + '睡觉')


class Dog(Animal):
    # def __init__(self, name, age):
    # self.name = name
    # self.age = age

    #def sleep(self):
       # print(self.name + '正在睡觉')

    def bark(self):
        print(self.name + '正在叫')


class Student(Animal):
    # def __init__(self, name, age):
    # self.name = name
    #
    # self.age = age
    #

    #def sleep(self):
       # print(self.name + '正在睡觉')

    def study(self):
        print(self.name + '正在好好学习')


# Dog() 调用__new__ 方法，在调用__init__方法
# 没有__new__方法，回去查看父类是否重写了__new__方法
# 父类也没有， 就回去查找父类的父类， 找到了object
d1 = Dog('大黄', 3)
print(d1.name)
