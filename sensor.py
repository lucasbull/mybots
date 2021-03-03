import constants as c
import numpy
import pyrosim.pyrosim as pyrosim

class SENSOR:

	def __init__(self, linkName):

		self.linkName = linkName
		self.values = numpy.zeros(c.simulationSize)

	def Get_Value(self, time):
		self.values[time] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
		
		if time == c.simulationSize - 1:
			print(self.values)
		