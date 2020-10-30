import re
import json
import requests

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

def addportdescription(devicelist):

    for i in devicelist:

        for HostName,mgmt_ip in i.items():
            print(HostName)
            print(mgmt_ip)

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
                    "input": "show cdp neighbors",
                    "output_format": "json"
                }}

            response = requests.post(url, data=json.dumps(payload), headers=myheaders, auth=(switchuser, switchpassword)).json()
            output = json.dumps(response, indent=4, sort_keys=True)
            output_json = json.loads(output)
            neighbor_list=output_json['ins_api']['outputs']['output']['body']['TABLE_cdp_neighbor_brief_info']['ROW_cdp_neighbor_brief_info']





            for temp1 in neighbor_list:
                neighber_info = {"peername": temp1["device_id"], 'localport':temp1['intf_id'], 'peerport':temp1['port_id']}

                print(neighber_info)


                base_url = 'http://' + mgmt_ip + '/api/'

                # create credentials structure
                name_pwd = {'aaaUser': {'attributes': {'name': "admin", 'pwd': "cisco!123"}}}
                json_credentials = json.dumps(name_pwd)

                # log in to API
                login_url = base_url + 'aaaLogin.json'

                auth_cookie = {}
                response = requests.request("POST", login_url,data=json_credentials)

                if response.status_code == requests.codes.ok:
                    data=json.loads(response.text)["imdata"][0]

                    token=str(data['aaaLogin']['attributes']['token'])
                    auth_cookie={"APIC-cookie":token}


                headers = {'Content-Type':'application/json'}
                data2={
                    "interfaceEntity": {
                        "children": [
                            {
                                "l1PhysIf": {
                                    "attributes": {
                                        "descr": "cccccccc",
                                        "id": "eth1/4"
                                    }}}]}}

                data2["interfaceEntity"]["children"][0]["l1PhysIf"]["attributes"]["descr"]=f"To-{neighber_info['peername']}-{neighber_info['peerport']}"
                data2["interfaceEntity"]["children"][0]["l1PhysIf"]["attributes"]["id"] = f"{neighber_info['localport']}"[:3].lower()+f"{neighber_info['localport']}"[-3:]
                payload2=json.dumps(data2)
                changedecription = requests.request('POST',f'http://{mgmt_ip}/api/mo/sys/intf.json', headers = headers, cookies=auth_cookie,data=payload2)


                print(changedecription)

