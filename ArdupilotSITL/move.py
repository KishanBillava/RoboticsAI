# 
# https://ardupilot.org/dev/docs/copter-commands-in-guided-mode.html#movement-command-details
# 

from pymavlink import mavutil
# tcp:127.0.0.1:5762 
# udpin:localhost:14551
the_connection = mavutil.mavlink_connection('tcp:127.0.0.1:5762 ')
the_connection.wait_heartbeat()
print('Heartbeat from system (system %u component %u)'%(the_connection.target_system, the_connection.target_component))


the_connection.mav.send(mavutil.mavlink.MAVLink_set_position_target_global_int_message(10, 
                        the_connection.target_system, the_connection.target_component, 
                        mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT, 
                        int(0b110111111000), int(-35.3629849 * 10 ** 7), int(149.1649185 * 10 ** 7), 
                        10, 0, 0, 0, 0, 0, 0, 1.57, 0.5))


while 1:
    msg = the_connection.recv_match(type='LOCAL_POSITION_NED', blocking=True)
    print(msg)
