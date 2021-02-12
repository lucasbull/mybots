import pyrosim.pyrosim as pyrosim

def main():
	Create_World()
	Create_Robot()

def Create_World():
	x_pos = -3
	z_pos = 3
	y_pos = 0.5
	length = 1
	width = 1
	height = 1
	pyrosim.Start_SDF("world.sdf")
	pyrosim.Send_Cube(name="Box", pos=[x_pos,z_pos,y_pos] ,
		size=[length,height,width])
	pyrosim.End()

def Create_Robot():
	x_pos = 0
	z_pos = 0
	y_pos = 0.5
	length = 1
	width = 1
	height = 1
	pyrosim.Start_URDF("body.urdf")
	pyrosim.Send_Cube(name="Torso", pos=[x_pos,z_pos,y_pos] ,
		size=[length,height,width])
	pyrosim.End()

main()