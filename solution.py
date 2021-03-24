import numpy
import pyrosim.pyrosim as pyrosim
import os
import random

class SOLUTION:

	def __init__(self):

		self.weights = numpy.random.rand(3, 2)
		self.weights = self.weights * 2 - 1

	def Evaluate(self, string):

		self.Create_World()
		self.Create_Body()
		self.Create_Brain()
		os.system("python simulate.py " + string)
		fitness = open("fitness.txt", "r")
		self.fitness = float(fitness.read())
		fitness.close()

	def Create_World(self):
		pyrosim.Start_SDF("world.sdf")
		pyrosim.Send_Cube(name="Box", pos=[-3,3,0.5] ,
		size=[1,1,1])
		pyrosim.End()

	def Create_Body(self):
		pyrosim.Start_URDF("body.urdf")
		pyrosim.Send_Cube(name="Torso", pos=[1.5,0,1.5] ,
		size=[1,1,1])
		pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , 
		child = "BackLeg" , type = "revolute", position = "1 0 1")
		pyrosim.Send_Cube(name="BackLeg", pos=[-0.5,0,-0.5] ,
		size=[1,1,1])
		pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , 
		child = "FrontLeg" , type = "revolute", position = "2 0 1")
		pyrosim.Send_Cube(name="FrontLeg", pos=[0.5,0,-0.5] ,
		size=[1,1,1])
		pyrosim.End()


	def Create_Brain(self):
		pyrosim.Start_NeuralNetwork("brain.nndf")
		pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
		pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")
		pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg")
		pyrosim.Send_Motor_Neuron( name = 3 , jointName = "Torso_BackLeg")
		pyrosim.Send_Motor_Neuron( name = 4 , jointName = "Torso_FrontLeg")

		for currentColumn in range(3):


			for currentRow in range(2):

				pyrosim.Send_Synapse(sourceNeuronName = currentColumn , targetNeuronName = currentRow + 3 , weight = 
				self.weights[currentColumn][currentRow])

		pyrosim.End()

	def Mutate(self):

		randomColumn = random.randint(0, 2)
		randomRow = random.randint(0, 1)
		self.weights[randomColumn][randomRow] = random.random() * 2 - 1