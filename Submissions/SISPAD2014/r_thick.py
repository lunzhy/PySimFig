__author__ = 'lunzhy'
import os, sys
path = os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), os.pardir, os.pardir))
if not path in sys.path:
    sys.path.append(path)
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
from Submissions.SISPAD2014 import *
from QuikView.TwoDim import TrapOccupy as occ
import lib.common as comm
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


Main_path = Directory_Sispad2014
Main_prj = 'retention'
Time_list = [1e-1, 1, 10, 1e2, 1e3, 1e4, 1e5]
Prj_name = 'thick'


def trappedDensity(cut_point, along='x'):
    # lateral
    prj_path = os.path.join(Main_path, Main_prj, Prj_name)
    prj_path = comm.Debug_Folder_Path
    fig = plt.figure()
    ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
    for index, time in enumerate(Time_list):
        trap_directory = os.path.join(prj_path, 'Trap')
        trap_file = comm.searchFilePathByTime(trap_directory, 'trap', time)
        x, y, dens, occ = comm.cutAlongXY(trap_file, cut_point, along)
        if along == 'x':
            ax.plot(x, dens, lw=2, c=comm.getColor(index))
        else:
            ax.plot(y, dens, lw=2, c=comm.getColor(index))

    ax.set_xlim(6, 14)
    return


def freeDensity(cut_point):
    # vertical
    prj_path = os.path.join(Main_path, Main_prj, Prj_name)
    prj_path = comm.Debug_Folder_Path
    fig = plt.figure()
    ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
    for index, time in enumerate(Time_list):
        density_directory = os.path.join(prj_path, 'Density')
        density_file = comm.searchFilePathByTime(density_directory, 'eDens', time)
        x, y, dens = comm.cutAlongXY(density_file, cut_point, along='y')
        ax.plot(y, dens, lw=2, c=comm.getColor(index))
    ax.set_yscale('log')
    return

def plot3DTrappedDensity():
    prj_path = os.path.join(Main_path, Main_prj, Prj_name)
    prj_path = comm.Debug_Folder_Path
    fig = plt.figure()
    ax = fig.add_axes([0.05, 0.05, 0.9, 0.9], projection='3d')
    # near tunnel oxide
    for index, time in enumerate(Time_list):
        trap_directory = os.path.join(prj_path, 'Trap')
        trap_file = comm.searchFilePathByTime(trap_directory, 'trap', time)
        x, y, dens, occ = comm.cutAlongXY(trap_file, 4, along='x')
        ax.plot(x, y, dens, lw=2, c=comm.getColor(index))

    # in the middle
    for index, time in enumerate(Time_list):
        trap_directory = os.path.join(prj_path, 'Trap')
        trap_file = comm.searchFilePathByTime(trap_directory, 'trap', time)
        x, y, dens, occ = comm.cutAlongXY(trap_file, 10, along='x')
        ax.plot(x, y, dens, lw=2, c=comm.getColor(index))

    # near block oxide
    for index, time in enumerate(Time_list):
        trap_directory = os.path.join(prj_path, 'Trap')
        trap_file = comm.searchFilePathByTime(trap_directory, 'trap', time)
        x, y, dens, occ = comm.cutAlongXY(trap_file, 14, along='x')
        ax.plot(x, y, dens, lw=2, c=comm.getColor(index))

    ax.set_xlim(0, 100)
    ax.set_ylim(4, 14)
    ax.set_xlabel('X Coordinate (nm)')
    ax.set_ylabel('Y Coordinate (nm)')
    # ax.set_zlabel('Trapped electron density (cm^-3)', labelpad=5)
    ax.view_init(30, -50)
    ax.dist = 10
    return


def main():
    # trappedDensity(50, 'y')
    # freeDensity(50)
    plot3DTrappedDensity()
    plt.show()

if __name__ == '__main__':
    main()
