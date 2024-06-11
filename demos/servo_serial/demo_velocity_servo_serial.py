#from sys import path
#path.append("/home/pi/TMotorCANControl/src/")
from TMotorCANControl.servo_serial import *
from NeuroLocoMiddleware.SoftRealtimeLoop import SoftRealtimeLoop

vel = 9

with TMotorManager_servo_serial(port = '/dev/ttyUSB0', motor_params=Servo_Params_Serial['AK80-9']) as dev:
        loop = SoftRealtimeLoop(dt=0.005, report=True, fade=0.0)
        dev.enter_velocity_control()
        
        dev.set_zero_position()
        dev.update()
        
        for t in loop:
            dev.set_output_velocity_radians_per_second(vel)
            dev.update()
            print(f"\r {dev}", end='')

        