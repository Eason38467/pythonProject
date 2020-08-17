sites = ['baidu', 'google', 'runoob', 'taobao']

for site in sites:
    if site == 'runoob':
        print("菜鸟教程！")
        break
    print("循环数据" + site)
else:
    print("没有完成循环")

print("完成循环！")