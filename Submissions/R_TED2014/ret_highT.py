#! /usr/bin/env python3
# -*- coding: utf-8 -*- 
import os, sys
path = os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), os.pardir, os.pardir))
if not path in sys.path:
    sys.path.append(path)
from Submissions.R_TED2014 import *
import matplotlib.pyplot as plt
import lib.common as comm
from QuickView.TwoDim import TrapOccupy as occ
from QuickView.TwoDim import eDensity as edens
import lib.format as fmt
from matplotlib.ticker import FuncFormatter
import matplotlib.gridspec as gridspec
import numpy as np

Main_path = os.path.join(Directory_RTED2014, 'ret_highK')

def to_simple(x, position):
    s = x / 1e19
    return int(s)


def to_scientific(x, position):
    s = x / 1e19
    return str(int(s)) + 'e19'


def to_scientific_math(x, position):
    s = x / 1e19
    return r'$\mathbf{%s\times10^{%s}%s}$' % (s, '19')


def plotCutsInThreePositions():
    cut_tunnel = 6
    cut_block = 12
    cut_middle = 9
    time_to_plot = ['1', '1e3', '1e4', '1e5', '1e6', '1e7']
    # prj_name = os.path.join('frequency', '1e11')
    prj_path = os.path.join(Directory_RTED2014, 'ret-demo')
    print(prj_path)
    fig = plt.figure()
    ax = fig.add_axes([0, 0, 1, 1], projection='3d')
    # near tunnel oxide
    for index, time in enumerate(time_to_plot):
        time = float(time)
        trap_directory = os.path.join(prj_path, 'Trap')
        trap_file = comm.searchFilePathByTime(trap_directory, 'eTrap', time)
        x, y, dens, occ = comm.cutAlignXY(trap_file, cut_tunnel, align='y')
        ax.plot(x, y, dens, lw=2.5, c=comm.getColor(index))

    # in the middle
    for index, time in enumerate(time_to_plot):
        time = float(time)
        trap_directory = os.path.join(prj_path, 'Trap')
        trap_file = comm.searchFilePathByTime(trap_directory, 'eTrap', time)
        x, y, dens, occ = comm.cutAlignXY(trap_file, cut_middle, align='y')
        ax.plot(x, y, dens, lw=2.5, c=comm.getColor(index))

    # near block oxide
    for index, time in enumerate(time_to_plot):
        time = float(time)
        trap_directory = os.path.join(prj_path, 'Trap')
        trap_file = comm.searchFilePathByTime(trap_directory, 'eTrap', time)
        x, y, dens, occ = comm.cutAlignXY(trap_file, cut_block, align='y')
        ax.plot(x, y, dens, lw=2.5, c=comm.getColor(index))

    ax.set_xlim3d(0, 190)
    # ax.set_ylim3d(4, 15)
    # ax.set_xlabel('BL direction (nm)', labelpad=50, linespacing=3.2)
    # ax.set_ylabel('Vertical direction (nm)')
    # ax.set_zlabel('Trapped electron density (1e19${cm^{-3}}$)')
    # ax.set_xlim3d(50, 140)
    ax.set_xticks([0, 80, 110, 190])
    ax.set_zticks([1e19, 3e19, 5e19])
    # ax.set_zticklabels([1e19, 3e19, 5e19, 7e19])
    zformatter = FuncFormatter(to_simple)
    ax.zaxis.set_major_formatter(zformatter)

    fmt.setAxesLabel(ax)
    # ax.set_zlabel('Trapped electron density (cm^-3)', labelpad=5)
    ax.view_init(25, -55)
    ax.dist = 10
    # legend_text = ['%.es' % leg for leg in time_to_plot]
    legend_text = fmt.setLegendLabelExp(time_to_plot, 's')
    legend = ax.legend(legend_text, loc='upper left', handlelength=3)
    fmt.setLegend(legend)
    plt.show()
    return


def main():
    plotCutsInThreePositions()
    return

if __name__ == '__main__':
    main()