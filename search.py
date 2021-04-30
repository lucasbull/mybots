import os
from parallelHillClimber import PARALLEL_HILL_CLIMBER

showArms = True

phc = PARALLEL_HILL_CLIMBER(showArms)
phc.Evolve()
phc.Show_Best()