__author__ = 'Lunzhy'
import re, math, os, sys
import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate
from matplotlib.colors import LogNorm
from operator import itemgetter
path = os.path.abspath(os.path.dirname(__file__))
if not path in sys.path:
    sys.path.append(path)
import parameter as param


############ global variables used in PySimFig ##############
# platform related
Debug_Folder_Path = r'E:\PhD Study\SimCTM\SctmTest\SolverPackTest'
Default_Parfile_Path = r'E:\PhD Study\SimCTM\default.param'

#file and folder name of relative path
Flatband_File_Relpath = 'Miscellaneous\VfbShift.txt'
TrapDistr_Folder = 'Trap'
Potential_Folder = 'Potential'
User_Param_File = r'user.param'
Vfb_File = 'VfbShift.txt'

# related to matplotlib
Colors = ['black', 'blue', 'fuchsia', 'gray', 'green', 'purple', 'maroon', 'red',
          'navy', 'olive', 'orange', 'lime', 'silver', 'aqua', 'teal']
Linestyles = ['-', '--']
Markers = ['o', 's', 'v', 'd', 'h']

# physics
Convert_cm_to_nm = 1e7

############ global parameters not in used ##################
Dir_Cmp = r'E:\PhD Study\SimCTM\SctmTest\ParameterCheck'
Dir_W_WO = r'E:\PhD Study\SimCTM\SctmTest\W_WO';
Dir_SaveFig = r'E:\PhD Study\SimCTM\SctmTest\figures'



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


def getCoordsInXY(file, mode='x'):
    """
    get the coordinates in x direction, new
    @param file: name of the data file
    @return: (string) coordinate list in x direction
    """
    f = open(file)
    info = f.readline()
    coord_list = []
    while (True):
        line = f.readline()
        if not line:
            break
        var_list = line.split()
        if mode=='x':
            coord = var_list[0]
            if coord in coord_list:
                break
            else:
                coord_list.append(coord)
        elif mode=='y':
            coord = var_list[1]
            if coord in coord_list:
                continue
            else:
                coord_list.append(coord)
    f.close()
    return coord_list


def getPlottedValueList(file, coord, mode='x'):
    """
    get the value list to be plotted, new
    @param file: data file name
    @param coord: (string) the coordinate in x direction
    @return:
    """
    f = open(file)
    info = f.readline()
    data_tupleList = []
    for line in f.readlines():
        if not line:
            continue
        line_data = line.split()
        if mode=='x':
            index = 0
        elif mode=='y':
            index = 1
        if line_data[index] == coord:
            line_data = [float(value) for value in line_data]
            line_data[0] = line_data[0] * Convert_cm_to_nm
            line_data[1] = line_data[1] * Convert_cm_to_nm
            data_tupleList.append(tuple(line_data))
    data_list = list(zip(*data_tupleList))
    return data_list


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
    xCoords = getCoordsInXY(filename)
    data = getPlottedValueList(filename, xCoords[0])
    y = data[1]  # data[0] is the xCoords
    val = data[col_index]
    return y, val


########## specificly used in plotting 2D figures ##########
def cutAlongXY(filename, coord_in_nm, col_index, along='x'):
    # the along value is different from align value
    if along == 'x':
        align = 'y'
        data_index = 0
    elif along == 'y':
        align = 'x'
        data_index = 1
    coords_list = getCoordsInXY(filename, align)
    coord_in_cm = coord_in_nm * 1e-7
    coord_diff = [math.fabs(coord_in_cm - float(coord)) for coord in coords_list]
    min_index = coord_diff.index(min(coord_diff))
    data = getPlottedValueList(filename, coords_list[min_index], align)
    x_or_y = data[data_index]
    val = data[col_index]
    return x_or_y, val


def cutAlongY(filename, x_in_nm, col_index):
    xCoords = getCoordsInXY(filename, 'x')
    x_in_cm = x_in_nm * 1e-7
    coord_diff = [math.fabs(x_in_cm - float(coord)) for coord in xCoords]
    min_index = coord_diff.index(min(coord_diff))
    data = getPlottedValueList(filename, xCoords[min_index], 'x')
    y = data[0]
    val = data[col_index]
    return y, val


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


def makeValueGridzWithMask(x, y, values, prj_path):
    xi, yi = np.linspace(min(x), max(x), 100), np.linspace(min(y), max(y), 100)
    grid_x, grid_y = np.meshgrid(xi, yi)
    grid_z = scipy.interpolate.griddata((x, y), values, (grid_x, grid_y), method='linear')

    tunnel_thick = float(param.getParamValue('tc.tunnel.thick', prj_path))
    trap_thick = float(param.getParamValue('tc.trap.thick', prj_path))
    block_thick = float(param.getParamValue('tc.block.thick', prj_path))
    gate1_width = float(param.getParamValue('tc.gate1.width', prj_path))
    iso2_width = float(param.getParamValue('tc.iso2.width', prj_path))
    gate2_width = float(param.getParamValue('tc.gate2.width', prj_path))
    iso3_width = float(param.getParamValue('tc.iso3.width', prj_path))
    gate3_width = float(param.getParamValue('tc.gate3.width', prj_path))
    main_thick = tunnel_thick + trap_thick + block_thick

    mask_y = np.array(grid_y > main_thick)
    mask_x_gate1 = np.array( grid_x < gate1_width)
    mask_x_gate2 = np.logical_and(grid_x > gate1_width + iso2_width,
                                grid_x < gate1_width + iso2_width + gate2_width)
    mask_x_gate3 = np.logical_and(grid_x> gate1_width + iso2_width + gate2_width + iso3_width,
                                  grid_x <= gate1_width + iso2_width + gate2_width + iso3_width + gate3_width)
    mask_z = mask_y & (mask_x_gate1 | mask_x_gate2 | mask_x_gate3)
    grid_z_masked = np.ma.array(grid_z, mask=mask_z)
    return grid_z_masked