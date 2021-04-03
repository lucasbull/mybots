from solution import SOLUTION
import constants as c
import copy

class PARALLEL_HILL_CLIMBER:

	def __init__(self):

		self.nextAvailableID = 0

		self.parents = {

			}

		for parentNumber in range(c.populationSize):
			self.parents[parentNumber] = SOLUTION(self.nextAvailableID)
			self.nextAvailableID = self.nextAvailableID + 1

	def Evolve(self):
		
		for parent in self.parents:
			self.parents[parent].Evaluate("GUI")

		# for currentGeneration in range(c.numberOfGenerations):

		# 	print("Current Generation:", currentGeneration)
		# 	self.Evolve_For_One_Generation()


	def Evolve_For_One_Generation(self):

		self.Spawn()
		self.Mutate()
		self.child.Evaluate("DIRECT")
		self.Print()
		self.Select()

	def Spawn(self):

		self.child = copy.deepcopy(self.parent)
		self.child.Set_ID(self.nextAvailableID)
		self.nextAvailableID = self.nextAvailableID + 1

	def Mutate(self):

		self.child.Mutate()

	def Select(self):

		if self.parent.fitness > self.child.fitness:

			self.parent = self.child

	def Print(self):

		print("Parent:", self.parent.fitness, "Child:", self.child.fitness)

	def Show_Best(self):

		#self.parent.Evaluate("GUI")
		pass