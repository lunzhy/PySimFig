#! /usr/bin/env python3
# -*- coding: utf-8 -*- 
import os, sys
path = os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), os.pardir, os.pardir))
if not path in sys.path:
    sys.path.append(path)
from Submissions.R_TED2014 import *
import matplotlib.pyplot as plt
import lib.common as comm
from QuickView.TwoDim import TrapOccupy as occ
from QuickView.TwoDim import eDensity as edens
import lib.format as fmt
from matplotlib.ticker import FuncFormatter
import matplotlib.gridspec as gridspec
import numpy as np

Main_path = os.path.join(Directory_RTED2014, 'Lg', 'PF1e12')


def plot_vth_lg():
    prj_list = ['10', '20', '30', '40', '50']
    fig = plt.figure()
    ax = fig.add_axes([0.15, 0.15, 0.8, 0.8])
    for index, prj in enumerate(prj_list):
        prj_path = os.path.join(Main_path, prj)
        time, vfb1, vfb2, vfb3 = comm.readVfbOfCells(prj_path)
        ax.plot(time, vfb2, color=comm.getColor(index), lw=4)
    ax.set_xscale('log')
    ax.set_xlim(1e2, 1e8)
    ax.set_ylim(3.5, 5.5)
    #ax.set_xticks([])
    ax.set_xlabel(r'Retention Time (s)')
    ax.set_ylabel(r'Threshold Voltage Shift (V)')
    legend_label = [r'$Lg = %snm$' % lg for lg in prj_list]
    legend = ax.legend(legend_label, loc='lower left')
    fmt.setAxesLabel(ax)
    fmt.setAxesTicks(ax)
    fmt.setLegend(legend)

    return


def plot_lateral_by_lg():
    plot_time = ['1e2', '1e5', '1e6', '1e8']
    cut_pos = 9
    main_prj_path = Main_path
    lg_list = [20, 30, 40, 50]
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
            file_path = comm.searchFilePathByTime(os.path.join(prj_path, 'Trap'), 'eTrap', time)
            x, y, dens, occ = comm.cutAlignXY(file_path, cut_pos, align='y')
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


def plot_vertical_by_lg():
    ls_length = 30
    ls_length_edge = 20
    plot_time = ['1e2', '1e3', '1e4', '1e5', '1e6', '1e7']
    main_prj_path = Main_path
    lg_list = [20, 30, 40, 50]
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

    for prj_path, ax_lg, lg_length in zip(prj_path_list, ax_lg_list, lg_list):
        cut_pos = ls_length_edge + lg_length + ls_length + lg_length / 2
        for index, time in enumerate(plot_time):
            if isinstance(time, str):
                time = float(time)
            file_path = comm.searchFilePathByTime(os.path.join(prj_path, 'Trap'), 'eTrap', time)
            x, y, dens, occ = comm.cutAlignXY(file_path, cut_pos, align='x')
            ax_lg.plot(y, occ, color=comm.getColor(index), lw=4)


    for ax_lg in ax_lg_list[:-1]:
        ax_lg.set_xticks([])

    for ax_lg in ax_lg_list:
        ax_lg.set_ylim(0.3, 0.7)
        # ax_lg.set_yticks([1e19, 2e19, 3e19])
        ax_lg.set_yticks([0.4, 0.5, 0.6])
        fmt.setAxesLabel(ax_lg)
        fmt.setAxesTicks(ax_lg)

    ax_lg_b.set_ylabel('Trap Occupation')
    ax_lg_c.set_xlabel('Vertical Direction (nm)')

    legend_text = fmt.setLegendLabelExp(plot_time, 's')
    legend = ax_lg_a.legend(legend_text, loc='upper center',
                            ncol=2, borderaxespad=0.)
    fmt.setLegend(legend, font_size=18)
    return


def plot_vertical_cut():
    lg_length = 20
    ls_length = 30
    ls_length_edge = 20
    cut_pos = ls_length_edge + lg_length + ls_length + lg_length / 2
    ####################### cut position need be optimized ###############
    # plot_time = ['1e2', '1e3', '1e5', '1e6', '1e7', '5e7', '1e8', '3e8']
    plot_time = ['1e2', '1e3', '1e4', '1e5']
    # plot_time = ['1e3']
    # prj_path = os.path.join(Main_path, 'frequency', '1e12')
    prj_path = os.path.join(Main_path, str(lg_length))
    fig = plt.figure()
    ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
    for index, time in enumerate(plot_time):
        if isinstance(time, str):
            time = float(time)
        file_path = comm.searchFilePathByTime(os.path.join(prj_path, 'Trap'), 'trap', time)
        x, y, dens, occ = comm.cutAlignXY(file_path, cut_pos, align='x')
        ax.plot(y, dens, color=comm.getColor(index))

    legend_labels = [str(time) for time in plot_time]
    legend_labels = fmt.setLegendLabelExp(legend_labels, 's')
    legend = ax.legend(legend_labels)

    ax.set_ylim(1.5e19, 3.8e19)
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
        x, y, dens, occ = comm.cutAlignXY(file_path, cut_pos, align='y')
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


def main():
    plot_vth_lg()
    plot_lateral_by_lg()
    plot_vertical_by_lg()
    plt.show()
    return


if __name__ == '__main__':
    main()
