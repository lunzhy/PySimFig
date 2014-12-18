#! /usr/bin/env python3
# -*- coding: utf-8 -*- 
__author__ = 'Lunzhy'

# 2014.12.12
# demonstrate the result of the effect of curvature on the program, erasing and retention

import os, sys
path = os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), os.pardir))
if not path in sys.path:
    sys.path.append(path)
import matplotlib.pyplot as plt
import lib.common as cm


Project_Path = 'E:\PhD Study\SimCTM\SctmTest\HoleTunnelTest'
Temp_Data_File = os.path.join(Project_Path, 'data.txt')


def write_trap_occ():
    time = 1e-8
    file_trap = cm.searchFilePathByTime(os.path.join(Project_Path, 'Trap'), 'eTrap', time)
    y, etrapped, occ = cm.cutAlignX_1D(file_trap)
    cm.write_data(Temp_Data_File, y, occ)
    return


def write_edensity():
    time = 1e-9
    file_trap = cm.searchFilePathByTime(os.path.join(Project_Path, 'Density'), 'eDens', time)
    y, edens = cm.cutAlignX_1D(file_trap)
    cm.write_data(Temp_Data_File, y, edens)
    return


def main():
    write_trap_occ()
    # write_edensity()
    return


if __name__ == '__main__':
    main()