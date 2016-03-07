#! /usr/bin/env python3
# -*- coding: utf-8 -*- 
__author__ = 'Lunzhy'
import os
import sys
import numpy as np
import scipy
path = os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), os.pardir, os.pardir))
if path not in sys.path:
    sys.path.append(path)
import lib.common as comm
from Submissions.CPB2015 import Directory_CPB2015
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
from matplotlib.colors import SymLogNorm

Colormap_Type = plt.cm.jet
Colormap_Type = plt.cm.RdYlBu


def get_condition(prj_name):
    splits = prj_name.split('_')
    trap_energy, pos = float(splits[0][1:]), float(splits[1][1:])
    return pos, trap_energy


def read_current(prj_path):
    current_folder = os.path.join(prj_path, 'Current')
    file_path = comm.searchFilePathByTime(current_folder, 'eTAT_', 1e7)
    x, y, curr = comm.read_data(file_path)
    current_density = curr[0]
    return current_density


def main():
    main_prj = os.path.join(Directory_CPB2015, 'ret_TAT_pos_energy')
    pos_list, trap_energy_list, curr_dens_list = [], [], []
    for prj_name in os.listdir(main_prj):
        if prj_name == 'sample':
            continue
        if 'txt' in prj_name:
            continue
        pos, trap_energy = get_condition(prj_name)
        prj_path = os.path.join(main_prj, prj_name)
        curr_dens = read_current(prj_path)
        pos_list.append(pos)
        trap_energy_list.append(trap_energy)
        curr_dens_list.append(curr_dens)
    comm.write_data(os.path.join(main_prj, 'ret_current_pos_energy.txt'), pos_list,
                    trap_energy_list, curr_dens_list)
    plot(pos_list, trap_energy_list, curr_dens_list)
    return None


def interpolate_data(x, y, values):
    xi, yi = np.linspace(min(x), max(x), 200), np.linspace(min(y), max(y), 200)
    grid_x, grid_y = np.meshgrid(xi, yi)
    grid_z = scipy.interpolate.griddata((x, y), values, (grid_x, grid_y), method='linear')
    return xi, yi, grid_z


def plot(pos, trap_energy, curr_dens):
    x, y, grid_z = interpolate_data(pos, trap_energy, curr_dens)
    fig = plt.figure()
    ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
    im = ax.imshow(grid_z, cmap=Colormap_Type, vmin=min(curr_dens), vmax=max(curr_dens),
                   origin='lower', extent=[min(x), max(x), min(y), max(y)], aspect='auto',
                   norm=LogNorm())
    plt.colorbar(im)
    plt.show()
    return


if __name__ == '__main__':
    main()