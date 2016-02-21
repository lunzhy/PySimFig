#! /usr/bin/env python3
# -*- coding: utf-8 -*- 
__author__ = 'Lunzhy'
import os
import sys
import numpy as np
import scipy
path = os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), os.pardir, os.pardir))
if path not in sys.path:
    sys.path.append(path)
import lib.common as comm
from Submissions.CPB2015 import Directory_CPB2015


File_to_write = r'E:\PhD Study\Submissions\CPB2015\SctmData\ret_T_effect\current.txt'


def write_current_FN(prj_path):
    current_folder = os.path.join(prj_path, 'Current')
    time_list, curr_dens_list = [], []
    for file_name in os.listdir(current_folder):
        if 'eCurr' in file_name:
            file_path = os.path.join(current_folder, file_name)
            time_step = comm.getTime(file_path)
            x, y, curr_dens, curr_dens_x, curr_dens_y = comm.cutAlignXY(file_path, 0, align='x')
            time_list.append(time_step)
            curr_dens_list.append(curr_dens_y[0])
    time_list, curr_dens_list = zip(*sorted(zip(time_list, curr_dens_list),
                                            key=lambda pair: pair[0]))

    time_list, tat_curr_dens_list = [], []
    for file_name in os.listdir(current_folder):
        if 'eTAT_' in file_name:
            file_path = os.path.join(current_folder, file_name)
            time_step = comm.getTime(file_path)
            x, y, tat_curr_dens = comm.read_data(file_path, usecols=(0, 1, 2))
            time_list.append(time_step)
            tat_curr_dens_list.append(tat_curr_dens[0])
    time_list, tat_curr_dens_list = zip(*sorted(zip(time_list, tat_curr_dens_list),
                                            key=lambda pair: pair[0]))

    # print(len(time_list), len(curr_dens_list), len(tat_curr_dens_list))
    comm.write_data(File_to_write, time_list, curr_dens_list, tat_curr_dens_list)


def write_current_TAT(prj_path):
    current_folder = os.path.join(prj_path, 'Current')
    time_list, curr_dens_list = [], []
    for file_name in os.listdir(current_folder):
        if 'eTAT' in file_name:
            file_path = os.path.join(current_folder, file_name)
            time_step = comm.getTime(file_path)
            x, y, curr_dens = comm.read_data(file_path, usecols=(0, 1, 2))
            time_list.append(time_step)
            curr_dens_list.append(curr_dens[0])
    time_list, curr_dens_list = zip(*sorted(zip(time_list, curr_dens_list),
                                            key=lambda pair: pair[0]))
    comm.write_data(File_to_write, time_list, curr_dens_list)


def main():
    write_current_FN(r'E:\PhD Study\Submissions\CPB2015\SctmData\ret_T_effect\330K_tat5e18')
    return


if __name__ == '__main__':
    main()