#! /usr/bin/env python3
# -*- coding: utf-8 -*- 
__author__ = 'lunzhy'
import os, sys
path = os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), os.pardir, os.pardir))
if not path in sys.path:
    sys.path.append(path)
import lib.common as comm
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
from Submissions.Journal2015 import *

Prj_Name = 'erase-demo'
Time_List = [1e-8, 1e-1]


def plot_occ_single(ax, prj_name, time):
    trap_folder_path = os.path.join(Directory_SCIS2015, prj_name, comm.TrapDistr_Folder)
    file_path = comm.searchFilePathByTime(trap_folder_path, 'trapped', time)
    x, y, e_trap, e_occ, h_trap, h_occ = comm.readData2D(file_path, 1)
    grid_z = comm.makeValueGridZ(x, y, e_occ)
    im = ax.imshow(grid_z, cmap=plt.cm.jet, vmin=1e-4, vmax=1, origin='lower',
                   extent=[min(x), max(x), min(y), max(y)], aspect='auto', norm=LogNorm())
    return im


def plot_occ_multi(prj_name, time_list, type='occ'):
    for index, time in enumerate(time_list):
        fig = plt.figure()
        ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
        if type == 'occ':
            im = plot_occ_single(ax, prj_name, time)
        title = 'time = %2.0es' % time
        ax.set_title(title)
        # ax.set_xticks([0, 15, 45, 75, 105, 135, 165, 180])
        plt.colorbar(im)
    return

if __name__ == '__main__':
    plot_occ_multi(Prj_Name, Time_List)
    plt.show()