from netmiko import ConnectHandler

# 编辑需要管理的交换机的基本信息， 注意device_type 参数支持的类型：

# cisco_asa
# cisco_ios
# cisco_nxos
# cisco_s300
# cisco_tp
# cisco_wlc
# cisco_xe
# cisco_xr


switches = {"device_type": 'cisco_nxos',
            'host': '10.124.39.29',
            'user': 'siyxiao',
            'pass': '284561379Xsy!'}

# 使用Connecthandler方法来ssh到设备上
net_connect = ConnectHandler(ip=switches['host'],
                             username=switches['user'],
                             password=switches['pass'],
                             device_type=switches['device_type'])

# 需要进行的操作：
interface_cli = net_connect.send_command('show ip inter bri')
print(interface_cli)
print(type(interface_cli))

# 修改操作：
# cfg_commands = ['int e1/1', 'no sw', 'des test-1']
# interface_cli = net_connect.send_config_set(cfg_commands)

# print(interface_cli)

# 从配置文件中导入:

interface_cli = net_connect.send_config_from_file('config1.log')
print(interface_cli)
