__author__ = 'lunzhy'
import os, sys
path = os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), os.pardir, os.pardir))
if not path in sys.path:
    sys.path.append(path)
import lib.common as cm
import matplotlib.pyplot as plt


Debug_path = cm.Debug_Folder_Path
Debug_path = '/home/lunzhy/SimCTM/projects/SSDM2014/p_side/Lg30_pSide'
Time_list = [1e-8, 1e-6, 1e-4, 1e-3, 1e-2, 1e-1, 1]
Time_list = [1e-8, 0.0002, 0.00020001, 0.0003, 0.0004]


def plotCut():
    fig = plt.figure()
    ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
    for index, time in enumerate(Time_list):
        band_dir = os.path.join(Debug_path, 'Density')
        file = cm.searchFilePathByTime(band_dir, 'eDens', time)
        x, y, edens = cm.cutAlongXY(file, coord_in_nm=30, align='x')
        ax.plot(y, edens, c=cm.getColor(index), lw=3, label='%2.0es' % time)
        # x, y, edens = cm.cutAlongXY(file, coord_in_nm=50, align='x')
        # ax.plot(x, edens, c=cm.getColor(index), lw=3, label='%2.0es' % time)
    ax.set_xlabel('Y coordinate (nm)')
    ax.set_ylabel('Electron density')
    ax.set_ylim(1e5, 1e15)
    ax.set_yscale('log')
    # legend = ax.legend(loc='lower left')
    return


if __name__ == '__main__':
    plotCut()
    plt.show()