from dronekit import connect, VehicleMode
import socket

import time
from pymavlink import mavutil

def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]
ip = get_ip_address()
print(ip)
port = '45455'
connection_string = 'udp:' + ip + ':' + port

data = mavutil.mavlink_connection(connection_string)
counter = 0
while True:
    msg = data.recv_match(type='LOCAL_POSITION_NED')
    # If we have a valid message
    if msg is not None:
        print(msg.x, msg.y, msg.z, msg.vx, msg.vy, msg.vz)
	print(counter)
	counter += 1
