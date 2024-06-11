#from TMotorCANControl.servo_serial import TMotorManager_servo_serial

#import sys
#sys.path.append('/home/test_ws/src/TMotorCANControl/src/')
from TMotorCANControl.servo_serial import TMotorManager_servo_serial

# CHANGE THESE TO MATCH YOUR DEVICE!
Type = 'AK80-9'
ID = 0

with TMotorManager_servo_serial(port= '/dev/ttyUSB0') as dev: #motor_type=Type, motor_ID=ID
    if dev.check_connection():
        print("\nmotor is successfully connected!\n")
    else:
        print("\nmotor not connected. Check dev power, network wiring, and Serial bus connection.\n")
    