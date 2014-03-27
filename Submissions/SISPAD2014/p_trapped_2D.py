__author__ = 'lunzhy'
import os, sys
path = os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), os.pardir, os.pardir))
if not path in sys.path:
    sys.path.append(path)
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
from Submissions.SISPAD2014 import *
from QuikView.TwoDim import TrapOccupy as occ
from lib.common import Debug_Folder_Path as Debug_path
from mpl_toolkits.axes_grid1 import make_axes_locatable
import lib.format as ft


Prj_name = r'p_trapped_2D'
Main_path = Directory_Sispad2014
Time_to_plot = 1

def main():
    # prj_path = os.path.join(Main_path, Prj_name)
    prj_path = Debug_path
    fig = plt.figure()
    #ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
    ax = fig.add_subplot(111)
    im = occ.plotSingleTime(ax, prj_path, Time_to_plot)
    ax.set_aspect(4)
    #divider = make_axes_locatable(ax)
    #cax = divider.append_axes('right', size='5%', pad=.05)
    cb = fig.colorbar(im, ax=ax, shrink=0.4, pad=0.05, aspect=10)

    # ax
    ax.set_xlabel('X Coordinate (nm)')
    ax.set_ylabel('Y Coordinate (nm)')
    plt.show()
    return


if __name__ == '__main__': main()