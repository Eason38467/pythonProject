import time


def cal_time(fn):
    start = time.time()
    fn()
    endtime = time.time()
    print(f'程序本次运行时间{endtime-start}')

@cal_time
def demo():
    x=0
    for i in range(1,10000000):
        x*=i
    print(x)
@cal_time  # 函数修饰器
def foo():
    print('hello')
    time.sleep(3)
    print('world')


cal_time(demo)
cal_time(foo)

