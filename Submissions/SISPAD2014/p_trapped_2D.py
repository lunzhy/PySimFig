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
from matplotlib import font_manager

Main_path = Directory_Sispad2014
Main_prj = r'program'
Prj_name = 'demo'
Time_to_plot = 1

def main():
    prj_path = os.path.join(Main_path, Main_prj, Prj_name)
    # prj_path = Debug_path
    fig = plt.figure()
    #ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
    ax = fig.add_subplot(111)
    im = occ.plotDensitySingleTime(ax, prj_path, Time_to_plot)
    ax.set_aspect(4)
    #divider = make_axes_locatable(ax)
    #cax = divider.append_axes('right', size='5%', pad=.05)
    cb = fig.colorbar(im, ax=ax, shrink=0.4, pad=0.05, aspect=10,extend='both')

    # ax
    # ax.set_xlabel('X Coordinate (nm)')
    # ax.set_ylabel('Y Coordinate (nm)')
    ax.set_xlabel('X (nm)')
    ax.set_ylabel('Y (nm)')
    ax.set_yticks([4, 8, 12])
    for axis in ['top', 'bottom', 'left', 'right']:
        ax.spines[axis].set_linewidth(0)

    ticks_font = font_manager.FontProperties(family='times new roman', style='normal',
                                             size=24, weight='normal', stretch='normal')
    labels_font = font_manager.FontProperties(family='times new roman', style='normal',
                                              size=26, weight='normal', stretch='normal')
    for label_item in ([ax.xaxis.label, ax.yaxis.label]):
        label_item.set_fontproperties(labels_font)
    for label_item in (ax.get_xticklabels() + ax.get_yticklabels()):
        label_item.set_fontproperties(ticks_font)
    ft.setColorbar(cb, 24)
    cb.set_label('Trapped electron\ndensity ($\mathbf{cm^{-3}}$)', rotation=90, labelpad=40)
    cb.set_ticks([1e16, 1e17, 1e18, 1e19, 1e20])

    ### axis tick
    ax.xaxis.set_tick_params(which='major', width=0, size=5)
    ax.xaxis.set_tick_params(which='minor', width=0, size=3)
    ax.yaxis.set_tick_params(which='major', width=0, size=5)
    ax.yaxis.set_tick_params(which='minor', width=0, size=3)

    for tick in ax.get_xaxis().get_major_ticks():
        tick.set_pad(8.)


    drawFig(fig, 'p_trapped')
    #plt.show()
    return


if __name__ == '__main__': main()