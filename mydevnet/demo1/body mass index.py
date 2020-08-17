print('---------欢迎使用本BMI计算器----------')
name = input("请输入您的姓名：")
hight = eval(input("请输入您的身高（m）："))
weight = eval(input("请输入您的体重（Kg）："))
temp = input("请输入您的性别（F/M）：")
gender = temp.upper()
BMI = float(float(weight)/(float(hight)**2))

if BMI<=18.4:
    print('姓名:',name,'身体状态:偏瘦')
elif BMI<=23.9:
    print('姓名:',name,'身体状态:正常')
elif BMI<=27.9:
    print('姓名:',name,'身体状态:超重')
elif BMI>=28:
    print('姓名:',name,'身体状态:肥胖')

import time

nowtime = (time.asctime(time.localtime(time.time())))

if gender=='F':
    print('感谢',name,'女士在',nowtime,'使用本程序,祝您身体健康!')
if gender=='M':
    print('感谢',name,'先生在',nowtime,'使用本程序,祝您身体健康!')

