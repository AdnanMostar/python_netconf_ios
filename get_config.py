from ncclient import manager

RTR1_MGR=manager.connect(host= '192.168.255.127',
                  port=830,
                  username='cisco',
                  password='cisco',
                  hostkey_verify=False,
                  device_params={'name':'csr'})

print (RTR1_MGR.get_config('running'))
RTR1_MGR.close_session()
