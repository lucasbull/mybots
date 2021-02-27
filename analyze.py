import numpy
import matplotlib.pyplot as mp

backLegSensorValues = numpy.load('data/backLegSensorValues.npy')
frontLegSensorValues = numpy.load('data/frontLegSensorValues.npy')
targetAnglesValuesBack = numpy.load('data/targetAnglesBack.npy')
targetAnglesValuesFront = numpy.load('data/targetAnglesFront.npy')
#print(targetAnglesValues)


#mp.plot(backLegSensorValues, "black", label="Back Leg Sensor Values", linewidth="3")
#mp.plot(frontLegSensorValues, "red", label="Front Leg Sensor Values")
mp.plot(targetAnglesValuesBack)
mp.plot(targetAnglesValuesFront)

#mp.legend()
mp.show()