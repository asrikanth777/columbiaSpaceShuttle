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

a1 = np.array([ 0, 0, 0])
v1 = np.array([ 0, 0, 0])
x1 = np.array([ 0, 0, 0])
m1 = 0
Fdrag = 0
rho = 0


# going to simulate how it pitches as it ascends to that it goes into orbit
# this is because i am approximating thrust with the sealevel and vacuum readings
# might not even use the atmosphere calculations i planned before

a1[1] += ((Fthrust - FgravPhase1) / phase1mass)
v1[1] += (a1*timeStep)
x1[1] += (v1*timeStep)
totalFuelRate = columbia.ssme.fuel_flowrate + columbia.srb.fuel_flowrate
m1 += (phase1mass - (totalFuelRate)*timeStep)
timePassed += timeStep

# max altitude of the shuttle was at 274km
while (0 <= x1[1] <= 274000):

    rho = rocEq.atmosDensity(x1)

    if timePassed <= 120:
        cDrag = 0.55
        dragSurfaceAr = columbia.ssme.shuttle_surfacearea + columbia.ssme.externaltank_surfacearea + columbia.srb.tank_surfacearea

    else:
        cDrag = 1.1
        dragSurfaceAr = columbia.ssme.shuttle_surfacearea + columbia.ssme.externaltank_surfacearea

    Fdrag = rocEq.dragForce(rho, v1, cDrag, dragSurfaceAr)
    Fgrav = phase1mass * rocEq.gravity(x1[1])

    a1[1] = (Fthrust - Fdrag - Fgrav) / phase1mass
    v1[1] += a1[1] * timeStep
    x1[1] += v1[1] * timeStep

    m1 -= totalFuelRate*timeStep

    








