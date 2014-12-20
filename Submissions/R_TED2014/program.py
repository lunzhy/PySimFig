#! /usr/bin/env python3
# -*- coding: utf-8 -*- 
__author__ = 'lunzhy'
import os, sys
path = os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), os.pardir, os.pardir))
if not path in sys.path:
    sys.path.append(path)
from Submissions.R_TED2014 import *
import matplotlib.pyplot as plt
import lib.common as comm


Main_path = Directory_RTED2014
Main_prj = r'program'
# Prj_name = ['p14V_u0.001', 'p14V_u0.01']
Prj_name = ['p14V_u0.1', 'p14V_u0.01', 'p14V_u0.001']
Cut_time = [1e-4]
Cut_position = 2.5


def plotTrapCutLateral():
    fig = plt.figure()
    ax = fig.add_axes([0.15, 0.15, 0.8, 0.8])
    for prj_ind, prj in enumerate(Prj_name):
        prj_path = os.path.join(Main_path, Main_prj, prj)
        for time_ind, time in enumerate(Cut_time):
            trap_path = os.path.join(prj_path, 'Trap')
            file = comm.searchFilePathByTime(trap_path, 'eTrap', time)
            x, y, dens, occ = comm.cutAlignXY(file, Cut_position, align='y')
            ax.plot(x, occ, color=comm.getColor(prj_ind), lw=3)

    labels = [label[1:] + 'cm$^{2}$(Vs)$^{-1}$' for label in Prj_name]
    legend = ax.legend(labels, loc='upper left')
    ax.set_xlabel('Bitline Direction (nm)')
    ax.set_ylabel('Trap Occupation')
    ax.set_xlim(0, 180)
    # ax.set_xticks([0, 15, 45, 75, 105, 135, 165, 180])
    ax.set_xticks([0, 20, 50, 80, 110, 140, 170, 190])
    return


def plotTrapCutRadial():
    fig = plt.figure()
    ax = fig.add_axes([0.15, 0.15, 0.8, 0.8])
    for prj_ind, prj in enumerate(Prj_name):
        prj_path = os.path.join(Main_path, Main_prj, prj)
        for time_ind, time in enumerate(Cut_time):
            trap_path = os.path.join(prj_path, 'Trap')
            file = comm.searchFilePathByTime(trap_path, 'eTrap', time)
            x, y, dens, occ = comm.cutAlignXY(file, 95, align='x')
            ax.plot(y, occ, color=comm.getColor(prj_ind), lw=3)

    labels = [label[1:] + ' cm$^{2}$(Vs)$^{-1}$' for label in Prj_name]
    legend = ax.legend(labels, loc='upper center')
    ax.set_xlabel('Radial Direction (nm)')
    ax.set_ylabel('Trap Occupation')
    return


def main():
    # plotVthCompare()
    plotTrapCutRadial()
    plotTrapCutLateral()
    plt.show()


if __name__ == '__main__':
    main()