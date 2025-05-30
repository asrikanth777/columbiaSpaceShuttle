"""
This is the equations file, which will be used to calculate trajectory
- Kepler's Laws
- Vis-viva Equation

"""

import numpy as np
from scipy import constants as spcons
from astropy import constants as apcons

# Important Constants
gravity = apcons.g0.value
gravityConst = spcons.gravitational_constant # N*m^2 / kg^2
earthMass = apcons.M_earth.value
earthRadius = apcons.R_earth.value
seaLevelPA = apcons.atm.value
seaLevelKPA = seaLevelPA / 1000



def vis_viva(mu, r, a):
    """
    Calculate orbital speed using the vis-viva equation.

    Parameters:
        mu (float): Standard gravitational parameter (G*M)
        r (float): Current distance from central body [m]
        a (float): Semi-major axis of the orbit [m]

    Returns:
        float: Orbital velocity [m/s]
    """
    return np.sqrt(mu * (2/r - 1/a))



