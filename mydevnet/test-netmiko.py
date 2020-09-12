from netmiko import ConnectHandler

router = {"device_type":'cisco_nxos',
          'host':'10.124.39.29',
          'user':'siyxiao',
          'pass':'284561379Xsy!'}

net_connect = ConnectHandler(ip = router['host'],
                             username = router['user'],
                             password = router['pass'],
                             device_type= router['device_type'])

interface_cli = net_connect.send_command('show ip inter bri')

print(interface_cli)


cfg_commands = ['int e1/1', 'no sw', 'des test-1']
interface_cli = net_connect.send_config_set(cfg_commands)

print(interface_cli)