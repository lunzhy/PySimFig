__author__ = 'lunzhy'
import os, sys
path = os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), os.pardir, os.pardir))
if not path in sys.path:
    sys.path.append(path)
import matplotlib.pyplot as plt
import numpy as np
import lib.common as comm
from matplotlib.colors import LogNorm
from Submissions.SISPAD2014 import *
from QuikView.TwoDim import TrapOccupy as occ

Main_path = Directory_Sispad2014
Main_prj = 'retention'
Sub_prj = 'diff_thick'
# Time_list = [1e-1, 1, 10, 1e2, 1e3, 1e4, 1e5]
Prj_names = ['trap4', 'trap6', 'trap8']
# Prj_names = [comm.Debug_Folder_Path]


def main():
    fig = plt.figure()
    ax = fig.add_axes([0.05, 0.05, 0.9, 0.9])
    for (index, prj) in enumerate(Prj_names):
        prj_path = os.path.join(Main_path, Main_prj, Sub_prj, prj)
        file_path = os.path.join(prj_path, 'Miscellaneous', 'chargeRegionwise.txt')
        data = np.loadtxt(file_path, skiprows=1)
        time, main_cell, other_region = data[:, 0], data[:, 2], data[:, 3]
        # ax.plot(time, main_cell, c=comm.getColor(0))
        ax.plot(time, other_region, c=comm.getColor(index))

    ax.set_xscale('log')
    legend = ax.legend(Prj_names)
    return


if __name__ == '__main__':
    main()
    plt.show()