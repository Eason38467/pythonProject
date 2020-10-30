

#先判断接口是否三层接口

import re
import json
import requests
import time
from addportdescription import *

print('''

此脚本基于Nexus 9000v测试，提前开启
feature nxapi
nxapi http port 80

''')


#创建一个空列表接收设备信息
devicelist=[]


def collectspinemgmt():
    while True:
        print('******登记switches***********')
        name=input('请输入需要管理的设备名：')
        mgmtip=input('请输入需要这个设备的管理地址：')
        compile_ip = re.compile('^(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|[1-9])\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)$')

        #判断输入的IP是否合法
        if compile_ip.match(mgmtip):
            #每个设备名字和管理口地址用字典的形式保存
            device1={name:mgmtip}
            devicelist.append(device1)
        else:
            print('Invalid ip')


        exitinput=input('继续？（Y/N）：')
        if exitinput.lower() == 'n':
            break

def genip():
    host_network=[]
    for add_network_bit in range(1, 254):
        host_bit = 1
        while host_bit < 254:
            host_network.append(f'10.1.{add_network_bit}.{host_bit}/30')
            host_bit += 4

    return host_network




def getdeviceinfo(mgmt_ip):

    url = f'http://{mgmt_ip}/ins'

    switchuser = 'admin'
    switchpassword = 'cisco!123'

    myheaders = {'content-type': 'application/json'}
    payload = {
        "ins_api": {
            "version": "1.0",
            "type": "cli_show",
            "chunk": "0",
            "sid": "1",
            "input": "show cdp neighbors detail",
            "output_format": "json"
        }}

    response = requests.post(url, data=json.dumps(payload), headers=myheaders, auth=(switchuser, switchpassword)).json()
    output = json.dumps(response, indent=4, sort_keys=True)
    output_json = json.loads(output)

    neighbor_list=output_json['ins_api']['outputs']['output']['body']['TABLE_cdp_neighbor_detail_info']['ROW_cdp_neighbor_detail_info']

    return neighbor_list


def getl3interface(port_list,mgmt_ip):
    l3interface = []
    #过滤需要的信息，并通过循环拿到所有l3接口

    url = f'http://{mgmt_ip}/ins'

    switchuser = 'admin'
    switchpassword = 'cisco!123'

    myheaders = {'content-type': 'application/json'}
    payload = {
        "ins_api": {
            "version": "1.0",
            "type": "cli_show",
            "chunk": "0",
            "sid": "1",
            "input": "show cdp neighbors detail",
            "output_format": "json"
        }}
    for temp1 in port_list:

        neighbor_info = {"peername": temp1["device_id"], 'localport': temp1['intf_id'],'peerport': temp1['port_id'],'peerportv4add':temp1['v4addr']}

        getport = neighbor_info['localport']
        payload['ins_api']["input"] = f'show interface eth{getport[-3:]} switchport'
        response = requests.post(url, data=json.dumps(payload), headers=myheaders, auth=(switchuser, switchpassword)).json()
        output2 = json.dumps(response, indent=4, sort_keys=True)
        output_json2 = json.loads(output2)

        port_capability = output_json2['ins_api']['outputs']['output']['body']['TABLE_interface']['ROW_interface']['switchport']
        if port_capability == 'Disabled':
            l3interface.append(getport)
    return l3interface



def addip(l3interface,mgmt_ip):

    counts=0
    url = f'http://{mgmt_ip}/ins'

    switchuser = 'admin'
    switchpassword = 'cisco!123'

    myheaders = {'content-type': 'application/json'}
    payload = {
        "ins_api": {
            "version": "1.0",
            "type": "cli_show",
            "chunk": "0",
            "sid": "1",
            "input": "show cdp neighbors detail",
            "output_format": "json"
        }}

    #判断cdp nei detai中对端是否有ip,并且ip不是v4mgmtaddr
    for ports in l3interface:

        ip=iplist.pop(counts)
        payload['ins_api']["input"] = f'show cdp neighbors interface e{ports[-3:]} detail'

        response = requests.post(url, data=json.dumps(payload), headers=myheaders, auth=(switchuser, switchpassword)).json()
        output3 = json.dumps(response, indent=4, sort_keys=True)
        output_json3 = json.loads(output3)
        neighbor_v4add = output_json3['ins_api']['outputs']['output']['body']['TABLE_cdp_neighbor_detail_info']['ROW_cdp_neighbor_detail_info']['v4addr']
        neighbor_mgmtadd= output_json3['ins_api']['outputs']['output']['body']['TABLE_cdp_neighbor_detail_info']['ROW_cdp_neighbor_detail_info']['v4mgmtaddr']


        # api get token
        base_url = 'http://' + mgmt_ip + '/api/'

        # create credentials structure
        name_pwd = {'aaaUser': {'attributes': {'name': "admin", 'pwd': "cisco!123"}}}
        json_credentials = json.dumps(name_pwd)

        # log in to API
        login_url = base_url + 'aaaLogin.json'

        auth_cookie = {}
        response = requests.request("POST", login_url, data=json_credentials)

        if response.status_code == requests.codes.ok:
            data = json.loads(response.text)["imdata"][0]

            token = str(data['aaaLogin']['attributes']['token'])
            auth_cookie = {"APIC-cookie": token}
            # build add_ip api
            headers = {'Content-Type': 'application/json'}
            data2 = {"topSystem": {"children": [{"ipv4Entity": {"children": [{"ipv4Inst": {"children": [{"ipv4Dom": {"attributes": {"name": "default"},"children": [
                                                                                                                    {
                                                                                                                        "ipv4If": {
                                                                                                                            "attributes": {
                                                                                                                                "id": "eth1/2"},
                                                                                                                            "children": [
                                                                                                                                {
                                                                                                                                    "ipv4Addr": {
                                                                                                                                        "attributes": {
                                                                                                                                            "addr": "10.0.0.1/30"}}}]}}]}}]}}]}}]}}

            #如果 neighbor_v3add == neighbor_mgmtadd ，说明对端接口没有， 本地需要配置ip
            if neighbor_v4add == neighbor_mgmtadd:

                #修改payload中 接口
                data2["topSystem"]["children"][0]['ipv4Entity']['children'][0]['ipv4Inst']['children'][0]['ipv4Dom']['children'][0]['ipv4If']['attributes']['id'] = f"{ports}"[:3].lower() + f"{ports}"[-3:]
                #修改payload中的ip
                data2["topSystem"]["children"][0]['ipv4Entity']['children'][0]['ipv4Inst']['children'][0]['ipv4Dom']['children'][0]['ipv4If']['children'][0]['ipv4Addr']['attributes']['addr']= ip
                payload2 = json.dumps(data2)
                changedecription = requests.request('POST', f'http://{mgmt_ip}/api/mo/sys.json', headers=headers, cookies=auth_cookie, data=payload2)

                print('修改没有ip的接口')


            else:
                data2["topSystem"]["children"][0]['ipv4Entity']['children'][0]['ipv4Inst']['children'][0]['ipv4Dom']['children'][0]['ipv4If']['attributes']['id'] = f"{ports}"[:3].lower() + f"{ports}"[-3:]
                #修改payload中的ip
                host_ip=neighbor_v4add.split('.')
                new_host_ip=str(int(host_ip[3])+1)
                newip=host_ip[0] + '.'+host_ip[1]+'.'+host_ip[2]+'.'+ new_host_ip+'/30'
                data2["topSystem"]["children"][0]['ipv4Entity']['children'][0]['ipv4Inst']['children'][0]['ipv4Dom']['children'][0]['ipv4If']['children'][0]['ipv4Addr']['attributes']['addr']= newip
                payload2 = json.dumps(data2)
                changedecription = requests.request('POST', f'http://{mgmt_ip}/api/mo/sys.json',headers=headers, cookies=auth_cookie, data=payload2)
                print('修改有ip的接口')


        counts += 1




devices= [{'spine1':"192.168.50.101"},{'spine2':"192.168.50.102"},{'leaf1':"192.168.50.103"},{'leaf2':"192.168.50.104"},{'leaf3':"192.168.50.105"},{'leaf4':"192.168.50.106"},]



iplist = genip()

addportdescription(devices)

for i in devices:

    for Hostname, mgmt_ip in i.items():

        #clear cdp nei
        url = f'http://{mgmt_ip}/ins'

        switchuser = 'admin'
        switchpassword = 'cisco!123'

        myheaders = {'content-type': 'application/json'}
        payload = {
            "ins_api": {
                "version": "1.0",
                "type": "cli_show",
                "chunk": "0",
                "sid": "1",
                "input": "clear cdp table",
                "output_format": "json"
            }}

        response = requests.post(url, data=json.dumps(payload), headers=myheaders,auth=(switchuser, switchpassword)).json()


        time.sleep(6)

        device_lists = getdeviceinfo(mgmt_ip)
        portlists=getl3interface(device_lists,mgmt_ip)

        addipforeachdevice=addip(portlists,mgmt_ip)
        print(addipforeachdevice)







