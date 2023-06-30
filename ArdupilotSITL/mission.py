import time 
from dronekit import connect, VehicleMode, LocationGlobalRelative, Command, LocationGlobal
from pymavlink import mavutil

# Reference 
# https://dronekit-python.readthedocs.io/en/latest/guide/taking_off.html 
# https://dronekit-python.readthedocs.io/en/latest/examples/drone_delivery.html
# https://dronekit-python.readthedocs.io/en/latest/automodule.html#dronekit.LocationGlobalRelative

# Object Oriented approach to code and checkpoints to each action 

class Drone(object):
    def __init__(self):
        self._log('Connecting to vehicle')
        self.vehicle = vehicle

    def launch(self, altitude):
        self._log("setting up to launch Drone")
        while not self.vehicle.is_armable: # Returns True if the vehicle is ready to arm, false otherwise (Boolean).
            self._log("Vehicle is not ready to arm")
            time.sleep(1)    

        self.arm()
        self.takeoff(altitude)
        self.vehicle.airspeed = 5
        self.go_to()  # (lat, lon, alt=None)

        # Here we can do anything 
        time.sleep(10)
        
        self.come_back()


    def arm(self):
        self._log("vehicle is ready to arm")
        self._log("Waiting for arming...")
        self.vehicle.mode = VehicleMode("GUIDED") # This attribute is used to get and set the current flight mode.
        self.vehicle.armed = True  # This attribute can be used to get and set the armed state of the vehicle (boolean).
        while not self.vehicle.armed:
            time.sleep(1)
        
    def takeoff(self,altitude):
        self._log("Taking off")
        self.vehicle.simple_takeoff(altitude)
        # wait to reach the target altitude 
        while True:
            v_alt = vehicle.location.global_relative_frame.alt # A global location object, with attitude relative to home location altitude.
            if v_alt >= altitude -1:
                self._log("altitude reached")
                break
            time.sleep(1)

    def go_to(self):
        self._log("Go to the waypoint")
        # LocationGlobalRelative(lat, lon, alt=None)
        # A global location object, with attitude relative to home location altitude
        waypoint_1 = LocationGlobalRelative(-35.363031, 149.159348, 20) 
        self.vehicle.simple_goto(waypoint_1)

    def come_back(self):
        self._log("returning to home")
        self.vehicle.mode = VehicleMode("RTL")
        time.sleep(20)
        vehicle.close()

    def _log(self,message):
        print("[DEBUG]:{0}".format(message))


# Connect to the Vehicle
vehicle = connect('tcp:127.0.0.1:5762', wait_ready=True)
Drone().launch(10)
# End 


#  ---------------------------------------------------------------------------------- # 
# Output 

# [DEBUG]:Connecting to vehicle
# [DEBUG]:setting up to launch Drone
# [DEBUG]:vehicle is ready to arm
# [DEBUG]:Waiting for arming...
# [DEBUG]:Taking off
# [DEBUG]:altitude reached
# [DEBUG]:Go to the waypoint
# [DEBUG]:returning to home
# 

# Mavproxy Output

# ARMED
# GUIDED> Mode GUIDED
# AP: Arming motors
# AP: EKF3 IMU1 MAG0 in-flight yaw alignment complete
# AP: EKF3 IMU0 MAG0 in-flight yaw alignment complete
# height 15
# RTL> Mode RTL
# Flight battery warning
# AP: SIM Hit ground at 0.477301 m/s
# AP: Disarming motors
# DISARMED
# height 5
