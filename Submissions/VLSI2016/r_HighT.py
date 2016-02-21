__author__ = 'lunzhy'
import os, sys
path = os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), os.pardir, os.pardir))
if not path in sys.path:
    sys.path.append(path)
from Submissions.VLSI2016 import *
import matplotlib.pyplot as plt
import lib.common as comm
from QuickView.TwoDim import TrapOccupy as occ
from QuickView.TwoDim import eDensity as edens
import lib.format as fmt
from matplotlib import font_manager

from matplotlib import rc
# rc('text', usetex=True)

Main_path = os.path.join(Directory_VLSI2016, 'high_T')

def to_simple(x, position):
    s = x / 1e19
    return int(s)


def to_scientific(x, position):
    s = x / 1e19
    return str(int(s)) + 'e19'


def to_scientific_math(x, position):
    s = x / 1e19
    return r'$\mathbf{%s\times10^{%s}%s}$' % (s, '19')


def plot2DOcc(plot_time):
    prj_path = os.path.join(Main_path, '30nm')
    # prj_path = os.path.join(Directory_VLSI2016, 'demo')
    fig = plt.figure()
    ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
    im = occ.plotDensitySingleTime(ax, prj_path, plot_time)
    cb = fig.colorbar(im, ax=ax, pad=0.05, aspect=15, extend='both')

    ax.set_xlabel('Bitline Direction (nm)')
    ax.set_ylabel('Vertical Direction (nm)')
    ax.set_yticks([5, 6, 7, 8, 8, 10, 11, 12, 13])
    ax.set_xticks([0, 90, 120, 210])

    fmt.set2DAxe(ax)
    fmt.setColorbar(cb, 24)
    cb.set_label('Trapped Electron Density ($\mathbf{cm^{-3}}$)', rotation=90, labelpad=10)
    cb.set_ticks([1e16, 1e17, 1e18, 1e19, 1e20])

    drawFig(fig, 'highK_2Dtrap')
    return


def plot2DDensity(plot_time):
    prj_path = os.path.join(Main_path, '30nm')
    fig = plt.figure()
    ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
    im = edens.plotEdensSingleTime(ax, prj_path, plot_time, vmin=1e1, vmax=1e5)
    cb = fig.colorbar(im, ax=ax, pad=0.05, aspect=15, extend='both')
    ax.set_xlabel('Bitline Direction (nm)')
    ax.set_ylabel('Vertical Direction (nm)')
    ax.set_yticks([6, 7, 8, 9, 10, 11, 12])
    ax.set_xticks([0, 80, 110, 190])
    fmt.set2DAxe(ax)
    fmt.setColorbar(cb, 24)
    cb.set_label('Free Electron Density ($\mathbf{cm^{-3}}$)', rotation=90, labelpad=10)
    cb.set_ticks([1e1, 1e2, 1e3, 1e4, 1e5, 1e6])

    drawFig(fig, 'highK_2Ddensity')
    return





def main():
    # plot2DOcc(plot_time=1e8)
    plot2DDensity(plot_time=1e8)
    plt.show()
    return


if __name__ == '__main__':
    main()
