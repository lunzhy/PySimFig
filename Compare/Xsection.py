__author__ = 'Lunzhy'
import matplotlib.pyplot as plt
import Compare

direc = 'Xsection'
unit = '$cm^{-2}$'
figOcc = plt.figure()
figVfb = plt.figure()
Compare.plotCmpOccupation(figOcc, direc, unit)
Compare.plotCmpVfb(figVfb, direc, unit)
plt.show()