from NeuroLocoMiddleware.SoftRealtimeLoop import SoftRealtimeLoop
try:
     from TMotorCANControl.mit_can import TMotorManager
except ModuleNotFoundError:
    from sys import path
    path.append("/home/pi/TMotorCANControl/src")
    from TMotorCANControl.mit_can import TMotorManager
import numpy as np
import time


with TMotorManager(motor_type='AK80-9', motor_ID=3, CSV_file="log.csv") as dev:
    dev.zero_position() # has a delay!
    time.sleep(1.5)
    dev.set_impedance_gains_real_unit(K=10,B=0.5)
    loop = SoftRealtimeLoop(dt = 0.01, report=True, fade=0)
    for t in loop:
        dev.update()
        if t < 1.0:
            dev.θ = 0.0
        else:
            dev.θ = 0.5*np.sin(np.pi*t)
        

    del loop