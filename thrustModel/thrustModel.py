import numpy as np
import scipy as sp
import atmosphere as atm
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
timeStep = 0.01
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

altitude_log = []
velocity_log = []
time_log = []



while x1[1] <= 274000:  # 274 km = rough orbital insertion height
    altitude = x1[1]
    velocity = v1[1]
    pitchAngle = 0
    
    if timePassed % 5.67 == 0:
        pitchAngle += 1


    pressure = atm.getPressure(altitude)
    rho = rocEq.atmosDensity(altitude)
    Fthrust = rocEq.ThrustEquation(altitude, timePassed)

    if timePassed <= 123:
        srbMass -= columbia.srb.fuel_flowrate * timeStep
    if timePassed <= 510:
        eTankMass -= columbia.ssme.fuel_flowrate * timeStep

    currentMass = shuttleMass + max(eTankMass, 0) + max(srbMass, 0)

    if timePassed <= 123:
        cD = 0.55
        area = columbia.shuttle.surfacearea + columbia.srb.tanksurfacearea
    else:
        cD = 1.1
        area = columbia.shuttle.surfacearea + columbia.ssme.tanksurfacearea

    Fdrag = rocEq.dragForce(rho, v1, cD, area)
    Fgrav = currentMass * rocEq.gravity(altitude)

    a1[1] = (Fthrust - Fdrag - Fgrav) / currentMass
    v1[1] += a1[1] * timeStep
    x1[1] += v1[1] * timeStep

    timePassed += timeStep

    # Logging for plots
    altitude_log.append(x1[1])
    velocity_log.append(v1[1])
    time_log.append(timePassed)












