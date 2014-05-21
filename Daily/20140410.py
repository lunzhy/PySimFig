__author__ = 'Lunzhy'
import os, sys
path = os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), os.pardir))
if not path in sys.path:
    sys.path.append(path)
import matplotlib.pyplot as plt
from Submissions.SISPAD2014 import *
import Submissions.SISPAD2014.r_voltage as sispad
import numpy as np
import lib.common as comm
import lib.format as fmt
from operator import itemgetter

Main_path = Directory_Sispad2014
Main_prj = 'retention'
Prj_4nm_300K = r'4nm_300K_1.6eV_PF2e11_T2B5e5'  # thick_1.6eV_PF1e10, 4nm_300K_1.6eV_PF2e11_T2B2e6
Prj_4nm_350K = r'4nm_350K_1.6eV_PF2e11_T2B5e5'
Prj_6nm_300K = r'thick_300K_1.6eV_PF2e11'
Prj_6nm_350K = r'thick_350K_1.6eV_PF2e11'
Time_to_plot = 1e6

def plotVoltageShift():
    fig = plt.figure()
    ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])

    # vth shift
    time, vth = sispad.readVthShift(Prj_4nm_300K)
    ax.plot(time, vth, lw=4, c='k', marker='o', ms=16, fillstyle='none', mew=3, markerfacecolor='w')
    time, vth = sispad.readVthShift(Prj_4nm_350K)
    ax.plot(time, vth, lw=4, c='k', marker='o', ms=16, fillstyle='full', mew=3)
    time, vth = sispad.readVthShift(Prj_6nm_300K)
    ax.plot(time, vth, lw=4, c='b', marker='s', ms=16, fillstyle='none', mew=3, markerfacecolor='w')
    time, vth = sispad.readVthShift(Prj_6nm_350K)
    ax.plot(time, vth, lw=4, c='b', marker='s', ms=16, fillstyle='full', mew=3, mec='b')

    # averaged vfb shift
    time, vth = sispad.readVfbAvgShift(Prj_4nm_300K)
    ax.plot(time, vth, lw=4, c='k', ls='--')
    time, vth = sispad.readVfbAvgShift(Prj_4nm_350K)
    ax.plot(time, vth, lw=4, c='k')
    time, vth = sispad.readVfbAvgShift(Prj_6nm_300K)
    ax.plot(time, vth, lw=4, c='b', ls='--')
    time, vth = sispad.readVfbAvgShift(Prj_6nm_350K)
    ax.plot(time, vth, lw=4, c='b')

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

    comm.saveFigure(fig, 'retention_voltage_new')
    return


def main():
    plotVoltageShift()
    plt.show()
    return


if __name__ == '__main__':
    main()