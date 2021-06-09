from ncclient import manager

RTR1_MGR=manager.connect(host= '192.168.255.127',
                  port=830,
                  username='cisco',
                  password='cisco',
                  hostkey_verify=False,
                  device_params={'name':'csr'})

for RTR_Capability in RTR1_MGR.server_capabilities:
    print (RTR_Capability)

RTR1_MGR.close_session()
