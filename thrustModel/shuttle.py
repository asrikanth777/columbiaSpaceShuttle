"""
this file is for shuttle information in regards to calculating thrust
"""
import equations


class Shuttlecraft:
    def __init__(self, name, mass, engine):
        self.name = name
        self.mass = mass
        self.engine = engine

class Engine:
    def __init__(self, name, thrust_vacuum, thrust_sealevel, fuel_flowrate, burn_time, isp_vacuum, isp_sealevel):
        self.name = name
        self.thrust_vacuum = thrust_vacuum
        self.thrust_sealevel = thrust_sealevel
        self.fuel_flowrate = fuel_flowrate
        self.burn_time = burn_time
        self.isp_vacuum = isp_vacuum
        self.isp_sealevel = isp_sealevel
        self.fuel_consumed = 0
    
    def thrustCalculation(self, time):
        if time <= self.burn_time:
            # updates fuel consumed
            self.fuel_consumed += self.fuel_flowrate * time
            return self.thrust
        else:
            return 0
        
    def deltaV_calculation(self, mass):
        return self.isp * equations.gravity * (1 - (self.fuel_consumed / mass))








