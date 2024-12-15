# this will handle the calcualtions for thrust
import shuttle
"""
There are three main engines used
- Space Shuttle Main Engines (SSMEs) - used after initial launch to propel through atmosphere and acheive orbit
- Solid Rocket Boosters (SRBs) - used for launch for most thrust, detach at 2min
- Orbital Maneuvering System (OMS) - used for fine-tuning once shuttle is outside of atmosphere and attempting to reach orbit

For now, we will ignore the orbital maneuvering system, focusing on the SSMEs and SRBs during launch and entering orbit
"""

"""
Timeline for Shuttle
1) -6.6 to 0s, the SSMEs ignite for pre-lift checks
2) 0 to 120s (2min), both the SSME and SRB launch together from pad
3) at 120s, the SRBs detach and fall into ocean
4) 120s to 510s, the shuttle is has reached far enough to enter orbit, external tank drops
"""

"""
Important Equations to use:
1) Thrust Equation:    F = mdot* ve + ae(pe - pa)
    F = Thrust Force
    mdot = Mass flow rate of propellant
    ve = exhaust velocity
    ae = exit area of thruster
    pe = pressure at nozzle exit
    pa = atmospheric pressure

2) Mass Flow Rate: mdot = rho*a*ve
    rho = propellant density
    a = throat area of nozzle (spot most narrow cross section)
    ve = exhaust velocity

3) Tsiolkovsky Rocket Equation: deltaV = ve ln (mi/mf)
    ve = exhaust velocity
    mi = initial mass of rocket + propellant
    mf = mass after propellant is burned

4) Drag Force: Fdrag = (1/2)*rho*(v^2)*Cd*A
    rho = atmospheric density
    v = velocity of rocket
    Cd = drag coefficient
    A = cross sectional area (part that is facing outward from the center of body and perpendicular to drag/thrust direction)
    p.s. we gonna have to figure out how to adjust for the heads of the shuttle and thrusters, since they are rounded.

5) Specific Impulse: Isp = Fthrust/(mdot*g)
    Isp = Specific Impulse
    Fthrust = thrust force
    mdot = mass flowrate
    g = grav accel (9.81)

6) Exhaust Velocity Relation: ve = Isp * g
ve = exhaust velocity
Isp - specific impulse
g = grav accel
"""

