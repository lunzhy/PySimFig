__author__ = 'Lunzhy'
import os, sys
path = os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), os.pardir))
if not path in sys.path:
    sys.path.append(path)
import matplotlib.pyplot as plt
import numpy as np
import lib.common as cm

Target_folder = cm.Debug_Folder_Path
Target_folder = '/home/lunzhy/SimCTM/projects/SSDM2014/standard_program/5e5_2e11_1.6'
Target_folder ='/home/lunzhy/SimCTM/projects/CPB2014/ret_lowK/SiN/0.1'

# times, Vfbs = cm.readVfb(Target_folder)
time, vfb_cell1, vfb_cell2, vfb_cell3 = cm.readVfbOfCells(Target_folder)

plt.plot(time, vfb_cell2, marker='o')
plt.xlim(1e-2, 1e7)
plt.xscale('log')
plt.show()