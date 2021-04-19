import pybullet as p
import time
import pybullet_data
import os

os.system("python generate.py")

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
p.loadSDF("box.sdf")

robot = p.loadURDF("body.urdf")



for x in range(1000):
   p.stepSimulation()
   time.sleep(1/60)
   print(p.getLinkState(robot, 0))
p.disconnect()
