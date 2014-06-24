__author__ = 'lunzhy'
import os, sys
path = os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), os.pardir, os.pardir))
if not path in sys.path:
    sys.path.append(path)
from Submissions.CPB2014 import *
import matplotlib.pyplot as plt
import lib.common as comm


Main_path = os.path.join(Directory_CPB2014, 'ret_tb_pf')


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


def main():
    plotCompareTbPf()
    plt.show()
    return


if __name__ == '__main__':
    main()
