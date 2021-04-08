import pybullet as p
import os

class WORLD:

	def __init__(self, solutionID):

		self.planeId = p.loadURDF("plane.urdf")
		p.loadSDF("world" + solutionID + ".sdf")
		os.system("del world" + solutionID + ".sdf")