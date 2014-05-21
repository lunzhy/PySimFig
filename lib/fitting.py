__author__ = 'Lunzhy'
import os
from matplotlib.pyplot import *


Colors = ['black', 'blue', 'red', 'purple', 'fuchsia', 'gray', 'green', 'maroon',
          'navy', 'olive', 'orange', 'lime', 'silver', 'aqua', 'teal']
Linestyles = ['-', '--']
Markers = ['o', 's', 'v', 'd', 'h']
Flatband_File_Relpath = 'Miscellaneous\VfbShift.txt'


def readVfb(prj_path):
    """
    read the flat band voltage shift file in given project Directory
    @param Directory: the Directory of the project
    @return: time list and vfb list
    """
    file = os.path.join(prj_path, Flatband_File_Relpath)
    if not os.path.exists(file):
        return [], []
    data = np.loadtxt(file)
    times, vfbs = data[:, 0], data[:, 1]
    return times, vfbs


def getFlatbandList(exp_data, isShift=True):
    """
    get the flatband voltage shift value list from experiment data
    @param exp_data:
    @param isShift: check if the experiment data is voltage shift
    @return:
    """
    exp_data = sorted(exp_data, key=lambda x: x[1])
    if not isShift:
        min_voltage_tuple = min(exp_data, key=lambda x: x[1])
        min_voltage = min_voltage_tuple[1]
    else:
        min_voltage = 0
    flatband_list = [x[1] - min_voltage for x in exp_data]
    return flatband_list


def getTimeList(exp_data):
    """
    get the time list from experiment data
    @param exp_data:
    @return:
    """
    exp_data = sorted(exp_data, key=lambda x: x[1])
    time_list = [x[0] for x in exp_data]
    return time_list


########################## plot 1D problems ####################
def getColor(index):
    """
    get color in the Colors list
    """
    i = index % len(Colors)
    return Colors[i]


def getLinestyle(index):
    """
    get the linestyle
    @param index:
    @return:
    """
    i = index % len(Linestyles)
    return Linestyles[i]


def getMarker(index):
    """
    get the marker
    @param index:
    @return:
    """
    i = index % len(Markers)
    return Markers[i]


def plotExpVfb(ax, index, exp_time, exp_flatband, prj_label=""):
    exp_label = 'exp %s' % prj_label
    mark = getMarker(index)
    ax.plot(exp_time, exp_flatband, marker=mark, ls='None', fillstyle='none', ms=12, mew=3, mec=getColor(index),
            c=getColor(index), label=exp_label)
    return


def plotFittingVfb(ax, index, sim_time, sim_flatband, prj_label=""):
    """
    plot the comparison result
    @param ax:
    @param index: (color index, ls index)
    @param sim_time:
    @param sim_flatband:
    @param prj_label:
    @return:
    """
    sim_label = 'sim %s' % prj_label
    if len(index) == 1:
        color_index = index[0]
        ls_index = 0
    else:
        ls_index = index[0]
        color_index = index[1]
    ax.plot(sim_time, sim_flatband, ls=getLinestyle(ls_index), lw=3, c=getColor(color_index), label=sim_label)
    return


def test():
    file = os.path.join('E:\PhD Study\SimCTM\SctmTest\SolverPackTest', Flatband_File_Relpath)


if __name__ == '__main__': test()