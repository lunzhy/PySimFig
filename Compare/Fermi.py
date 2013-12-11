__author__ = 'Lunzhy'
import matplotlib.pyplot as plt
import Compare

direc = 'FermiAbove'
unit = '$eV$'
figOcc = plt.figure()
figVfb = plt.figure()
Compare.plotCmpOccupation(figOcc, direc, unit)
Compare.plotCmpVfb(figVfb, direc, unit)
plt.show()
