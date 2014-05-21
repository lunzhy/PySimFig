__author__ = 'lunzhy'
import os, sys
path = os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), os.pardir, os.pardir))
if not path in sys.path:
    sys.path.append(path)
from Submissions.CPB2014 import *
import matplotlib.pyplot as plt
import lib.common as comm

Main_path = Directory_CPB2014
Main_prj = r'ret_lowK'

Emass_list = ['0.1', '0.2', '0.3']
Frequency_list = ['1e7', '1e8', '1e10']


def plotVth(prj_name, prj_list):
    fig = plt.figure()
    ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])

    for index, prj in enumerate(prj_list):
        prj_path = os.path.join(Main_path, Main_prj, prj_name, prj)
        time, vfb1, vfb2, vfb3 = comm.readVfbOfCells(prj_path)
        ax.plot(time, vfb2, color=comm.getColor(index), lw=3)

    ax.set_xscale('log')
    return ax


def main():
    ax = plotVth('SiN', Emass_list)
    ax2 = plotVth('frequency', Frequency_list)
    plt.show()


if __name__ == '__main__':
    main()