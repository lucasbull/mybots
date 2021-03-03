import pybullet as p
import pyrosim.pyrosim as pyrosim
import constants as c
import numpy

class MOTOR:

	def __init__(self, jointName):

		self.jointName = jointName
		self.prepare_To_Act()

	def Prepare_To_Act(self):

		self.amplitude = c.amplitudeBack
		self.frequency = c.frequencyBack
		self.offset = c.phaseOffsetBack
		self.pi = c.pi

		self.i = numpy.linspace(-self.pi, self.pi, c.simulationSize)
		self.motorValuesBack = self.amplitude * numpy.sin(self.frequency  * self.i + self.offset)
		self.motorValuesFront = self.amplitude * numpy.sin(self.frequency  * self.i + self.offset)

	def Set_Value(self):

		pyrosim.Set_Motor_For_Joint(bodyIndex = robot, jointName = "Torso_BackLeg", 
		controlMode = p.POSITION_CONTROL, targetPosition = targetAnglesBack[x], maxForce = c.motorMaxForce)	

		#CURRENTLY ON STEP 92