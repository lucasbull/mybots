import pybullet as p
import pyrosim.pyrosim as pyrosim
from sensor import SENSOR
from motor import MOTOR
from pyrosim.neuralNetwork import NEURAL_NETWORK
import os
import constants as c
import numpy
import math

class ROBOT:

	def __init__(self, solutionID, showArms):

		self.showArms = showArms
		self.solutionID = solutionID
		self.fitnessList = []
		self.robot = p.loadURDF("body" + self.solutionID + ".urdf")
		pyrosim.Prepare_To_Simulate("body" + self.solutionID + ".urdf")
		self.Prepare_To_Sense()
		self.Prepare_To_Act()
		self.nn = NEURAL_NETWORK("brain" + self.solutionID + ".nndf")
		os.system("del brain" + solutionID + ".nndf")
		os.system("del body" + solutionID + ".urdf")


	def Prepare_To_Sense(self):

		self.sensors = {

		}

		for linkName in pyrosim.linkNamesToIndices:
			self.sensors[linkName] = SENSOR(linkName)

	def Sense(self, time):
		for sensorName in self.sensors:
			self.sensors[sensorName].Get_Value(time)

	def Prepare_To_Act(self):

		self.motors = {

		}

		for jointName in pyrosim.jointNamesToIndices:
			self.motors[jointName] = MOTOR(jointName)

	def Act(self, time):

		if self.showArms:
			allowableTargetAngles = c.allowableTargetAnglesWithArms

		else:
			allowableTargetAngles = c.allowableTargetAnglesWithoutArms

		for neuronName in self.nn.Get_Neuron_Names():
			if self.nn.Is_Motor_Neuron(neuronName):

				jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
				neuronValue = self.nn.Get_Value_Of(neuronName)
				motorNeuronNumber = int(neuronName) - (c.numSensorNeurons + c.numHiddenNeurons)
				#Allowable interval (a, b)
				a = allowableTargetAngles[motorNeuronNumber][0]
				b = allowableTargetAngles[motorNeuronNumber][1]
				desiredAngle = (b-a)*(numpy.arctan(4*neuronValue)/c.pi)+(b+a)/2
				self.motors[jointName].Set_Value(self.robot, desiredAngle)

	def Think(self, time):
		self.nn.Update()
		
		#Get the link states
		torsoState = p.getBasePositionAndOrientation(self.robot)
		leftFootState = p.getLinkState(self.robot, 2)
		rightFootState = p.getLinkState(self.robot, 9)

		#Caculate distance (average of torso and both feet)
		distance = max(leftFootState[0][0],rightFootState[0][0],torsoState[0][0])

		#Get all quaternion values
		#Torso/hip		
		qxHip = torsoState[1][0]
		qyHip = torsoState[1][1]
		qzHip = torsoState[1][2]
		qwHip = torsoState[1][3]

		#Left foot
		qxLFoot = leftFootState[1][0]
		qyLFoot = leftFootState[1][1]
		qzLFoot = leftFootState[1][2]
		qwLFoot = leftFootState[1][3]	
		
		#Right foot
		qxRFoot = rightFootState[1][0]
		qyRFoot = rightFootState[1][1]
		qzRFoot = rightFootState[1][2]
		qwRFoot = rightFootState[1][3]	

		#Translate to rotations about the axes
		hipRotationX = math.atan2(2*qxHip*qwHip-2*qyHip*qzHip, 1 - 2*qxHip**2 - 2*qzHip**2)				#Torso Falling Sideways
		hipRotationY = math.atan2(2*qyHip*qwHip-2*qxHip*qzHip, 1 - 2*qyHip**2 - 2*qzHip**2)					#Torso Falling Forward
		hipRotationZ = math.asin(2*qxHip*qyHip + 2*qzHip*qwHip)												#Torso Turning

		leftFootRotationZ = math.asin(2*qxLFoot*qyLFoot + 2*qzLFoot*qwLFoot)										#Left Foot Turning

		rightFootRotationZ = math.asin(2*qxRFoot*qyRFoot + 2*qzRFoot*qwRFoot)										#Right Foot Turning

		#Get full fitness value and add to the list
		fitness = distance * (1/(1+abs(hipRotationX))) * (1/(1+abs(hipRotationY))) * (1/(1+abs(hipRotationZ))) * (1/(1+abs(leftFootRotationZ))) * (1/(1+abs(rightFootRotationZ)))

		self.fitnessList.append(fitness)

	def Get_Fitness(self):
		
		finalFitness = numpy.mean(self.fitnessList)

		tempFitness = open("tmp" + self.solutionID + ".txt", "w")
		tempFitness.write(str(finalFitness))
		tempFitness.close()
		os.system("rename tmp" + self.solutionID + ".txt" " fitness" + self.solutionID + ".txt")