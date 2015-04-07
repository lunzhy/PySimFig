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
from Submissions.SNW2015 import *

Colormap_Type = plt.cm.jet

Prj_Name = 'program-bm'
Time_to_plot = 1e-6


def plot_occ(ax, prj_name, time):
    trap_folder_path = os.path.join(Directory_SNW2015, prj_name, comm.TrapDistr_Folder)
    file_path = comm.searchFilePathByTime(trap_folder_path, 'trapped', time)
    x, y, e_trap, e_occ, h_trap, h_occ = comm.readData2D(file_path, 1)

    vmin, vmax = 1e-4, 1.0
    log_norm = LogNorm()

    grid_z = comm.makeValueGridZ(x, y, e_occ)
    im = ax.imshow(grid_z, cmap=Colormap_Type, vmin=vmin, vmax=vmax, origin='lower',
                   extent=[min(x), max(x), min(y), max(y)], aspect='auto', norm=log_norm)
    return im


def plot_dens(ax, prj_name, time):
    trap_folder_path = os.path.join(Directory_SNW2015, prj_name, comm.Density_Folder)
    file_path = comm.searchFilePathByTime(trap_folder_path, 'eDens', time)
    x, y, edens = comm.readData2D(file_path, 1)

    vmin, vmax = 1e3, 1e9
    log_norm = LogNorm()

    grid_z = comm.makeValueGridZ(x, y, edens)
    im = ax.imshow(grid_z, cmap=Colormap_Type, vmin=vmin, vmax=vmax, origin='lower',
                   extent=[min(x), max(x), min(y), max(y)], aspect='auto', norm=log_norm)
    return im


def plot_vfb(ax, prj_name):
    time, vfb = comm.read_vfb(os.path.join(Directory_SNW2015, prj_name))
    ax.plot(time, vfb, marker='o')

    ax.set_xlim(1e-9, 1)
    ax.set_xscale('log')
    return


if __name__ == '__main__':
    fig = plt.figure()
    ax_occ = fig.add_axes([0.1, 0.1, 0.8, 0.8])
    im = plot_occ(ax_occ, Prj_Name, Time_to_plot)
    plt.colorbar(im)

    fig = plt.figure()
    ax_dens = fig.add_axes([0.1, 0.1, 0.8, 0.8])
    im = plot_dens(ax_dens, Prj_Name, Time_to_plot)
    plt.colorbar(im)

    fig = plt.figure()
    ax_vfb = fig.add_axes([0.1, 0.1, 0.8, 0.8])
    plot_vfb(ax_vfb, Prj_Name)

    plt.show()
