#! /usr/bin/env python3
# -*- coding: utf-8 -*- 
__author__ = 'lunzhy'
import os, sys
path = os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), os.pardir, os.pardir))
if not path in sys.path:
    sys.path.append(path)
from Submissions.R_TED2014 import *
import matplotlib.pyplot as plt
import lib.common as comm
import math


Main_path = Directory_RTED2014
Main_prj = r'program'
# Prj_name = ['p14V_u0.001', 'p14V_u0.01']
Prj_name = ['p14V_u0.1', 'p14V_u0.01', 'p14V_u0.001']
Cut_time = [1e-4]
Cut_position = 2.5


def plotTrapCutLateral():
    fig = plt.figure()
    ax = fig.add_axes([0.15, 0.15, 0.8, 0.8])
    for prj_ind, prj in enumerate(Prj_name):
        prj_path = os.path.join(Main_path, Main_prj, prj)
        for time_ind, time in enumerate(Cut_time):
            trap_path = os.path.join(prj_path, 'Trap')
            file = comm.searchFilePathByTime(trap_path, 'eTrap', time)
            x, y, dens, occ = comm.cutAlignXY(file, Cut_position, align='y')
            ax.plot(x, occ, color=comm.getColor(prj_ind), lw=3)

    labels = [label[1:] + 'cm$^{2}$(Vs)$^{-1}$' for label in Prj_name]
    legend = ax.legend(labels, loc='upper left')
    ax.set_xlabel('Bitline Direction (nm)')
    ax.set_ylabel('Trap Occupation')
    ax.set_xlim(0, 180)
    # ax.set_xticks([0, 15, 45, 75, 105, 135, 165, 180])
    ax.set_xticks([0, 20, 50, 80, 110, 140, 170, 190])
    return


def plotTrapCutRadial():
    fig = plt.figure()
    ax = fig.add_axes([0.15, 0.15, 0.8, 0.8])
    for prj_ind, prj in enumerate(Prj_name):
        prj_path = os.path.join(Main_path, Main_prj, prj)
        for time_ind, time in enumerate(Cut_time):
            trap_path = os.path.join(prj_path, 'Trap')
            file = comm.searchFilePathByTime(trap_path, 'eTrap', time)
            x, y, dens, occ = comm.cutAlignXY(file, 95, align='x')
            ax.plot(y, occ, color=comm.getColor(prj_ind), lw=3)

    labels = [label[1:] + ' cm$^{2}$(Vs)$^{-1}$' for label in Prj_name]
    legend = ax.legend(labels, loc='upper center')
    ax.set_xlabel('Radial Direction (nm)')
    ax.set_ylabel('Trap Occupation')
    return


def plotMemoryWindow(ax):
    main_prj = os.path.join(Directory_RTED2014, 'radius_14V')
    time_to_read = 1e-1
    mobility_list = ['0.001', '0.001']  # 0.01 or 0.001
    radius_list = ['10', '20', '30', '40', '50', '60', '70', '80', '90', '100', '110', '120']
    windows_list = ()
    for mobility in mobility_list:
        windows = []
        for radius in radius_list:
            prj = '%s_%s' % (radius, mobility)
            prj_path = os.path.join(main_prj, prj)
            time_list, vfb_list = comm.read_vfb(prj_path)
            time_diff = [math.fabs(time-time_to_read) for time in time_list]
            min_index = time_diff.index(min(time_diff))
            vfb_to_read = vfb_list[min_index]
            windows.append(vfb_to_read)
        windows_list += (windows, )
    radius_list = [float(radius) for radius in radius_list]
    windows, windows2 = windows_list
    comm.write_data(Folder_Write_Data, radius_list, windows, windows2)
    return


def plotBandDiagram(ax):
    main_prj = os.path.join(Directory_RTED2014, 'radius_14V')
    prj_name = ['20_0.001', '20_0.01']
    time_to_plot = 1e-5
    data_to_write = ()
    for prj in prj_name:
        file_to_plot = comm.searchFilePathByTime(os.path.join(main_prj, prj, 'Band'), 'band',
                                                 time_to_plot)
        dummy_x, y, cband, vband = comm.cutAlignXY(file_to_plot, 0, 'x')
        ax.plot(y, cband, label=prj)
        ax.plot(y, vband, label=prj)
        data_to_write += (cband, vband,)
    # ax.set_xlim(0, 3)
    ax.set_ylim(-10, 2.5)
    ax.legend()
    cband, vband, cband2, vband2 = data_to_write
    comm.write_data(Folder_Write_Data, y, cband, vband, cband2, vband2)
    return


def plotElectricField(ax):
    main_prj = [os.path.join(Directory_RTED2014, 'radius_14V', '10_0.001'),
                os.path.join(Directory_RTED2014, 'radius_14V', 'planar_0.001')]

    time_to_plot = 1e-9
    data_to_write = ()
    for prj in main_prj:
        file_to_plot = comm.searchFilePathByTime(os.path.join(prj, 'ElecField'), 'elec',
                                                 time_to_plot)
        dummy_x, y, efield_x, efield_y, efield_abs = comm.cutAlignXY(file_to_plot, 0, 'x')
        efield_y = [math.fabs(ef) / 1e6 for ef in efield_y]
        data_to_write += (efield_y,)
    efield_y, efield_y2 = data_to_write
    comm.write_data(Folder_Write_Data, y, efield_y, efield_y2)
    return


def plotOccCompare(ax):
    main_prj = os.path.join(Directory_RTED2014, 'curvature')
    prj_name = ['p14V_dd', 'p14V_planar']
    time_to_plot = 1e-2
    data_to_write = ()
    for prj in prj_name:
        file_to_plot = comm.searchFilePathByTime(os.path.join(main_prj, prj, 'Trap'), 'eTrap',
                                                 time_to_plot)
        dummy_x, y, etrapped, occ = comm.cutAlignXY(file_to_plot, 0, 'x')
        data_to_write += (occ,)
        ax.plot(y, occ, label=prj)
    occ1, occ2 = data_to_write
    comm.write_data(Folder_Write_Data, y, occ1, occ2)
    ax.legend()
    return


def plotDensCompare(ax):
    main_prj = os.path.join(Directory_RTED2014, 'radius_14V')
    prj_name = ['20_0.001', '20_0.01']
    time_to_plot = 1e-2
    for prj in prj_name:
        file_to_plot = comm.searchFilePathByTime(os.path.join(main_prj, prj, 'Density'), 'eDens',
                                                 time_to_plot)
        dummy_x, y, edens = comm.cutAlignXY(file_to_plot, 0, 'x')
        ax.plot(y, edens, label=prj)
    ax.legend()
    ax.set_yscale('log')
    return


def plotTotalTrappedDensity(ax):
    main_prj = os.path.join(Directory_RTED2014, 'radius_14V')
    prj_name = ['20_0.001', '20_0.01']
    for prj in prj_name:
        time, free_e, trapped_e, free_h, trapped_h = comm.read_data(os.path.join(main_prj, prj,
                                                                    'Miscellaneous', 'ehDens.txt'))
        ax.plot(time, free_e, label=prj)

    ax.set_xscale('log')
    ax.legend()
    return


def plotTunnelCurrent(ax):
    main_prj = os.path.join(Directory_RTED2014, 'radius_14V')
    prj_name = ['20_0.001', '20_0.01']
    for prj in prj_name:
        time_list = ()
        currdens_list = ()
        prj_path = os.path.join(main_prj, prj)
        files = comm.getFiles(os.path.join(prj_path, 'Current'), 'eTunnel')
        for file in files:
            time = comm.getTime(file)
            time_list += (time, )
            dummy, y, currdens, direction = comm.cutAlignXY(file, 0, 'x')
            currdens_list += (currdens[0], )
        ax.plot(time_list, currdens_list, label=prj)

    ax.set_xscale('log')
    ax.set_yscale('log')
    ax.legend()
    return


def main():
    fig = plt.figure()
    ax = fig.add_axes([0.15, 0.15, 0.8, 0.8])
    # plotTrapCutRadial()
    # plotTrapCutLateral()
    # plotMemoryWindow(ax)
    # plotBandDiagram(ax)
    # plotElectricField(ax)
    plotOccCompare(ax)
    # plotTotalTrappedDensity(ax)
    # plotTunnelCurrent(ax)
    # plotDensCompare(ax)
    plt.show()


if __name__ == '__main__':
    main()