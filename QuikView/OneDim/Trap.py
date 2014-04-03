__author__ = 'lunzhy'
import os, sys
path = os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), os.pardir, os.pardir))
if not path in sys.path:
    sys.path.append(path)
import lib.common as cm
import matplotlib.pyplot as plt


Debug_path = cm.Debug_Folder_Path
Time_list = [1e6]

def plotCut():
    fig = plt.figure()
    ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
    for index, time in enumerate(Time_list):
        band_dir = os.path.join(Debug_path, 'Trap')
        file = cm.searchFilePathByTime(band_dir, 'trap', time)
        x, y, etrapped, occ = cm.cutAlongXY(file, coord_in_nm=0, align='y')
        ax.plot(y, etrapped, c=cm.getColor(index), lw=3, label='%2.0es' % time)
        # x, y, etrapped, occ = cm.cutAlongXY(file, coord_in_nm=4, along='x')
        # ax.plot(x, etrapped, c=cm.getColor(index), lw=3, label='%2.0es' % time)
    ax.set_xlabel('Y coordinate (nm)')
    ax.set_ylabel('Trap Occupy')
    # ax.set_ylim(0, 1)
    ax.set_yscale('log')
    # legend = ax.legend(loc='lower left')
    return


if __name__ == '__main__':
    plotCut()
    plt.show()