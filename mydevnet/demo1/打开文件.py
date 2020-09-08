#open(file, mode='r', buffering=None, encoding=None, errors=None, newline=None, closefd=True):
#file :  用来指定打开文件的路径， 如果在同一个目录， 就是文件名。

#mode ： 打开文件的模式， r 默认只读

#encoding ： 打开文件的编码方式,在Windows 里面， 默认用gbk打开

file = open('xx.txt', encoding='utf-8')
file.close()
