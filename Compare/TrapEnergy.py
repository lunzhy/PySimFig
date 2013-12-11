__author__ = 'Lunzhy'
import matplotlib.pyplot as plt
import Compare

direc = 'TrapEnergy'
unit = '$eV$'
figVfb = plt.figure()
figOcc = plt.figure()
Compare.plotCmpVfb(figVfb, direc, unit)
Compare.plotCmpOccupation(figOcc, direc, unit)
plt.show()