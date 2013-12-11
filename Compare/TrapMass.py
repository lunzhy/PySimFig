# the effective elctron mass of trapping layer
__author__ = 'Lunzhy'
import matplotlib.pyplot as plt
import Compare

direc = 'Si3N4Mass'
unit = '$m0$'
figVfb = plt.figure()
figOcc = plt.figure()
Compare.plotCmpVfb(figVfb, direc, unit)
Compare.plotCmpOccupation(figOcc, direc, unit)
plt.show()