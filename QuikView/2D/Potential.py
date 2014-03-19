__author__ = 'Lunzhy'
import os, sys, scipy
path = os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), os.pardir, os.pardir))
if not path in sys.path:
    sys.path.append(path)
import lib.common as cm
import matplotlib.pyplot as plt
import numpy as np

Target_folder = os.path.join(cm.Debug_Folder_Path, cm.Potential_Folder)
Potential_directory = os.path.join(cm.Debug_Folder_Path, cm.Potential_Folder)
Time_list = [1e-1, 1, 10, 1e2, 1e3, 1e4, 1e5, 5e5, 1e6]
# Time_list = [1e-1]


def plotSingleTime(ax, file_path):
    x, y, potential = cm.readData2D(file_path, 1)
    grid_z = cm.makeValueGridzWithMask(x, y, potential, cm.Debug_Folder_Path)
    im = ax.imshow(grid_z, cmap=plt.cm.jet, vmin=-3, vmax=0, origin='lower',
                   extent=[min(x), max(x), min(y), max(y)], aspect='auto')
    return im

def plotTimesInFigs(time_list):
    for index, time in enumerate(time_list):
        fig = plt.figure()
        ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
        time_file = cm.searchFilePathByTime(Potential_directory, 'potential', time)
        im = plotSingleTime(ax, time_file)
        title = 'time = %2.0es' % time
        ax.set_title(title)
        plt.colorbar(im)
    return


def main():
    # fig = plt.figure()
    # ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
    # im = plotSingleTime(ax, Target_folder, 1e-1)
    # plt.colorbar(im)
    plotTimesInFigs(Time_list)
    plt.show()

if __name__ == '__main__': main()