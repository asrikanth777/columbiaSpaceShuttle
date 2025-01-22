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
rhoInit = rocEq.atmosDensity(10000)
print(rhoInit)

# mass of shuttle, tank, and boosters
eTankMass = columbia.ssme.fueltank_max
shuttleMass = columbia.shuttle.mass
srbMass = columbia.srb.fueltank_max

# thrust of shuttle engines and boosters
ssmeThrust = columbia.ssme.thrust_sealevel
srbThrust = columbia.srb.thrust_sealevel

# mass flow rate of eTank and boosters
eTankFlow = columbia.ssme.fuel_flowrate*timeStep
srbFlow = columbia.srb.fuel_flowrate*timeStep

#ignoring drag in the first time step at 10s


a1 = np.array([ 0, 0, 0])
v1 = np.array([ 0, 0, 0])
x1 = np.array([ 0, 0, 0])

Fdrag = 0

# going to simulate how it pitches as it ascends to that it goes into orbit
# this is because i am approximating thrust with the sealevel and vacuum readings
# might not even use the atmosphere calculations i planned before

while (0 <= x1[1] <= 274000):
    totalMass = eTankMass + shuttleMass + srbMass
    x[1] = 28000000000

    



"""
a1[1] += ((Fthrust - FgravPhase1) / phase1mass)
v1[1] += (a1*timeStep)
x1[1] += (v1*timeStep)

totalFuelRate = columbia.ssme.fuel_flowrate + columbia.srb.fuel_flowrate + columbia.shuttle.mass
m1 += (phase1mass - (totalFuelRate)*timeStep)
timePassed += timeStep

# max altitude of the shuttle was at 274km
while (0 <= x1[1] <= 274000):

    rho = rocEq.atmosDensity(x1)

    if timePassed <= 120:
        cDrag = 0.55
        dragSurfaceAr = columbia.ssme.shuttle_surfacearea + columbia.ssme.externaltank_surfacearea + columbia.srb.tank_surfacearea
        totalFuelRate = columbia.ssme.fuel_flowrate
        

    else:
        cDrag = 1.1
        # need to work more on this part, i have it as if the SRB burns up completely before external tank is used, but both are used simulatenously.
        # maybe i should have separate tank masses and use fuel rates individually before combining?
        # need to spend more time on this part
        dragSurfaceAr = columbia.ssme.shuttle_surfacearea + columbia.ssme.externaltank_surfacearea
        currentMass = columbia.ssme.fueltank_max + columbia.shuttle.mass

    Fthrust = rocEq.ThrustEquation(x1[1], timePassed)
    Fdrag = rocEq.dragForce(rho, v1, cDrag, dragSurfaceAr)
    Fgrav = currentMass * rocEq.gravity(x1[1])

    a1[1] = (Fthrust - Fdrag - Fgrav) / currentMass
    v1[1] += a1[1] * timeStep
    x1[1] += v1[1] * timeStep
"""
    












