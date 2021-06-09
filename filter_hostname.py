from ncclient import manager

RTR1_MGR=manager.connect(host= '192.168.255.127',
                  port=830,
                  username='cisco',
                  password='cisco',
                  hostkey_verify=False,
                  device_params={'name':'csr'})

FILTER = """
<filter>
   <native
       xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
       <hostname></hostname>
   </native>
</filter>"""

print (RTR1_MGR.get_config('running',FILTER))

RTR1_MGR.close_session()
