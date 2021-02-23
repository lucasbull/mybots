import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import math
import random

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

pi = math.pi

p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robot = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")


pyrosim.Prepare_To_Simulate("body.urdf")

backLegSensorValues = numpy.zeros(1000)
frontLegSensorValues = numpy.zeros(1000)

for x in range(1000):
   p.stepSimulation()
   backLegSensorValues[x] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
   frontLegSensorValues[x] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
   pyrosim.Set_Motor_For_Joint(bodyIndex = robot, jointName = "Torso_BackLeg", 
   controlMode = p.POSITION_CONTROL, targetPosition = random.random()*pi-pi/2, maxForce = 50)
   pyrosim.Set_Motor_For_Joint(bodyIndex = robot, jointName = "Torso_FrontLeg", 
   controlMode = p.POSITION_CONTROL, targetPosition = random.random()*pi-pi/2, maxForce = 50)
   time.sleep(1/60)
numpy.save('data/backLegSensorValues', backLegSensorValues)
numpy.save('data/frontLegSensorValues', frontLegSensorValues)
p.disconnect()