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


main_prj = os.path.join(Directory_RTED2014, 'r_lowK')


def plotVfbCurvatureEffect(ax):
    prj_names = ['cylindrical', 'cartesian']
    for prj in prj_names:
        prj_path = os.path.join(main_prj, prj)
        time, vfb = comm.read_vfb(prj_path)
        ax.plot(time, vfb, label=prj)
    ax.set_xscale('log')
    ax.legend()
    return


def plotBandDiagram(ax):
    prj_names = ['cylindrical', 'cartesian']
    time_to_plot = 1e-8
    data_to_write = ()
    for prj in prj_names:
        file_to_plot = comm.searchFilePathByTime(os.path.join(main_prj, prj, 'Band'), 'band',
                                                 time_to_plot)
        dummy_x, y, cband, vband = comm.cutAlignXY(file_to_plot, 0, 'x')
        ax.plot(y, cband, label=prj)
        ax.plot(y, vband, label=prj)
        data_to_write += (cband, vband,)
    # ax.set_xlim(0, 3)
    # ax.set_ylim(-10, 2.5)
    ax.legend()
    cband, vband, cband2, vband2 = data_to_write
    comm.write_data(Folder_Write_Data, y, cband, vband, cband2, vband2)
    return


def main():
    fig = plt.figure()
    ax = fig.add_axes([0.15, 0.15, 0.8, 0.8])

    plotVfbCurvatureEffect(ax)
    plt.show()
    return


if __name__ == '__main__':
    main()
