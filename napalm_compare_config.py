from napalm import get_network_driver

driver = get_network_driver('ios')
device = driver('192.168.164.136','anwea','02anwe05')
device.open()

device.load_merge_candidate(filename='napalm_compare_vlan')
print(device.compare_config())

choice = input ('\nWould you like to commit the changes? [yN]: ')
if choice == 'y':
	print('Committing...')
	device.commit_config()
else:
	print('Discarding...')
	device.discard_config()
device.close()
print('Done.')
	
