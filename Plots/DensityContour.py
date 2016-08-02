#! /usr/bin/env python3
# -*- coding: utf-8 -*- 
__author__ = 'lunzhy'
import os, sys
path = os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), os.pardir, os.pardir))
if not path in sys.path:
    sys.path.append(path)
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
from QuickView.TwoDim import TrapOccupy as occ
from QuickView.TwoDim import eDensity as edens
import lib.format as fmt


Prj_path = '/home/lunzhy/Desktop/'
Time = 1e5


def plotTrappedDensity(prj_path, plot_time):
    fig = plt.figure()
    ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
    im = occ.plotDensitySingleTime(ax, prj_path, plot_time)
    cb = fig.colorbar(im, ax=ax, pad=0.05, aspect=15, extend='both')

    ax.set_xlabel('Bitline Direction (nm)')
    ax.set_ylabel('Vertical Direction (nm)')

    ax.set_xticks([])

    fmt.set2DAxe(ax)
    fmt.setColorbar(cb, 24)
    cb.set_label('Trapped Electron Density ($\mathbf{cm^{-3}}$)', rotation=90, labelpad=10)
    cb.set_ticks([1e16, 1e17, 1e18, 1e19, 1e20])

    plt.show()

    return fig


def plotFreeDensity(prj_path, plot_time):
    fig = plt.figure()
    ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
    im = edens.plotEdensSingleTime(ax, prj_path, plot_time, vmin=1e1, vmax=1e5)
    cb = fig.colorbar(im, ax=ax, pad=0.05, aspect=15, extend='both')
    ax.set_xlabel('Bitline Direction (nm)')
    ax.set_ylabel('Vertical Direction (nm)')

    ax.set_xticks([])

    fmt.set2DAxe(ax)
    fmt.setColorbar(cb, 24)
    cb.set_label('Free Electron Density ($\mathbf{cm^{-3}}$)', rotation=90, labelpad=10)
    cb.set_ticks([1e1, 1e2, 1e3, 1e4, 1e5, 1e6])

    plt.show()
    return fig


def main():
    plotTrappedDensity(Prj_path, Time)
    return


if __name__ == '__main__':
    main()