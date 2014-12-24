#! /usr/bin/env python3
# -*- coding: utf-8 -*- 
__author__ = 'lunzhy'
import os, sys
path = os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), os.pardir, os.pardir))
if not path in sys.path:
    sys.path.append(path)
import lib.common as cm
import matplotlib.pyplot as plt
import math


Debug_path = cm.Debug_Folder_Path
Target_project = Debug_path
Target_project = '/home/lunzhy/SimCTM/projects/SSDM2014/p_side/Lg30_pSide'
Target_project = '/home/lunzhy/SimCTM/projects/SSDM2014/read_disturb/Ls20_pSide_zero'
Target_project = '/home/lunzhy/SimCTM/projects/TED2014/ret_lowK/SiN/0.4'
Target_project = 'E:\PhD Study\SimCTM\SctmTest\HoleTunnelTest'
Target_project = r'E:\PhD Study\Submissions\TED2014\Revision\SctmData\r_highT\1e11'
Time_list = [1e-8, 1e-2, 1.25, 1.58]
Time_list = [1e-8]

def plotCut():
    V_in_MV = 1e-6
    fig = plt.figure()
    ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
    for index, time in enumerate(Time_list):
        band_dir = os.path.join(Target_project, 'ElecField')
        file = cm.searchFilePathByTime(band_dir, 'elec', time)
        x, y, efield_x, efield_y, efield = cm.cutAlignXY(file, coord_in_nm=95, align='x')
        efield_y = [math.fabs(ef) * V_in_MV for ef in efield_y]
        ax.plot(y, efield_y, c=cm.getColor(index), lw=3, label='%2.0es' % time)
    ax.set_xlabel('Y coordinate (nm)')
    ax.set_ylabel('Electric Field (MV/cm)')
    # ax.set_ylim(0, 25)
    # legend = ax.legend(loc='lower left')
    return


if __name__ == '__main__':
    plotCut()
    plt.show()