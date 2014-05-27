__author__ = 'lunzhy'
import os, sys
path = os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), os.pardir, os.pardir))
if not path in sys.path:
    sys.path.append(path)
from Submissions.CPB2014 import *
import matplotlib.pyplot as plt
import lib.common as comm
from QuikView.TwoDim import TrapOccupy as occ


Main_path = os.path.join(Directory_CPB2014, 'ret_highK')


def plot2DOcc():
    plot_time = 1e6
    prj_path = os.path.join(Main_path, 'frequency', '1e12')
    fig = plt.figure()
    ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
    im = occ.plotOccSingleTime(ax, prj_path, plot_time)
    return


def plotVerticalCut():
    cut_pos = 95
    plot_time = 1e5
    prj_path = os.path.join(Main_path, 'frequency', '1e12')
    fig = plt.figure()
    ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
    file_path = comm.searchFilePathByTime(os.path.join(prj_path, 'Trap'), 'trap', plot_time)
    x, y, dens, occ = comm.cutAlongXY(file_path, cut_pos, align='x')
    ax.plot(y, dens)
    return


def plotLateralCut():
    cut_pos = 6
    plot_time = [1e2, 1e4, 1e8, 1e8]
    prj_path = os.path.join(Main_path, 'frequency', '1e12')
    fig = plt.figure()
    ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
    for time in plot_time:
        file_path = comm.searchFilePathByTime(os.path.join(prj_path, 'Trap'), 'trap', time)
        x, y, dens, occ = comm.cutAlongXY(file_path, cut_pos, align='y')
        ax.plot(x, dens)
    return


def plotLgEffect():
    prj_list = ['10', '20', '30', '40']
    fig = plt.figure()
    ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
    for index, prj in enumerate(prj_list):
        prj_path = os.path.join(Main_path, 'Lg', prj)
        time, vfb1, vfb2, vfb3 = comm.readVfbOfCells(prj_path)
        ax.plot(time, vfb2, color=comm.getColor(index))
    ax.set_xscale('log')
    return


def plotFrequencyEffect():
    prj_list = ['1e10', '1e11', '1e12']
    fig = plt.figure()
    ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
    for index, prj in enumerate(prj_list):
        prj_path = os.path.join(Main_path, 'frequency', prj)
        time, vfb1, vfb2, vfb3 = comm.readVfbOfCells(prj_path)
        ax.plot(time, vfb2, color=comm.getColor(index))
    ax.set_xscale('log')
    return


def main():
    # plot2DOcc()
    plotLgEffect()
    # plotFrequencyEffect()
    # plotVerticalCut()
    # plotLateralCut()
    plt.show()
    return


if __name__ == '__main__':
    main()
