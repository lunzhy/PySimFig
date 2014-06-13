__author__ = 'lunzhy'
import os, sys
path = os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), os.pardir, os.pardir))
if not path in sys.path:
    sys.path.append(path)
import lib.common as cm
import matplotlib.pyplot as plt


Debug_path = cm.Debug_Folder_Path
Debug_path = r'/home/lunzhy/SimCTM/projects/SISPAD2014/retention/thick_300K_1.6eV_PF2e11'
Debug_path = '/home/lunzhy/SimCTM/projects/SSDM2014/p_side/Lg30_pSide'
Debug_path = '/home/lunzhy/SimCTM/projects/SSDM2014/read_disturb/Ls20_pSide_central'
Debug_path = '/home/lunzhy/SimCTM/projects/CPB2014/ret_400K_sideToCenter/Ls10_Lg10'
Time_list = [1e-8, 1e-6, 1e-4, 1e-2, 1e-1, 1]
Time_list = [1e-6, 0.0002, 0.00020001, 0.0003, 0.0004]
Time_list = [1, 10, 1e2, 1e3, 1e4, 1e5, 1e6]
Time_list = [1e2, 1e3, 1e4, 1e5, 1e6, 1e7, 1e8, 3e8]


def plotCut(ax=None, prj=Debug_path, time_list=Time_list, coord=0, align='y'):
    if ax == None:
        fig = plt.figure()
        ax = fig.add_axes([0.15, 0.15, 0.75, 0.75])
    for index, time in enumerate(time_list):
        band_dir = os.path.join(prj, 'Trap')
        time = float(time)
        file = cm.searchFilePathByTime(band_dir, 'trap', time)
        if align == 'y':
            x, y, etrapped, occ = cm.cutAlongXY(file, coord_in_nm=coord, align='y')
            ax.plot(x, etrapped, c=cm.getColor(index), lw=3, label='%2.0es' % time)
        elif align == 'x':
            x, y, etrapped, occ = cm.cutAlongXY(file, coord_in_nm=coord, align='x')
            ax.plot(y, etrapped, c=cm.getColor(index), lw=3, label='%2.0es' % time)
    if align == 'y':
        ax.set_xlabel('X coordinate (nm)')
    elif align == 'x':
        ax.set_xlabel('Y coordinate (nm)')
    ax.set_ylabel('Trapped Electron Density ($\mathbf{cm^{-3}}$)')
    # ax.set_ylim(0, 1)
    # ax.set_yscale('log')
    # legend = ax.legend(loc='lower left')
    return


if __name__ == '__main__':
    plotCut(coord=9)
    plt.show()