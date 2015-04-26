#! /usr/bin/env python3
# -*- coding: utf-8 -*- 
__author__ = 'Lunzhy'

# 2014.10.28 - 2014.10.29
# demonstrate the result of erase operation after implementing the hole effect in the simulation


import os, sys
path = os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), os.pardir))
if not path in sys.path:
    sys.path.append(path)
import matplotlib.pyplot as plt
import lib.common as cm

Project_Path = 'E:\PhD Study\SimCTM\SctmTest\HoleTunnelTest'
Project_Path = r'E:\PhD Study\Submissions\Journal2015\SctmData\Fitting\E_14V'


def plot_voltage_shift(ax):
    time, vfb = cm.read_vfb(Project_Path)
    ax.plot(time, vfb, marker='o')
    ax.set_xlim(1e-7, 1000)
    ax.set_xscale('log')
    return


def plot_current_density(ax):
    time_list, e_tunin_list, e_tunout_list, h_tunin_list, h_tunout_list = [], [], [], [], []
    current_path = os.path.join(Project_Path, 'Current')
    # for electron current
    tunnel_current_files = cm.getFiles(current_path, 'eCurr')
    for file in tunnel_current_files:
        time = cm.getTime(file)
        x, y, current, current_x, current_y = cm.cutAlignXY(file, 0, align='x')
        e_tunin, e_tunout = abs(current_y[-1]), abs(current_y[0])
        time_list.append(time)
        e_tunin_list.append(e_tunin)
        e_tunout_list.append(e_tunout)

    # for hole current
    tunnel_current_files = cm.getFiles(current_path, 'hCurr')
    for file in tunnel_current_files:
        time = cm.getTime(file)
        x, y, current, current_x, current_y = cm.cutAlignXY(file, 0, align='x')
        h_tunin, h_tunout = abs(current_y[0]), abs(current_y[-1])
        h_tunin_list.append(h_tunin)
        h_tunout_list.append(h_tunout)

    for index, data in enumerate([e_tunin_list, e_tunout_list, h_tunin_list, h_tunout_list]):
        ax.plot(time_list, data, marker=cm.getMarker(index))
    legend_label = ['e tunnel in', 'e tunnel out', 'h tunnel in', 'h tunnel out']
    ax.legend(legend_label, loc='lower left')
    ax.set_xlim(1e-7, 1)
    ax.set_yscale('log')
    ax.set_xscale('log')
    return


def plot_trap_dist(ax, plot_time):
    trap_folder = os.path.join(Project_Path, 'Trap')

    trap_file = cm.searchFilePathByTime(trap_folder, 'trapped', 0)
    x, y, etrap_init, eocc_init, htrap_init, hocc_init = cm.cutAlignXY(trap_file, 0, 'x')

    trap_file = cm.searchFilePathByTime(trap_folder, 'trapped', plot_time)
    x, y, etrapped, eocc_time, htrapped, hocc_time = cm.cutAlignXY(trap_file, 0, 'x')

    for index, data in enumerate([eocc_init, eocc_time, hocc_time]):
        ax.plot(y, data, marker=cm.getMarker(index))

    legend_label = ['initial trapped electrons', 'trapped electrons', 'trapped holes']
    ax.legend(legend_label, loc='center left')
    return


def plot_trap_net(ax, plot_time):
    trap_folder = os.path.join(Project_Path, 'Trap')

    trap_file = cm.searchFilePathByTime(trap_folder, 'trapped', plot_time)
    x, y_coord_list, etrapped, eocc, htrapped, hocc = cm.cutAlignXY(trap_file, 0, 'x')

    net_occ = [eo-ho for eo, ho in zip(eocc, hocc)]
    y_list, net_occ_list, sign_list = [], [], []

    prev_sign = True if net_occ[0] > 0 else False
    y_seg, occ_seg = [], []
    for y, occ in zip(y_coord_list, net_occ):
        curr_sign = True if occ > 0 else False
        if curr_sign is prev_sign:
            y_seg.append(y)
            occ_seg.append(abs(occ))
        else:
            y_list.append(y_seg)
            net_occ_list.append(occ_seg)
            sign_list.append(prev_sign)
            y_seg = []
            occ_seg = []
            y_seg.append(y)
            occ_seg.append(abs(occ))
        prev_sign = curr_sign
    y_list.append(y_seg)
    net_occ_list.append(occ_seg)
    sign_list.append(prev_sign)

    for index, (y_coords, net_occs, sign) in enumerate(zip(y_list, net_occ_list, sign_list)):
        if len(y_coords) == 1:
            y_coords += [y_list[index-1][-1]]
            net_occs += [net_occ_list[index-1][-1]]
        color = 'red' if sign is True else 'blue'
        ax.plot(y_coords, net_occs, color=color)
        ax.fill_between(y_coords, net_occs, 0, interpolate=True, color=color)
    # ax.legend(['negative', 'positive'])
    ax.set_xlim(min(y_coord_list), max(y_coord_list))
    return


def plot_density(ax, time_list, carrier_type='e'):
    dens_folder = os.path.join(Project_Path, 'Density')
    for index, time_to_plot in enumerate(time_list):
        if carrier_type is 'e':
            dens_file = cm.searchFilePathByTime(dens_folder, 'eDens', time_to_plot)
        elif carrier_type is 'h':
            dens_file = cm.searchFilePathByTime(dens_folder, 'hDens', time_to_plot)
        x, y, dens = cm.cutAlignXY(dens_file, 0, 'x')
        ax.plot(y, dens, color=cm.getColor(index), label=cm.getTimeLabel(dens_file)[1])
    ax.legend(loc='lower left')
    ax.set_yscale('log')
    ax.set_xlim(min(y), max(y))
    title = 'CB Electron Density' if carrier_type == 'e' else 'VB Hole Density'
    ax.set_title(title)
    return


def plot_band(ax, time_list):
    dens_folder = os.path.join(Project_Path, 'Band')
    for index, time_to_plot in enumerate(time_list):
        band_file = cm.searchFilePathByTime(dens_folder, 'band', time_to_plot)
        x, y, cb, vb = cm.cutAlignXY(band_file, 0, 'x')
        ax.plot(y, cb, color=cm.getColor(index), label=cm.getTimeLabel(band_file)[1])
        ax.plot(y, vb, color=cm.getColor(index), label=cm.getTimeLabel(band_file)[1])
    ax.legend(loc='lower right')
    ax.set_xlim(min(y), max(y))
    return


def main():

    fig_vfb = plt.figure()
    ax_vfb = fig_vfb.add_axes([0.1, 0.1, 0.85, 0.85])
    plot_voltage_shift(ax_vfb)

    fig_curr = plt.figure()
    ax_current_density = fig_curr.add_axes([0.1, 0.1, 0.85, 0.85])
    plot_current_density(ax_current_density)

    fig_trap = plt.figure()
    ax_trap = fig_trap.add_axes([0.1, 0.1, 0.85, 0.85])
    plot_trap_dist(ax_trap, plot_time=0.0001)

    fig_trap_net = plt.figure()
    ax_net = fig_trap_net.add_axes([0.1, 0.1, 0.85, 0.85])
    plot_trap_net(ax_net, plot_time=0.0001)

    fig_edens = plt.figure()
    timelist_to_plot = [1e-4, 1e-2, 1]
    ax_edens = fig_edens.add_axes([0.1, 0.1, 0.85, 0.85])
    plot_density(ax_edens, timelist_to_plot, carrier_type='e')

    fig_hdens = plt.figure()
    ax_hdens = fig_hdens.add_axes([0.1, 0.1, 0.85, 0.85])
    plot_density(ax_hdens, timelist_to_plot, carrier_type='h')

    timelist_to_plot = [1e-7]
    fig_band = plt.figure()
    ax_band = fig_band.add_axes([0.1, 0.1, 0.85, 0.85])
    plot_band(ax_band, timelist_to_plot)

    plt.show()
    return


if __name__ == '__main__':
    main()