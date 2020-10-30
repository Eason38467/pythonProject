#!/user/bin/env python

import xmltodict
from ncclient import manager


connect_params = { "host":"192.168.50.101", "port":830,"username":"admin", "password":"cisco!123","hostkey_verify":False, "allow_agent":False,"look_for_keys":False,"device_params":{"name":"nexus"},}


#**connnect_params 是将字典拆分为一个个参数
with manager.connect(**connect_params) as conn:

    nc_filter = """
  <System xmlns="http://cisco.com/ns/yang/cisco-nx-os-device">
    
    <currentTime/>
    <systemUpTime/>
    
  </System>
    """

    netconf_reply = conn.get_config('running', filter=("subtree",nc_filter))
    print(netconf_reply.xml)
    response = conn.get(filter=("subtree",nc_filter))
    print(response)
    intf_details = dict(xmltodict.parse(netconf_reply.xml))
    print(intf_details)

    #resp=conn.get_config(source="running")
    #print(resp.xml)



