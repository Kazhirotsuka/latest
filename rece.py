import json
import threading
import bluetooth
from server import rfcomm_server
from start_discoverable import start_discoverable


start_discoverable()

receive_data_list = []

server_sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )

port = 15
server_sock.bind(("",port))
server_sock.listen(1)

print('Waiting for data.')
client_sock,address = server_sock.accept()
print ("Accepted data from ",address)

print('receiving...')
data = client_sock.recv(1024)
print ("received [%s]" % data)
client_sock.close()

print('connection closed')

server_sock.close()
