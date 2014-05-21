__author__ = 'lunzhy'
import os, sys, math
import numpy as np
import matplotlib.pyplot as plt
path = os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), os.pardir, os.pardir))
if not path in sys.path:
    sys.path.append(path)
from Submissions.SSDM2014 import *
import lib.common as comm

Exp_data = [(8.9871, 0.026087), (9.99355, 0.0652174), (11, 0.221739), (11.9871, 0.6), (12.9935, 1.23913),
            (13.9806, 1.91739), (14.9871, 2.59565), (15.9935, 3.26087), (16.9806, 3.83478), (18.0065, 4.34348),
            (18.9935, 4.77391), (20, 5.12609)]

Main_path = Directory_Ssdm2014
Main_prj = 'ispp_fitting'
Prj_name = 'demo'
TimeStep = 100e-6
EffStep_Ispp = [0] + list(np.arange(19, 11*20, 20))

def plotSim(ax):
    prj_path = os.path.join(Main_path, Main_prj, Prj_name)
    times, vfb_cell1, vfb_cell2, vfb_cell3 = comm.readVfbOfCells(prj_path)
    time_eff, vfb_eff = [], []
    for index, tup in enumerate(zip(times, vfb_cell2)):
        if index in EffStep_Ispp:
            time_eff.append(tup[0])
            vfb_eff.append(tup[1])
    voltage_eff = [8+index for index, tup in enumerate(time_eff)]
    print(voltage_eff)

    ax.plot(voltage_eff, vfb_eff, c='k', lw=3)
    return


def plotFitting():
    fig = plt.figure()
    ax = fig.add_axes([0.13, 0.17, 0.75, 0.75])

    ax.plot([exp[0] for exp in Exp_data], [exp[1] for exp in Exp_data], marker='o', ls='None', fillstyle='none',
            c='k', mec='k', ms=12, mew=3)

    plotSim(ax)

    return

if __name__ == '__main__':
    plotFitting()
    # plotSim()
    plt.show()