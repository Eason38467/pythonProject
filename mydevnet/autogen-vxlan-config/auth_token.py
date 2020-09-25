import requests

def get_token():


    auth = ('admin','cisco!123')
    headers={'Content-Type':'application/json'}

    auth_resp = requests.post(f'http://{v}/api/mo/sys/intf.json', headers=headers,auth=auth)
    auth_resp.raise_for_status()
    token = auth_resp.json()['Token']