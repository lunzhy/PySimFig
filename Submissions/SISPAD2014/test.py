__author__ = 'lunzhy'
import os, sys
path = os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), os.pardir, os.pardir))
if not path in sys.path:
    sys.path.append(path)
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
from Submissions.SISPAD2014 import *
from QuickView.TwoDim import TrapOccupy as occ
import lib.common as comm
from mpl_toolkits.axes_grid1 import make_axes_locatable
import lib.format as ft
from matplotlib import font_manager
import numpy as np
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D


Main_path = Directory_Sispad2014
Main_prj = 'retention'
Prj_name = '300K_1.5eV' # 300K_1.5eV, lowT_1.7eV_1e8Hz
Time_to_plot = 10000


def main():
    prj_path = os.path.join(Main_path, Main_prj, Prj_name)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    file_path = comm.searchFilePathByTime(os.path.join(prj_path, 'Band'), 'band', Time_to_plot)
    x, y, cb, vb = comm.readData2D(file_path)
    xi, yi = np.linspace(min(x), max(x), 100), np.linspace(min(y), max(y), 100)
    grid_x, grid_y = np.meshgrid(xi, yi)
    grid_z = comm.makeValueGridZ(x, y, cb)
    surf = ax.plot_surface(grid_x, grid_y, grid_z, cstride=1, rstride=1)
    ax.set_ylim3d(0, 24.2)
    plt.show()
    return


if __name__ == '__main__': main()