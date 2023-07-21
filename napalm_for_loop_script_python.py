import json
from napalm import get_network_driver

device_ip = ['192.168.164.136', '192.168.164.137', '192.168.164.138']
for ip in device_ip:
	driver = get_network_driver('ios')
	device = driver(ip, 'anwea', '02anwe05')
	device.open()
	facts = (device.get_facts())
	print(json.dumps(facts, sort_keys=True, indent=8))
	print('###############\nPING TEST\n###############')
	pingtest = device.ping(ip)
	print(json.dumps(pingtest, sort_keys=True, indent=8) + '\n\n\n')

device.close()
