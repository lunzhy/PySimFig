__author__ = 'lunzhy'
import os, sys
path = os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), os.pardir, os.pardir))
if not path in sys.path:
    sys.path.append(path)
from Submissions.CPB2014 import *
import matplotlib.pyplot as plt
import lib.common as comm
import lib.format as fmt

Main_path = Directory_CPB2014
Main_prj = r'program'
Prj_name = ['u0.01', 'u0.1', 'u1']
Cut_time = [1e-1]


def plotVthCompare():
    fig = plt.figure()
    ax = fig.add_axes([0.15, 0.15, 0.8, 0.8])
    for index, prj in enumerate(Prj_name):
        prj_path = os.path.join(Main_path, Main_prj, prj)
        time, vfb_cell1, vfb_cell2, vfb_cell3 = comm.readVfbOfCells(prj_path)
        ax.plot(time, vfb_cell2, color=comm.getColor(index), lw=3)

    ax.set_xscale('log')
    ax.set_xlabel('Programming Time (s)')
    ax.set_ylabel('Threshold Voltage Shift (V)')
    return


def plotTrapCutVertical():
    fig = plt.figure()
    ax = fig.add_axes([0.15, 0.15, 0.8, 0.8])
    for prj_ind, prj in enumerate(Prj_name):
        prj_path = os.path.join(Main_path, Main_prj, prj)
        for time_ind, time in enumerate(Cut_time):
            trap_path = os.path.join(prj_path, 'Trap')
            file = comm.searchFilePathByTime(trap_path, comm.TrapFile_Pattern, time)
            x, y, dens, occ = comm.cutAlongXY(file, 95, align='x')
            ax.plot(y, occ, color=comm.getColor(prj_ind), lw=3)

    ax.set_xlabel('Vertical Direction (nm)')
    ax.set_ylabel('Trap Occupation')
    return


def plotTrapCutLateral():
    fig = plt.figure()
    ax = fig.add_axes([0.15, 0.15, 0.8, 0.8])
    for prj_ind, prj in enumerate(Prj_name):
        prj_path = os.path.join(Main_path, Main_prj, prj)
        for time_ind, time in enumerate(Cut_time):
            trap_path = os.path.join(prj_path, 'Trap')
            file = comm.searchFilePathByTime(trap_path, comm.TrapFile_Pattern, time)
            x, y, dens, occ = comm.cutAlongXY(file, 4, align='y')
            ax.plot(x, occ, color=comm.getColor(prj_ind), lw=3)
    return


def main():
    plotVthCompare()
    plotTrapCutVertical()
    plotTrapCutLateral()
    plt.show()

if __name__ == '__main__':
    main()