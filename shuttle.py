"""
this file is for shuttle information in regards to calculating thrust
"""
import equations


class Shuttle:
    def __init__(self, name, mass, engine):
        self.name = name
        self.mass = mass
        self.engine = engine

class Engine:
    def __init__(self, name, thrust, fuel_flowrate, burn_time, isp):
        self.name = name
        self.thrust = thrust
        self.fuel_flowrate = fuel_flowrate
        self.burn_time = burn_time
        self.isp = isp
        self.fuel_consumed = 0
    
    def thrustCalculation(self, time):
        if time <= self.burn_time:
            # updates fuel consumed
            self.fuel_consumed += self.fuel_flowrate * time
            return self.thrust
        else:
            return 0
        
    def deltaV_calculation(self, mass):
        return self.isp * equations.gravity * (1- (self.fuel_consumed / mass))








7