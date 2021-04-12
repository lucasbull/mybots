from solution import SOLUTION
import constants as c
import copy
import os

class PARALLEL_HILL_CLIMBER:

	def __init__(self):

		os.system("del brain*.nndf")
		os.system("del fitness*.txt")
		os.system("del tmp*.txt")
		os.system("del body*.urdf")
		os.system("del world*.sdf")

		self.nextAvailableID = 0

		self.parents = {

			}

		for parentNumber in range(c.populationSize):
			self.parents[parentNumber] = SOLUTION(self.nextAvailableID)
			self.nextAvailableID = self.nextAvailableID + 1


	def Evolve(self):

		self.Evaluate(self.parents)

		for currentGeneration in range(c.numberOfGenerations):

			#print("Current Generation:", currentGeneration)
			self.Evolve_For_One_Generation()


	def Evolve_For_One_Generation(self):
		self.Spawn()
		self.Mutate()
		self.Evaluate(self.children)
		self.Print()
		self.Select()

	def Spawn(self):
		
		self.children = {
			}

		for parent in self.parents:
			self.children[parent] = copy.deepcopy(self.parents[parent])
			self.children[parent].Set_ID(self.nextAvailableID)
			self.nextAvailableID = self.nextAvailableID + 1

	def Mutate(self):

		for child in self.children:
			self.children[child].Mutate()

	def Select(self):

		for key in self.parents:
			if self.parents[key].fitness > self.children[key].fitness:
				self.parents[key] = self.children[key]

	def Print(self):
		print()
		for key in self.parents:
			print("Parent:", self.parents[key].fitness, "Child:", self.children[key].fitness)
		print()

	def Evaluate(self, solutions):
		for solution in solutions:
			solutions[solution].Start_Simulation("DIRECT", True)

		for solution in solutions:
			solutions[solution].Wait_For_Simulation_To_End()

	def Show_Best(self):
		currentFitness = 100
		for key in self.parents:
			if self.parents[key].fitness < currentFitness:
				bestKey = key
				currentFitness = self.parents[key].fitness
		self.parents[bestKey].Start_Simulation("GUI", False)
		print("Best fitness: " + str(self.parents[bestKey].fitness))