import numpy as np
import matplotlib as mpl
from scipy import constants as spcons
from astropy import constants as apcons

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

# I am starting by defining a class Atmosphere to declare important variables for calculation
class Atmosphere:
    def __init__(self, name, basePressure, baseAltitude, scaleHeight, lapseRate): # these are characteristics
        # pressure and altitude are self explanatory, but scale height and lapse rates were new to me so here is what i learned
        # scale height is when atmosphere pressure to 37% of starting value (e^-1)
        # lapse rate is how temp decreases by each km, since it gets colder as you go up (Brrrrrrr)
        self.name = name
        self.basePressure = basePressure
        self.baseAltitude = baseAltitude
        self.scaleHeight = scaleHeight
        self.lapseRate = lapseRate

tropoSphere = Atmosphere(
    
)

stratoSphere = Atmosphere(

)

mesoSphere = Atmosphere(

)

thermoSphere = Atmosphere(
    
)    

