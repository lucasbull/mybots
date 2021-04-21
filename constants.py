import numpy as np

simulationSize = 2000
pi = np.pi
gravity_x = 0
gravity_y = 0
gravity_z = -9.8
motorMaxForce = 30
timeStepGUI = 1/60
motorJointRange = 1

populationSize = 20
numberOfGenerations = 55

numSensorNeurons = 10
numHiddenNeurons = 5
numMotorNeuronsWithoutArms = 14
numMotorNeuronsWithArms = 18

robotScale = 4

allowableTargetAnglesWithArms = [(-1,0.5),(-0.05,0.05),(-0.05,0.05),(-0.25,0.25),(-0.05,0.05),	#Left foot
						(-1,0.5),(-0.05,0.05),(-0.05,0.05),(-0.25,0.25),(-0.05,0.05),	#Right foot
						(-0.1,1),(-1,0),								#Left leg
						(-0.1,1),(-1,0),								#Right leg
						(-1,1),(0,1),									#Left shoulder, elbow
						(-1,1),(0,1)]									#Right shoulder, elbow

allowableTargetAnglesWithoutArms = [(-1,0.5),(-0.05,0.05),(-0.05,0.05),(-0.25,0.25),(-0.05,0.05),	#Left foot
						(-1,0.5),(-0.05,0.05),(-0.05,0.05),(-0.25,0.25),(-0.05,0.05),	#Right foot
						(-0.1,1),(-1,0),								#Left leg
						(-0.1,1),(-1,0)]								#Right leg