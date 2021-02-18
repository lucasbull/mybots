import numpy
import matplotlib.pyplot as mp

backLegSensorValues = numpy.load('data/backLegSensorValues.npy')
frontLegSensorValues = numpy.load('data/frontLegSensorValues.npy')

mp.plot(backLegSensorValues, "black", label="Back Leg Sensor Values", linewidth="3")
mp.plot(frontLegSensorValues, "red", label="Front Leg Sensor Values")
mp.legend()
mp.show()