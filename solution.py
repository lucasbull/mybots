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

		# #LEFT ARM
		# pyrosim.Send_Joint( name = "Torso_UpperLeftArm" , parent= "Torso" , 
		# child = "UpperLeftArm" , type = "revolute", position = "0 " + str(float(-1/c.robotScale)) + " " + str(float(7/c.robotScale)), jointAxis = "0 1 0")
		# pyrosim.Send_Cube(name="UpperLeftArm", pos=[0,-0.375/c.robotScale,-0.875/c.robotScale] ,
		# size=[0.75/c.robotScale,0.75/c.robotScale,1.75/c.robotScale])
		# pyrosim.Send_Joint( name = "UpperLeftArm_LowerLeftArm" , parent= "UpperLeftArm" , 
		# child = "LowerLeftArm" , type = "revolute", position = "0 " + str(float(-0.375/c.robotScale)) + " " + str(float(-1.75/c.robotScale)), jointAxis = "0 1 0")
		# pyrosim.Send_Cube(name="LowerLeftArm", pos=[0,0,-0.875/c.robotScale] ,
		# size=[0.75/c.robotScale,0.75/c.robotScale,1.75/c.robotScale])

		# #RIGHT ARM
		# pyrosim.Send_Joint( name = "Torso_UpperRightArm" , parent= "Torso" , 
		# child = "UpperRightArm" , type = "revolute", position = "0 " + str(float(1/c.robotScale)) + " " + str(float(7/c.robotScale)), jointAxis = "0 1 0")
		# pyrosim.Send_Cube(name="UpperRightArm", pos=[0,0.375/c.robotScale,-0.875/c.robotScale] ,
		# size=[0.75/c.robotScale,0.75/c.robotScale,1.75/c.robotScale])
		# pyrosim.Send_Joint( name = "UpperRightArm_LowerRightArm" , parent= "UpperRightArm" , 
		# child = "LowerRightArm" , type = "revolute", position = "0 " + str(float(0.375/c.robotScale)) + " " + str(float(-1.75/c.robotScale)), jointAxis = "0 1 0")
		# pyrosim.Send_Cube(name="LowerRightArm", pos=[0,0,-0.875/c.robotScale] ,
		# size=[0.75/c.robotScale,0.75/c.robotScale,1.75/c.robotScale])

		# #NECK AND HEAD
		# pyrosim.Send_Joint( name = "Torso_Neck" , parent= "Torso" , 
		# child = "Neck" , type = "revolute", position = "0 0 " + str(float(7/c.robotScale)), jointAxis = "0 1 0")
		# pyrosim.Send_Cube(name="Neck", pos=[0,0,0] ,
		# size=[0.75/c.robotScale,0.75/c.robotScale,1/c.robotScale])
		# pyrosim.Send_Joint( name = "Neck_Head" , parent= "Neck" , 
		# child = "Head" , type = "revolute", position = "0 0 " + str(float(1/c.robotScale)), jointAxis = "0 1 0")
		# pyrosim.Send_Cube(name="Head", pos=[0,0,0] ,
		# size=[1/c.robotScale,1/c.robotScale,1.5/c.robotScale])
		
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


		#Motor Neurons
		#Left foot
		pyrosim.Send_Motor_Neuron( name = 10 , jointName = "LowerLeftLeg_MiddleLeftFoot")
		pyrosim.Send_Motor_Neuron( name = 11 , jointName = "MiddleLeftFoot_LeftLeftFoot")
		pyrosim.Send_Motor_Neuron( name = 12 , jointName = "MiddleLeftFoot_RightLeftFoot")
		pyrosim.Send_Motor_Neuron( name = 13 , jointName = "MiddleLeftFoot_LeftToes")
		pyrosim.Send_Motor_Neuron( name = 14 , jointName = "MiddleLeftFoot_LeftHeel")

		#Right foot
		pyrosim.Send_Motor_Neuron( name = 15 , jointName = "LowerRightLeg_MiddleRightFoot")
		pyrosim.Send_Motor_Neuron( name = 16 , jointName = "MiddleRightFoot_LeftRightFoot")
		pyrosim.Send_Motor_Neuron( name = 17 , jointName = "MiddleRightFoot_RightRightFoot")
		pyrosim.Send_Motor_Neuron( name = 18 , jointName = "MiddleRightFoot_RightToes")
		pyrosim.Send_Motor_Neuron( name = 19 , jointName = "MiddleRightFoot_RightHeel")

		#Left leg
		pyrosim.Send_Motor_Neuron( name = 20 , jointName = "Torso_UpperLeftLeg")
		pyrosim.Send_Motor_Neuron( name = 21 , jointName = "UpperLeftLeg_LowerLeftLeg")

		#Right leg
		pyrosim.Send_Motor_Neuron( name = 22 , jointName = "Torso_UpperRightLeg")
		pyrosim.Send_Motor_Neuron( name = 23 , jointName = "UpperRightLeg_LowerRightLeg")

		#Left arm
		#pyrosim.Send_Motor_Neuron( name = 24 , jointName = "Torso_UpperLeftArm")
		#pyrosim.Send_Motor_Neuron( name = 25 , jointName = "UpperLeftArm_LowerLeftArm")

		#Right arm
		#pyrosim.Send_Motor_Neuron( name = 26 , jointName = "Torso_UpperRightArm")
		#pyrosim.Send_Motor_Neuron( name = 27 , jointName = "UpperRightArm_LowerRightArm")


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