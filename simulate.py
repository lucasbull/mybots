import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import random

amplitudeBack = 0.55
frequencyBack = 8
phaseOffsetBack = 0+.315
amplitudeFront = .45
frequencyFront = 8
phaseOffsetFront = 1.15+.315


physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robot = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")


pyrosim.Prepare_To_Simulate("body.urdf")

backLegSensorValues = numpy.zeros(1000)
frontLegSensorValues = numpy.zeros(1000)
i = numpy.linspace(-numpy.pi, numpy.pi, 1000)
targetAnglesBack = amplitudeBack * numpy.sin(frequencyBack * i + phaseOffsetBack)
targetAnglesFront = amplitudeFront * numpy.sin(frequencyFront * i + phaseOffsetFront)

#numpy.save('data/targetAnglesBack', targetAnglesBack)
#numpy.save('data/targetAnglesFront', targetAnglesFront)
#exit()

for x in range(1000):
   p.stepSimulation()
   backLegSensorValues[x] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
   frontLegSensorValues[x] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
   pyrosim.Set_Motor_For_Joint(bodyIndex = robot, jointName = "Torso_BackLeg", 
   controlMode = p.POSITION_CONTROL, targetPosition = targetAnglesBack[x], maxForce = 50)
   pyrosim.Set_Motor_For_Joint(bodyIndex = robot, jointName = "Torso_FrontLeg", 
   controlMode = p.POSITION_CONTROL, targetPosition = targetAnglesFront[x], maxForce = 50)
   time.sleep(1/60)
numpy.save('data/backLegSensorValues', backLegSensorValues)
numpy.save('data/frontLegSensorValues', frontLegSensorValues)
p.disconnect()