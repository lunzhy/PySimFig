#! /usr/bin/env python3
# -*- coding: utf-8 -*- 
import os, sys
path = os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), os.pardir, os.pardir))
if not path in sys.path:
    sys.path.append(path)
from Submissions.R_TED2014 import *
import matplotlib.pyplot as plt
import lib.common as comm
import lib.format as fmt


Main_path = os.path.join(Directory_RTED2014, 'r_temperature')


def plot_lateral_diffusion():
    fig = plt.figure()
    ax = fig.add_axes([0.15, 0.15, 0.8, 0.8])
    prj_list = ['340', '350', '360', '370']
    time_to_plot = ['1e2', '1e4', '1e6', '1e8']

    data_to_write = ()
    for index, prj in enumerate(prj_list):
        prj_path = os.path.join(Main_path, prj)
        time, total, main_per, other_per = comm.readChargeRegionwise(prj_path)
        other_per = [per - other_per[0] for per in other_per]
        ax.plot(time, other_per, color=comm.getColor(index), lw=4)
        data_to_write += (other_per, )

    ax.set_xscale('log')
    ax.set_ylim(-0.02, 0.35)
    ax.set_yticks([0, 0.05, 0.1, 0.15, 0.20, 0.25])
    ax.set_xlim(1e2, 1e7)
    ax.set_xlabel(r'Retention Time (s)')
    ax.set_ylabel(r'Ratio of Lateral Spreading')
    legend_label = [r'Temperature = %s' % tem for tem in prj_list]
    legend = ax.legend(legend_label, loc='upper left')
    fmt.setAxesLabel(ax)
    fmt.setAxesTicks(ax)
    fmt.setLegend(legend)

    data1, data2, data3, data4 = data_to_write
    comm.write_data(Folder_Write_Data, time, data1, data2, data3, data4)
    return


def plot_tunnel_out():
    main_prj_path = os.path.join(r'E:\PhD Study\Submissions\TED2014\SctmData', 'ret_tb_pf')
    fig = plt.figure()
    ax = fig.add_axes([0.15, 0.15, 0.8, 0.8])
    prj_list = ['340', '350', '360', '370']
    time_to_plot = ['1e2', '1e4', '1e6', '1e8']

    data_to_write = ()
    for index, prj in enumerate(prj_list):
        prj_path = os.path.join(main_prj_path, prj)
        time, tun_subs, tb_subs, tun_gate, tb_gate = comm.readTunnelOut(prj_path, isAcc=True)
        tun_acc = [t_s + t_g + tb_s + tb_g for t_s, t_g, tb_s, tb_g in zip(tun_subs, tb_subs, tun_gate, tb_gate)]

        time, total, main_per, other_per = comm.readChargeRegionwise(prj_path)
        total_trap = total[0]

        tun_acc = [tun / total_trap for tun in tun_acc]
        ax.plot(time, tun_acc, color=comm.getColor(index), lw=4)
        data_to_write += (tun_acc, )

    ax.set_xscale('log')
    ax.set_ylim(-0.01, 0.09)
    ax.set_yticks([0, 0.02, 0.04, 0.06, 0.08])
    ax.set_xlim(1e2, 1e7)
    ax.set_xlabel(r'Retention Time (s)')
    ax.set_ylabel(r'Ratio of Tunneling Out')
    legend_label = [r'Temperature = %s' % tem for tem in prj_list]
    legend = ax.legend(legend_label, loc='upper left')
    fmt.setAxesLabel(ax)
    fmt.setAxesTicks(ax)
    fmt.setLegend(legend)

    data1, data2, data3, data4 = data_to_write
    comm.write_data(Folder_Write_Data, time, data1, data2, data3, data4)
    return


def main():
    # plot_lateral_diffusion()
    plot_tunnel_out()
    plt.show()


if __name__ == '__main__':
    main()