# Import mavutil
from pymavlink import mavutil

# Create the connection
# Need to provide the serial port and baudrate
master = mavutil.mavlink_connection(
            '/dev/serial/by-id/usb-ArduPilot_fmuv3_2F004A000F51363130363134-if00',
            baud=115200)

# Restart the ArduSub board !
master.reboot_autopilot()

