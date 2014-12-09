__author__ = 'lunzhy'
import os, sys
path = os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), os.pardir, os.pardir))
if not path in sys.path:
    sys.path.append(path)
import lib.common as cm
import matplotlib.pyplot as plt


Debug_path = cm.Debug_Folder_Path
Target_project = Debug_path
Target_project = '/home/lunzhy/SimCTM/projects/SSDM2014/p_side/Lg30_pSide'
Target_project = '/home/lunzhy/SimCTM/projects/SSDM2014/read_disturb/Ls20_pSide_zero'
Target_project = '/home/lunzhy/SimCTM/projects/CPB2014/ret_lowK/SiN/0.4'
Target_project = 'E:\PhD Study\SimCTM\SctmTest\HoleTunnelTest'
Time_list = [1e-6, 1e-2, 1.25, 1.58]

def plotCut():
    fig = plt.figure()
    ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
    for index, time in enumerate(Time_list):
        band_dir = os.path.join(Target_project, 'Band')
        file = cm.searchFilePathByTime(band_dir, 'band', time)
        # xCoord, occ = cm.cutAlignXY(file, coord_in_nm=10.5, col_index=3, along='x')
        x, y, cb, vb = cm.cutAlignXY(file, coord_in_nm=0, align='x')
        ax.plot(y, cb, c=cm.getColor(index), lw=3, label='%2.0es' % time)
        ax.plot(y, vb, c=cm.getColor(index), lw=3, label='%2.0es' % time)
    ax.set_xlabel('Y coordinate (nm)')
    ax.set_ylabel('Band Energy (eV)')
    # ax.set_ylim(0, 1)
    # legend = ax.legend(loc='lower left')
    return


if __name__ == '__main__':
    plotCut()
    plt.show()