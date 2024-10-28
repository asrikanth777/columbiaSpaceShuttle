"""
This is the equations file, which will be used to calculate trajectory
- Kepler's Laws
- Vis-viva Equation

"""

import numpy as np
import matplotlib as mpl
from scipy import constants as spcons
from astropy import constants as apcons

# Important Constants
gravity = spcons.gravitational_constant # N*m^2 / kg^2
earthMass = apcons.E



# Vis-Viva Equation
# the Equation is v = sqrt(mew(2/r - 1/a))
# def VisViva():


