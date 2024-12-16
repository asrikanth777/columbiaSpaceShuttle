import numpy as np
import equations as eq
import shuttle as s



def ThrustEquation(altitude):
    # i have sealevel and vacuum values, im going to just approximate based on altitude
    thrust_SRB = s.srb.thrust_sealevel + (altitude/100000)*(s.srb.thrust_vacuum-s.srb.thrust_sealevel)
    thrust_SSME = s.ssme.thrust_sealevel + (altitude/100000) * (s.ssme.thrust_vacuum-s.srb.thrust_sealevel)


def tsiolkovsky(ve, mi, mf):
    deltaV = ve * np.log(mi/mf)
    return deltaV

def dragForce(rho, v, cD, a):
    # cD at launch is 0.55 with srb and tank, and cD after dispatch is 1.1
    vNorm = np.linalg.norm(v)
    Fdrag = (1/2)*rho*(vNorm**2)*cD*a
    return Fdrag

def specificImpulse(h, time):
    # assuming that iSP vaccuum range is at 100km
    # we are using an approximation between sealevel and vaccuum values
    # using that i am finding the exhaust velocity
    iSP_srb = s.srb.isp_sealevel + (h/100000)*(s.srb.isp_vacuum-s.srb.isp_sealevel)
    iSP_ssme = s.ssme.isp_sealevel + (h/100000) * (s.ssme.isp_vacuum-s.srb.isp_sealevel)


    return iSP

def exhaustVelRelat(iSP):
    ve = iSP * eq.gravity
    return ve

def atmosDensity(altitude):
    # sea level density = 1.225kg/m^3
    rhoFin = 1.225*np.exp(altitude/8500)


def gravity(altitude):
    G = eq.gravityConst
    M = eq.earthMass
    R = eq.earthRadius
    return G * M / (R + altitude)**2


""" some extra info
a = Fthrust - Fdrag - Fgravity / m
vNew = vOld+ a*deltaT
xNew = xOld + vNew*deltaT
"""
