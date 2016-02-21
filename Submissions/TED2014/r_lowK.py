__author__ = 'lunzhy'
import os, sys
path = os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), os.pardir, os.pardir))
if not path in sys.path:
    sys.path.append(path)
from Submissions.TED2014 import *
import matplotlib.pyplot as plt
import lib.common as comm
import QuickView.TwoDim.TrapOccupy as occ
import lib.format as fmt
from matplotlib import font_manager

from matplotlib import rc
# rc('text', usetex=True)

Main_path = Directory_TED2014
Main_prj = r'ret_lowK'

Emass_list = ['0.1', '0.2', '0.3']
Frequency_list = ['1e7', '1e8', '1e10']  # do not use 1e7, use 1x10^7


def formatPlots(ax, legend):
    fmt.setAxesLabel(ax)
    fmt.setAxesTicks(ax)
    fmt.setLegend(legend)
    return


def plotVth(prj_name, prj_list):
    fig = plt.figure()
    ax = fig.add_axes([0.15, 0.15, 0.8, 0.8])

    for index, prj in enumerate(prj_list):
        prj_path = os.path.join(Main_path, Main_prj, prj_name, prj)
        time, vfb1, vfb2, vfb3 = comm.readVfbOfCells(prj_path)
        ax.plot(time, vfb2, color=comm.getColor(index), marker=comm.getMarker(index), lw=3,
                markersize=14, markeredgecolor=comm.getColor(index), markevery=2)

    labels = []
    if prj_name == 'SiN':
        labels = [r'$\mathbf{ m_{SiN} = %s m_0}$' % label for label in prj_list]
    elif prj_name == 'frequency':
        for label in prj_list:
            superscript = label[2:]
            labels.append(r'$\mathbf{TB\,frequency = 1\times10^{%s}Hz}$' % superscript)
    legend = ax.legend(labels, loc='lower left', numpoints=1)

    ax.set_xscale('log')
    ax.set_xlim(1e2, 1e7)
    ax.set_ylim(4.0, 5.2)
    ax.set_xlabel(r'Retention time (s)')
    ax.set_ylabel('Threshold voltage shift (V)')
    formatPlots(ax, legend)

    drawFig(fig, 'lowK_%s_new' % prj_name)

    return ax


def plot2D(par_name, par_value, time):
    fig = plt.figure()
    ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
    prj_path = os.path.join(Main_path, Main_prj, par_name, par_value)
    im = occ.plotDensitySingleTime(ax, prj_path, time)
    cb = fig.colorbar(im, ax=ax, pad=0.05, aspect=15, extend='both')

    ax.set_xlabel('Bitline Direction (nm)')
    ax.set_ylabel('Vertical Direction (nm)')
    ax.set_yticks([4, 5, 6, 7, 8, 9])
    ax.set_xticks([0, 80, 110, 190])

    fmt.set2DAxe(ax)

    fmt.setColorbar(cb, 24)
    cb.set_label('Trapped Electron Density ($\mathbf{cm^{-3}}$)', rotation=90, labelpad=10)
    cb.set_ticks([1e16, 1e17, 1e18, 1e19, 1e20])

    drawFig(fig, 'lowK_2D')
    return


def plotVthParameters():
    return


def main():
    ax = plotVth('SiN', Emass_list)
    ax2 = plotVth('frequency', Frequency_list)
    # plot2D('frequency', '1e8', 3e8)
    plt.show()


if __name__ == '__main__':
    main()