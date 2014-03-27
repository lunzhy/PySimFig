__author__ = 'Lunzhy'
import os, sys
path = os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), os.pardir))
if not path in sys.path:
    sys.path.append(path)
import matplotlib.pyplot as plt
import numpy as np
import lib.common as cm

Target_folder = cm.Debug_Folder_Path

times, Vfbs = cm.readVfb(Target_folder)

plt.plot(times, Vfbs, marker='o')
plt.xlim(1e-7, 1)
plt.xscale('log')
plt.show()