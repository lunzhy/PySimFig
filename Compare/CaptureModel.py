__author__ = 'Lunzhy'
import os

import matplotlib.pyplot as plt

import Compare
import Common


fig = plt.figure()
mechDir = 'CaptureModel_J'
Compare.plotW_woCompare(fig, mechDir)
#plt.show()
figname = os.path.join(Common.figSaveDir, 'CaptureModel')
plt.savefig(figname, dpi=600)