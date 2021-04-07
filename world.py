import pybullet as p

class WORLD:

	def __init__(self, solutionID):

		self.planeId = p.loadURDF("plane.urdf")
		p.loadSDF("world" + solutionID + ".sdf")