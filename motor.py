import pybullet as p
import pyrosim.pyrosim as pyrosim
import constants as c
import numpy

class MOTOR:

	def __init__(self, jointName):

		self.jointName = jointName
		self.Prepare_To_Act()

	def Prepare_To_Act(self):

		self.amplitude = c.amplitudeBack
		self.frequency = c.frequencyBack
		self.offset = c.phaseOffsetBack
		self.pi = c.pi

		if self.jointName == "Torso_FrontLeg":
			self.frequency = self.frequency/2

		self.i = numpy.linspace(-self.pi, self.pi, c.simulationSize)
		self.motorValues = self.amplitude * numpy.sin(self.frequency  * self.i + self.offset)

	def Set_Value(self, robot, time):

		pyrosim.Set_Motor_For_Joint(bodyIndex = robot, jointName = self.jointName, 
		controlMode = p.POSITION_CONTROL, targetPosition = self.motorValues[time], maxForce = c.motorMaxForce)	

	def Save_Values(self):
		numpy.save('data/' + self.jointName, self.motorValues)