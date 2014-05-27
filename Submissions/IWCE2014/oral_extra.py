__author__ = 'lunzhy'
import os, sys
path = os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), os.pardir, os.pardir))
if not path in sys.path:
    sys.path.append(path)
import matplotlib.pyplot as plt
from QuikView.TwoDim import TrapOccupy as occ
import lib.format as ft
from matplotlib import font_manager
from QuikView.OneDim import Trap as trap


Main_path = '/home/lunzhy/SimCTM/projects/IWCE2014'
Time_to_plot = 1


IsSaveFigure = True

def drawFig(fig, name):
    if IsSaveFigure:
        fig_path = os.path.join(Main_path, name)
        fig.savefig(fig_path+'.png', dpi=1020, bbox_inches='tight', pad_inches=0.1)
    return


def plot2D(prj_name, time_to_plot):
    prj_path = os.path.join(Main_path, prj_name)

    fig = plt.figure()
    ax = fig.add_axes([0.15, 0.15, 0.8, 0.8])
    # ax = fig.add_subplot(111)
    im = occ.plotDensitySingleTime(ax, prj_path, time_to_plot)
    # ax.set_aspect(8)
    cb = fig.colorbar(im, ax=ax, pad=0.05, extend='both')

    # ax
    ax.set_xlabel('X (nm)')
    ax.set_ylabel('Y (nm)')
    # ax.set_yticks([4, 8, 12])
    ax.set_xlim(45, 135)
    ax.set_xticks([45, 75, 105, 135])
    ax.set_xticklabels(['0', '30', '60', '90'])
    for axis in ['top', 'bottom', 'left', 'right']:
        ax.spines[axis].set_linewidth(0)

    ticks_font = font_manager.FontProperties(family='Arial', style='normal',
                                             size=24, weight='normal', stretch='normal')
    labels_font = font_manager.FontProperties(family='Arial', style='normal',
                                              size=26, weight='normal', stretch='normal')
    for label_item in ([ax.xaxis.label, ax.yaxis.label]):
        label_item.set_fontproperties(labels_font)
    for label_item in (ax.get_xticklabels() + ax.get_yticklabels()):
        label_item.set_fontproperties(ticks_font)
    ft.setColorbar(cb, 24)
    cb.set_label('Trapped Electron Density ($\mathbf{cm^{-3}}$)', rotation=90, labelpad=10)
    cb.set_ticks([1e16, 1e17, 1e18, 1e19, 1e20])

    ### axis tick
    ax.xaxis.set_tick_params(which='major', width=0, size=5)
    ax.xaxis.set_tick_params(which='minor', width=0, size=3)
    ax.yaxis.set_tick_params(which='major', width=0, size=5)
    ax.yaxis.set_tick_params(which='minor', width=0, size=3)

    for tick in ax.get_xaxis().get_major_ticks():
        tick.set_pad(8.)

    drawFig(fig, '%s_2D' % prj_name)
    return


def plotCut(prj_name, time_list, coord, align):
    fig = plt.figure()
    ax = fig.add_axes([0.15, 0.15, 0.75, 0.75])
    prj_path = os.path.join(Main_path, prj_name)
    trap.plotCut(ax, prj=prj_path, time_list=time_list, coord=coord, align=align)
    ax.set_xlim(45, 135)
    ax.set_xticks([45, 75, 105, 135])
    ax.set_xticklabels(['0', '30', '60', '90'])
    ft.setAxesLabel(ax, 24, 22)
    ft.setAxesTicks(ax)

    labels = ['%ss' % time for time in time_list]
    legend = ax.legend(labels, loc='upper left')
    ft.setLegend(legend, 20)
    drawFig(fig, '%s_cut' % prj_name)
    return


def plotRetention():
    return


def main():
    plot2D('program', 1)
    prg_time_list = ['1e-5', '1e-3', '1e-2', '1e-1', '1']
    ret_time_list = ['1e2', '1e3', '1e4', '1e5', '1e6', '1e7']
    plotCut('program', prg_time_list, coord=4, align='y')
    plot2D('retention', 1e6)
    plotCut('retention', ret_time_list, coord=4, align='y')
    plt.show()


if __name__ == '__main__':
    main()

