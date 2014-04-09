__author__ = 'lunzhy'
import os, sys
path = os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), os.pardir, os.pardir))
if not path in sys.path:
    sys.path.append(path)
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
from Submissions.SISPAD2014 import *
from QuikView.TwoDim import TrapOccupy as occ
import lib.common as comm
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import lib.format as fmt
from matplotlib.ticker import FuncFormatter
from matplotlib import font_manager
from mpl_toolkits.axes_grid1 import make_axes_locatable
import matplotlib.gridspec as gridspec


Main_path = Directory_Sispad2014
Main_prj = 'retention'
# Time_list = [1, 10, 1e2, 1e3, 1e4, 1e5, 1e6]
Time_list = [1, 1e2, 1e3, 1e4, 1e5, 5e5, 5e6]
Time_list_few = [1e2, 1e3, 1e4, 1e5, 5e6]
Prj_name = r'thick_350K_1.6eV_PF2e11'  # thick_1.6eV_PF1e10
Time_to_plot = 1e6
Cutline = [50, 40, 30]

def to_simple(x, position):
    s = x / 1e19
    return int(s)

def to_scientific(x, position):
    s = x / 1e19
    return str(int(s)) + 'e19'


def trappedDensity(ax, prj_path, cut_point, align='x'):
    lines = []
    for index, time in enumerate(Time_list_few):
        trap_directory = os.path.join(prj_path, 'Trap')
        trap_file = comm.searchFilePathByTime(trap_directory, 'trap', time)
        x, y, dens, occ = comm.cutAlongXY(trap_file, cut_point, align)
        if align == 'x':
            new_line, = ax.plot(y, dens, lw=3, c=comm.getColor(index))
        else:
            new_line, = ax.plot(x, dens, lw=3, c=comm.getColor(index))
        lines += [new_line]
    return lines


def freeDensity(ax, prj_path, cut_point):
    # vertical
    lines = []
    for index, time in enumerate(Time_list_few):
        density_directory = os.path.join(prj_path, 'Density')
        density_file = comm.searchFilePathByTime(density_directory, 'eDens', time)
        x, y, dens = comm.cutAlongXY(density_file, cut_point, align='x')
        new_linel, = ax.plot(y, dens, lw=3, c=comm.getColor(index))
        lines += [new_linel]
    return lines


def plotVerticalCut():
    prj_path = os.path.join(Main_path, Main_prj, Prj_name)
    fig = plt.figure()
    ax_trapped = fig.add_subplot(211)
    ax_free = fig.add_subplot(212)

    lines = trappedDensity(ax_trapped, prj_path, 50, 'x')
    lines += freeDensity(ax_free, prj_path, 50)

    # legend
    legend_text = ['%.es' % leg for leg in Time_list_few]
    legend = ax_trapped.legend(legend_text, loc='upper center', handlelength=2, ncol=3, borderaxespad=0.,
                               bbox_to_anchor=(0.5, 1))
    fmt.setLegend(legend, font_size=20)

    # trapped electrons
    ax_trapped.set_xlim(6, 14)
    ax_trapped.yaxis.tick_right()
    ax_trapped.yaxis.labelpad = 15
    ax_trapped.yaxis.set_ticks_position('both')
    fmt.setAxesLabel(ax_trapped, 22, 20)
    fmt.setAxesTicks(ax_trapped)
    for tick in ax_trapped.get_xaxis().get_major_ticks():
        tick.set_pad(0)
    ax_trapped.set_ylabel('Trapped Electrons ($\mathbf{cm^{-3}}$)')
    ax_trapped.yaxis.set_label_position("right")
    # ax_trapped.yaxis.tick_right()
    ax_trapped.set_ylim(0.5e19, 7.5e19)
    ax_trapped.set_yticks([1e19, 3e19, 5e19, 7e19])
    ax_trapped.set_xticklabels([])
    # formatter = FuncFormatter(to_scientific)
    # ax_trapped.yaxis.set_major_formatter(formatter)
    ax_trapped.yaxis.set_offset_position('right')

    #free electrons
    ax_free.set_xlim(6, 14)
    # legend = ax_free.legend(legend_text, loc='upper left', handlelength=3, ncol=3)
    fmt.setAxesLabel(ax_free, 22, 20)
    fmt.setAxesTicks(ax_free)
    ax_free.set_xlabel('Vertical Direction (nm)')
    ax_free.set_ylabel('CB Electrons ($\mathbf{cm^{-3}}$)')
    ax_free.set_ylim(1, 5e7)
    ax_free.set_yscale('log')
    ax_free.set_yticks([1e1, 1e3, 1e5, 1e7])
    fig.subplots_adjust(hspace=0.001)

    drawFig(fig, 'cut')
    return


def plot3DTrappedDensity():
    prj_path = os.path.join(Main_path, Main_prj, Prj_name)
    fig = plt.figure()
    ax = fig.add_axes([0, 0, 1, 1], projection='3d')
    # near tunnel oxide
    for index, time in enumerate(Time_list):
        trap_directory = os.path.join(prj_path, 'Trap')
        trap_file = comm.searchFilePathByTime(trap_directory, 'trap', time)
        x, y, dens, occ = comm.cutAlongXY(trap_file, 4, align='y')
        ax.plot(x, y, dens, lw=2.5, c=comm.getColor(index))

    # in the middle
    for index, time in enumerate(Time_list):
        trap_directory = os.path.join(prj_path, 'Trap')
        trap_file = comm.searchFilePathByTime(trap_directory, 'trap', time)
        x, y, dens, occ = comm.cutAlongXY(trap_file, 10, align='y')
        ax.plot(x, y, dens, lw=2.5, c=comm.getColor(index))

    # near block oxide
    for index, time in enumerate(Time_list):
        trap_directory = os.path.join(prj_path, 'Trap')
        trap_file = comm.searchFilePathByTime(trap_directory, 'trap', time)
        x, y, dens, occ = comm.cutAlongXY(trap_file, 14, align='y')
        ax.plot(x, y, dens, lw=2.5, c=comm.getColor(index))


    ax.set_xlim3d(0, 100)
    ax.set_ylim3d(4, 15)
    # ax.set_xlabel('BL direction (nm)', labelpad=50, linespacing=3.2)
    # ax.set_ylabel('Vertical direction (nm)')
    # ax.set_zlabel('Trapped electron density (1e19${cm^{-3}}$)')
    ax.set_zticks([1e19, 3e19, 5e19, 7e19])
    # ax.set_zticklabels([1e19, 3e19, 5e19, 7e19])
    zformatter = FuncFormatter(to_simple)
    ax.zaxis.set_major_formatter(zformatter)

    fmt.setAxesLabel(ax)
    # ax.set_zlabel('Trapped electron density (cm^-3)', labelpad=5)
    ax.view_init(25, -35)
    ax.dist = 10
    legend_text = ['%.es' % leg for leg in Time_list]
    legend = ax.legend(legend_text, loc='upper left', handlelength=3)
    fmt.setLegend(legend)

    drawFig(fig, '3D')
    return


def plotTrappedDensity2D(ax, fig):
    prj_path = os.path.join(Main_path, Main_prj, Prj_name)
    # fig = plt.figure()
    # ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
    # ax = fig.add_subplot(111)
    im = occ.plotDensitySingleTime(ax, prj_path, Time_to_plot)
    # ax.set_aspect(5.5)
    # divider = make_axes_locatable(ax)
    # cax = divider.append_axes('right', size='5%', pad=.05)
    cb = fig.colorbar(im, ax=ax, pad=0.05, aspect=10, extend='both')

    # ax
    # ax.set_xlabel('X Coordinate (nm)')
    # ax.set_ylabel('Y Coordinate (nm)')
    ax.set_xlabel('X (nm)', labelpad=0)
    ax.set_ylabel('Y (nm)', labelpad=0)
    ax.set_yticks([6, 8, 10, 12, 14])
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
    fmt.setColorbar(cb, 20)
    cb.set_label('Trapped Electron\n Density ($\mathbf{cm^{-3}}$)', rotation=90, labelpad=10)
    cb.set_ticks([1e16, 1e17, 1e18, 1e19, 1e20])

    ### axis tick
    ax.xaxis.set_tick_params(which='major', width=0, size=5)
    ax.xaxis.set_tick_params(which='minor', width=0, size=3)
    ax.yaxis.set_tick_params(which='major', width=0, size=5)
    ax.yaxis.set_tick_params(which='minor', width=0, size=3)

    for tick in ax.get_xaxis().get_major_ticks():
        tick.set_pad(8.)

    # drawFig(fig, 'r_thick_trapped_2D')
    return


def plotFreeDensity2D(ax, fig):
    prj_path = os.path.join(Main_path, Main_prj, Prj_name)
    # fig = plt.figure()
    # ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
    # ax = fig.add_subplot(111)

    edens_dir = os.path.join(prj_path, 'Density')
    file_path = comm.searchFilePathByTime(edens_dir, 'eDensity', Time_to_plot)
    x, y, edens = comm.readData2D(file_path)
    grid_z = comm.makeValueGridZ(x, y, edens)
    im = ax.imshow(grid_z, cmap=plt.cm.jet, vmin=1e1, vmax=1e5, origin='lower',
                   extent=[min(x), max(x), min(y), max(y)], aspect='auto', norm=LogNorm())

    # ax.set_aspect(5.5)
    # divider = make_axes_locatable(ax)
    # cax = divider.append_axes('right', size='5%', pad=.05)
    cb = fig.colorbar(im, ax=ax, pad=0.05, aspect=10, extend='both')

    # ax
    # ax.set_xlabel('X Coordinate (nm)')
    # ax.set_ylabel('Y Coordinate (nm)')
    ax.set_xlabel('X (nm)', labelpad=0)
    ax.set_ylabel('Y (nm)', labelpad=0)
    ax.set_yticks([6, 8, 10, 12, 14])
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
    fmt.setColorbar(cb, 20)
    cb.set_label('CB Electron\n Density ($\mathbf{cm^{-3}}$)', rotation=90, labelpad=10)
    # cb.set_ticks([1e16, 1e17, 1e18, 1e19, 1e20])

    ### axis tick
    ax.xaxis.set_tick_params(which='major', width=0, size=5)
    ax.xaxis.set_tick_params(which='minor', width=0, size=3)
    ax.yaxis.set_tick_params(which='major', width=0, size=5)
    ax.yaxis.set_tick_params(which='minor', width=0, size=3)

    for tick in ax.get_xaxis().get_major_ticks():
        tick.set_pad(8.)

    # drawFig(fig, 'r_thick_free_2D')
    return


def plot2D():
    fig = plt.figure()
    ax_trapped = fig.add_subplot(211)
    ax_free = fig.add_subplot(212)
    plotTrappedDensity2D(ax_trapped, fig)
    plotFreeDensity2D(ax_free, fig)
    fig.subplots_adjust(hspace=0.4)
    drawFig(fig, 'thick_trapped_free')
    return


def plotBandCuts():
    fig = plt.figure()
    ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
    prj_path = os.path.join(Main_path, Main_prj, Prj_name)
    plot_to_label = []
    y_extent = 100
    for index, cut_coord in enumerate(Cutline):
        band_dir = os.path.join(prj_path, 'Band')
        file_path = comm.searchFilePathByTime(band_dir, 'band', Time_to_plot)
        x, y, cb, vb = comm.cutAlongXY(file_path, coord_in_nm=cut_coord, align='x')
        y_extent = min(max(y), y_extent)
        pl, = ax.plot(y, cb, c=comm.getColor(index), lw=3)
        plot_to_label.append(pl)
        ax.plot(y, vb, comm.getColor(index), lw=3)

    labels = ["cutline a-a'", "cutline b-b'", "cutline c-c'"]
    legend = ax.legend(plot_to_label, labels, bbox_to_anchor=(0.55, 0.25))

    ax.set_xlim(0, y_extent-0.1)
    ax.set_ylim(-7, 9)
    ax.set_yticks(np.arange(-7, 9, 3))
    ax.set_xlabel('Vertical Direction (nm)', labelpad=0)
    ax.set_ylabel('Band Energy (eV)', labelpad=0)
    fmt.setAxesLabel(ax)
    fmt.setAxesTicks(ax)
    fmt.setLegend(legend, 20)

    drawFig(fig, 'band_cuts')
    return


def plotTwoCutlines():
    prj_path = os.path.join(Main_path, Main_prj, Prj_name)
    fig = plt.figure()
    ax_trapped = fig.add_axes([0.1, 0.1, 0.8, 0.8])
    ax_free = ax_trapped.twinx()

    min_x = 100
    max_x = 100
    for index, cut_pos in enumerate(Cutline):
        trap_dir = os.path.join(prj_path, 'Trap')
        trap_file = comm.searchFilePathByTime(trap_dir, 'trap', Time_to_plot)
        x, y, trapped, occ = comm.cutAlongXY(trap_file, cut_pos, 'x')
        min_x = min(min(y), min_x)
        max_x = min(max(y), max_x)
        ax_trapped.plot(y, trapped, lw=3, c='b')

        edens_dir = os.path.join(prj_path, 'Density')
        edens_file = comm.searchFilePathByTime(edens_dir, 'eDens', Time_to_plot)
        x, y, edens = comm.cutAlongXY(edens_file, cut_pos, 'x')
        ax_free.plot(y, edens, lw=3, c='k')

    ax_trapped.set_xlim(min_x, max_x)
    ax_free.set_yscale('log')
    return


def plotCutlines():
    prj_path = os.path.join(Main_path, Main_prj, Prj_name)
    fig = plt.figure()
    gs = gridspec.GridSpec(2, 2, width_ratios=[1, 1])
    ax_band = fig.add_subplot(gs[:, 0])
    ax_trapped = fig.add_subplot(gs[0, 1])
    ax_free = fig.add_subplot(gs[1, 1])
    fig.subplots_adjust(hspace=0., wspace=0.05, right=0.86)

    # band
    plot_to_label = []
    y_extent = 100
    for index, cut_coord in enumerate(Cutline):
        band_dir = os.path.join(prj_path, 'Band')
        file_path = comm.searchFilePathByTime(band_dir, 'band', Time_to_plot)
        x, y, cb, vb = comm.cutAlongXY(file_path, coord_in_nm=cut_coord, align='x')
        y_extent = min(max(y), y_extent)
        pl, = ax_band.plot(y, cb, c=comm.getColor(index), lw=3)
        plot_to_label.append(pl)
        ax_band.plot(y, vb, comm.getColor(index), lw=3)

    labels = ["cut a-a'", "cut b-b'", "cut c-c'"]
    legend = ax_band.legend(plot_to_label, labels, loc='lower left', bbox_to_anchor=(0, 1.02, 1.7, 0.1),
                            ncol=3, borderaxespad=0., mode='expand')

    ax_band.set_xlim(0, y_extent - 0.1)
    ax_band.set_ylim(-7, 9)
    ax_band.set_yticks(np.arange(-7, 9, 3))
    ax_band.set_xlabel('Vertical Direction (nm)', labelpad=0)
    ax_band.set_ylabel('Band Energy (eV)', labelpad=0)
    fmt.setAxesLabel(ax_band, 22, 20)
    fmt.setAxesTicks(ax_band)
    fmt.setLegend(legend, 20)

    # trapped/free electron density
    min_x = 100
    max_x = 100
    for index, cut_pos in enumerate(Cutline):
        trap_dir = os.path.join(prj_path, 'Trap')
        trap_file = comm.searchFilePathByTime(trap_dir, 'trap', Time_to_plot)
        x, y, trapped, occ = comm.cutAlongXY(trap_file, cut_pos, 'x')
        min_x = min(min(y), min_x)
        max_x = min(max(y), max_x)
        ax_trapped.plot(y, trapped, lw=2, c=comm.getColor(index))

        edens_dir = os.path.join(prj_path, 'Density')
        edens_file = comm.searchFilePathByTime(edens_dir, 'eDens', Time_to_plot)
        x, y, edens = comm.cutAlongXY(edens_file, cut_pos, 'x')
        ax_free.plot(y, edens, lw=2, c=comm.getColor(index))

    # ax_trapped
    ax_trapped.set_ylabel('Trapped\nElectrons ($\mathbf{cm^{-3}}$)', labelpad=10)
    ax_trapped.set_yticks([1e19, 3e19, 5e19, 7e19])
    ax_trapped.yaxis.tick_right()
    ax_trapped.yaxis.set_label_position('right')
    ax_trapped.yaxis.set_offset_position('right')
    ax_trapped.yaxis.set_label_coords(1.1, 0.6)
    ax_trapped.set_xticks([6, 8, 10, 12, 14])
    ax_trapped.set_xticklabels([])
    fmt.setAxesLabel(ax_trapped, 22, 20)
    fmt.setAxesTicks(ax_trapped)
    offset_text = ax_trapped.yaxis.get_offset_text()
    if not offset_text is None:
        offset_text.set_size(18)

    # ax_free
    ax_free.set_ylim(1e1, 1e5)
    ax_free.set_yscale('log')
    ax_free.set_xlabel('Vertical Direction (nm)', labelpad=0)
    ax_free.set_ylabel('CB Electrons ($\mathbf{cm^{-3}}$)')
    ax_free.yaxis.tick_right()
    ax_free.yaxis.set_label_position('right')
    ax_free.set_yticks([1e1, 1e3, 1e5])
    ax_free.set_xticks([6, 8, 10, 12, 14])
    fmt.setAxesLabel(ax_free, 22, 20)
    fmt.setAxesTicks(ax_free)


    drawFig(fig, 'thick_cuts')
    return


def main():
    # trappedDensity(50, 'y')
    # freeDensity(50)
    # plot3DTrappedDensity()
    plotVerticalCut()
    # plotTrappedDensity2D()
    # plotBandCuts()
    plotCutlines()
    # plotFreeDensity2D()
    # plot2D()
    # plotTwoCutlines()
    # plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    main()
