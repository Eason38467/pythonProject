from collectdeviceinfo import *
import json
import requests

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
        print(output)
