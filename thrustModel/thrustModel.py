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
Fthrust = columbia.ssme.thrust_sealevel + columbia.srb.thrust_sealevel
rhoInit = rocEq.atmosDensity(0)

#ignoring drag in the first time step at 10s

phase1mass = columbia.ssme.fueltank_max + columbia.srb.fueltank_max 
FgravPhase1  = phase1mass * eq.gravity

a1 = 0
v1 = 0
x1 = 0
m1 = 0
Fdrag = 0
rho = 0


# for the sake of time, i am not going to simulate how it moves side to side
# i am going to assume it goes straight up, not complicating calculations

a1 += ((Fthrust - FgravPhase1) / phase1mass)
v1 += (a1*timeStep)
x1 += (v1*timeStep)
m1 += (phase1mass - (columbia.ssme.fuel_flowrate - columbia.srb.fuel_flowrate)*timeStep)
timePassed += timeStep

# max altitude of the shuttle was at 274km
while (0 <= x1 <= 274000):

    rho = rocEq.atmosDensity(x1)

    if timePassed <= 120:
        cDrag = 0.55
    else:
        cDrag = 1.1


    Fdrag = rocEq.dragForce(rho, v1, cDrag, )









