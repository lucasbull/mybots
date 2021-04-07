import numpy
import pyrosim.pyrosim as pyrosim
import os
import random
import time
import constants as c

class SOLUTION:

	def __init__(self, myID):

		self.myID = myID
		self.weights = numpy.random.rand(3, 2)
		self.weights = self.weights * 2 - 1

	def Start_Simulation(self, directOrGUI):
		self.Create_World()
		self.Create_Body()
		self.Create_Brain()
		os.system("start /B python simulate.py " + directOrGUI + " " + str(self.myID))

	def Wait_For_Simulation_To_End(self):
		fitnessFileName = "fitness" + str(self.myID) + ".txt"
		while not os.path.exists(fitnessFileName):
			time.sleep(0.01)
		fitness = open(fitnessFileName, "r")
		self.fitness = float(fitness.read())
		fitness.close()
		os.system("del " + fitnessFileName)

	def Create_World(self):
		pyrosim.Start_SDF("world.sdf")
		pyrosim.Send_Cube(name="Box", pos=[-3,3,0.5] ,
		size=[1,1,1])
		pyrosim.End()

	def Create_Body(self):
		pyrosim.Start_URDF("body.urdf")
		pyrosim.Send_Cube(name="Torso", pos=[0,0,1] ,
		size=[1,1,1])
		pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , 
		child = "BackLeg" , type = "revolute", position = "0 -0.5 1", jointAxis = "[0 1 0]")
		pyrosim.Send_Cube(name="BackLeg", pos=[0,-0.5,0] ,
		size=[0.2,1,0.2])
		pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , 
		child = "FrontLeg" , type = "revolute", position = "0 0.5 1", jointAxis = "[-1 0 0]")
		pyrosim.Send_Cube(name="FrontLeg", pos=[0,0.5,0] ,
		size=[0.2,1,0.2])
		pyrosim.End()


	def Create_Brain(self):
		pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")
		pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
		pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")
		pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg")
		pyrosim.Send_Motor_Neuron( name = 3 , jointName = "Torso_BackLeg")
		pyrosim.Send_Motor_Neuron( name = 4 , jointName = "Torso_FrontLeg")

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