"""
this file is for shuttle information in regards to calculating thrust
"""
import equations
import numpy as np


class Shuttlecraft:
    def __init__(self, name, mass, engine):
        self.name = name
        self.mass = mass
        self.engine = engine

class Engine:
    def __init__(self, name, thrust_vacuum, thrust_sealevel, fuel_flowrate, burn_time, isp_vacuum, isp_sealevel, fueltank_max,empty_tank):
        self.name = name
        self.thrust_vacuum = thrust_vacuum
        self.thrust_sealevel = thrust_sealevel
        self.fuel_flowrate = fuel_flowrate
        self.burn_time = burn_time
        self.isp_vacuum = isp_vacuum
        self.isp_sealevel = isp_sealevel
        self.fuel_consumed = 0
        self.fueltank_max = fueltank_max 
        self.empty_tank = empty_tank
"""
    def thrustCalculation(self, time):
        if time <= self.burn_time:
            # updates fuel consumed
            self.fuel_consumed += self.fuel_flowrate * time
            return self.thrust
        else:
            return 0
        
    def deltaV_calculation(self, mass):
        return self.isp * equations.gravity * (1 - (self.fuel_consumed / mass))
"""

ssme = Engine(
    name = "RS-25",
    thrust_vacuum = 2279, # kN
    thrust_sealevel = 1860, # kN
    fuel_flowrate = 514.49, # kg/s
    burn_time = 510, # seconds (8.5 minutes) 
    isp_vacuum= 452.3, # seconds (4.436km/s)
    isp_sealevel= 366, # seconds (3.59km/s)
    fueltank_max= 733000, # combined
    empty_tank= 26500,
    externaltank_diameters = 8.4, #m
    externaltank_height = 46.93, #m 
    externaltank_surfacearea = 1238.45, #m^2
    shuttle_diameter = 5.2, #m
    shuttle_length = 37.24, #m
    shuttle_surfacearea = 608.36

)

srb = Engine (
    name = "SRB BI-1",
    thrust_vacuum = 27000, # kN
    thrust_sealevel = 24000, # kN
    fuel_flowrate = 3662, # kg/s (both boosters burn fuel)
    burn_time = 123, # seconds (8.5 minutes) 
    isp_vacuum= 268, # seconds (4.436km/s)
    isp_sealevel= 242, # seconds (3.59km/s)  
    fueltank_max = 454000, # kg (combined)
    empty_tank= 180000,
    tank_diameters = 3.71, # m
    tank_height = 45.46, #m
    tank_surfacearea = 1061.08 #m^2 its 2 * (2*pi*(3.71/2)*45.46)
"""     srb cross sectional area
        45.46m long, 3.71m diam
        area = 2pi*(d/2)*h
"""

)











