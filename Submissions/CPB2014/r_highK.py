__author__ = 'lunzhy'
import os, sys
path = os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), os.pardir, os.pardir))
if not path in sys.path:
    sys.path.append(path)
from Submissions.CPB2014 import *
import matplotlib.pyplot as plt
import lib.common as comm
from QuickView.TwoDim import TrapOccupy as occ
from QuickView.TwoDim import eDensity as edens
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


def to_scientific_math(x, position):
    s = x / 1e19
    return r'$\mathbf{%s\times10^{%s}%s}$' % (s, '19')


def plot2DOcc():
    plot_time = 1e8
    prj_path = os.path.join(Main_path, 'frequency', '1e12')
    fig = plt.figure()
    ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
    im = occ.plotDensitySingleTime(ax, prj_path, plot_time)
    cb = fig.colorbar(im, ax=ax, pad=0.05, aspect=15, extend='both')

    ax.set_xlabel('Bitline Direction (nm)')
    ax.set_ylabel('Vertical Direction (nm)')
    ax.set_yticks([6, 7, 8, 9, 10, 11, 12])
    ax.set_xticks([0, 80, 110, 190])

    fmt.set2DAxe(ax)
    fmt.setColorbar(cb, 24)
    cb.set_label('Trapped Electron Density ($\mathbf{cm^{-3}}$)', rotation=90, labelpad=10)
    cb.set_ticks([1e16, 1e17, 1e18, 1e19, 1e20])

    return


def plot2DDensity():
    plot_time = 5e7
    prj_path = os.path.join(Main_path, 'frequency', '1e12')
    fig = plt.figure()
    ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
    im = edens.plotEdensSingleTime(ax, prj_path, plot_time, vmin=1e1, vmax=1e5)
    cb = fig.colorbar(im, ax=ax, pad=0.05, aspect=15, extend='both')
    ax.set_xlabel('Bitline Direction (nm)')
    ax.set_ylabel('Vertical Direction (nm)')
    ax.set_yticks([6, 7, 8, 9, 10, 11, 12])
    ax.set_xticks([0, 80, 110, 190])
    fmt.set2DAxe(ax)
    fmt.setColorbar(cb, 24)
    cb.set_label('Free Electron Density ($\mathbf{cm^{-3}}$)', rotation=90, labelpad=10)
    cb.set_ticks([1e1, 1e2, 1e3, 1e4, 1e5, 1e6])
    return


def plotVerticalCut():
    cut_pos = 95
    # plot_time = ['1e2', '1e3', '1e5', '1e6', '1e7', '5e7', '1e8', '3e8']
    plot_time = ['1e3', '1e4', '1e5', '1e7', '1e8']
    # plot_time = ['1e3']
    # prj_path = os.path.join(Main_path, 'frequency', '1e12')
    prj_path = os.path.join(Main_path, 'Lg', '10')
    fig = plt.figure()
    ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
    for index, time in enumerate(plot_time):
        if isinstance(time, str):
            time = float(time)
        file_path = comm.searchFilePathByTime(os.path.join(prj_path, 'Trap'), 'trap', time)
        x, y, dens, occ = comm.cutAlongXY(file_path, cut_pos, align='x')
        ax.plot(y, dens, color=comm.getColor(index))

    legend_labels = [str(time) for time in plot_time]
    legend_labels = fmt.setLegendLabelExp(legend_labels, 's')
    legend = ax.legend(legend_labels)

    fmt.setAxesLabel(ax)
    fmt.setAxesTicks(ax)
    fmt.setLegend(legend)
    return


def plotLateralCut():
    cut_pos = 6
    lg_length = 40
    plot_time = ['1e2', '1e4', '1e6', '1e7', '1e8']
    prj_path = os.path.join(Main_path, 'frequency', '1e12')
    prj_path = os.path.join(Main_path, 'Lg', str(lg_length))
    fig = plt.figure()
    ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
    for index, time in enumerate(plot_time):
        if isinstance(time, str):
            time = float(time)
        file_path = comm.searchFilePathByTime(os.path.join(prj_path, 'Trap'), 'trap', time)
        x, y, dens, occ = comm.cutAlongXY(file_path, cut_pos, align='y')
        ax.plot(x, dens, color=comm.getColor(index), lw=4)

    start = 0
    middle = 20 + lg_length + 30 + lg_length / 2
    end = middle * 2
    start_cell2 = 20 + lg_length + 30
    end_cell2 = start_cell2 + lg_length

    ax.set_xlim(0, end)
    ax.set_ylim(0, 4e19)
    ax.set_xticks([0, start_cell2, end_cell2, end])

    ax.set_xlabel('Bitline Direction (nm)')
    ax.set_ylabel('Threshold Voltage Shift (V)')
    legend_labels = [str(time) for time in plot_time]
    legend_labels = fmt.setLegendLabelExp(legend_labels, 's')
    legend = ax.legend(legend_labels)

    fmt.setAxesLabel(ax)
    fmt.setAxesTicks(ax)
    fmt.setLegend(legend)

    return


def plotLgEffect():
    prj_list = ['10', '20', '30', '40']
    fig = plt.figure()
    ax = fig.add_axes([0.15, 0.15, 0.8, 0.8])
    for index, prj in enumerate(prj_list):
        prj_path = os.path.join(Main_path, 'Lg', prj)
        time, vfb1, vfb2, vfb3 = comm.readVfbOfCells(prj_path)
        ax.plot(time, vfb2, color=comm.getColor(index), lw=4)
    ax.set_xscale('log')
    ax.set_xlim(1e2, 1e8)
    #ax.set_xticks([])
    ax.set_xlabel(r'Retention Time (s)')
    ax.set_ylabel(r'Threshold Voltage Shift (V)')
    legend_label = [r'$Lg = %snm$' % lg for lg in prj_list]
    legend = ax.legend(legend_label, loc='lower left')
    fmt.setAxesLabel(ax)
    fmt.setAxesTicks(ax)
    fmt.setLegend(legend)
    return


def plotFrequencyEffect():
    prj_list = ['1e10', '1e11', '1e12']
    fig = plt.figure()
    ax = fig.add_axes([0.15, 0.15, 0.8, 0.8])
    for index, prj in enumerate(prj_list):
        prj_path = os.path.join(Main_path, 'frequency', prj)
        time, vfb1, vfb2, vfb3 = comm.readVfbOfCells(prj_path)
        ax.plot(time, vfb2, color=comm.getColor(index), lw=4)

    ax.set_xscale('log')
    ax.set_xlim(1e3, 3e8)
    ax.set_ylim(4.0, 5.6)
    ax.set_yticks([4.0, 4.4, 4.8, 5.2, 5.6])
    ax.set_xlabel(r'Retention Time (s)')
    ax.set_ylabel('Threshold Voltage Shift (V)')

    labels = []
    for label in prj_list:
        superscript = label[2:]
        labels.append(r'$\mathbf{1\times10^{%s}Hz}$' % superscript)
    legend = ax.legend(labels, loc='lower left')

    fmt.setAxesLabel(ax)
    fmt.setAxesTicks(ax)
    fmt.setLegend(legend)

    return


def plotCutsInThreePositions():
    cut_tunnel = 6
    cut_block = 12
    cut_middle = 9
    time_to_plot = ['1', '1e3', '1e4', '1e5', '1e6', '1e7']
    prj_name = os.path.join('frequency', '1e11')
    prj_path = os.path.join(Main_path, prj_name)
    fig = plt.figure()
    ax = fig.add_axes([0, 0, 1, 1], projection='3d')
    # near tunnel oxide
    for index, time in enumerate(time_to_plot):
        time = float(time)
        trap_directory = os.path.join(prj_path, 'Trap')
        trap_file = comm.searchFilePathByTime(trap_directory, 'trap', time)
        x, y, dens, occ = comm.cutAlongXY(trap_file, cut_tunnel, align='y')
        ax.plot(x, y, dens, lw=2.5, c=comm.getColor(index))

    # in the middle
    for index, time in enumerate(time_to_plot):
        time = float(time)
        trap_directory = os.path.join(prj_path, 'Trap')
        trap_file = comm.searchFilePathByTime(trap_directory, 'trap', time)
        x, y, dens, occ = comm.cutAlongXY(trap_file, cut_middle, align='y')
        ax.plot(x, y, dens, lw=2.5, c=comm.getColor(index))

    # near block oxide
    for index, time in enumerate(time_to_plot):
        time = float(time)
        trap_directory = os.path.join(prj_path, 'Trap')
        trap_file = comm.searchFilePathByTime(trap_directory, 'trap', time)
        x, y, dens, occ = comm.cutAlongXY(trap_file, cut_block, align='y')
        ax.plot(x, y, dens, lw=2.5, c=comm.getColor(index))

    ax.set_xlim3d(0, 190)
    # ax.set_ylim3d(4, 15)
    # ax.set_xlabel('BL direction (nm)', labelpad=50, linespacing=3.2)
    # ax.set_ylabel('Vertical direction (nm)')
    # ax.set_zlabel('Trapped electron density (1e19${cm^{-3}}$)')
    # ax.set_xlim3d(50, 140)
    ax.set_xticks([0, 80, 110, 190])
    ax.set_zticks([1e19, 3e19, 5e19])
    # ax.set_zticklabels([1e19, 3e19, 5e19, 7e19])
    zformatter = FuncFormatter(to_simple)
    ax.zaxis.set_major_formatter(zformatter)

    fmt.setAxesLabel(ax)
    # ax.set_zlabel('Trapped electron density (cm^-3)', labelpad=5)
    ax.view_init(25, -55)
    ax.dist = 10
    # legend_text = ['%.es' % leg for leg in time_to_plot]
    legend_text = fmt.setLegendLabelExp(time_to_plot, 's')
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


def plotLateralByLg():
    plot_time = ['1e2', '1e4', '1e6', '1e8']
    cut_pos = 6
    main_prj_path = os.path.join(Main_path, 'Lg')
    lg_list = [20, 30, 40]
    prj_path_a = os.path.join(main_prj_path, str(lg_list[0]))
    prj_path_b = os.path.join(main_prj_path, str(lg_list[1]))
    prj_path_c = os.path.join(main_prj_path, str(lg_list[2]))
    prj_path_list = [prj_path_a, prj_path_b, prj_path_c]
    fig = plt.figure()
    ax_lg_a = fig.add_subplot(3, 1, 1)
    ax_lg_b = fig.add_subplot(3, 1, 2)
    ax_lg_c = fig.add_subplot(3, 1, 3)
    ax_lg_list = [ax_lg_a, ax_lg_b, ax_lg_c]
    fig.subplots_adjust(hspace=0., wspace=0.05, right=0.86)
    ax_lg_a.set_xticklabels([])
    ax_lg_b.set_xticklabels([])

    for prj_path, ax_lg in zip(prj_path_list, ax_lg_list):
        for index, time in enumerate(plot_time):
            file_path = comm.searchFilePathByTime(os.path.join(prj_path, 'Trap'), 'trap', time)
            x, y, dens, occ = comm.cutAlongXY(file_path, cut_pos, align='y')
            ax_lg.plot(x, occ, color=comm.getColor(index), lw=4)


    for lg, ax_lg in zip(lg_list, ax_lg_list):
        diff = 20 * 2 + 30 * 2 + lg * 3
        end = (diff + 220) / 2
        start = - (220 - end)
        ax_lg.set_xlim(start, end)
        ax_lg.set_ylim(0, 0.8)
        # ax_lg.set_yticks([1e19, 2e19, 3e19])
        ax_lg.set_yticks([0.2, 0.4, 0.6])


    for ax_lg in ax_lg_list[:-1]:
        ax_lg.set_xticks([])

    # ax_lg_c.set_xticks([0, 55, 110, 165, 220])
    # ax_lg_c.set_xticklabels([-110, -55, 0, 55, 110])

    #ax_lg_c.set_xticklabels([0, 55, 110, 165, 220])
    for ax_lg in ax_lg_list:
        fmt.setAxesLabel(ax_lg)
        fmt.setAxesTicks(ax_lg)

    ax_lg_b.set_ylabel('Trap Occupation')
    ax_lg_c.set_xlabel('Bitline Direction (nm)')

    legend_text = fmt.setLegendLabelExp(plot_time, 's')
    legend = ax_lg_a.legend(legend_text, loc='upper right',
                            ncol=1, borderaxespad=0.)
    fmt.setLegend(legend, font_size=18)
    return


def main():
    ##plot2DOcc()
    #plotLgEffect()
    # plotCompareTunnelOut()
    # plotCompareChargeRegion()
    # plotTunnelOutVsRegion()
    # plotFrequencyEffect()
    # plotVerticalCut()
    # plotCutlines()
    # plotLateralCut()
    plotLateralByLg()
    ##plotCutsInThreePositions()
    #plot2DDensity()
    plt.show()
    return


if __name__ == '__main__':
    main()
