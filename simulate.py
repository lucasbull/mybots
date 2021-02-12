import pybullet as p
import time

physicsClient = p.connect(p.GUI)

p.loadSDF("world.sdf")

for x in range(1000):
   p.stepSimulation()
   time.sleep(1/60)
p.disconnect()