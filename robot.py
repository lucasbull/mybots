import pybullet as p
import pyrosim.pyrosim as pyrosim
from sensor import SENSOR
from motor import MOTOR
from pyrosim.neuralNetwork import NEURAL_NETWORK
import os
import constants as c
import numpy

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
				#Allowable interval (a, b)
				a = allowableTargetAngles[neuronName][0]
				b = allowableTargetAngles[neuronName][1]
				desiredAngle = (b-a)*(numpy.arctan(4*neuronValue)/c.pi)+(b+a)/2
				self.motors[jointName].Set_Value(self.robot, desiredAngle)

	def Think(self, time):
		self.nn.Update()
		torsoState = p.getBasePositionAndOrientation(self.robot)
		leftFootState = p.getLinkState(self.robot, 2)
		rightFootState = p.getLinkState(self.robot, 9)
		distance = (leftFootState[0][0]+rightFootState[0][0]+torsoState[0][0])/3
		hipRotationX = torsoState[1][0]
		hipRotationY = torsoState[1][1]
		hipRotationZ = torsoState[1][2]
		leftFootRotationZ = leftFootState[1][2]
		rightFootRotationZ = rightFootState[1][2]
		fitness = distance * (1/(1+2*abs(hipRotationX))) * (1/(1+2*abs(hipRotationY))) * (1/(1+2*abs(hipRotationZ))) * (1/(1+2*abs(leftFootRotationZ))) * (1/(1+2*abs(rightFootRotationZ)))
		self.fitnessList.append(fitness)


	def Get_Fitness(self):
		finalFitness = numpy.mean(self.fitnessList)

		tempFitness = open("tmp" + self.solutionID + ".txt", "w")
		tempFitness.write(str(finalFitness))
		tempFitness.close()
		os.system("rename tmp" + self.solutionID + ".txt" " fitness" + self.solutionID + ".txt")