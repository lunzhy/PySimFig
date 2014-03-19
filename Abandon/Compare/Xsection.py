__author__ = 'Lunzhy'
import os

import matplotlib.pyplot as plt

import Compare
import Common


direc = 'Xsection'
unit = '$cm^{-2}$'
figOcc = plt.figure()
figVfb = plt.figure()
Compare.plotCmpOccupation(figOcc, direc, unit)
Compare.plotCmpVfb(figVfb, direc, unit)
plt.show()

figname = os.path.join(Common.figSaveDir, direc)
figVfb.savefig(figname, dpi=600)

figname = os.path.join(Common.figSaveDir, direc + '_Occ')
figOcc.savefig(figname, dpi=600)