from solution import SOLUTION
import constants as c
import copy
import os


class PARALLEL_HILL_CLIMBER:

	def __init__(self, showArms):

		os.system('del files\\brain*.nndf')
		os.system('del files\\fitness*.txt')
		os.system('del files\\tmp*.txt')
		os.system('del files\\body*.urdf')
		os.system('del files\\world*.sdf')

		self.showArms = showArms

		self.nextAvailableID = 0

		self.parents = {

			}

		for parentNumber in range(c.populationSize):
			self.parents[parentNumber] = SOLUTION(self.nextAvailableID, showArms)
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
				os.system("del files\\brain" + str(self.parents[key].myID) + ".nndf")
				os.system("del files\\body" + str(self.parents[key].myID) + ".urdf")
				os.system("del files\\world" + str(self.parents[key].myID) + ".sdf")
				self.parents[key] = self.children[key]

			else:
				os.system("del files\\brain" + str(self.children[key].myID) + ".nndf")
				os.system("del files\\body" + str(self.children[key].myID) + ".urdf")
				os.system("del files\\world" + str(self.children[key].myID) + ".sdf")

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
		currentFitness = 1000000000000000000
		for key in self.parents:
			if self.parents[key].fitness < currentFitness:
				bestKey = key
				currentFitness = self.parents[key].fitness
		self.parents[bestKey].Start_Simulation("GUI", False)
		print("Best fitness: " + str(self.parents[bestKey].fitness))
		if os.path.exists("files\\bestRobot.txt"):
			os.system("del files\\bestRobot.txt")
		bestID = str(self.parents[bestKey].myID)
		keyFitnessGenerationPopulation = open("files\\bestRobot.txt", "w")
		keyFitnessGenerationPopulation.write(bestID + "\n" + str(self.showArms) + "\n" + str(self.parents[bestKey].fitness))
		keyFitnessGenerationPopulation.close()

		os.system("rename files\\brain" + bestID + ".nndf" " bestbrain.nndf")
		os.system("rename files\\body" + bestID + ".urdf" " bestbody.urdf")
		os.system("rename files\\world" + bestID + ".sdf" " bestworld.sdf")

		os.system("del files\\brain*.nndf")
		os.system("del files\\body*.urdf")
		os.system("del files\\world*.sdf")

		os.system("rename files\\bestbrain.nndf" + " brain" + bestID + ".nndf")
		os.system("rename files\\bestbody.urdf" + " body" + bestID + ".urdf")
		os.system("rename files\\bestworld.sdf" + " world" + bestID + ".sdf")