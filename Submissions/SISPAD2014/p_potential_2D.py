__author__ = 'lunzhy'
import os, sys
path = os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), os.pardir, os.pardir))
if not path in sys.path:
    sys.path.append(path)
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
from Submissions.SISPAD2014 import *
from QuikView.TwoDim import Potential as Pot
from lib.common import Debug_Folder_Path as Debug_path
import lib.format as ft


Prj_name = r'p_potential_2D'
Main_path = Directory_Sispad2014
Time_to_plot = 1

def main():
    # prj_path = os.path.join(Main_path, Prj_name)
    prj_path = Debug_path
    fig = plt.figure()
    #ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
    ax = fig.add_subplot(111)
    im = Pot.plotSingleTime(ax, prj_path, Time_to_plot)
    ax.set_aspect(1)
    #divider = make_axes_locatable(ax)
    #cax = divider.append_axes('right', size='5%', pad=.05)
    cb = fig.colorbar(im, ax=ax, shrink=0.4, pad=0.05, aspect=10)

    # ax
    ax.set_xlabel('X Coordinate (nm)')
    ax.set_ylabel('Y Coordinate (nm)')
    ax.set_yticks([0, 10, 20, 30])

    # colorbar
    cb.set_label('Potential (V)')
    cb.set_ticks([-3, 1, 5, 9, 13, 17])
    plt.show()
    return


if __name__ == '__main__': main()