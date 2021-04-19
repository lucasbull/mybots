import numpy as np

simulationSize = 2000
pi = np.pi
gravity_x = 0
gravity_y = 0
gravity_z = -9.8
motorMaxForce = 50
timeStepGUI = 1/60
motorJointRange = 1

populationSize = 15
numberOfGenerations = 40

numSensorNeurons = 10
numMotorNeurons = 14

robotScale = 4

allowableTargetAngles = {"10":(-1,0.5),"11":(-0.05,0.05),"12":(-0.05,0.05),"13":(-0.25,0.25),"14":(-0.05,0.05),	#Left foot
						"15":(-1,0.5),"16":(-0.05,0.05),"17":(-0.05,0.05),"18":(-0.25,0.25),"19":(-0.05,0.05),	#Right foot
						"20":(-0.1,1),"21":(-1,0),								#Left leg
						"22":(-0.1,1),"23":(-1,0)}								#Right leg