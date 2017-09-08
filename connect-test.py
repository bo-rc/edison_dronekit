import time
from dronekit import connect, VehicleMode

# vehicle = connect("tcp:127.0.0.1:5760", wait_ready=True) # TCP
# vehicle = connect("127.0.0.1:14550", wait_ready=True) # UDP
vehicle = connect("/dev/ttyMFD1", wait_ready=True) # serial to pixhawk2

print(" Mode: " + vehicle.mode.name)
print(" GPS: " + vehicle.gps_0)
print(" Global Location: " + vehicle.location.global_frame)
print(" Local Location: " + vehicle.location.local_frame)

vehicle.close()

print("Completed")

