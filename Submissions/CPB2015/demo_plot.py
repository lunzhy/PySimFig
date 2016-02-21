#! /usr/bin/env python3
# -*- coding: utf-8 -*- 
__author__ = 'Lunzhy'
import os
import sys
path = os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), os.pardir, os.pardir))
if path not in sys.path:
    sys.path.append(path)
import lib.common as comm
from Submissions.CPB2015 import Directory_CPB2015, File_Write_Data


def plot_band():
    band_dir = os.path.join(os.path.join(Directory_CPB2015, 'trap_energy', 'trap_1.0'), 'Band')
    file = comm.searchFilePathByTime(band_dir, 'band', 1e-8)
    x, y, cb, vb = comm.cutAlignXY(file, coord_in_nm=0, align='x')
    print(File_Write_Data)
    comm.write_data(File_Write_Data, y, cb, vb)
    return None


def main():
    plot_band()


if __name__ == '__main__':
    main()


