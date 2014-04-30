__author__ = 'Lunzhy'
import os, sys
path = os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), os.pardir, os.pardir))
if not path in sys.path:
    sys.path.append(path)
import matplotlib.pyplot as plt
from Submissions.SISPAD2014 import *
from QuikView.TwoDim import TrapOccupy as occ
import numpy as np
import lib.common as comm
import lib.format as fmt
from matplotlib import font_manager
from mpl_toolkits.axes_grid1 import make_axes_locatable
import matplotlib.gridspec as gridspec
from operator import itemgetter

Main_path = Directory_Sispad2014
Main_prj = 'retention'
Prj_4nm_300K = r'4nm_300K_1.6eV_PF2e11_T2B5e5'  # thick_1.6eV_PF1e10, 4nm_300K_1.6eV_PF2e11_T2B2e6
Prj_4nm_350K = r'4nm_350K_1.6eV_PF2e11_T2B5e5'
Prj_6nm_300K = r'thick_300K_1.6eV_PF2e11'
Prj_6nm_350K = r'thick_350K_1.6eV_PF2e11'
Time_to_plot = 1e6


def readVthShift(prj_path):
    vth_path = os.path.join(Main_path, Main_prj, prj_path, comm.Threshold_File_Relpath)
    data = np.loadtxt(vth_path)
    time, vth = data[:, 0], data[:, 1]
    sorted_tup_list = sorted(zip(time, vth), key=itemgetter(0))
    time, vth = zip(*sorted_tup_list)
    initial_vth = vth[0]
    vth_shift = [voltage - initial_vth for voltage in vth]
    return time, vth_shift


def readVfbAvgShift(prj_path):
    vth_path = os.path.join(Main_path, Main_prj, prj_path, comm.AvgFlatband_File)
    data = np.loadtxt(vth_path)
    time, vth = data[:, 0], data[:, 1]
    sorted_tup_list = sorted(zip(time, vth), key=itemgetter(0))
    time, vth = zip(*sorted_tup_list)
    initial_vth = vth[0]
    vth_shift = [voltage - initial_vth for voltage in vth]
    return time, vth_shift


def plotVoltageShift():
    fig = plt.figure()
    ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])

    # time, vth = readVthShift(Prj_4nm_300K)
    # ax.plot(time, vth, lw=4, c='k', marker='o', ms=16, fillstyle='none', mew=3, markerfacecolor='w')
    # time, vth = readVthShift(Prj_4nm_350K)
    # ax.plot(time, vth, lw=4, c='k', marker='o', ms=16, fillstyle='full', mew=3)
    # time, vth = readVthShift(Prj_6nm_300K)
    # ax.plot(time, vth, lw=4, c='b', marker='s', ms=16, fillstyle='none', mew=3, markerfacecolor='w')
    # time, vth = readVthShift(Prj_6nm_350K)
    # ax.plot(time, vth, lw=4, c='b', marker='s', ms=16, fillstyle='full', mew=3, mec='b')

    time, vth = readVfbAvgShift(Prj_4nm_300K)
    ax.plot(time, vth, lw=4, c='k', marker='o', ms=16, fillstyle='none', mew=3, markerfacecolor='w', markevery=10)
    time, vth = readVfbAvgShift(Prj_4nm_350K)
    ax.plot(time, vth, lw=4, c='k', marker='o', ms=16, fillstyle='full', mew=3, markevery=10)
    time, vth = readVfbAvgShift(Prj_6nm_300K)
    ax.plot(time, vth, lw=4, c='b', marker='s', ms=16, fillstyle='none', mew=3, markerfacecolor='w', markevery=10)
    time, vth = readVfbAvgShift(Prj_6nm_350K)
    ax.plot(time, vth, lw=4, c='b', marker='s', ms=16, fillstyle='full', mew=3, mec='b', markevery=10)

    labels = ['4/8/12nm T=300K', '4/8/12nm T=350K', '6/8/12nm T=300K', '6/8/12nm T=350K']
    legend = ax.legend(labels, loc='lower left', handlelength=3, numpoints=1)
    fmt.setLegend(legend, 24)

    ax.set_xlabel('Retention Time (s)')
    ax.set_ylabel('Threshold Voltage Shift (V)')
    ax.set_xscale('log')
    ax.set_xlim(1e1, 1e7)
    ax.set_ylim(-5, 1)
    fmt.setAxesLabel(ax)
    fmt.setAxesTicks(ax)

    drawFig(fig, 'retention_voltage_new')
    return


def main():
    plotVoltageShift()
    plt.show()
    return


if __name__ == '__main__':
    main()