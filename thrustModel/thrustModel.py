import numpy as np
import scipy as sp
import equations as eq
import rocketThrustEqs as rocEq
import shuttle as columbia

"""
at launch, we have our initial conditions, specifically our thrust
we start with a, and our time step of t

a = Fthrust - Fdrag - Fgravity / m
vNew = vOld+ a*deltaT
xNew = xOld + vNew*deltaT
"""
timeStep = 10
timePassed = 0
FthrustInit = columbia.ssme.thrust_sealevel + columbia.srb.thrust_sealevel
rhoInit = rocEq.atmosDensity(0)

#ignoring drag in the first time step at 10s

phase1mass = columbia.ssme.fueltank_max + columbia.srb.fueltank_max 
FgravPhase1  = phase1mass * eq.gravity

a1 = 0
v1 = 0
x1 = 0
m1 = 0

a1 += ((FthrustInit - FgravPhase1) / phase1mass)
v1 += (a1*timeStep)
x1 += (v1*timeStep)
m1 += (phase1mass - (columbia.ssme.fuel_flowrate - columbia.srb.fuel_flowrate)*timeStep)











