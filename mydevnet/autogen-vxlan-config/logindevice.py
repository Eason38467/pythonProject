from collectdeviceinfo import *
import json
import requests

from auth_token import get_token

allinfo=[]

def addportdescription(devicelist):

    for i in devicelist:
        for k,v in i.items():
            print(k)
            print(v)

            url = f'http://{v}/ins'
            print(url)
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
            print(response)
            print(output)
            neighber_list=output_json['ins_api']['outputs']['output']['body']['TABLE_cdp_neighbor_brief_info']['ROW_cdp_neighbor_brief_info']

            print(neighber_list)

            for temp1 in neighber_list:
                neighber_info = {"peername": temp1["device_id"], 'localport':temp1['intf_id'], 'peerport':temp1['port_id']}
                allinfo.append((k,temp1['intf_id']))

                print(neighber_info)


                base_url = 'http://' + v + '/api/'

                # create credentials structure
                name_pwd = {'aaaUser': {'attributes': {'name': "admin", 'pwd': "cisco!123"}}}
                json_credentials = json.dumps(name_pwd)

                # log in to API
                login_url = base_url + 'aaaLogin.json'

                auth_cookie = {}
                response = requests.request("POST", login_url,data=json_credentials)

                if response.status_code == requests.codes.ok:
                    data=json.loads(response.text)["imdata"][0]
                    print(data)
                    token=str(data['aaaLogin']['attributes']['token'])
                    auth_cookie={"APIC-cookie":token}

                print()
                print("aaaLogin RESPONSE:")
                print(json.dumps(json.loads(response.text), indent=2))
                print()

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
                changedecription = requests.request('POST',f'http://{v}/api/mo/sys/intf.json', headers = headers, cookies=auth_cookie,data=payload2)

                print(changedecription)




addportdescription()

print(allinfo)