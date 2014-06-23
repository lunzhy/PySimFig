__author__ = 'Lunzhy'
import os, sys
path = os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), os.pardir, os.pardir))
if not path in sys.path:
    sys.path.append(path)
import lib.common as comm
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm


Target_directory = comm.Debug_Folder_Path
Target_directory = '/home/lunzhy/SimCTM/projects/SSDM2014/p_side/Lg30_pSide'
Density_directory = os.path.join(Target_directory, comm.Density_Folder)
Dens_file_pattern = 'eDens'
# Time_list = [2e-9, 1e-8, 1e-7, 1e-6, 1e-5, 1e-4, 1e-3, 1e-2, 1e-1, 1]
# Time_list = [2e-9, 1e-8, 1e-7, 1e-6, 1e-5, 1e-4, 1e-3, 1e-2, 1e-1, 1]
# Time_list = [1e-2, 1e-1]
# Time_list = [1e2, 1e3, 1e4, 5e4, 1e5, 5e5, 1e6]
# Time_list = [1e-1, 1e2, 1e4, 1e5, 5e5, 1e6, 1e7]
# Time_list = [1e5, 5e5, 1e6, 1e7]
# Time_list = [1.2e-8, 1e-7, 1e-6, 1e-5, 1e-4, 1e-3, 1e-2, 1e-1, 1]
Time_list = [1e-8, 0.0002, 0.00020001, 0.0003, 0.0004]


def plotEdensSingleTime(ax, prj_path, time, vmin=1, vmax=1e7):
    densDistr_directory = os.path.join(prj_path, comm.Density_Folder)
    file_path = comm.searchFilePathByTime(densDistr_directory, Dens_file_pattern, time)
    x, y, edens = comm.readData2D(file_path, 1)
    grid_z = comm.makeValueGridZ(x, y, edens)
    im = ax.imshow(grid_z, cmap=plt.cm.jet, vmin=vmin, vmax=vmax, origin='lower',
                   extent=[min(x), max(x), min(y), max(y)], aspect='auto', norm=LogNorm())
    return im


def plotTimesInOneFig(time_list):
    fig = plt.figure()
    for index, time in enumerate(time_list):
        ax = fig.add_subplot(3, 3, index + 1)
        time_file = comm.searchFilePathByTime(Density_directory, Dens_file_pattern, time)
        im = plotEdensSingleTime(ax, time_file)
    fig.subplots_adjust(right=0.8)
    ax_cb = fig.add_axes([0.85, 0.15, 0.05, 0.7])
    cb = plt.colorbar(im, cax=ax_cb)
    return


def plotTimesInFigs(prj_path, time_list):
    for index, time in enumerate(time_list):
        fig = plt.figure()
        ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
        im = plotEdensSingleTime(ax, prj_path, time)
        title = 'time = %2.0es' % time
        ax.set_title(title)
        plt.colorbar(im)
        #fig_name = os.path.join(r'C:\Users\Lunzhy\Desktop\pic', str(time))
        #fig.savefig(fig_name, dpi=600, bbox_inches='tight', pad_inches=0.1)
    return

def main():
    # hit_file = common.searchFileNameByTime(TrapDistr_directory, Trap_file_pattern, 1)
    # plotEdensSingleTime(hit_file)
    # plotTimesInOneFig(Time_list)
    plotTimesInFigs(Target_directory, Time_list)
    plt.show()
    return

if __name__ == '__main__': main()
