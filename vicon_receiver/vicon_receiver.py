from dronekit import connect, VehicleMode

import time
from pymavlink import mavutil

data = mavutil.mavlink_connection('udp:192.168.1.11:45454')

while True:
    msg = data.recv_match(type='LOCAL_POSITION_NED')
    # If we have a valid message
    if msg is not None:
        print(msg.x, msg.y, msg.z, msg.vx, msg.vy, msg.vz)
