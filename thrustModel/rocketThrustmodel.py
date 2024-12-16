import numpy as np
import equations as eq



def ThrustEquation(mdot, ve, ae, pe, pa):
    if mdot <= 0 or ve <= 0 or ae <= 0 or pe < 0 or pa < 0:
        raise ValueError("input variables must be positive, check")

    Fthrust = mdot*ve + ae*(pe-pa)

    if Fthrust <= 0:
        raise ValueError("Thrust must be positive, check parameters")

    return Fthrust

def massFlowRate(rho, ae, ve):
    if rho <= 0 or ae <= 0 or ve <= 0:
        raise ValueError("")
    
    mdot = rho*ae*ve
    if mdot <= 0:
        raise ValueError("mass flow rate should not be negative here")
    return mdot

def tsiolkovsky(ve, mi, mf):
    deltaV = ve * np.log(mi/mf)
    return deltaV

def dragForce(rho, v, cD, a):
    Fdrag = (1/2)*rho*(v**2)*cD*a
    return Fdrag

def specificImpulse(Fthrust, mdot):
    iSP = Fthrust/(mdot*eq.gravity)
    return iSP

def exhaustVelRelat(iSP):
    ve = iSP * eq.gravity
    return ve

