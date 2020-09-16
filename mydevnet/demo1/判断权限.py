user_permission = 11 #1011

#权限因子与用户权限都转化为二进制比较
#用户权限 & 权限因子 ！=0 即为有对应的权限，例如
DEL_PERMISSION = 8  # 1000 & 1011  --》1000
READ_PERMISSION = 4  # 0100 & 1011 ==》 0000
WRITE_PERMISSION = 2  # 0010 & 1011 ==》0010
EXE_PERMISSION = 1  # 0001 & 1011 ==》 0001

def check_permission(x,y):
    def handle_action(fn):
        def do_action():
            if x & y != 0:
                fn()
            else:
                print('对不起，您没有相对应权限')
        return do_action
    return handle_action

@check_permission(user_permission,READ_PERMISSION)
def read():
    print('reading')
@check_permission(user_permission,WRITE_PERMISSION)
def write():
    print('writing')

@check_permission(user_permission,EXE_PERMISSION)
def exe():
    print('exeing')

@check_permission(user_permission,DEL_PERMISSION)
def delete():
    print('deleting')


read()
write()
exe()
delete()