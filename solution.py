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
		pyrosim.Send_Cube(name="Torso", pos=[0,0,5.5/c.robotScale] ,
		size=[1/c.robotScale,2/c.robotScale,3/c.robotScale])
		pyrosim.Send_Joint( name = "Torso_UpperLeftLeg" , parent= "Torso" , 
		child = "UpperLeftLeg" , type = "revolute", position = "0 " + str(float(-0.5/c.robotScale)) + " " + str(float(4/c.robotScale)), jointAxis = "0 1 0")
		pyrosim.Send_Cube(name="UpperLeftLeg", pos=[0,0,-1/c.robotScale] ,
		size=[1/c.robotScale,1/c.robotScale,2/c.robotScale])
		pyrosim.Send_Joint( name = "Torso_UpperRightLeg" , parent= "Torso" , 
		child = "UpperRightLeg" , type = "revolute", position = "0 " + str(float(0.5/c.robotScale)) + " " + str(float(4/c.robotScale)), jointAxis = "0 1 0")
		pyrosim.Send_Cube(name="UpperRightLeg", pos=[0,0,-1/c.robotScale] ,
		size=[1/c.robotScale,1/c.robotScale,2/c.robotScale])
		pyrosim.Send_Joint( name = "UpperLeftLeg_LowerLeftLeg" , parent= "UpperLeftLeg" , 
		child = "LowerLeftLeg" , type = "revolute", position = "0 0 " + str(float(-2/c.robotScale)), jointAxis = "0 1 0")
		pyrosim.Send_Cube(name="LowerLeftLeg", pos=[0,0,-1/c.robotScale] ,
		size=[1/c.robotScale,1/c.robotScale,2/c.robotScale])
		pyrosim.Send_Joint( name = "UpperRightLeg_LowerRightLeg" , parent= "UpperRightLeg" , 
		child = "LowerRightLeg" , type = "revolute", position = "0 0 " + str(float(-2/c.robotScale)), jointAxis = "0 1 0")
		pyrosim.Send_Cube(name="LowerRightLeg", pos=[0,0,-1/c.robotScale] ,
		size=[1/c.robotScale,1/c.robotScale,2/c.robotScale])
		pyrosim.Send_Joint( name = "LowerLeftLeg_LeftFoot" , parent= "LowerLeftLeg" , 
		child = "LeftFoot" , type = "revolute", position = "0 0 " + str(float(-2/c.robotScale)), jointAxis = "0 1 0")
		pyrosim.Send_Cube(name="LeftFoot", pos=[-0.5/c.robotScale,0,0.125/c.robotScale] ,
		size=[2/c.robotScale,1/c.robotScale,0.25/c.robotScale])
		pyrosim.Send_Joint( name = "LowerRightLeg_RightFoot" , parent= "LowerRightLeg" , 
		child = "RightFoot" , type = "revolute", position = "0 0 " + str(float(-2/c.robotScale)), jointAxis = "0 1 0")
		pyrosim.Send_Cube(name="RightFoot", pos=[-0.5/c.robotScale,0,0.125/c.robotScale] ,
		size=[2/c.robotScale,1/c.robotScale,0.25/c.robotScale])
		pyrosim.Send_Joint( name = "Torso_UpperLeftArm" , parent= "Torso" , 
		child = "UpperLeftArm" , type = "revolute", position = "0 " + str(float(-1/c.robotScale)) + " " + str(float(7/c.robotScale)), jointAxis = "0 1 0")
		pyrosim.Send_Cube(name="UpperLeftArm", pos=[0,-0.375/c.robotScale,-0.875/c.robotScale] ,
		size=[0.75/c.robotScale,0.75/c.robotScale,1.75/c.robotScale])
		pyrosim.Send_Joint( name = "UpperLeftArm_LowerLeftArm" , parent= "UpperLeftArm" , 
		child = "LowerLeftArm" , type = "revolute", position = "0 " + str(float(-0.375/c.robotScale)) + " " + str(float(-1.75/c.robotScale)), jointAxis = "0 1 0")
		pyrosim.Send_Cube(name="LowerLeftArm", pos=[0,0,-0.875/c.robotScale] ,
		size=[0.75/c.robotScale,0.75/c.robotScale,1.75/c.robotScale])
		pyrosim.Send_Joint( name = "Torso_UpperRightArm" , parent= "Torso" , 
		child = "UpperRightArm" , type = "revolute", position = "0 " + str(float(1/c.robotScale)) + " " + str(float(7/c.robotScale)), jointAxis = "0 1 0")
		pyrosim.Send_Cube(name="UpperRightArm", pos=[0,0.375/c.robotScale,-0.875/c.robotScale] ,
		size=[0.75/c.robotScale,0.75/c.robotScale,1.75/c.robotScale])
		pyrosim.Send_Joint( name = "UpperRightArm_LowerRightArm" , parent= "UpperRightArm" , 
		child = "LowerRightArm" , type = "revolute", position = "0 " + str(float(0.375/c.robotScale)) + " " + str(float(-1.75/c.robotScale)), jointAxis = "0 1 0")
		pyrosim.Send_Cube(name="LowerRightArm", pos=[0,0,-0.875/c.robotScale] ,
		size=[0.75/c.robotScale,0.75/c.robotScale,1.75/c.robotScale])
		pyrosim.Send_Joint( name = "Torso_Neck" , parent= "Torso" , 
		child = "Neck" , type = "revolute", position = "0 0 " + str(float(7/c.robotScale)), jointAxis = "0 1 0")
		pyrosim.Send_Cube(name="Neck", pos=[0,0,0] ,
		size=[0.75/c.robotScale,0.75/c.robotScale,1/c.robotScale])
		pyrosim.Send_Joint( name = "Neck_Head" , parent= "Neck" , 
		child = "Head" , type = "revolute", position = "0 0 " + str(float(1/c.robotScale)), jointAxis = "0 1 0")
		pyrosim.Send_Cube(name="Head", pos=[0,0,0] ,
		size=[1/c.robotScale,1/c.robotScale,1.5/c.robotScale])
		pyrosim.End()


	def Create_Brain(self):
		pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")
		pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "LeftFoot")
		pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "RightFoot")
		pyrosim.Send_Motor_Neuron( name = 2 , jointName = "Torso_UpperLeftLeg")
		pyrosim.Send_Motor_Neuron( name = 3 , jointName = "Torso_UpperRightLeg")
		pyrosim.Send_Motor_Neuron( name = 4 , jointName = "UpperLeftLeg_LowerLeftLeg")
		pyrosim.Send_Motor_Neuron( name = 5 , jointName = "UpperRightLeg_LowerRightLeg")
		pyrosim.Send_Motor_Neuron( name = 6 , jointName = "LowerLeftLeg_LeftFoot")
		pyrosim.Send_Motor_Neuron( name = 7 , jointName = "LowerRightLeg_RightFoot")
		pyrosim.Send_Motor_Neuron( name = 8 , jointName = "Torso_UpperLeftArm")
		pyrosim.Send_Motor_Neuron( name = 9 , jointName = "UpperLeftArm_LowerLeftArm")
		pyrosim.Send_Motor_Neuron( name = 10 , jointName = "Torso_UpperRightArm")
		pyrosim.Send_Motor_Neuron( name = 11 , jointName = "UpperRightArm_LowerRightArm")




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