__author__ = 'Lunzhy'
import re, math, os, sys
import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate
from matplotlib.colors import LogNorm
from operator import itemgetter


############ global variables used in PySimFig ##############
Directory_Debug = r'E:\PhD Study\SimCTM\SctmTest\SolverPackTest'
Directory = r'E:\PhD Study\SimCTM\SctmTest\SolverPackTest'
Dir_Cmp = r'E:\PhD Study\SimCTM\SctmTest\ParameterCheck'
Dir_W_WO = r'E:\PhD Study\SimCTM\SctmTest\W_WO';
Dir_SaveFig = r'E:\PhD Study\SimCTM\SctmTest\figures'
Flatband_File_Relpath = 'Miscellaneous\VfbShift.txt'
TrapDistr_Folder = 'Trap'
Potential_Folder = 'Potential'

#Colors = ['r', 'g', 'b', 'c', 'm', 'y', 'k']
Colors = ['black', 'blue', 'fuchsia', 'gray', 'green', 'purple', 'maroon', 'red',
          'navy', 'olive', 'orange', 'lime', 'silver', 'aqua', 'teal']
Linestyles = ['-', '--']
Markers = ['o', 's', 'v', 'd', 'h']

Vfb_File_Name = 'VfbShift.txt'
Convert_cm_to_nm = 1e7

########### the common functions of PySimFig ###############
def getMarker(index):
    """
    get the marker
    @param index:
    @return:
    """
    i = index % len(Markers)
    return Markers[i]


def getLinestyle(index):
    """
    get the linestyle
    @param index:
    @return:
    """
    i = index % len(Linestyles)
    return Linestyles[i]


def getColor(index):
    """
    get color in the Colors list
    """
    i = index % len(Colors)
    return Colors[i]


def getColor_time(time):
    """
    get color according to the time
    @param time:
    @return:
    """
    arg = int(abs(math.log10(time)))
    return getColor(arg)


def fileCount(nameString):
    """
    count the file with specified name string
    """
    num = 0
    for file in os.listdir(Directory):
        if nameString in file:
            num += 1
    return num


def getCoordsInX(file):
    """
    get the coordinates in x direction, new
    @param file: name of the data file
    @return: (string) coordinate list in x direction
    """
    f = open(file)
    info = f.readline()
    xCoord_list = []
    while (True):
        line = f.readline()
        var_list = line.split()
        xCoord = var_list[0]
        if xCoord in xCoord_list:
            break
        else:
            xCoord_list.append(xCoord)
    f.close()
    return xCoord_list


def getPlottedValueList(file, xCoord):
    """
    get the value list to be plotted, new
    @param file: data file name
    @param xCoord: (string) the coordinate in x direction
    @return:
    """
    f = open(file)
    info = f.readline()
    data_tupleList = []
    for line in f.readlines():
        if not line:
            continue
        line_data = line.split()
        if line_data[0] == xCoord:
            line_data = [float(value) for value in line_data]
            line_data[0] = line_data[0] * Convert_cm_to_nm
            line_data[1] = line_data[1] * Convert_cm_to_nm
            data_tupleList.append(tuple(line_data))
    data_list = list(zip(*data_tupleList))
    return data_list


def sliceX(file):
    """
    old
    sliceX gets the list of x coordinates and the number of vertex in x direction
    @param file:
    @return:
    """
    f = open(file)
    info = f.readline()
    currY = 0
    xList = []
    while (True):
        aLine = f.readline()
        aList = aLine.split()
        if len(xList) == 0 or currY == aList[1]:
            xList.append(aList[0])
        else:
            break
    f.close()
    return xList, len(xList)


def getTimeLabel(filename):
    """
    get the time string and corresponding label for plotting
    @param filename:
    @return: time string and label for plotting
    """
    f = open(filename)
    title = f.readline()
    f.close()
    match = re.search(r'\[.+\]', title)
    time = match.group()
    time = float(time[1:-1])
    # time = '%.0e' % time
    label = 'Time = ' + str(time) + 's'
    return time, label


def isPlot(filename):
    """
    plot only when the expotential argument is integer
    @param filename:
    @return:
    """
    time, labelTime = getTimeLabel(filename)
    time = float(time)
    return math.log10(time) == math.floor(math.log10(time))


def getStepNumber(filename):
    """
    get the step number from file name
    @param filename:
    @return:
    """
    match = re.search(r's.+\.', filename)
    suffix = match.group()
    return int(suffix[1:-1])


def getFiles(directory, filenameBase):
    """
    get the full filenames of correct sequence in a Directory containing the fileNameBase
    @param directory:
    @param filenameBase:
    @return:
    """
    fileList = []
    for file in os.listdir(directory):
        if filenameBase in file:
            fileList.append(file)
    fileList = sorted(fileList, key=getStepNumber)
    for index, file in enumerate(fileList):
        file = os.path.join(directory, file)
        fileList[index] = file
    return fileList


def saveFigure(fig, name):
    """

    @param plt:
    @param name:
    @return:
    """
    figname = os.path.join(common.figSaveDir, name)
    fig.savefig(figname, dpi=600)
    return


def getTime(filename):
    """
    get the time string and corresponding label for plotting
    @param filename:
    @return: time step of the file
    """
    f = open(filename)
    title = f.readline()
    f.close()
    match = re.search(r'\[.+\]', title)
    time = match.group()
    time = float(time[1:-1])
    return time


def searchFilePathByTime(folder, pattern, time):
    time_filepath = []  # stores tuple (time, file_path)
    for file in os.listdir(folder):
        if pattern in file:
            file_path = os.path.join(folder, file)
            time_filepath.append((getTime(file_path), file_path))
    time_filepath = sorted(time_filepath, key=itemgetter(0))
    time_diff = [math.fabs(time - time_path[0]) for time_path in time_filepath]
    min_index = time_diff.index(min(time_diff))
    return time_filepath[min_index][1]


def readVfb(directory, isFile=False):
    """
    read the flat band voltage shift file in given Directory
    @param directory: the Directory of the project
    @return: time list and vfb list
    """
    if not isFile:
        file = os.path.join(directory, Flatband_File_Relpath)
    else:
        file = directory
    data = np.loadtxt(file)
    times, vfbs = data[:, 0], data[:, 1]
    return times, vfbs


########## specificly used in plotting 1D figures ##########
def getDataAlongY_1D(filename, col_index):
    """
    get data along y direction for the first slice
    @param filename: the file path containing the data
    @param col_index: the column index of the required data in the file
    @return: y coordinates list, required data list
    """
    xCoords = getCoordsInX(filename)
    data = getPlottedValueList(filename, xCoords[0])
    y = data[1]  # data[0] is the xCoords
    val = data[col_index]
    return y, val


def readData1D(file, xSkip):
    """
    odd
    read the file and get the data list for 1D plotting
    @param file:
    @param xSkip:
    @return:
    """
    data = np.loadtxt(file, skiprows=1)
    x, y, val = data[:, 0], data[:, 1], data[:, 2]
    x, y = x / 1e-7, y / 1e-7
    x, y = x - min(x), y - min(y)
    # get the first slice of the data, i.e. the slice with x=0
    y, val = y[::xSkip], val[::xSkip]
    return y, val


########## specificly used in plotting 2D figures ##########

def readData2D(file, skip = 1):
    data = np.loadtxt(file, skiprows=skip)
    cols = data.shape[1] # return ndarray shape
    x, y, val = data[:, 0], data[:, 1], data[:, 2]
    x, y = x * Convert_cm_to_nm, y * Convert_cm_to_nm
    if cols == 3:
        return x, y, val
    elif cols == 4:
        val_second = data[:, 3]
        return x, y, val, val_second
    return None


def makeValueGridZ(x, y, values):
    xi, yi = np.linspace(min(x), max(x), 100), np.linspace(min(y), max(y), 100)
    grid_x, grid_y = np.meshgrid(xi, yi)
    grid_z = scipy.interpolate.griddata((x, y), values, (grid_x, grid_y), method='linear')
    return grid_z
