#! /usr/bin/env python3
# -*- coding: utf-8 -*- 
__author__ = 'Lunzhy'
import matplotlib.pyplot as plt
import os, sys
path = os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), '..'))
if not path in sys.path:
    sys.path.append(path)
import lib.common as cm
from matplotlib.colors import LogNorm

Project_Path = 'E:\PhD Study\SimCTM\SctmTest\HoleTunnelTest'
Temp_Data_File = os.path.join(Project_Path, 'data.txt')


def get_time_constant(prj_path, plot_time):
    file_time_constant = cm.searchFilePathByTime(os.path.join(prj_path, 'Trap'),
                                                 'timeTAT', plot_time)
    y, cap_time, emi_time, occ = cm.cutAlignX_1D(file_time_constant)
    cm.write_data(Temp_Data_File, y, cap_time, emi_time, occ)
    return


def get_trap_occupy(prj_path, plot_time):
    file_plot = cm.searchFilePathByTime(os.path.join(prj_path, 'Trap'), 'eTrapped', plot_time)
    y, dens, occ = cm.cutAlignX_1D(file_plot)
    cm.write_data(Temp_Data_File, y, occ)
    return


def plot_time_constant(prj_path, plot_time):
    file_time_constant = cm.searchFilePathByTime(os.path.join(prj_path, 'Trap'),
                                                 'timeTAT', plot_time)
    x, y, cap_time, emi_time, occ = cm.readData2D(file_time_constant, skip=1)

    value_to_plot = 1 / (cap_time + emi_time)
    value_to_plot = occ

    grid_z = cm.makeValueGridZ(x, y, value_to_plot)
    vmin, vmax = min(value_to_plot), max(value_to_plot)
    print(vmin, vmax)
    fig = plt.figure()
    ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])

    im = ax.imshow(grid_z, cmap=plt.cm.jet, vmin=vmin, vmax=vmax, origin='lower',
                   extent=[min(x), max(x), min(y), max(y)], aspect='auto')

    cb = fig.colorbar(im, ax=ax)
    return im


def main():
    plot_time_constant(Project_Path, '1e-5')
    # get_trap_occupy(Project_Path, '1e8')
    return


if __name__ == '__main__':
    main()
    plt.show()
    # get_time_constant(Project_Path, '1e-9')