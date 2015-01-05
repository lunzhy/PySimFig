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
import QuickView.TwoDim.TrapOccupy as occ
import lib.format as fmt


main_prj = os.path.join(Directory_RTED2014, 'r_lowT')


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


def plotVthCompare(ax):
    # main_prj_name = 'm_sin'
    # prj_name = ['0.2', '0.3', '0.4']
    main_prj_name = 'f_t2b'
    prj_name = ['1e7', '1e8', '1e9']
    vfb_to_write = ()
    for prj in prj_name:
        prj_path = os.path.join(main_prj, main_prj_name, prj)
        time, vfb_left, vfb_center, vfb_right = comm.readVfbOfCells(prj_path)
        ax.plot(time, vfb_center, label=prj)
        vfb_to_write += (vfb_center, )
    vfb1, vfb2, vfb3 = vfb_to_write
    comm.write_data(Folder_Write_Data, time, vfb1, vfb2, vfb3)
    ax.set_xlim(1e3, 1e7)
    ax.set_xscale('log')
    ax.legend()
    return


def plot2D(fig, ax, par_name, par_value, time=1e8):
    prj_path = os.path.join(main_prj, par_name, par_value)
    im = occ.plotDensitySingleTime(ax, prj_path, time)
    cb = fig.colorbar(im, ax=ax, pad=0.05, aspect=15, extend='both')

    ax.set_xlabel('Bitline Direction (nm)')
    ax.set_ylabel('Radial Direction (nm)')
    ax.set_yticks([4, 5, 6, 7, 8, 9])
    ax.set_xticks([0, 80, 110, 190])

    fmt.set2DAxe(ax)

    fmt.setColorbar(cb, 24)
    cb.set_label('Trapped Electron Density ($\mathbf{cm^{-3}}$)', rotation=90, labelpad=10)
    cb.set_ticks([1e16, 1e17, 1e18, 1e19, 1e20])

    save_figure(fig, 'lowT_Dens')
    return


def main():
    fig = plt.figure()
    ax = fig.add_axes([0.15, 0.15, 0.8, 0.8])
    plot2D(fig, ax, 'm_sin', '0.4', 1e8)
    # plot2D(fig, ax, 'f_t2b', '1e9', 1e8)
    # plotVthCompare(ax)
    # plotVfbCurvatureEffect(ax)
    plt.show()
    return


if __name__ == '__main__':
    main()
