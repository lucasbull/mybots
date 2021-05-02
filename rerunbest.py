import os


directOrGUI = "GUI"
needFitness = True

filename = open("bestRobot.txt", "r")
ID = filename.readline()
showArms = filename.readline()

string = "start /B python simulate.py " + directOrGUI + " " + str(ID).rstrip() + " " + str(needFitness) + " " + str(showArms)

os.system(string)

