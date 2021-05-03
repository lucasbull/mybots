import pybullet as p
import os

class WORLD:

	def __init__(self, solutionID):

		self.planeId = p.loadURDF("plane.urdf")
		p.loadSDF("files\\world" + solutionID + ".sdf")