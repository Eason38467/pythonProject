import re

with open('hosts',"w") as file:
    file.write('[vxlanspine]')
    file.write('\n')

devicelist=[]

def collectspinemgmt():
    while True:
        print('******登记Spine switches***********')
        name=input('请输入需要管理的设备名：')
        mgmtip=input('请输入需要这个设备的管理地址：')
        compile_ip = re.compile('^(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|[1-9])\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)$')
        if compile_ip.match(mgmtip):
            device1={name:mgmtip}
            with open('hosts',"a") as file:

                file.write(f'{name} ansible_ssh_host={mgmtip}')
                file.write('\n')
            devicelist.append(device1)
        else:
            print('invailed ip')
            break

        exitinput=input('继续？（Y/N）：')
        with open('hosts', "a") as file:
            file.write('\n')
            file.write('[vxlanleaf]')
            file.write('\n')
        if exitinput.lower() == 'n':
            break




def collectleafmgmt():
    while True:
        print('******登记Leaf switches***********')
        name=input('请输入需要管理的设备名：')
        mgmtip=input('请输入需要这个设备的管理地址：')
        compile_ip = re.compile('^(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|[1-9])\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)$')
        if compile_ip.match(mgmtip):
            device1={name:mgmtip}
            with open('hosts',"a") as file:
                file.write(f'{name} ansible_ssh_host={mgmtip}')
                file.write('\n')
            devicelist.append(device1)
        else:
            print('invailed ip')
            break

        exitinput=input('继续？（Y/N）：')
        if exitinput.lower() == 'n':
            return

def exportdevicelist():
    return devicelist

if __name__== "__main__":
    exportdevicelist()
