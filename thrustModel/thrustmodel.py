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


