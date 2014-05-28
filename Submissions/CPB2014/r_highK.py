__author__ = 'lunzhy'
import os, sys
path = os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), os.pardir, os.pardir))
if not path in sys.path:
    sys.path.append(path)
from Submissions.CPB2014 import *
import matplotlib.pyplot as plt
import lib.common as comm
from QuikView.TwoDim import TrapOccupy as occ
import lib.format as fmt
from matplotlib.ticker import FuncFormatter


Main_path = os.path.join(Directory_CPB2014, 'ret_highK')


def to_simple(x, position):
    s = x / 1e19
    return int(s)


def to_scientific(x, position):
    s = x / 1e19
    return str(int(s)) + 'e19'


def plot2DOcc():
    plot_time = 1e6
    prj_path = os.path.join(Main_path, 'frequency', '1e12')
    fig = plt.figure()
    ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
    im = occ.plotOccSingleTime(ax, prj_path, plot_time)
    return


def plotVerticalCut():
    cut_pos = 95
    plot_time = 1e6
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


def plotCutsInThreePositions():
    time_to_plot = [1, 1e2, 1e4, 1e6, 1e7]
    prj_name = os.path.join('frequency', '1e11')
    prj_path = os.path.join(Main_path, prj_name)
    fig = plt.figure()
    ax = fig.add_axes([0, 0, 1, 1], projection='3d')
    # near tunnel oxide
    for index, time in enumerate(time_to_plot):

        trap_directory = os.path.join(prj_path, 'Trap')
        trap_file = comm.searchFilePathByTime(trap_directory, 'trap', time)
        x, y, dens, occ = comm.cutAlongXY(trap_file, 6, align='y')
        ax.plot(x, y, dens, lw=2.5, c=comm.getColor(index))

    # in the middle
    for index, time in enumerate(time_to_plot):
        trap_directory = os.path.join(prj_path, 'Trap')
        trap_file = comm.searchFilePathByTime(trap_directory, 'trap', time)
        x, y, dens, occ = comm.cutAlongXY(trap_file, 9, align='y')
        ax.plot(x, y, dens, lw=2.5, c=comm.getColor(index))

    # near block oxide
    for index, time in enumerate(time_to_plot):
        trap_directory = os.path.join(prj_path, 'Trap')
        trap_file = comm.searchFilePathByTime(trap_directory, 'trap', time)
        x, y, dens, occ = comm.cutAlongXY(trap_file, 12, align='y')
        ax.plot(x, y, dens, lw=2.5, c=comm.getColor(index))

    # ax.set_xlim3d(0, 100)
    # ax.set_ylim3d(4, 15)
    # ax.set_xlabel('BL direction (nm)', labelpad=50, linespacing=3.2)
    # ax.set_ylabel('Vertical direction (nm)')
    # ax.set_zlabel('Trapped electron density (1e19${cm^{-3}}$)')
    ax.set_zticks([1e19, 3e19, 5e19, 7e19])
    # ax.set_zticklabels([1e19, 3e19, 5e19, 7e19])
    zformatter = FuncFormatter(to_simple)
    ax.zaxis.set_major_formatter(zformatter)

    fmt.setAxesLabel(ax)
    # ax.set_zlabel('Trapped electron density (cm^-3)', labelpad=5)
    ax.view_init(25, -35)
    ax.dist = 10
    legend_text = ['%.es' % leg for leg in time_to_plot]
    legend = ax.legend(legend_text, loc='upper left', handlelength=3)
    fmt.setLegend(legend)

    return


def main():
    # plot2DOcc()
    plotLgEffect()
    # plotFrequencyEffect()
    # plotVerticalCut()
    # plotLateralCut()
    # plotCutsInThreePositions()
    plt.show()
    return


if __name__ == '__main__':
    main()
