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
# Target_directory = r'/home/lunzhy/SimCTM/projects/SISPAD2014/retention/4nm_350K_1.6eV_PF2e11_T2B5e5'
# Target_directory = '/home/lunzhy/SimCTM/projects/SISPAD2014/retention/diff_thick/trap6'
# Target_directory = '/home/lunzhy/SimCTM/projects/SSDM2014/standard_program/1e5_1e11_1.7_0.1'
Target_directory = '/home/lunzhy/SimCTM/projects/SSDM2014/p_side/Ls10_noSide'
# Target_directory = '/home/lunzhy/SimCTM/projects/SSDM2014/p_fitting/15V'
# Target_directory = '/home/lunzhy/SimCTM/projects/SSDM2014/r_common/Ls20_eSide_360K'
# Target_directory = '/home/lunzhy/SimCTM/projects/SSDM2014/p_side_pass/Ls20_pSide'
# Target_directory = '/home/lunzhy/SimCTM/projects/SSDM2014/read_disturb/Ls20_noSide_central'
Target_directory = '/home/lunzhy/SimCTM/projects/CPB2014/ret_lowK/SiN/0.1'
Target_directory = '/home/lunzhy/SimCTM/projects/CPB2014/ret_highK/frequency/1e12'
Target_directory = '/home/lunzhy/SimCTM/projects/CPB2014/ret_highK_side/all'
Target_directory = '/home/lunzhy/SimCTM/projects/CPB2014/ret_360K_sideToCenter/Ls10_Lg10'
# Target_directory = '/home/lunzhy/SimCTM/projects/CPB2014/ret_compare/highK'
# Target_directory = '/home/lunzhy/SimCTM/projects/SolverTest/pardiso'
TrapDistr_directory = os.path.join(Target_directory, comm.TrapDistr_Folder)
Trap_file_pattern = 'trapOccupation'
# Time_list = [2e-9, 1e-8, 1e-7, 1e-6, 1e-5, 1e-4, 1e-3, 1e-2, 1e-1, 1]
# Time_list = [2e-9, 1e-8, 1e-7, 1e-6, 1e-5, 1e-4, 1e-3, 1e-2, 1e-1, 1]
# Time_list = [1e-2, 1e-1]
# Time_list = [1e2, 1e3, 1e4, 5e4, 1e5, 5e5, 1e6]
# Time_list = [1e-1, 1e2, 1e4, 1e5, 5e5, 1e6, 1e7]
# Time_list = [1e5, 5e5, 1e6, 1e7]
# Time_list = [1.2e-8, 1e-7, 1e-6, 1e-5, 1e-4, 1e-3, 1e-2, 1e-1, 1]
# Time_list = [i * 1e-4 for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
# Time_list = [200e-6]
Time_list = [1e-8, 1e-5, 1e-4, 1e6]
Time_list = [0.1, 1e2, 1e4, 1e6, 1e7, 3e8]
# Time_list = [1e-8, 4e-4, 1]


def plotOccSingleTime(ax, prj_path, time):
    trapDistr_directory = os.path.join(prj_path, comm.TrapDistr_Folder)
    file_path = comm.searchFilePathByTime(trapDistr_directory, Trap_file_pattern, time)
    x, y, etrap, trapOcc = comm.readData2D(file_path, 1)
    grid_z = comm.makeValueGridZ(x, y, trapOcc)
    im = ax.imshow(grid_z, cmap=plt.cm.jet, vmin=1e-4, vmax=1, origin='lower',
                   extent=[min(x), max(x), min(y), max(y)], aspect='auto', norm=LogNorm())
    return im


def plotDensitySingleTime(ax, prj_path, time):
    trapDistr_directory = os.path.join(prj_path, comm.TrapDistr_Folder)
    file_path = comm.searchFilePathByTime(trapDistr_directory, Trap_file_pattern, time)
    x, y, etrap, trapOcc = comm.readData2D(file_path, 1)
    grid_z = comm.makeValueGridZ(x, y, etrap)
    im = ax.imshow(grid_z, cmap=plt.cm.jet, vmin=1e16, vmax=1e20, origin='lower',
                   extent=[min(x), max(x), min(y), max(y)], aspect='auto', norm=LogNorm())
    return im


def plotTimesInOneFig(time_list):
    fig = plt.figure()
    for index, time in enumerate(time_list):
        ax = fig.add_subplot(3, 3, index + 1)
        time_file = comm.searchFilePathByTime(TrapDistr_directory, Trap_file_pattern, time)
        im = plotOccSingleTime(ax, time_file)
    fig.subplots_adjust(right=0.8)
    ax_cb = fig.add_axes([0.85, 0.15, 0.05, 0.7])
    cb = plt.colorbar(im, cax=ax_cb)
    return


def plotTimesInFigs(prj_path, time_list):
    for index, time in enumerate(time_list):
        fig = plt.figure()
        ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
        im = plotOccSingleTime(ax, prj_path, time)
        title = 'time = %2.0es' % time
        ax.set_title(title)
        # ax.set_xticks([0, 15, 45, 75, 105, 135, 165, 180])
        plt.colorbar(im)
        #fig_name = os.path.join(r'C:\Users\Lunzhy\Desktop\pic', str(time))
        #fig.savefig(fig_name, dpi=600, bbox_inches='tight', pad_inches=0.1)
    return

def main():
    # hit_file = common.searchFileNameByTime(TrapDistr_directory, Trap_file_pattern, 1)
    # plotOccSingleTime(hit_file)
    # plotTimesInOneFig(Time_list)
    plotTimesInFigs(Target_directory, Time_list)
    plt.show()
    return

if __name__ == '__main__': main()