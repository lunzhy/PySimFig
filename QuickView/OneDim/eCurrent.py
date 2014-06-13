__author__ = 'lunzhy'
import os, sys, math
path = os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), os.pardir, os.pardir))
if not path in sys.path:
    sys.path.append(path)
import lib.common as cm
import matplotlib.pyplot as plt


Debug_path = cm.Debug_Folder_Path
Time_list = [0.001]

def plotCut():
    fig = plt.figure()
    ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
    for index, time in enumerate(Time_list):
        band_dir = os.path.join(Debug_path, 'Current')
        file = cm.searchFilePathByTime(band_dir, 'eCurr', time)
        x, y, curr, xcurr, ycurr = cm.cutAlongXY(file, coord_in_nm=2, align='y')
        # ycurr = [math.fabs(current) for current in curr]
        # ax.plot(y, ycurr, c=cm.getColor(index), lw=3, label='%2.0es' % time)
        x, y, curr, xcurr, ycurr = cm.cutAlongXY(file, coord_in_nm=4.2, align='x')
        ax.plot(x, xcurr, c=cm.getColor(index), lw=3, label='%2.0es' % time)
    ax.set_xlabel('Y coordinate (nm)')
    ax.set_ylabel('Current density')
    # ax.set_yscale('log')
    # ax.set_ylim(-1, 1)
    # legend = ax.legend(loc='lower left')
    return


if __name__ == '__main__':
    plotCut()
    plt.show()