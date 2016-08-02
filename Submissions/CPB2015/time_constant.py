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


def write_time_const(project, time_list):
    prj_path = os.path.join(Directory_CPB2015, project)
    tat_current_list = ()
    for time in time_list:
        file = comm.searchFilePathByTime(os.path.join(prj_path, 'Trap'), 'timeTAT', time)
        x, y, cap_time, emi_time, occ = comm.cutAlignXY(file, coord_in_nm=0, align='x')
        tat_current = [1 / (a_cap_time + a_emi_time)
                       for a_cap_time, a_emi_time in zip(cap_time, emi_time)]
        tat_current_list = tat_current_list + (tat_current, )

    # tat_current_list = (y, ) + tat_current_list
    tat_current_list = (y, cap_time, emi_time, tat_current)
    file_to_write = os.path.join(Directory_CPB2015, project, 'time.txt')
    comm.write_data(file_to_write, *tat_current_list)
    return


def main():
    # time_list = [1e-4, 1.1e-4, 1.2e-4]
    time_list = [1e-6]
    write_time_const(os.path.join('tat_effect', '16V_tat'), time_list)
    time_list = [1e3, 1e5, 1e7]
    # write_time_const(os.path.join('ret_T_effect', '330K_tat5e18'), 1e1)
    # write_time_const(os.path.join('tat_fitting', 'f_14V'), 1e-4)
    write_time_const(os.path.join('r_fitting', 'R_375K'), time_list)
    return None

if __name__ == '__main__':
    main()