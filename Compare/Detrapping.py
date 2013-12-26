__author__ = 'Lunzhy'
import os

import matplotlib.pyplot as plt

import Compare
import Common


fig = plt.figure()
mechDir = 'Detrapping'
Compare.plotW_woCompare(fig, mechDir)
#plt.show()
figname = os.path.join(Common.figSaveDir, 'Detrapping')
plt.savefig(figname, dpi=600)