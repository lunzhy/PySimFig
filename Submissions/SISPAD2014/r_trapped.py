__author__ = 'lunzhy'
import os, sys
path = os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), os.pardir, os.pardir))
if not path in sys.path:
    sys.path.append(path)
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
from Submissions.SISPAD2014 import *
from QuickView.TwoDim import TrapOccupy as occ
import lib.common as comm
from mpl_toolkits.axes_grid1 import make_axes_locatable
import lib.format as ft
from matplotlib import font_manager
import numpy as np


Main_path = Directory_Sispad2014
Main_prj = 'retention'
Prj_name = '300K_1.5eV' # 300K_1.5eV, lowT_1.7eV_1e8Hz
Time_to_plot = 1000000

def plot2DOcc(prj_name, time):
    prj_path = os.path.join(Main_path, Main_prj, prj_name)
    fig = plt.figure()
    ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
    im = occ.plotDensitySingleTime(ax, prj_path, time)
    ax.set_aspect(5)
    #divider = make_axes_locatable(ax)
    #cax = divider.append_axes('right', size='5%', pad=.05)
    cb = fig.colorbar(im, ax=ax, shrink=0.4, pad=0.05, aspect=10, extend='both')

    # ax property
    ax.set_xlabel('X (nm)')
    ax.set_ylabel('Y (nm)')
    ax.set_yticks([4, 6, 8, 10, 12])
    ticks_font = font_manager.FontProperties(family='times new roman', style='normal',
                                             size=24, weight='normal', stretch='normal')
    labels_font = font_manager.FontProperties(family='times new roman', style='normal',
                                              size=26, weight='normal', stretch='normal')
    for label_item in ([ax.xaxis.label, ax.yaxis.label]):
        label_item.set_fontproperties(labels_font)
    for label_item in (ax.get_xticklabels() + ax.get_yticklabels()):
        label_item.set_fontproperties(ticks_font)
    ft.setColorbar(cb)
    cb.set_label('Trapped electron density ($mathbf\{cm^{-3}}$)', rotation=270, labelpad=40)
    cb.set_ticks([1e16, 1e17, 1e18, 1e19, 1e20])

    drawFig(fig, ('%s_%ss' % (prj_name, time)))
    return


def main():
    # plot2DOcc(comm.Debug_Folder_Path)
    plot2DOcc('300K_1.7eV_1e8Hz', 5000)
    plot2DOcc('300K_1.7eV_1e8Hz', 1000000)

    plot2DOcc('400K_1.6eV_PF1e10', 5000)
    plot2DOcc('400K_1.6eV_PF1e10', 1000000)


if __name__ == '__main__': main()