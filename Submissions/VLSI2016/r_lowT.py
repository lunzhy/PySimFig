__author__ = 'lunzhy'
import os, sys
path = os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), os.pardir, os.pardir))
if not path in sys.path:
    sys.path.append(path)
from Submissions.VLSI2016 import *
import matplotlib.pyplot as plt
import lib.common as comm
import QuickView.TwoDim.TrapOccupy as occ
import lib.format as fmt
from matplotlib import font_manager

from matplotlib import rc
# rc('text', usetex=True)

Main_path = Directory_VLSI2016
Main_prj = r'low_T'

Emass_list = ['0.1', '0.2', '0.3']
Frequency_list = ['1e7', '1e8', '1e10']  # do not use 1e7, use 1x10^7


def formatPlots(ax, legend):
    fmt.setAxesLabel(ax)
    fmt.setAxesTicks(ax)
    fmt.setLegend(legend)
    return


def plot2D(par_name, time):
    fig = plt.figure()
    ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
    prj_path = os.path.join(Main_path, Main_prj, '30nm')
    im = occ.plotDensitySingleTime(ax, prj_path, time)
    cb = fig.colorbar(im, ax=ax, pad=0.05, aspect=15, extend='both')

    ax.set_xlabel('Bitline Direction (nm)')
    ax.set_ylabel('Vertical Direction (nm)')
    ax.set_yticks([5, 7, 9, 11, 13])
    ax.set_xticks([0, 90, 120, 210])

    fmt.set2DAxe(ax)

    fmt.setColorbar(cb, 24)
    cb.set_label('Trapped Electron Density ($\mathbf{cm^{-3}}$)', rotation=90, labelpad=10)
    cb.set_ticks([1e16, 1e17, 1e18, 1e19, 1e20])

    drawFig(fig, 'lowK_2D')
    return


def plotVthParameters():
    return


def main():
    # ax = plotVth('SiN', Emass_list)
    # ax2 = plotVth('frequency', Frequency_list)
    plot2D('frequency', 3e7)
    plt.show()


if __name__ == '__main__':
    main()