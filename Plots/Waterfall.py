#! /usr/bin/env python3
# -*- coding: utf-8 -*- 
__author__ = 'lunzhy'
import os, sys
path = os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), os.pardir, os.pardir))
if not path in sys.path:
    sys.path.append(path)
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
import lib.common as comm
import lib.format as fmt
from matplotlib.ticker import FuncFormatter
from Plots import *


Prj_path = '/home/lunzhy/Desktop'
Time_list = [1, 1e2, 1e3, 1e4, 1e5, 5e5, 5e6]


def to_simple(x, position):
    s = x / 1e19
    return int(s)


def plot3DTrappedDensity(prj_path, time_list):
    fig = plt.figure()
    ax = fig.add_axes([0, 0, 1, 1], projection='3d')
    # near tunnel oxide
    for index, time in enumerate(time_list):
        trap_directory = os.path.join(prj_path, 'Trap')
        trap_file = comm.searchFilePathByTime(trap_directory, 'trap', time)
        x, y, dens, dens_hole, occ, occ_hole = comm.cutAlignXY(trap_file, 4, align='y')
        ax.plot(x, y, dens, lw=2.5, c=comm.getColor(index))

    # in the middle
    for index, time in enumerate(time_list):
        trap_directory = os.path.join(prj_path, 'Trap')
        trap_file = comm.searchFilePathByTime(trap_directory, 'trap', time)
        x, y, dens, dens_hole, occ, occ_hole = comm.cutAlignXY(trap_file, 10, align='y')
        ax.plot(x, y, dens, lw=2.5, c=comm.getColor(index))

    # near block oxide
    for index, time in enumerate(time_list):
        trap_directory = os.path.join(prj_path, 'Trap')
        trap_file = comm.searchFilePathByTime(trap_directory, 'trap', time)
        x, y, dens, dens_hole, occ, occ_hole = comm.cutAlignXY(trap_file, 14, align='y')
        ax.plot(x, y, dens, lw=2.5, c=comm.getColor(index))


    ax.set_xlim3d(0, 100)
    ax.set_ylim3d(4, 15)
    # ax.set_xlabel('BL direction (nm)', labelpad=50, linespacing=3.2)
    # ax.set_ylabel('Vertical direction (nm)')
    # ax.set_zlabel('Trapped electron density (1e19${cm^{-3}}$)')
    ax.set_zticks([1e19, 3e19, 5e19, 7e19])
    # ax.set_zticklabels([1e19, 3e19, 5e19, 7e19])
    zformatter = FuncFormatter(to_simple)
    ax.zaxis.set_major_formatter(zformatter)

    fmt.setAxesLabel(ax)
    # ax.set_zlabel('Trapped electron density (cm^-3)', labelpad=5)
    ax.view_init(25, -35)
    ax.dist = 10
    legend_text = ['%.es' % leg for leg in Time_list]
    legend = ax.legend(legend_text, loc='upper left', handlelength=3)
    fmt.setLegend(legend)

    # drawFig(fig, '3D')
    return


def main():
    plot3DTrappedDensity(Prj_path, Time_list)
    plt.show()
    return


if __name__ == '__main__':
    main()