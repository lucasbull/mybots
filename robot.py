import pybullet as p
import pyrosim.pyrosim as pyrosim
from sensor import SENSOR
from motor import MOTOR
from pyrosim.neuralNetwork import NEURAL_NETWORK
import os
import constants as c

class ROBOT:

	def __init__(self, solutionID):

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

		for neuronName in self.nn.Get_Neuron_Names():

			if self.nn.Is_Motor_Neuron(neuronName):

				jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
				desiredAngle = self.nn.Get_Value_Of(neuronName)
				if desiredAngle < c.allowableTargetAngles[neuronName][0]:
					desiredAngle = c.allowableTargetAngles[neuronName][0]
				if desiredAngle > c.allowableTargetAngles[neuronName][1]:
					desiredAngle = c.allowableTargetAngles[neuronName][1]
				self.motors[jointName].Set_Value(self.robot, desiredAngle)

	def Think(self, time):
		self.nn.Update()
		torsoState = p.getBasePositionAndOrientation(self.robot)
		distance = torsoState[0][0]

	def Get_Fitness(self):

		basePositionAndOrientation = p.getBasePositionAndOrientation(self.robot)
		basePosition = basePositionAndOrientation[0]
		xPosition = basePosition[0]
		zPosition = basePosition[2]
		fitnessValue = -2*zPosition + xPosition
		tempFitness = open("tmp" + self.solutionID + ".txt", "w")
		tempFitness.write(str(fitnessValue))
		tempFitness.close()
		os.system("rename tmp" + self.solutionID + ".txt" " fitness" + self.solutionID + ".txt")