import numpy as np
import matplotlib as mpl
from scipy import constants as spcons
from astropy import constants as apcons
import equations as adiEq

"""
An important thing to note is that the rocket travels through different atmospheres as it reaches orbit.
And because of this, air pressure keeps dropping as the rocket reaches higher.
So because of this, I need to model atmosphere constantly, and so it would be changing as a result of altitude, which is also a function of time by seconds
(it would be unreasonable to have altitude function over time in nanoseconds, i dont need that much accuracy)
Here are the different atmospheres it travels through, from first to last
1) Troposphere
2) Stratosphere
3) Mesosphere
4) Thermosphere
"""

altitude = 0
currentAtmosSphere = None
seaLevelTemp = 288.15 #Kelvin
gasConstant = apcons.R.value # gas constant (J/ mol*k)
airMolarMass = 0.0289647 # kg/mol


# I am starting by defining a class Atmosphere to declare important variables for calculation
class Atmosphere:
    def __init__(self, name, baseTemperature, basePressure, baseAltitude, scaleHeight, lapseRate): # these are characteristics
        # pressure and altitude are self explanatory, but scale height and lapse rates were new to me so here is what i learned
        # scale height is when atmosphere pressure to 37% of starting value (e^-1)
        # lapse rate is how temp decreases by each km, since it gets colder as you go up (Brrrrrrr)
        self.name = name
        self.baseTemperature = baseTemperature
        self.basePressure = basePressure
        self.baseAltitude = baseAltitude
        self.scaleHeight = scaleHeight
        self.lapseRate = lapseRate
    
    def altitudePressure(self, altitude):
        raise NotImplementedError("Each atmosphere should have its own calculation")
    
    


class tropoSphere(Atmosphere):
    def __init__(self):
        super().__init__(
            name =              "Troposphere",
            baseTemperature =   288.15,
            basePressure =      101.3,
            baseAltitude =      0,
            scaleHeight =       8.5,
            lapseRate =         -0.0065
        )
    # P = P(0) * (1 + lapserate/sealeveltemp * altitude_diff) ** ((-g * air molarmass) / (R * lapserate))
    def altitudePressure(self, altitude):
        if altitude <= 11000:
            instantPressure = self.basePressure * \
            (1 + (self.lapseRate/self.baseTemperature) * (altitude - self.baseAltitude)) ** ((-adiEq.gravity*airMolarMass) / (self.lapseRate * gasConstant))
            return instantPressure
   

class stratoSphere(Atmosphere):
    def __init__(self):
        super().__init__(
            name =              "Stratosphere",
            baseTemperature =   216.65,
            basePressure =      26.5,
            baseAltitude =      11000,
            scaleHeight =       7.0,
            lapseRate =         0
        )
    
    # P = P(0) * e**((-g*airmolarmass*altitude_diff)/(R*baseTemp)) 
    def altitudePressure(self, altitude):
        if 11000 <= altitude < 25000:
            instantPressure = self.basePressure * np.exp((-adiEq.gravity*airMolarMass*(altitude - self.baseAltitude))/(gasConstant*self.baseTemperature))
            return instantPressure
        
class mesoSphere(Atmosphere):
    def __init__(self):
        super().__init__(
            name =              "Mesosphere",
            baseTemperature =   270, 
            basePressure =      0.3,
            baseAltitude =      25000,
            scaleHeight =       6.5,
            lapseRate =         -0.0028

        )
    
    # P = P(0) * (1 + lapserate/sealeveltemp * altitude_diff) ** ((-g * air molarmass) / (R * lapserate))
    def altitudePressure(self, altitude):
        if 25000 <= altitude < 85000:
            instantPressure = self.basePressure * \
            (1 + (self.lapseRate/self.baseTemperature) * (altitude - self.baseAltitude)) ** ((-adiEq.gravity*airMolarMass) / (self.lapseRate * gasConstant))
            return instantPressure
       


class thermoSphere(Atmosphere):
    def __init__(self):
        super().__init__(
            name =              "Thermosphere",
            baseTemperature =   2340978510894571205, # doesnt matter, it isn't used and temp there is fluctuating
            basePressure =      0,
            baseAltitude =      85000,
            scaleHeight =       5.0,
            lapseRate =         0 # its not zero, but it is difficult to calculate lapserate, but its actually some what positive
        )
    
    # P = P(0) * e**(-(altitude_diff)/scale_height)
    def altitudePressure(self, altitude):
        if altitude >= 85000:
            instantPressure = self.basePressure * np.exp(-(altitude - self.baseAltitude)/self.scaleHeight)
            return instantPressure
        
    


def updateAtmosphere(altitude):
    if altitude < 11000:
        return tropoSphere()
    elif 11000 <= altitude < 25000:
        return stratoSphere()
    elif 25000 <= altitude < 85000:
        return mesoSphere()
    else:
        return thermoSphere()

    return currentAtmosSphere
    
def getPressure(altitude):
    currentAtmosSphere = updateAtmosphere(altitude)

    if currentAtmosSphere:
        pressure = currentAtmosSphere.altitudePressure(altitude)
        if pressure <= 0:
            return "Invalid Pressure at this altitude"
        return pressure
    else:
        return "Invalid Altitude"

# for testing purposes
test1 = 10000
test2 = 20000
test3 = 60000
test4 = 90000

print(getPressure(test1))
print(getPressure(test2))
print(getPressure(test3))
print(getPressure(test4))

""" Recap on calculated pressures
Given that I am struggling to find the right equations to model pressure,
these should be good enough/close enough to give accurate readings
trying to refine it more and more will be pointless, so its time
to move to modeling thrust
"""