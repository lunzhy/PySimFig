#! /usr/bin/env python3
# -*- coding: utf-8 -*- 
__author__ = 'Lunzhy'
import os
import sys
path = os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), os.pardir, os.pardir))
if not path in sys.path:
    sys.path.append(path)
import lib.common as comm
from Submissions.CPB2015 import Directory_CPB2015


def write_time_const():
    prj_path = os.path.join(Directory_CPB2015, 'tat_effect', '18V_tat')
    file = comm.searchFilePathByTime(os.path.join(prj_path, 'Trap'), 'timeTAT', 1e-2)
    x, y, cap_time, emi_time, occ = comm.cutAlignXY(file, coord_in_nm=0, align='x')
    file_to_write = os.path.join(Directory_CPB2015, 'tat_effect', 'time.txt')
    comm.write_data(file_to_write, y, cap_time, emi_time)
    return


def main():
    write_time_const()
    return None

if __name__ == '__main__':
    main()