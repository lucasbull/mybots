import os

name = "286"
directOrGUI = "GUI"
needFitness = str(False)

filename = open("files\\bestRobot.txt", "r")
originalID = filename.readline().rstrip()
showArms = str(filename.readline()).rstrip()
fitness = str(filename.readline())

string = "start /B python simulate.py " + directOrGUI + " " + name + " " + needFitness + " " + showArms

os.system(string)
print("Fitness:")
print(fitness)