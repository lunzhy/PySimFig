__author__ = 'lunzhy'
import os, sys
path = os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), os.pardir, os.pardir))
if not path in sys.path:
    sys.path.append(path)
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
from Submissions.SISPAD2014 import *
import lib.common as common
import lib.format as ft
from mpl_toolkits.mplot3d import axes3d
from matplotlib import cm
import numpy as np


Time_to_plot = 1e-2

def main():
    prj_path = common.Debug_Folder_Path
    band_directory = os.path.join(prj_path, 'Trap')
    file_path = common.searchFilePathByTime(band_directory, 'trap', Time_to_plot)
    x, y, dens, occ = common.readData2D(file_path)
    fig = plt.figure()
    ax = fig.gca(projection='3d')

    xi, yi = np.linspace(min(x), max(x), 100), np.linspace(min(y), max(y), 100)
    grid_x, grid_y = np.meshgrid(xi, yi)
    grid_z = common.makeValueGridZ(x, y, dens)
    ax.plot_surface(grid_x, grid_y, grid_z, rstride=30, cstride=30, cmap=cm.coolwarm)

    # cset = ax.contourf(X, Y, Z, zdir='z', offset=-100, cmap=cm.coolwarm)
    # cset = ax.contourf(X, Y, Z, zdir='x', offset=-40, cmap=cm.coolwarm)
    # cset = ax.contourf(X, Y, Z, zdir='y', offset=40, cmap=cm.coolwarm)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.show()
    return

if __name__ == '__main__': main()
