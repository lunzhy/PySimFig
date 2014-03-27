__author__ = 'lunzhy'
import os, sys
path = os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), os.pardir, os.pardir))
if not path in sys.path:
    sys.path.append(path)
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
from Submissions.SISPAD2014 import *
from QuikView.TwoDim import TrapOccupy as occ
import lib.common as comm
from mpl_toolkits.axes_grid1 import make_axes_locatable
import lib.format as ft


Main_path = Directory_Sispad2014
Main_prj = 'retention'
Prj_name = '300K_1.5eV' # 300K_1.5eV, lowT_1.7eV_1e8Hz
Time_to_plot = 1000000

def plot2DOcc(prj_name, time):
    prj_path = os.path.join(Main_path, Main_prj, prj_name)
    fig = plt.figure()
    ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
    im = occ.plotSingleTime(ax, prj_path, time)
    ax.set_aspect(5)
    #divider = make_axes_locatable(ax)
    #cax = divider.append_axes('right', size='5%', pad=.05)
    cb = fig.colorbar(im, ax=ax, shrink=0.4, pad=0.05, aspect=10)

    # ax property
    ax.set_xlabel('X Coordinate (nm)')
    ax.set_ylabel('Y Coordinate (nm)')
    return


def main():
    # plot2DOcc(comm.Debug_Folder_Path)
    plot2DOcc('300K_1.7eV_1e8Hz', 5000)
    plot2DOcc('300K_1.7eV_1e8Hz', 1000000)

    plot2DOcc('400K_1.6eV_PF1e10', 5000)
    plot2DOcc('400K_1.6eV_PF1e10', 1000000)
    plt.show()


if __name__ == '__main__': main()