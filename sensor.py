import constants as c
import numpy
import pyrosim.pyrosim as pyrosim

class SENSOR:

	def __init__(self, linkName):

		self.linkName = linkName
		self.values = numpy.zeros(c.simulationSize)

	def Get_Value(self, time):
		self.values[time] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)

	def Save_Values(self):
		numpy.save('data/' + self.linkName, self.values)