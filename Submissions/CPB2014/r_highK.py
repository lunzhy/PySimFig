__author__ = 'lunzhy'
import os, sys
path = os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), os.pardir, os.pardir))
if not path in sys.path:
    sys.path.append(path)
from Submissions.CPB2014 import *
import matplotlib.pyplot as plt
import lib.common as comm
from QuickView.TwoDim import TrapOccupy as occ
import lib.format as fmt
from matplotlib.ticker import FuncFormatter
import matplotlib.gridspec as gridspec
import numpy as np

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
    plot_time = [1e2, 1e3, 1e5, 1e6, 1e7, 5e7, 1e8, 3e8]
    # prj_path = os.path.join(Main_path, 'frequency', '1e12')
    prj_path = os.path.join(Main_path, 'Lg', '40')
    fig = plt.figure()
    ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
    for index, time in enumerate(plot_time):
        file_path = comm.searchFilePathByTime(os.path.join(prj_path, 'Trap'), 'trap', time)
        x, y, dens, occ = comm.cutAlongXY(file_path, cut_pos, align='x')
        ax.plot(y, dens, color=comm.getColor(index))
    legend_labels = [str(time) for time in plot_time]
    legend = ax.legend(legend_labels)
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


def plotCompareTunnelOut():
    prj_list = ['10', '20', '30', '40']
    fig = plt.figure()
    ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
    for index, prj in enumerate(prj_list):
        prj_path = os.path.join(Main_path, 'Lg', prj)
        time, tun_subs_acc, tb_subs_acc, tun_gate_acc, subs_gate_acc = comm.readTunnelOut(prj_path)
        tunnel_out = [(tun_subs + tun_gate) / float(prj) for tun_subs, tun_gate in zip(tun_subs_acc, tun_gate_acc)]
        ax.plot(time, tunnel_out, color=comm.getColor(index))
    ax.set_xscale('log')
    ax.set_yscale('log')
    return


def plotTunnelOutVsRegion():
    prj_list = ['10', '20', '30', '40']
    fig = plt.figure()
    ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
    for index, prj in enumerate(prj_list):
        prj_path = os.path.join(Main_path, 'Lg', prj)

        time, total, main_per, others_per = comm.readChargeRegionwise(prj_path)
        others_per = [others - others_per[0] for others in others_per]
        main_per = [main_step / main_per[0] for main_step in main_per]
        # lateral_dens = [total_dens * percentage for total_dens, percentage in zip(total, others_per)]
        total_dens = total[-1]

        time, tun_subs_acc, tb_subs_acc, tun_gate_acc, subs_gate_acc = comm.readTunnelOut(prj_path, isAcc=True)
        tunnel_out = [(tun_subs + tun_gate) / total_dens for tun_subs, tun_gate in zip(tun_subs_acc, tun_gate_acc)]

        ax.plot(time, tunnel_out, color=comm.getColor(index))
        ax.plot(time, main_per, color=comm.getColor(index), marker='o')

    ax.set_xscale('log')
    return


def plotCompareChargeRegion():
    prj_list = ['10', '20', '30', '40']
    fig = plt.figure()
    ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
    for index, prj in enumerate(prj_list):
        prj_path = os.path.join(Main_path, 'Lg', prj)
        time, total, main_per, lateral = comm.readChargeRegionwise(prj_path)
        lateral = [other - lateral[0] for other in lateral]
        ax.plot(time, lateral, color=comm.getColor(index))
    ax.set_xscale('log')


def plotCutlines():
    time_to_plot = 1e8
    cutline = [95]
    prj_path = os.path.join(Main_path, 'Lg', '40')
    fig = plt.figure()
    gs = gridspec.GridSpec(2, 2, width_ratios=[1, 1])
    ax_band = fig.add_subplot(gs[:, 0])
    ax_trapped = fig.add_subplot(gs[0, 1])
    ax_free = fig.add_subplot(gs[1, 1])
    fig.subplots_adjust(hspace=0., wspace=0.05, right=0.86)

    # band
    plot_to_label = []
    y_extent = 100
    for index, cut_coord in enumerate(cutline):
        band_dir = os.path.join(prj_path, 'Band')
        file_path = comm.searchFilePathByTime(band_dir, 'band', time_to_plot)
        x, y, cb, vb = comm.cutAlongXY(file_path, coord_in_nm=cut_coord, align='x')
        y_extent = min(max(y), y_extent)
        pl, = ax_band.plot(y, cb, c=comm.getColor(index), lw=3)
        plot_to_label.append(pl)
        ax_band.plot(y, vb, comm.getColor(index), lw=3)

    labels = ["cut a-a'", "cut b-b'", "cut c-c'"]
    legend = ax_band.legend(plot_to_label, labels, loc='lower left', bbox_to_anchor=(0, 1.02, 1.7, 0.1),
                            ncol=3, borderaxespad=0., mode='expand')

    ax_band.set_xlim(0, y_extent - 0.1)
    ax_band.set_ylim(-7, 9)
    ax_band.set_yticks(np.arange(-7, 9, 3))
    ax_band.set_xlabel('Vertical Direction (nm)', labelpad=0)
    ax_band.set_ylabel('Band Energy (eV)', labelpad=0)
    fmt.setAxesLabel(ax_band, 22, 20)
    fmt.setAxesTicks(ax_band)
    fmt.setLegend(legend, 20)

    # trapped/free electron density
    min_x = 100
    max_x = 100
    for index, cut_pos in enumerate(cutline):
        trap_dir = os.path.join(prj_path, 'Trap')
        trap_file = comm.searchFilePathByTime(trap_dir, 'trap', time_to_plot)
        x, y, trapped, occ = comm.cutAlongXY(trap_file, cut_pos, 'x')
        min_x = min(min(y), min_x)
        max_x = min(max(y), max_x)
        ax_trapped.plot(y, trapped, lw=2, c=comm.getColor(index))

        edens_dir = os.path.join(prj_path, 'Density')
        edens_file = comm.searchFilePathByTime(edens_dir, 'eDens', time_to_plot)
        x, y, edens = comm.cutAlongXY(edens_file, cut_pos, 'x')
        ax_free.plot(y, edens, lw=2, c=comm.getColor(index))

    # ax_trapped
    ax_trapped.set_ylabel('Trapped\nElectrons ($\mathbf{cm^{-3}}$)', labelpad=10)
    ax_trapped.set_yticks([1e19, 3e19, 5e19, 7e19])
    ax_trapped.yaxis.tick_right()
    ax_trapped.yaxis.set_label_position('right')
    ax_trapped.yaxis.set_offset_position('right')
    ax_trapped.yaxis.set_label_coords(1.1, 0.6)
    ax_trapped.set_xticks([6, 8, 10, 12])
    ax_trapped.set_xticklabels([])
    fmt.setAxesLabel(ax_trapped, 22, 20)
    fmt.setAxesTicks(ax_trapped)
    offset_text = ax_trapped.yaxis.get_offset_text()
    if not offset_text is None:
        offset_text.set_size(18)

    # ax_free
    ax_free.set_ylim(1e1, 1e5)
    ax_free.set_yscale('log')
    ax_free.set_xlabel('Vertical Direction (nm)', labelpad=0)
    ax_free.set_ylabel('CB Electrons ($\mathbf{cm^{-3}}$)')
    ax_free.yaxis.tick_right()
    ax_free.yaxis.set_label_position('right')
    ax_free.set_yticks([1e1, 1e3, 1e5])
    ax_free.set_xticks([6, 8, 10, 12])
    fmt.setAxesLabel(ax_free, 22, 20)
    fmt.setAxesTicks(ax_free)
    return


def main():
    # plot2DOcc()
    plotLgEffect()
    # plotCompareTunnelOut()
    # plotCompareChargeRegion()
    plotTunnelOutVsRegion()
    # plotFrequencyEffect()
    # plotVerticalCut()
    # plotCutlines()
    # plotLateralCut()
    # plotCutsInThreePositions()
    plt.show()
    return


if __name__ == '__main__':
    main()
