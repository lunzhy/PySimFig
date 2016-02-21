__author__ = 'lunzhy'
import os, sys
path = os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), os.pardir, os.pardir))
if not path in sys.path:
    sys.path.append(path)
from Submissions.TED2014 import *
import matplotlib.pyplot as plt
import lib.common as comm
import lib.format as fmt


Main_path = os.path.join(Directory_TED2014, 'ret_tb_pf')


def plotCompareTwoMechanism():
    prj_list = ['330K', '360K', '380K', '400K']
    for index, prj in enumerate(prj_list):
        prj_path = os.path.join(Main_path, prj)
        time, tun_subs_acc, tb_subs_acc, tun_gate_acc, tb_gate_acc = comm.readTunnelOut()
    return


def plotCompareTbPf():
    fig = plt.figure()
    ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])

    prj_list = ['300K', '330K', '360K', '390K']
    time, tun_out, other_region = [], [], []
    for index, prj in enumerate(prj_list):
        prj_path = os.path.join(Main_path, prj)
        time, total, main_per, other_per = comm.readChargeRegionwise(prj_path)
        other_per = [per - other_per[0] for per in other_per]
        other_region = [total[0] * per for per in other_per]
        time, tun_subs, tb_subs, tun_gate, tb_gate = comm.readTunnelOut(prj_path)
        tb_acc = [t_s + t_g + tb_s + tb_g for t_s, t_g, tb_s, tb_g in zip(tun_subs, tb_subs, tun_gate, tb_gate)]
        ax.plot(time, other_region, lw=3)
        ax.plot(time, tun_out, lw=3, marker='o')
    ax.set_xscale('log')
    return


def plotLateralDiffusion():
    fig = plt.figure()
    ax = fig.add_axes([0.15, 0.15, 0.8, 0.8])
    prj_list = ['340K', '350K', '360K', '370K']
    time_to_plot = ['1e2', '1e4', '1e6', '1e8']

    for index, prj in enumerate(prj_list):
        prj_path = os.path.join(Main_path, prj)
        time, total, main_per, other_per = comm.readChargeRegionwise(prj_path)
        other_per = [per - other_per[0] for per in other_per]
        ax.plot(time, other_per, color=comm.getColor(index), marker=comm.getMarker(index), lw=3,
                markersize=14, markeredgecolor=comm.getColor(index), markevery=2)

    ax.set_xscale('log')
    ax.set_ylim(-0.02, 0.27)
    ax.set_yticks([0, 0.05, 0.1, 0.15, 0.20, 0.25])
    ax.set_xlim(1e2, 1e7)
    ax.set_xlabel(r'Retention time (s)')
    ax.set_ylabel(r'Ratio of lateral spreading')
    legend_label = [r'Temperature = %s K' % tem[:-1] for tem in prj_list]
    legend = ax.legend(legend_label, loc='upper left', numpoints=1)
    fmt.setAxesLabel(ax)
    fmt.setAxesTicks(ax)
    fmt.setLegend(legend)

    drawFig(fig, 'lateral_ratio')
    return


def plotTunnelOut():
    fig = plt.figure()
    ax = fig.add_axes([0.15, 0.15, 0.8, 0.8])
    prj_list = ['340K', '350K', '360K', '370K']
    time_to_plot = ['1e2', '1e4', '1e6', '1e8']

    for index, prj in enumerate(prj_list):
        prj_path = os.path.join(Main_path, prj)
        time, tun_subs, tb_subs, tun_gate, tb_gate = comm.readTunnelOut(prj_path, isAcc=True)
        tun_acc = [t_s + t_g + tb_s + tb_g for t_s, t_g, tb_s, tb_g in zip(tun_subs, tb_subs, tun_gate, tb_gate)]

        time, total, main_per, other_per = comm.readChargeRegionwise(prj_path)
        total_trap = total[0]

        tun_acc = [tun / total_trap for tun in tun_acc]
        ax.plot(time, tun_acc, color=comm.getColor(index), marker=comm.getMarker(index), lw=3,
                markersize=14, markeredgecolor=comm.getColor(index), markevery=2)

    ax.set_xscale('log')
    ax.set_ylim(-0.01, 0.09)
    ax.set_yticks([0, 0.02, 0.04, 0.06, 0.08])
    ax.set_xlim(1e2, 1e7)
    ax.set_xlabel(r'Retention time (s)')
    ax.set_ylabel(r'Ratio of tunneling out')
    legend_label = [r'Temperature = %s K' % tem[:-1] for tem in prj_list]
    legend = ax.legend(legend_label, loc='upper left', numpoints=1)
    fmt.setAxesLabel(ax)
    fmt.setAxesTicks(ax)
    fmt.setLegend(legend)

    drawFig(fig, 'tunnel_ratio')
    return



def main():
    # plotCompareTbPf()
    plotLateralDiffusion()
    plotTunnelOut()
    plt.show()
    return


if __name__ == '__main__':
    main()
