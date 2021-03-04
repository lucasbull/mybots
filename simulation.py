from world import WORLD
from robot import ROBOT
import pybullet as p
import constants as c
import pybullet_data
import time

class SIMULATION:

	def __init__(self):

		self.physicsClient = p.connect(p.GUI)
		p.setAdditionalSearchPath(pybullet_data.getDataPath())

		p.setGravity(c.gravity_x,c.gravity_y,c.gravity_z)

		self.world = WORLD()
		self.robot = ROBOT()

	def Run(self):
		for t in range(c.simulationSize):
			p.stepSimulation()
			self.robot.Sense(t)
			self.robot.Act(t)
			time.sleep(c.timeStep)

	def __del__(self):
		p.disconnect()