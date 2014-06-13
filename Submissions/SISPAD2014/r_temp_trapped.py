__author__ = 'Lunzhy'
import os, sys
path = os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), os.pardir, os.pardir))
if not path in sys.path:
    sys.path.append(path)
import matplotlib.pyplot as plt
from Submissions.SISPAD2014 import *
from QuickView.TwoDim import TrapOccupy as occ
import lib.common as comm
import lib.format as fmt
from matplotlib import font_manager
from mpl_toolkits.axes_grid1 import make_axes_locatable
import matplotlib.gridspec as gridspec


Main_path = Directory_Sispad2014
Main_prj = 'retention'
Prj_300K = r'4nm_300K_1.6eV_PF2e11_T2B5e5'  # thick_1.6eV_PF1e10, 4nm_300K_1.6eV_PF2e11_T2B2e6
Prj_350K = r'4nm_350K_1.6eV_PF2e11_T2B5e5'
Time_to_plot = 1e6


def plotTrappedDensity(prj_path, ax):
    im = occ.plotDensitySingleTime(ax, prj_path, Time_to_plot)
    return im


def formatAxes(ax):
    ax.set_xlabel('X (nm)', labelpad=0)
    ax.set_ylabel('Y (nm)', labelpad=0)
    ax.set_yticks([4, 6, 8, 10, 12])
    for axis in ['top', 'bottom', 'left', 'right']:
        ax.spines[axis].set_linewidth(0)
    ticks_font = font_manager.FontProperties(family='times new roman', style='normal',
                                             size=22, weight='normal', stretch='normal')
    labels_font = font_manager.FontProperties(family='times new roman', style='normal',
                                              size=24, weight='normal', stretch='normal')
    for label_item in ([ax.xaxis.label, ax.yaxis.label]):
        label_item.set_fontproperties(labels_font)
    for label_item in (ax.get_xticklabels() + ax.get_yticklabels()):
        label_item.set_fontproperties(ticks_font)
    ax.xaxis.set_tick_params(which='major', width=0, size=5)
    ax.xaxis.set_tick_params(which='minor', width=0, size=3)
    ax.yaxis.set_tick_params(which='major', width=0, size=5)
    ax.yaxis.set_tick_params(which='minor', width=0, size=3)
    for tick in ax.get_xaxis().get_major_ticks():
        tick.set_pad(8.)

    return

def plotTempCmp():
    fig = plt.figure()
    ax_low = fig.add_subplot(211)
    ax_high = fig.add_subplot(212)

    plotTrappedDensity(os.path.join(Main_path, Main_prj, Prj_300K), ax_low)
    im = plotTrappedDensity(os.path.join(Main_path, Main_prj, Prj_350K), ax_high)

    formatAxes(ax_low)
    formatAxes(ax_high)

    plt.tight_layout()
    fig.subplots_adjust(hspace=0.4, right=0.82)
    ax_cb = fig.add_axes([0.88, 0.2, 0.03, 0.7])
    cb = fig.colorbar(im, cax=ax_cb, extend='both')
    cb.set_label('Trapped Electron Density ($\mathbf{cm^{-3}}$)', rotation=90, labelpad=5)
    fmt.setColorbar(cb, font_size=22)
    drawFig(fig, 'Temperature_4nm_5e5')
    return


def main():
    plotTempCmp()
    plt.show()
    return


if __name__ == '__main__':
    main()