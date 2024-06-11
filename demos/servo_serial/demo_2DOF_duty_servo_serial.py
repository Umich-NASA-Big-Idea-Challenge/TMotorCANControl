from TMotorCANControl.servo_serial import *
from NeuroLocoMiddleware.SoftRealtimeLoop import SoftRealtimeLoop

duty = 0.1

with TMotorManager_servo_serial(port = '/dev/ttyUSB0', baud=921600, motor_params=Servo_Params_Serial['AK80-9']) as dev1:
    with TMotorManager_servo_serial(port = '/dev/ttyUSB1', motor_params=Servo_Params_Serial['AK80-9']) as dev2:
        loop = SoftRealtimeLoop(dt=0.005, report=True, fade=0.0)
        dev1.set_zero_position()
        dev2.set_zero_position()
        dev1.update()
        dev2.update()
        
        dev1.enter_duty_cycle_control()
        dev2.enter_duty_cycle_control()
        for t in loop:
            dev1.set_duty_cycle_percent(duty)
            dev2.set_duty_cycle_percent(-duty)
            dev1.update()
            dev2.update()
            print(f"\r {dev1} {dev2}", end='')

        