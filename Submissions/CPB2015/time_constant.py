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


def write_time_const(project, time):
    prj_path = os.path.join(Directory_CPB2015, project)
    file = comm.searchFilePathByTime(os.path.join(prj_path, 'Trap'), 'timeTAT', time)
    x, y, cap_time, emi_time, occ = comm.cutAlignXY(file, coord_in_nm=0, align='x')
    file_to_write = os.path.join(Directory_CPB2015, project, 'time.txt')
    comm.write_data(file_to_write, y, cap_time, emi_time)
    return


def main():
    # write_time_const(os.path.join('tat_effect', '18V_tat'), 1e-2)
    # write_time_const(os.path.join('ret_T_effect', '330K_tat5e18'), 1e1)
    # write_time_const(os.path.join('tat_fitting', 'f_14V'), 1e-2)
    write_time_const(os.path.join('r_fitting', 'R_375K'), 1e7)
    return None

if __name__ == '__main__':
    main()