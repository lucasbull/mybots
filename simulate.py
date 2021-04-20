from simulation import SIMULATION
import sys

directOrGUI = sys.argv[1]
solutionID = sys.argv[2]
needFitness = sys.argv[3]
showArms = bool(sys.argv[4])

simulation = SIMULATION(directOrGUI, solutionID, showArms)

simulation.Run()

if needFitness == "True":
	simulation.Get_Fitness()