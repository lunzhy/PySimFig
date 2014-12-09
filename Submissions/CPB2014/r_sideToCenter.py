__author__ = 'lunzhy'
import os, sys
path = os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), os.pardir, os.pardir))
if not path in sys.path:
    sys.path.append(path)
from Submissions.CPB2014 import *
import matplotlib.pyplot as plt
import lib.common as comm
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import lib.format as fmt

Main_prj = 'ret_400K_sideToCenter'
Main_path = os.path.join(Directory_CPB2014, Main_prj)


def plotLsDiffEffect():
    fig = plt.figure()
    ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
    length_spacer = ['10', '20', '30', '40']
    for length in length_spacer:
        prj_name = 'Ls%s_Lg10' % length
        prj_path = os.path.join(Main_path, prj_name)
        time, vfb1, vfb2, vfb3 = comm.readVfbOfCells(prj_path)
        ax.plot(time, vfb1)
        ax.plot(time, vfb2)
        ax.set_xscale('log')
    return


def plotVfbSideCenter():
    fig = plt.figure()
    ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
    ls_lg_pair = [(20, 10), (20, 20), (20, 30)]
    for index, ls_lg in enumerate(ls_lg_pair):
        prj_name = 'Ls%s_Lg%s' % ls_lg
        prj_path = os.path.join(Main_path, prj_name)
        time, vfb1, vfb2, vfb3 = comm.readVfbOfCells(prj_path)
        ax.plot(time, vfb1, color=comm.getColor(index))
        ax.plot(time, vfb2, color=comm.getColor(index))
        ax.set_xscale('log')
    return


def plotLsLg3D():
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ls_length = [10, 20, 30, 40, 50]
    lg_length = [10, 20, 30, 40, 50]
    x_ls, y_lg = np.meshgrid(ls_length, lg_length)
    deltaVth = []
    # x for ls, y for lg
    for ls in ls_length:
        dvth_ls = []
        for lg in lg_length:
            prj_name = 'Ls%s_Lg%s' % (ls, lg)
            prj_path = os.path.join(Main_path, prj_name)
            time, vfb1, vfb2, vfb3 = comm.readVfbOfCells(prj_path)
            dvth = vfb2[-1]
            dvth_ls += [dvth]
        deltaVth.append(dvth_ls)
    surf = ax.plot_surface(x_ls, y_lg, deltaVth)
    return


def plotLsLg2D():
    fig = plt.figure()
    ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
    ls_length = [10, 20, 30]
    lg_length = [10, 20, 30]
    # x for ls, y for lg
    for lg in lg_length:
        dvth_list = []
        for ls in ls_length:
            prj_name = 'Ls%s_Lg%s' % (ls, lg)
            prj_path = os.path.join(Main_path, prj_name)
            time, vfb1, vfb2, vfb3 = comm.readVfbOfCells(prj_path)
            dvth = vfb2[-1]
            dvth_list.append(dvth)
        ax.plot(ls_length, dvth_list, lw=3)
    ax.set_xlim(10, 30)
    return


def plotLateralCut():
    fig = plt.figure()
    ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
    plot_time = ['1e2', '1e4', '1e6', '1e7', '5e7']
    cut_pos = 9
    prj_path = os.path.join(Main_path, 'Ls30_Lg20')
    for index, time in enumerate(plot_time):
        if isinstance(time, str):
            time = float(time)
        file_path = comm.searchFilePathByTime(os.path.join(prj_path, 'Trap'), 'trap', time)
        x, y, dens, occ = comm.cutAlignXY(file_path, cut_pos, align='y')
        ax.plot(x, dens, color=comm.getColor(index), lw=4)
    return


def plotFinalLateralCut():
    fig = plt.figure()
    ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
    plot_time, cut_pos = 3e8, 9
    # prj_name = ['Ls30_Lg10', 'Ls30_Lg20', 'Ls30_Lg30']
    prj_name = ['Ls30_Lg20', 'Ls30_Lg30']
    ls_length = 30
    for index, prj in enumerate(prj_name):
        lg_length = float(prj[-2:])
        off_set = (30 - lg_length) * 1.5
        prj_path = os.path.join(Main_path, prj)
        file_path = comm.searchFilePathByTime(os.path.join(prj_path, 'Trap'), 'trap', plot_time)
        x, y, dens, occ = comm.cutAlignXY(file_path, cut_pos, align='y')
        x = [x_bit + off_set for x_bit in x]
        ax.plot(x, dens, color=comm.getColor(index), lw=4)

    legend_labels = ['Channel = 20nm', 'Channel = 30nm']
    legend = ax.legend(legend_labels, loc='upper center')
    fmt.setAxesLabel(ax)
    fmt.setAxesTicks(ax)
    fmt.setLegend(legend)

    drawFig(fig, 'lateral_cut')
    return



def main():
    # plotLsDiffEffect()
    # plotLsLg3D()
    # plotLsLg2D()
    # plotVfbSideCenter()
    # plotLateralCut()
    plotFinalLateralCut()
    plt.show()
    return


if __name__ == '__main__':
    main()
