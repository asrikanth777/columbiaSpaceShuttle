"""
This file is for the class: Rocket and components
- Rocket isn't restricted to rocket, any kind of spacecraft can usually work
- Spacecraft path trajectory can be roughly estimated with just mass, velocity, and altitude
"""

class Rocket:
    def __init__(self, name, mass, altitude, velocity, engine):
        self.name = name
        self.mass = mass
        self.altitude = altitude
        self.velocity = velocity
        self.engine = engine

class Engine:
    def __init__(self, thrust, isp):
        self.thrust = thrust
        self.isp = isp


