import numpy
import matplotlib.pyplot as mp

backLegSensorValues = numpy.load('data/backLegSensorValues.npy')

mp.plot(backLegSensorValues)
mp.show()