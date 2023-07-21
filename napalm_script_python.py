import json
from napalm import get_network_driver
import time

driver = get_network_driver('ios')
device = driver('192.168.164.136', 'anwea', '02anwe05')
device.open()

print('######\nGETTING FACTS\n######')
facts = (device.get_facts())
print(json.dumps(facts, sort_keys=True, indent=8))
time.sleep(5)

print('\n\n########\nPING TEST\n########')
pingtest = device.ping('192.168.164.136')
print(json.dumps(pingtest, sort_keys=True, indent=8))
time.sleep(5)

print('\n\n######\nGETTING INTERFACE\n######')
intf = (device.get_interfaces())
print(json.dumps(intf, sort_keys=True, indent=8))

device.close()
