from world import WORLD
from robot import ROBOT
import pybullet as p
import constants as c
import pybullet_data
import time

class SIMULATION:

	def __init__(self, directOrGUI, solutionID):

		self.directOrGUI = directOrGUI

		if directOrGUI == "DIRECT":
			self.physicsClient = p.connect(p.DIRECT)
		elif directOrGUI == "GUI":
			self.physicsClient = p.connect(p.GUI)
		else:
			raise Exception("directOrGUI must be DIRECT or GUI. Recieved " + directOrGUI)
			
		p.setAdditionalSearchPath(pybullet_data.getDataPath())

		p.setGravity(c.gravity_x,c.gravity_y,c.gravity_z)

		self.world = WORLD()
		self.robot = ROBOT(solutionID)

	def Run(self):
		for t in range(c.simulationSize):
			#p.stepSimulation()
			self.robot.Sense(t)
			self.robot.Think()
			self.robot.Act(t)

			if self.directOrGUI == "GUI":

				time.sleep(c.timeStepGUI)

	def Get_Fitness(self):

		self.robot.Get_Fitness()



	def __del__(self):
		p.disconnect()