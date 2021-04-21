import numpy
import pyrosim.pyrosim as pyrosim
import os
import random
import time
import constants as c

class SOLUTION:

	def __init__(self, myID, showArms):

		self.myID = myID
		if showArms:
			self.weightsFirst = numpy.random.rand(c.numSensorNeurons, c.numHiddenNeurons)
			self.weightsSecond = numpy.random.rand(c.numHiddenNeurons, c.numMotorNeuronsWithArms)
		else:
			self.weightsFirst = numpy.random.rand(c.numSensorNeurons, c.numHiddenNeurons)
			self.weightsSecond = numpy.random.rand(c.numHiddenNeurons, c.numMotorNeuronsWithoutArms)	
		self.weightsRecurrent = numpy.random.rand(c.numHiddenNeurons, c.numHiddenNeurons)		
		self.weightsFirst = self.weightsFirst * 2 - 1
		self.weightsSecond = self.weightsSecond * 2 - 1
		self.weightsRecurrent = self.weightsRecurrent * 2 - 1
		self.showArms = showArms

	def Start_Simulation(self, directOrGUI, needFitness):
		self.Create_World()
		self.Create_Body()
		self.Create_Brain()
		string = "start /B python simulate.py " + directOrGUI + " " + str(self.myID) + " " + str(needFitness) + " " + str(self.showArms)
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
		#Body/Torso
		pyrosim.Start_URDF("body" + str(self.myID) + ".urdf")
		pyrosim.Send_Cube(name="Torso", pos=[0,0,5.5/c.robotScale] ,
		size=[1/c.robotScale,2/c.robotScale,3/c.robotScale])

		#LEFT LEG
		pyrosim.Send_Joint( name = "Torso_UpperLeftLeg" , parent= "Torso" , 
		child = "UpperLeftLeg" , type = "revolute", position = "0 " + str(float(-0.5/c.robotScale)) + " " + str(float(4/c.robotScale)), jointAxis = "0 1 0")
		pyrosim.Send_Cube(name="UpperLeftLeg", pos=[0,0,-1/c.robotScale] ,
		size=[1/c.robotScale,1/c.robotScale,2/c.robotScale])
		pyrosim.Send_Joint( name = "UpperLeftLeg_LowerLeftLeg" , parent= "UpperLeftLeg" , 
		child = "LowerLeftLeg" , type = "revolute", position = "0 0 " + str(float(-2/c.robotScale)), jointAxis = "0 1 0")
		pyrosim.Send_Cube(name="LowerLeftLeg", pos=[0,0,-0.875/c.robotScale] ,
		size=[1/c.robotScale,1/c.robotScale,1.75/c.robotScale])

		#LEFT FOOT
		pyrosim.Send_Joint( name = "LowerLeftLeg_MiddleLeftFoot" , parent= "LowerLeftLeg" , 
		child = "MiddleLeftFoot" , type = "revolute", position = str(float(0.125/c.robotScale)) + " 0 " + str(float(-1.875/c.robotScale)), jointAxis = "0 1 0")
		pyrosim.Send_Cube(name="MiddleLeftFoot", pos=[-0.5/c.robotScale,0,0] ,
		size=[1.25/c.robotScale,0.5/c.robotScale,0.25/c.robotScale])
		pyrosim.Send_Joint( name = "MiddleLeftFoot_LeftLeftFoot" , parent= "MiddleLeftFoot" , 
		child = "LeftLeftFoot" , type = "revolute", position = str(float(-0.5/c.robotScale)) + " " + str(float(-0.25/c.robotScale)) + " 0", jointAxis = "1 0 0")
		pyrosim.Send_Cube(name="LeftLeftFoot", pos=[0,-0.125/c.robotScale,0] ,
		size=[1.25/c.robotScale,0.25/c.robotScale,0.25/c.robotScale])
		pyrosim.Send_Joint( name = "MiddleLeftFoot_RightLeftFoot" , parent= "MiddleLeftFoot" , 
		child = "RightLeftFoot" , type = "revolute", position = str(float(-0.5/c.robotScale)) + " " + str(float(0.25/c.robotScale)) + " 0", jointAxis = "1 0 0")
		pyrosim.Send_Cube(name="RightLeftFoot", pos=[0,0.125/c.robotScale,0] ,
		size=[1.25/c.robotScale,0.25/c.robotScale,0.25/c.robotScale])
		pyrosim.Send_Joint( name = "MiddleLeftFoot_LeftToes" , parent= "MiddleLeftFoot" , 
		child = "LeftToes" , type = "revolute", position = str(float(-1.125/c.robotScale)) + " 0 0", jointAxis = "0 1 0")
		pyrosim.Send_Cube(name="LeftToes", pos=[-0.125/c.robotScale,0,0] ,
		size=[0.25/c.robotScale,1/c.robotScale,0.25/c.robotScale])
		pyrosim.Send_Joint( name = "MiddleLeftFoot_LeftHeel" , parent= "MiddleLeftFoot" , 
		child = "LeftHeel" , type = "revolute", position = str(float(0.125/c.robotScale)) + " 0 0", jointAxis = "0 1 0")
		pyrosim.Send_Cube(name="LeftHeel", pos=[0.125/c.robotScale,0,0] ,
		size=[0.25/c.robotScale,1/c.robotScale,0.25/c.robotScale])

		#RIGHT LEG
		pyrosim.Send_Joint( name = "Torso_UpperRightLeg" , parent= "Torso" , 
		child = "UpperRightLeg" , type = "revolute", position = "0 " + str(float(0.5/c.robotScale)) + " " + str(float(4/c.robotScale)), jointAxis = "0 1 0")
		pyrosim.Send_Cube(name="UpperRightLeg", pos=[0,0,-1/c.robotScale] ,
		size=[1/c.robotScale,1/c.robotScale,2/c.robotScale])
		pyrosim.Send_Joint( name = "UpperRightLeg_LowerRightLeg" , parent= "UpperRightLeg" , 
		child = "LowerRightLeg" , type = "revolute", position = "0 0 " + str(float(-2/c.robotScale)), jointAxis = "0 1 0")
		pyrosim.Send_Cube(name="LowerRightLeg", pos=[0,0,-0.875/c.robotScale] ,
		size=[1/c.robotScale,1/c.robotScale,1.75/c.robotScale])

		#RIGHT FOOT
		pyrosim.Send_Joint( name = "LowerRightLeg_MiddleRightFoot" , parent= "LowerRightLeg" , 
		child = "MiddleRightFoot" , type = "revolute", position = str(float(0.125/c.robotScale)) + " 0 " + str(float(-1.875/c.robotScale)), jointAxis = "0 1 0")
		pyrosim.Send_Cube(name="MiddleRightFoot", pos=[-0.5/c.robotScale,0,0] ,
		size=[1.25/c.robotScale,0.5/c.robotScale,0.25/c.robotScale])
		pyrosim.Send_Joint( name = "MiddleRightFoot_LeftRightFoot" , parent= "MiddleRightFoot" , 
		child = "LeftRightFoot" , type = "revolute", position = str(float(-0.5/c.robotScale)) + " " + str(float(-0.25/c.robotScale)) + " 0", jointAxis = "1 0 0")
		pyrosim.Send_Cube(name="LeftRightFoot", pos=[0,-0.125/c.robotScale,0] ,
		size=[1.25/c.robotScale,0.25/c.robotScale,0.25/c.robotScale])
		pyrosim.Send_Joint( name = "MiddleRightFoot_RightRightFoot" , parent= "MiddleRightFoot" , 
		child = "RightRightFoot" , type = "revolute", position = str(float(-0.5/c.robotScale)) + " " + str(float(0.25/c.robotScale)) + " 0", jointAxis = "1 0 0")
		pyrosim.Send_Cube(name="RightRightFoot", pos=[0,0.125/c.robotScale,0] ,
		size=[1.25/c.robotScale,0.25/c.robotScale,0.25/c.robotScale])
		pyrosim.Send_Joint( name = "MiddleRightFoot_RightToes" , parent= "MiddleRightFoot" , 
		child = "RightToes" , type = "revolute", position = str(float(-1.125/c.robotScale)) + " 0 0", jointAxis = "0 1 0")
		pyrosim.Send_Cube(name="RightToes", pos=[-0.125/c.robotScale,0,0] ,
		size=[0.25/c.robotScale,1/c.robotScale,0.25/c.robotScale])
		pyrosim.Send_Joint( name = "MiddleRightFoot_RightHeel" , parent= "MiddleRightFoot" , 
		child = "RightHeel" , type = "revolute", position = str(float(0.125/c.robotScale)) + " 0 0", jointAxis = "0 1 0")
		pyrosim.Send_Cube(name="RightHeel", pos=[0.125/c.robotScale,0,0] ,
		size=[0.25/c.robotScale,1/c.robotScale,0.25/c.robotScale])

		if self.showArms:
			#LEFT ARM
			pyrosim.Send_Joint( name = "Torso_UpperLeftArm" , parent= "Torso" , 
			child = "UpperLeftArm" , type = "revolute", position = "0 " + str(float(-1/c.robotScale)) + " " + str(float(7/c.robotScale)), jointAxis = "0 1 0")
			pyrosim.Send_Cube(name="UpperLeftArm", pos=[0,-0.375/c.robotScale,-0.875/c.robotScale] ,
			size=[0.75/c.robotScale,0.75/c.robotScale,1.75/c.robotScale])
			pyrosim.Send_Joint( name = "UpperLeftArm_LowerLeftArm" , parent= "UpperLeftArm" , 
			child = "LowerLeftArm" , type = "revolute", position = "0 " + str(float(-0.375/c.robotScale)) + " " + str(float(-1.75/c.robotScale)), jointAxis = "0 1 0")
			pyrosim.Send_Cube(name="LowerLeftArm", pos=[0,0,-0.875/c.robotScale] ,
			size=[0.75/c.robotScale,0.75/c.robotScale,1.75/c.robotScale])

			#RIGHT ARM
			pyrosim.Send_Joint( name = "Torso_UpperRightArm" , parent= "Torso" , 
			child = "UpperRightArm" , type = "revolute", position = "0 " + str(float(1/c.robotScale)) + " " + str(float(7/c.robotScale)), jointAxis = "0 1 0")
			pyrosim.Send_Cube(name="UpperRightArm", pos=[0,0.375/c.robotScale,-0.875/c.robotScale] ,
			size=[0.75/c.robotScale,0.75/c.robotScale,1.75/c.robotScale])
			pyrosim.Send_Joint( name = "UpperRightArm_LowerRightArm" , parent= "UpperRightArm" , 
			child = "LowerRightArm" , type = "revolute", position = "0 " + str(float(0.375/c.robotScale)) + " " + str(float(-1.75/c.robotScale)), jointAxis = "0 1 0")
			pyrosim.Send_Cube(name="LowerRightArm", pos=[0,0,-0.875/c.robotScale] ,
			size=[0.75/c.robotScale,0.75/c.robotScale,1.75/c.robotScale])

			#NECK AND HEAD
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
		#Brain
		pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")

		#Sensor Neurons
		#Left foot
		pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "MiddleLeftFoot")
		pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "LeftLeftFoot")
		pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "RightLeftFoot")
		pyrosim.Send_Sensor_Neuron(name = 3 , linkName = "LeftToes")
		pyrosim.Send_Sensor_Neuron(name = 4 , linkName = "LeftHeel")

		#Right foot
		pyrosim.Send_Sensor_Neuron(name = 5 , linkName = "MiddleRightFoot")
		pyrosim.Send_Sensor_Neuron(name = 6 , linkName = "LeftRightFoot")
		pyrosim.Send_Sensor_Neuron(name = 7 , linkName = "RightRightFoot")
		pyrosim.Send_Sensor_Neuron(name = 8 , linkName = "RightToes")
		pyrosim.Send_Sensor_Neuron(name = 9 , linkName = "RightHeel")


		#Hidden Neurons
		pyrosim.Send_Hidden_Neuron(name = 10)
		pyrosim.Send_Hidden_Neuron(name = 11)
		pyrosim.Send_Hidden_Neuron(name = 12)
		pyrosim.Send_Hidden_Neuron(name = 13)
		pyrosim.Send_Hidden_Neuron(name = 14)
		pyrosim.Send_Hidden_Neuron(name = 15)
		pyrosim.Send_Hidden_Neuron(name = 16)
		pyrosim.Send_Hidden_Neuron(name = 17)
		pyrosim.Send_Hidden_Neuron(name = 18)
		pyrosim.Send_Hidden_Neuron(name = 19)

		#Motor Neurons
		#Left foot
		pyrosim.Send_Motor_Neuron( name = 20 , jointName = "LowerLeftLeg_MiddleLeftFoot")
		pyrosim.Send_Motor_Neuron( name = 21 , jointName = "MiddleLeftFoot_LeftLeftFoot")
		pyrosim.Send_Motor_Neuron( name = 22 , jointName = "MiddleLeftFoot_RightLeftFoot")
		pyrosim.Send_Motor_Neuron( name = 23 , jointName = "MiddleLeftFoot_LeftToes")
		pyrosim.Send_Motor_Neuron( name = 24 , jointName = "MiddleLeftFoot_LeftHeel")

		#Right foot
		pyrosim.Send_Motor_Neuron( name = 25 , jointName = "LowerRightLeg_MiddleRightFoot")
		pyrosim.Send_Motor_Neuron( name = 26 , jointName = "MiddleRightFoot_LeftRightFoot")
		pyrosim.Send_Motor_Neuron( name = 27 , jointName = "MiddleRightFoot_RightRightFoot")
		pyrosim.Send_Motor_Neuron( name = 28 , jointName = "MiddleRightFoot_RightToes")
		pyrosim.Send_Motor_Neuron( name = 29 , jointName = "MiddleRightFoot_RightHeel")

		#Left leg
		pyrosim.Send_Motor_Neuron( name = 30 , jointName = "Torso_UpperLeftLeg")
		pyrosim.Send_Motor_Neuron( name = 31 , jointName = "UpperLeftLeg_LowerLeftLeg")

		#Right leg
		pyrosim.Send_Motor_Neuron( name = 32 , jointName = "Torso_UpperRightLeg")
		pyrosim.Send_Motor_Neuron( name = 33 , jointName = "UpperRightLeg_LowerRightLeg")

		if self.showArms:
			#Left arm
			pyrosim.Send_Motor_Neuron( name = 34 , jointName = "Torso_UpperLeftArm")
			pyrosim.Send_Motor_Neuron( name = 35 , jointName = "UpperLeftArm_LowerLeftArm")

			#Right arm
			pyrosim.Send_Motor_Neuron( name = 36 , jointName = "Torso_UpperRightArm")
			pyrosim.Send_Motor_Neuron( name = 37 , jointName = "UpperRightArm_LowerRightArm")

			numMotorNeurons	= c.numMotorNeuronsWithArms

		else:
			numMotorNeurons = c.numMotorNeuronsWithoutArms

		for currentRow in range(c.numSensorNeurons):
			for currentColumn in range(c.numHiddenNeurons):

				pyrosim.Send_Synapse(sourceNeuronName = currentRow , targetNeuronName = currentColumn + c.numSensorNeurons , weight = 
				self.weightsFirst[currentRow][currentColumn])

		for currentRow in range(c.numHiddenNeurons):
			for currentColumn in range(numMotorNeurons):

				pyrosim.Send_Synapse(sourceNeuronName = currentRow + c.numSensorNeurons , targetNeuronName = currentColumn + c.numSensorNeurons + c.numHiddenNeurons , weight = 
				self.weightsSecond[currentRow][currentColumn])

		#Recurrent Connections
		for currentRow in range(c.numHiddenNeurons):
			for currentColumn in range(c.numHiddenNeurons):
				pyrosim.Send_Synapse(sourceNeuronName = currentColumn + c.numSensorNeurons , targetNeuronName = currentColumn + c.numSensorNeurons , weight = 
				self.weightsRecurrent[currentRow][currentColumn])

		pyrosim.End()

	def Mutate(self):

		if self.showArms:
			numMotorNeurons	= c.numMotorNeuronsWithArms

		else:
			numMotorNeurons = c.numMotorNeuronsWithoutArms

		numMutations = random.randint(1,6)

		for mutation in range(numMutations):
			selectArray = random.randint(0,3)
			if selectArray == 0:
				randomRow = random.randint(0, c.numSensorNeurons - 1)
				randomColumn = random.randint(0, c.numHiddenNeurons - 1)
				self.weightsFirst[randomRow][randomColumn] = random.random() * 2 - 1
			if selectArray == 1:
				randomRow = random.randint(0, c.numHiddenNeurons - 1)
				randomColumn = random.randint(0, numMotorNeurons - 1)
				self.weightsSecond[randomRow][randomColumn] = random.random() * 2 - 1
			else:
				randomRow = random.randint(0, c.numHiddenNeurons - 1)
				randomColumn = random.randint(0, c.numHiddenNeurons - 1)
				self.weightsRecurrent[randomRow][randomColumn] = random.random() * 2 - 1



	def Set_ID(self, myID):
		self.myID = myID