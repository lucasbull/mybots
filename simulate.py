from simulation import SIMULATION
# import pybullet as p
# import time
# import pybullet_data
# import pyrosim.pyrosim as pyrosim
# import numpy
# import random
# import constants as c

simulation = SIMULATION()

# physicsClient = p.connect(p.GUI)
# p.setAdditionalSearchPath(pybullet_data.getDataPath())

# p.setGravity(c.gravity_x,c.gravity_y,c.gravity_z)
# planeId = p.loadURDF("plane.urdf")
# robot = p.loadURDF("body.urdf")
# p.loadSDF("world.sdf")


# pyrosim.Prepare_To_Simulate("body.urdf")

# backLegSensorValues = numpy.zeros(c.simulationSize)
# frontLegSensorValues = numpy.zeros(c.simulationSize)
# i = numpy.linspace(-c.pi, c.pi, c.simulationSize)
# targetAnglesBack = c.amplitudeBack * numpy.sin(c.frequencyBack * i + c.phaseOffsetBack)
# targetAnglesFront = c.amplitudeFront * numpy.sin(c.frequencyFront * i + c.phaseOffsetFront)

# #numpy.save('data/targetAnglesBack', targetAnglesBack)
# #numpy.save('data/targetAnglesFront', targetAnglesFront)
# #exit()

# for x in range(c.simulationSize):
#    p.stepSimulation()
#    backLegSensorValues[x] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
#    frontLegSensorValues[x] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
#    pyrosim.Set_Motor_For_Joint(bodyIndex = robot, jointName = "Torso_BackLeg", 
#    controlMode = p.POSITION_CONTROL, targetPosition = targetAnglesBack[x], maxForce = c.motorMaxForce)
#    pyrosim.Set_Motor_For_Joint(bodyIndex = robot, jointName = "Torso_FrontLeg", 
#    controlMode = p.POSITION_CONTROL, targetPosition = targetAnglesFront[x], maxForce = c.motorMaxForce)
#    time.sleep(c.timeStep)
# numpy.save('data/backLegSensorValues', backLegSensorValues)
# numpy.save('data/frontLegSensorValues', frontLegSensorValues)
# p.disconnect()