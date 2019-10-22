
# Import mavutil
from pymavlink import mavutil

# Create the connection
#  If using a companion computer
#  the default connection is available
#  at ip 192.168.2.1 and the port 14550
# Note: The connection is done with 'udpin' and not 'udpout'.
#  You can check in http:192.168.2.2:2770/mavproxy that the communication made for 14550
#  uses a 'udpbcast' (client) and not 'udpin' (server).
#  If you want to use QGroundControl in parallel with your python script,
#  it's possible to add a new output port in http:192.168.2.2:2770/mavproxy as a new line.
#  E.g: --out udpbcast:192.168.2.255:yourport
# master = mavutil.mavlink_connection('udpin:/dev/serial/by-id/usb-ArduPilot_fmuv3_2F004A000F51363130363134-if00')
master = mavutil.mavlink_connection('udpin:127.0.0.1:14550')

# output_port = 'udpout:127.0.0.1:14560'
str_output_port = 'udpbcast:192.168.179.255:14560'
output_port = mavutil.mavlink_connection(str_output_port, input=False)
# MPState().mav_outputs.append(mavutil.mavlink_connection(port, baud=int(opts.baudrate), input=False))

# Get some information !
str_packet_type = 'mavpackettype'
# str_gps_raw_int = 'GPS_RAW_INT'
str_glo_pos_int = 'GLOBAL_POSITION_INT'

while True:
    try:
	current_info = master.recv_match(type=str_glo_pos_int)
	flag = (current_info != None)

	if flag == True:
		# msg = str(current_info[str_gps_raw_int])
		print(current_info)
        	# print(msg)
        	# print('hoge')
		output_port.mav.global_position_int_send(
			0,
			1.0,
			1.0,
			1.0,
			1.0,
			1.0,
			1.0,
			)
		
    except:
        pass
    # time.sleep(0.00001)
'''
Output:
{'mavpackettype': 'AHRS2', 'roll': -0.11364290863275528, 'pitch': -0.02841472253203392, 'yaw': 2.0993032455444336, 'altitude': 0.0, 'lat': 0, 'lng': 0}
{'mavpackettype': 'AHRS3', 'roll': 0.025831475853919983, 'pitch': 0.006112074479460716, 'yaw': 2.1514968872070312, 'altitude': 0.0, 'lat': 0, 'lng': 0, 'v1': 0.0, 'v2': 0.0, 'v3': 0.0, 'v4': 0.0}
{'mavpackettype': 'VFR_HUD', 'airspeed': 0.0, 'groundspeed': 0.0, 'heading': 123, 'throttle': 0, 'alt': 3.129999876022339, 'climb': 3.2699999809265137}
{'mavpackettype': 'AHRS', 'omegaIx': 0.0014122836291790009, 'omegaIy': -0.022567369043827057, 'omegaIz': 0.02394154854118824, 'accel_weight': 0.0, 'renorm_val': 0.0, 'error_rp': 0.08894175291061401, 'error_yaw': 0.0990816056728363}
'''

