# this will handle the calcualtions for thrust
import shuttle
"""
There are three main engines used
- Space Shuttle Main Engines (SSMEs) - used after initial launch to propel through atmosphere and acheive orbit
- Solid Rocket Boosters (SRBs) - used for launch for most thrust, detach at 2min
- Orbital Maneuvering System (OMS) - used for fine-tuning once shuttle is outside of atmosphere and attempting to reach orbit

For now, we will ignore the orbital maneuvering system, focusing on the SSMEs and SRBs during launch and entering orbit
"""

ssme = shuttle.Engine(
    name = "RS-25",
    thrust_vacuum = 2279000, # kN
    thrust_sealevel = 1860000, # kN
    fuel_flowrate = 514.49, # kg/s
    burn_time = 510, # seconds (8.5 minutes) 
    isp_vacuum= 452.3, # seconds (4.436km/s)
    isp_sealevel= 366 # seconds (3.59km/s)  
)

srb = shuttle.Engine (
    name = "SRB BI-1",
    thrust_vacuum = 27000000, # kN
    thrust_sealevel = 24000000, # kN
    fuel_flowrate = 1831, # kg/s (both boosters burn fuel at this rate)
    burn_time = 123, # seconds (8.5 minutes) 
    isp_vacuum= 268, # seconds (4.436km/s)
    isp_sealevel= 242 # seconds (3.59km/s)  
)

# another thing to consider is that the SRBs detach after 2 minutes, so we will make a separate variable for SRB mass,
# whereas SSME mass will be included in the shuttles mass