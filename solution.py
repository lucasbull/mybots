import numpy
import pyrosim.pyrosim as pyrosim
import os
import random
import time
import constants as c

class SOLUTION:

	def __init__(self, myID):

		self.myID = myID
		self.weights = numpy.random.rand(c.numSensorNeurons, c.numMotorNeurons)
		self.weights = self.weights * 2 - 1

	def Start_Simulation(self, directOrGUI, needFitness):
		self.Create_World()
		self.Create_Body()
		self.Create_Brain()
		string = "start /B python simulate.py " + directOrGUI + " " + str(self.myID) + " " + str(needFitness)
		os.system(string)

	def Wait_For_Simulation_To_End(self):
		fitnessFileName = "fitness" + str(self.myID) + ".txt"
		while not os.path.exists(fitnessFileName):
			time.sleep(0.01)
		time.sleep(0.01)
		fitness = open(fitnessFileName, "r")
		self.fitness = float(fitness.read())
		fitness.close()
		os.system("del " + fitnessFileName)

	def Create_World(self):
		pyrosim.Start_SDF("world" + str(self.myID) + ".sdf")
		#pyrosim.Send_Cube(name="Box", pos=[-3,3,0.5] ,
		#size=[1,1,1])
		pyrosim.End()

	def Create_Body(self):
		pyrosim.Start_URDF("body" + str(self.myID) + ".urdf")
		pyrosim.Send_Cube(name="Torso", pos=[0,0,5.5] ,
		size=[1,2,3])
		pyrosim.Send_Joint( name = "Torso_UpperLeftLeg" , parent= "Torso" , 
		child = "UpperLeftLeg" , type = "revolute", position = "0 -0.5 4", jointAxis = "0 1 0")
		pyrosim.Send_Cube(name="UpperLeftLeg", pos=[0,0,-1] ,
		size=[1,1,2])
		pyrosim.Send_Joint( name = "Torso_UpperRightLeg" , parent= "Torso" , 
		child = "UpperRightLeg" , type = "revolute", position = "0 0.5 4", jointAxis = "0 1 0")
		pyrosim.Send_Cube(name="UpperRightLeg", pos=[0,0,-1] ,
		size=[1,1,2])
		pyrosim.Send_Joint( name = "UpperLeftLeg_LowerLeftLeg" , parent= "UpperLeftLeg" , 
		child = "LowerLeftLeg" , type = "revolute", position = "0 0 -2", jointAxis = "0 1 0")
		pyrosim.Send_Cube(name="LowerLeftLeg", pos=[0,0,-1] ,
		size=[1,1,2])
		pyrosim.Send_Joint( name = "UpperRightLeg_LowerRightLeg" , parent= "UpperRightLeg" , 
		child = "LowerRightLeg" , type = "revolute", position = "0 0 -2", jointAxis = "0 1 0")
		pyrosim.Send_Cube(name="LowerRightLeg", pos=[0,0,-1] ,
		size=[1,1,2])
		pyrosim.Send_Joint( name = "LowerLeftLeg_LeftFoot" , parent= "LowerLeftLeg" , 
		child = "LeftFoot" , type = "revolute", position = "0 0 -2", jointAxis = "0 1 0")
		pyrosim.Send_Cube(name="LeftFoot", pos=[-0.5,0,0.125] ,
		size=[2,1,0.25])
		pyrosim.Send_Joint( name = "LowerRightLeg_RightFoot" , parent= "LowerRightLeg" , 
		child = "RightFoot" , type = "revolute", position = "0 0 -2", jointAxis = "0 1 0")
		pyrosim.Send_Cube(name="RightFoot", pos=[-0.5,0,0.125] ,
		size=[2,1,0.25])
		pyrosim.Send_Joint( name = "Torso_UpperLeftArm" , parent= "Torso" , 
		child = "UpperLeftArm" , type = "revolute", position = "0 -1 7", jointAxis = "0 1 0")
		pyrosim.Send_Cube(name="UpperLeftArm", pos=[0,-0.5,-0.875] ,
		size=[1,1,1.75])
		#pyrosim.Send_Joint( name = "UpperRightLeg_LowerRightLeg" , parent= "UpperRightLeg" , 
		#child = "LowerRightLeg" , type = "revolute", position = "0 0 -2", jointAxis = "0 1 0")
		#pyrosim.Send_Cube(name="LowerRightLeg", pos=[0,0,-1] ,
		#size=[1,1,2])
		#pyrosim.Send_Joint( name = "FrontLeg_LowerFrontLeg" , parent= "FrontLeg" , 
		#child = "LowerFrontLeg" , type = "revolute", position = "0 1 0", jointAxis = "1 0 0")
		#pyrosim.Send_Cube(name="LowerFrontLeg", pos=[0,0,-0.5] ,
		#size=[0.2,0.2,1])
		#pyrosim.Send_Joint( name = "BackLeg_LowerBackLeg" , parent= "BackLeg" , 
		#child = "LowerBackLeg" , type = "revolute", position = "0 -1 0", jointAxis = "1 0 0")
		#pyrosim.Send_Cube(name="LowerBackLeg", pos=[0,0,-0.5] ,
		#size=[0.2,0.2,1])
		#pyrosim.Send_Joint( name = "LeftLeg_LowerLeftLeg" , parent= "LeftLeg" , 
		#child = "LowerLeftLeg" , type = "revolute", position = "-1 0 0", jointAxis = "0 1 0")
		#pyrosim.Send_Cube(name="LowerLeftLeg", pos=[0,0,-0.5] ,
		#size=[0.2,0.2,1])
		#pyrosim.Send_Joint( name = "RightLeg_LowerRightLeg" , parent= "RightLeg" , 
		#child = "LowerRightLeg" , type = "revolute", position = "1 0 0", jointAxis = "0 1 0")
		#pyrosim.Send_Cube(name="LowerRightLeg", pos=[0,0,-0.5] ,
		#size=[0.2,0.2,1])
		pyrosim.End()


	def Create_Brain(self):
		pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")
		pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "LowerBackLeg")
		pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "LowerFrontLeg")
		pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "LowerLeftLeg")
		pyrosim.Send_Sensor_Neuron(name = 3 , linkName = "LowerRightLeg")
		pyrosim.Send_Motor_Neuron( name = 4 , jointName = "Torso_BackLeg")
		pyrosim.Send_Motor_Neuron( name = 5 , jointName = "Torso_FrontLeg")
		pyrosim.Send_Motor_Neuron( name = 6 , jointName = "Torso_LeftLeg")
		pyrosim.Send_Motor_Neuron( name = 7 , jointName = "Torso_RightLeg")
		pyrosim.Send_Motor_Neuron( name = 8 , jointName = "FrontLeg_LowerFrontLeg")
		pyrosim.Send_Motor_Neuron( name = 9 , jointName = "BackLeg_LowerBackLeg")
		pyrosim.Send_Motor_Neuron( name = 10 , jointName = "LeftLeg_LowerLeftLeg")
		pyrosim.Send_Motor_Neuron( name = 11 , jointName = "RightLeg_LowerRightLeg")




		for currentRow in range(c.numSensorNeurons):
			for currentColumn in range(c.numMotorNeurons):

				pyrosim.Send_Synapse(sourceNeuronName = currentRow , targetNeuronName = currentColumn + c.numSensorNeurons , weight = 
				self.weights[currentRow][currentColumn])
		pyrosim.End()

	def Mutate(self):

		randomColumn = random.randint(0, c.numSensorNeurons - 1)
		randomRow = random.randint(0, c.numMotorNeurons - 1)
		self.weights[randomColumn][randomRow] = random.random() * 2 - 1

	def Set_ID(self, myID):
		self.myID = myID