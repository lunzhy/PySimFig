__author__ = 'Lunzhy'
import matplotlib.pyplot as plt
import os, sys
path = os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), '..'))
if not path in sys.path:
    sys.path.append(path)
import lib.common as cm
from matplotlib import font_manager

Main_path = r'E:\PhD Study\SimCTM\SctmTest\Temp\mobility'
# prj_list = ['1', '1e-1', '1e-2', '1e-3', '1e-7']
prj_list = ['1', '1e-2', '1e-7']
# prj_list = [os.path.join(Main_path, prj) for prj in prj_list]
Time = 1e-2

Debug_path = r'/home/lunzhy/SimCTM/debug'
Time_list = [1e-1, 1e1, 1e2, 1e3, 1e4, 1e5, 1e6]
# Time_list = [1e-9, 1e-8, 1e-7, 1e-6, 1e-5, 1e-4, 1e-3, 1e-2, 1e-1, 1]


def plotCutAlongX():
    fig = plt.figure()
    ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
    for index, time in enumerate(Time_list):
        trap_dir = os.path.join(Debug_path, 'Trap')
        file = cm.searchFilePathByTime(trap_dir, 'Occ', time)
        # xCoord, occ = cm.cutAlongXY(file, coord_in_nm=10.5, col_index=3, along='x')
        x, y, dens, occ = cm.cutAlongXY(file, coord_in_nm=60, along='y')
        ax.plot(y, occ, c=cm.getColor(index), lw=3, label='%2.0es' % time)
    ax.set_xlabel('Y coordinate (nm)')
    ax.set_ylabel('Trap Occupation Rate')
    ax.set_ylim(0, 1)
    legend = ax.legend(loc='lower left')
    return


def compareElecDensity():
    fig = plt.figure()
    ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
    for index, prj in enumerate(prj_list):
        density_dir = os.path.join(Main_path, prj, 'Density')
        file = cm.searchFilePathByTime(density_dir, 'eDens', Time)
        yCoord, density = cm.getDataAlongY_1D(file, 2)
        ax.plot(yCoord, density, c=cm.getColor(index), lw=3, label=prj)
    ax.set_yscale('log')
    ax.set_ylim(1e5, 1e16)
    ax.set_xlabel('Distance Along Trapping Layer (nm)')
    ax.set_ylabel('Electron Density in Conduction Band (cm^-3)')
    legend = ax.legend(loc='lower left')
    #plt.show()
    return


def compareTrapOcc():
    fig = plt.figure()
    ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
    for index, prj in enumerate(prj_list):
        trap_dir = os.path.join(Main_path, prj, 'Trap')
        file = cm.searchFilePathByTime(trap_dir, 'Occ', Time)
        yCoord, occ = cm.getDataAlongY_1D(file, 3)
        ax.plot(yCoord, occ, c=cm.getColor(index), lw=3, label=prj)
    #ax.set_yscale('log')
    ax.set_xlabel('Distance Along Trapping Layer (nm)')
    ax.set_ylabel('Trap Occupation Rate (cm^-3)')
    ax.set_ylim(0, 1.05)
    legend = ax.legend(loc='lower left')
    #plt.show()
    return


def compareVfb():
    fig = plt.figure()
    ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
    for index, prj in enumerate(prj_list):
        prj_path = os.path.join(Main_path, prj)
        time, vfb = cm.readVfb(prj_path)
        ax.plot(time, vfb, c=cm.getColor(index), lw=3, label=prj)
    ax.set_xscale('log')
    ax.set_xlabel('Programming Time (s)')
    ax.set_ylabel('Flatband Voltage (V)')
    ax.legend(loc='upper left')
    legend = ax.legend(loc='lower left')
    #plt.show()
    return

if __name__ == '__main__':
    #compareVfb()
    #compareElecDensity()
    #compareTrapOcc()
    plotCutAlongX()
    plt.show()