#! /usr/bin/env python3
# -*- coding: utf-8 -*- 
import os, sys
path = os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), os.pardir, os.pardir))
if not path in sys.path:
    sys.path.append(path)
from Submissions.R_TED2014 import *
import matplotlib.pyplot as plt
import lib.common as comm
import numpy as np
import lib.format as fmt


Main_path = os.path.join(Directory_RTED2014, 'r_trap_thick')


def plot_lateral_by_thick():
    fig = plt.figure()
    ax = fig.add_axes([0.15, 0.15, 0.8, 0.8])
    prj_list = ['4nm', '5nm', '6nm', '7nm']
    vfb_to_plot = ()
    for index, prj in enumerate(prj_list):
        prj_path = os.path.join(Main_path, prj)
        time, total, main_per, other_per = comm.readChargeRegionwise(prj_path)
        other_per = [per - other_per[0] for per in other_per]
        vfb_to_plot += (other_per, )
        ax.plot(time, other_per, color=comm.getColor(index), lw=4)

    vfb1, vfb2, vfb3, vfb4 = vfb_to_plot
    comm.write_data(Folder_Write_Data, time, vfb1, vfb2, vfb3, vfb4)
    ax.set_xscale('log')
    ax.set_ylim(-0.02, 0.42)
    ax.set_yticks([0, 0.10, 0.20, 0.30, 0.40])
    ax.set_xlim(1e2, 1e7)
    ax.set_xlabel(r'Retention Time (s)')
    ax.set_ylabel(r'Ratio of Lateral Spreading')
    legend_label = [r'Thickness = %s' % tem for tem in prj_list]
    legend = ax.legend(legend_label, loc='upper left')

    fmt.setAxesLabel(ax)
    fmt.setAxesTicks(ax)
    fmt.setLegend(legend)

    return


def main():
    plot_lateral_by_thick()
    plt.show()


if __name__ == '__main__':
    main()
