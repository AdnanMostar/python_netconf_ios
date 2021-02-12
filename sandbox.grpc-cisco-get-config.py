from iosxr_grpc.cisco_grpc_client import CiscoGRPCClient

# IOS XR gRPC settings:
ios_xr_ip = "sbx-iosxr-mgmt.cisco.com"
ios_xr_port = 5777
ios_xr_timeout = 10
ios_xr_username = "admin"
ios_xr_password = "C1sco12345"

# YANG
yang_module = "Cisco-IOS-XR-ipv4-arp-cfg"
yang_container = "arpgmp"

# Connect to IOS XR router.
client = CiscoGRPCClient(ios_xr_ip, ios_xr_port, ios_xr_timeout,ios_xr_username,ios_xr_password)

path = '{"%s:%s": [null]}' % (yang_module,yang_container)
result = client.getconfig(path)
print(result[1])
