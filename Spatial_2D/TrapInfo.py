__author__ = 'Lunzhy'
import os
import lib.common as common

import matplotlib.pyplot as plt
import scipy.interpolate
import numpy as np
import math
from matplotlib.colors import LogNorm

File_relpath = r'Miscellaneous\TrapInfo.txt'
# File_path = os.path.join(common.Directory_Debug, File_relpath)
Prj_path = r'E:\PhD Study\SimCTM\SctmTest\Retention_2D\Demo\300K'
File_path = os.path.join(Prj_path, File_relpath)

x, y, trapdens = common.readData2D(File_path, 1)

xi, yi = np.linspace(min(x), max(x), 100), np.linspace(min(y), max(y), 100)
xi, yi = np.meshgrid(xi, yi)
grid_zi = scipy.interpolate.griddata((x, y), trapdens, (xi, yi), method='nearest')
plt.imshow(grid_zi, cmap=plt.cm.jet,vmin=min(trapdens), vmax=max(trapdens), origin='lower',
            extent=[min(x), max(x), min(y), max(y)], aspect='equal')
# plt.contour(grid_zi)
plt.colorbar()
plt.show()