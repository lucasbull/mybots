import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("boxes.sdf")

for x_pos in range(6):
	x = x_pos - 3
	for z_pos in range(6):
		z = z_pos - 3
		length = 1
		width = 1
		height = 1
		y = 0.5
		for count in range(10):
			pyrosim.Send_Cube(name="Box", pos=[x,z,y] , size=[length,width,height])
			y = y + 0.45*height + 0.5*height
			length = 0.9 * length
			width = 0.9 * width
			height = 0.9 * height
pyrosim.End()