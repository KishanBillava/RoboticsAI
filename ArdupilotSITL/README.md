# Ardupilot SITL using DroneKit



> **Start SITL simulator**

```
cd ardupilot/ArduCopter
sim_vehicle.py -w
sim_vehicle.py --console --map
```
![image](https://user-images.githubusercontent.com/84302215/141613076-917673c0-5c92-4dc7-b2fc-54b2b675a453.png)



> **mavproxy command** 
>  take off, arm the throttle, set the wind speed and fly, change mode and return 
```
qloiter
arm throttle
rc 3 1700
param set SIM_WIND_SPD 4
qhover
param set Q_RTL_MODE 1
cruise
rc 1 1300
rc 1 1500 

```
![image](https://user-images.githubusercontent.com/84302215/141613003-e6f1f584-d33b-4302-aeb4-1c9bc947ce1e.png)


>  **DroneKit**
```
dronekit-sitl copter
mavproxy.py --master tcp:127.0.0.1:5760 --sitl 127.0.0.1:55001 --out 127.0.0.1:14550 --out 127.0.0.1:14551
```


