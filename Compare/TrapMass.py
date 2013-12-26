# the effective elctron mass of trapping layer
__author__ = 'Lunzhy'
import os

import matplotlib.pyplot as plt

import Compare
import Common


direc = 'Si3N4Mass'
unit = '$m0$'
figVfb = plt.figure()
figOcc = plt.figure()
Compare.plotCmpVfb(figVfb, direc, unit)
Compare.plotCmpOccupation(figOcc, direc, unit)
plt.show()

figname = os.path.join(Common.figSaveDir, direc)
figVfb.savefig(figname, dpi=600)

figname = os.path.join(Common.figSaveDir, direc + '_Occ')
figOcc.savefig(figname, dpi=600)