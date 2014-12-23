__author__ = 'Lunzhy'
import os, sys
path = os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), os.pardir))
if not path in sys.path:
    sys.path.append(path)
import matplotlib.pyplot as plt
import numpy as np
import lib.common as cm

Target_folder = cm.Debug_Folder_Path
Target_folder = '/home/lunzhy/SimCTM/projects/SSDM2014/standard_program/5e5_2e11_1.6'
Target_folder ='E:\PhD Study\SimCTM\SctmTest\HoleTunnelTest'
Target_folder ='/home/lunzhy/SimCTM/projects/R_TED2014/program/p14V_u0.1'
Target_folder ='/home/lunzhy/SimCTM/projects/R_TED2014/r_lowT/m_sin/0.4'
Target_folder ='/home/lunzhy/SimCTM/projects/R_TED2014/ret-demo'


def plot_vfb(ax, prj, cell_type='single', label=None):
    if cell_type is 'single':
        time, vfb = cm.read_vfb(prj)
        ax.plot(time, vfb, marker='o')
    else:
        time, vfb_cell1, vfb_cell2, vfb_cell3 = cm.readVfbOfCells(prj)
        ax.plot(time, vfb_cell2, marker='o', label=label)
    ax.set_xlim(1e-2, 1e7)
    ax.set_xscale('log')
    return


if __name__ == '__main__':
    fig = plt.figure()
    ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
    plot_vfb(ax, Target_folder, cell_type='triple')
    plt.show()
