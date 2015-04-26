#! /usr/bin/env python3
# -*- coding: utf-8 -*- 
__author__ = 'lunzhy'
import os, sys
path = os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), os.pardir, os.pardir))
if not path in sys.path:
    sys.path.append(path)
import lib.common as comm
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
from matplotlib.colors import SymLogNorm
from Submissions.Journal2015 import *

Colormap_Type = plt.cm.RdYlBu
# Colormap_Type = plt.cm.jet

Prj_Name = 'erase-demo'
Prj_Name = os.path.join('program', 'P18V_50nm')
Prj_Name = os.path.join('retention', '50nm_18V', '400K', 's1_1e9')
Prj_Name = os.path.join('erase', '30nm', '18V_1e9')
# Time_List = [1e-8, 3.7e-6, 37e-6, 520e-3]
# Time_List = [1e-8, 26e-6, 370e-6, 10e-3]  # for 40nm_16V
Time_List = [1e-2, 1e3, 1e6, 1e7]
Time_List = [1e-8, 1e-3, 3e-3, 0.1]


def plot_occ_single(ax, prj_name, time, carrier='both'):
    trap_folder_path = os.path.join(Directory_Journal2015, prj_name, comm.TrapDistr_Folder)
    file_path = comm.searchFilePathByTime(trap_folder_path, 'trapped', time)
    x, y, e_trap, e_occ, h_trap, h_occ = comm.readData2D(file_path, 1)

    if carrier == 'e':
        net_occ = e_occ
        vmin, vmax = 1e-4, 1.0
        log_norm = LogNorm()
    elif carrier == 'h':
        net_occ = h_occ
        vmin, vmax = 1e-4, 1.0
        log_norm = LogNorm()
    else:
        net_occ = h_occ - e_occ
        vmin, vmax = -1.0, 1.0
        log_norm = SymLogNorm(linthresh=1e-6)

    grid_z = comm.makeValueGridZ(x, y, net_occ)
    im = ax.imshow(grid_z, cmap=Colormap_Type, vmin=vmin, vmax=vmax, origin='lower',
                   extent=[min(x), max(x), min(y), max(y)], aspect='auto', norm=log_norm)
    return im


def plot_dens_single(ax, prj_name, time, carrier='both'):
    trap_folder_path = os.path.join(Directory_Journal2015, prj_name, comm.TrapDistr_Folder)
    file_path = comm.searchFilePathByTime(trap_folder_path, 'trapped', time)
    x, y, e_trap, e_occ, h_trap, h_occ = comm.readData2D(file_path, 1)

    if carrier == 'e':
        net_occ = e_trap
        vmin, vmax = 1e16, 1e20
        log_norm = LogNorm()
    elif carrier == 'h':
        net_occ = h_trap
        vmin, vmax = 1e16, 1e20
        log_norm = LogNorm()
    else:
        net_occ = h_trap - e_trap
        vmin, vmax = -1e20, 1e20
        log_norm = SymLogNorm(linthresh=1e14)

    grid_z = comm.makeValueGridZ(x, y, net_occ)
    im = ax.imshow(grid_z, cmap=Colormap_Type, vmin=vmin, vmax=vmax, origin='lower',
                   extent=[min(x), max(x), min(y), max(y)], aspect='auto', norm=log_norm)
    return im


def plot_multi(prj_name, time_list, plot_type='occ', carrier='both'):
    for index, time in enumerate(time_list):
        fig = plt.figure()
        ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
        if plot_type == 'occ':
            im = plot_occ_single(ax, prj_name, time, carrier=carrier)
        elif plot_type == 'dens':
            im = plot_dens_single(ax, prj_name, time, carrier=carrier)

        title = 'time = %2.0es' % time
        ax.set_title(title)
        if '40nm' in Prj_Name:
            ax.set_xticks([0, 20, 60, 100, 140, 180, 220, 240])
        elif '30nm' in Prj_Name:
            ax.set_xticks([0, 15, 45, 75, 105, 135, 165, 180])
        elif '20nm' in Prj_Name:
            ax.set_xticks([0, 10, 30, 50, 70, 90, 110, 120])
        elif '50nm' in Prj_Name:
            ax.set_xticks([0, 25, 75, 125, 175, 225, 275, 300])

        if plot_type == 'occ':
            tick_locations = [-(10 ** -x) for x in range(7)] + [0.0] + [10 ** -x for x in reversed(range(7))]
        elif plot_type == 'dens':
            tick_locations = [-(10 ** x) for x in reversed(range(14, 21))] + [0.0] +\
                             [10 ** x for x in range(14, 21)]
        plt.colorbar(im, ticks=tick_locations, format='%0.e')
    return

if __name__ == '__main__':
    plot_multi(Prj_Name, Time_List, plot_type='dens', carrier='both')
    plt.show()