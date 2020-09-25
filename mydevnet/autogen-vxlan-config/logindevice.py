from collectdeviceinfo import *
import json
import requests

from auth_token import get_token

devices = [{'leaf-1': '192.168.50.104'}]

for i in devices:
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
        print(output_json)
        peername=output_json['ins_api']['outputs']['output']['body']['TABLE_cdp_neighbor_brief_info']['ROW_cdp_neighbor_brief_info']['device_id']
        localport= output_json['ins_api']['outputs']['output']['body']['TABLE_cdp_neighbor_brief_info']['ROW_cdp_neighbor_brief_info']['intf_id']
        peerport= output_json['ins_api']['outputs']['output']['body']['TABLE_cdp_neighbor_brief_info'][
                  'ROW_cdp_neighbor_brief_info']['port_id']
        print(peername,localport,peerport)



        session = requests.session()

        base_url = 'http://' + v + '/api/'

        # create credentials structure
        name_pwd = {'aaaUser': {'attributes': {'name': "admin", 'pwd': "cisco!123"}}}
        json_credentials = json.dumps(name_pwd)

        # log in to API
        login_url = base_url + 'aaaLogin.json'
        session.post(login_url, data=json_credentials)

        # get token from login response structure
        auth = json.loads(post_response.text)
        #login_attributes = auth['imdata'][0]['aaaLogin']['attributes']
        #auth_token = login_attributes['token']

        #print(auth_token)



        headers = {'Content-Type':'application/json', 'X-Auth-Token':auth_token}
        data={
            "interfaceEntity": {
                "children": [
                    {
                        "l1PhysIf": {
                            "attributes": {
                                "descr": f"To+' '+' '+{peername}+' '+{peerport}",
                                "id": f"{localport}"
                            }}}]}}

        changedecription = requests.post(f'http://{v}/api/mo/sys/intf.json', headers=headers,data=data)

        print(changedecription)




