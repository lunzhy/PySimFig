__author__ = 'lunzhy'
import os, sys, math
import numpy as np
import matplotlib.pyplot as plt
path = os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), os.pardir, os.pardir))
if not path in sys.path:
    sys.path.append(path)
from Submissions.TED2014 import *
import lib.common as comm
import lib.fitting as fitting
import lib.format as fmt

Exp_data_14V = [(9.635427e-8, -0.143508), (9.635427e-7, 1.15034), (9.635427e-6, 2.71754), (1.000000e-4, 3.6287),
                (9.635427e-4, 4.28474), (0.00963543, 4.97722), (0.0963543, 5.23235), (0.928415, 5.48747)]

Exp_data_15V = [(9.635427e-8, 0.530752), (9.284145e-7, 1.95216), (9.284145e-6, 3.51936), (9.284145e-5, 4.24829),
                (9.284145e-4, 5.05011), (0.00928415, 5.4328), (0.0928415, 5.72437), (0.894567, 5.94305)]


Main_path = Directory_TED2014
Main_prj = 'p_fitting'
Prj_name = ''


def plotFitting():
    fig = plt.figure()
    ax = fig.add_axes([0.13, 0.17, 0.75, 0.75])

    # plot 14V fitting
    exp_time_14V = fitting.getTimeList(Exp_data_14V)
    exp_voltage_14V = fitting.getFlatbandList(Exp_data_14V)

    prj_path = os.path.join(Main_path, Main_prj, '14V')
    time, vfb_cell1, vfb_cell2, vfb_cell3 = comm.readVfbOfCells(prj_path)

    vfb_cell2 = [vol - 0.6 for vol in vfb_cell2]

    ax.plot(exp_time_14V, exp_voltage_14V, marker='o', ls='None', fillstyle='none',
            c='k', mec='k', ms=12, mew=3, label='14V exp')
    ax.plot(time, vfb_cell2, c='k', lw=3, label='14V sim')

    # plot 15V fitting
    exp_time_15V = fitting.getTimeList(Exp_data_15V)
    exp_voltage_15V = fitting.getFlatbandList(Exp_data_15V)

    prj_path = os.path.join(Main_path, Main_prj, '15V')
    time, vfb_cell1, vfb_cell2, vfb_cell3 = comm.readVfbOfCells(prj_path)

    vfb_cell2 = [vol - 0.6 for vol in vfb_cell2]

    ax.plot(exp_time_15V, exp_voltage_15V, marker='o', ls='None', fillstyle='none',
            c='b', mec='b', ms=12, mew=3, label='15V exp')
    ax.plot(time, vfb_cell2, c='b', lw=3, label='15V sim')


    ax.set_xscale('log')
    legend = ax.legend(loc='lower right', numpoints=1, ncol=2)

    formatPlots(ax, legend)
    return fig


def formatPlots(ax, legend):
    ax.set_xlabel('Programming Time (s)')
    ax.set_ylabel('Threshold Voltage (V)')
    fmt.setAxesLabel(ax)
    fmt.setAxesTicks(ax)
    ax.set_xticks([1e-8, 1e-6, 1e-4, 1e-2, 1])
    fmt.setLegend(legend)
    return


if __name__ == '__main__':
    fig = plotFitting()
    drawFig(fig, 'fitting')
    # plotSim()
    plt.show()
