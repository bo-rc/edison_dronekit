from UdpReceiver import *

jeep = UdpReceiver(45456)
jeep2 = UdpReceiver(45456)

print('gps:')
for i in xrange(5):
    print(jeep2.get_hil_gps())


print('local position:')
for i in xrange(5):
    print(jeep.get_loc_pos())


print('mocap, should hang:')
print(jeep.get_mocap())

