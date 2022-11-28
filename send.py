import json
import threading
import bluetooth
from start_discoverable import start_discoverable


start_discoverable()

json_file = open('settings.json', 'r')
json_data = json.load(json_file)

bd_addr = "DC:A6:32:8C:8F:AA"


send_data_list = ('Hello')
port = 15
sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )

print(f'trying to connect to {bd_addr} on {port}')
sock.connect((bd_addr, port))
print('connected. type stuff')
sock.send(send_data_list)
print(f'Data received:{str(send_data_list)}')

sock.close()

