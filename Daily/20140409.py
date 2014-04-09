__author__ = 'Lunzhy'
import matplotlib.pyplot as plt
import os, sys
path = os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), '..'))
if not path in sys.path:
    sys.path.append(path)
import lib.common as comm
import numpy as np


Prj_name = 'ChargeBalanceTest'
woPF_largestep = 'woPF_largestep.txt'
woPF_smallstep = 'woPF_smallstep.txt'
wPF_smallstep = 'wPF_smallstep.txt'
wPF_largestep = 'wPF_largestep.txt'


def loadData(file_name):
    file_path = os.path.join(comm.Sctm_Test_Folder, Prj_name, file_name)
    data = np.loadtxt(file_path)
    time, line_dens = data[:, 0], data[:, 2]
    percent = [dens/line_dens[0] for dens in line_dens]
    return time, percent


def main():
    fig = plt.figure()
    ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])

    time, percent = loadData(wPF_smallstep)
    ax.plot(time, percent, lw=3, c='b', ls='--')

    time, percent = loadData(wPF_largestep)
    ax.plot(time, percent, lw=3, c='b')

    time, percent = loadData(woPF_smallstep)
    ax.plot(time, percent, lw=3, c='k', ls='--')

    time, percent = loadData(woPF_largestep)
    ax.plot(time, percent, lw=3, c='k')

    legend_labels = ['wPF LargeTimeStep', 'wPF SmallTimeStep', 'woPF LargeTimeStep', 'woPF SmallTimeStep']
    legend = ax.legend(legend_labels, loc='upper left')
    ax.set_xlabel('Retention Time (s)')
    ax.set_ylabel('Total Charge (normalized)')
    ax.set_xscale('log')
    ax.set_xlim(1e3, 1e7)
    return
if __name__ == '__main__':
    main()
    plt.show()