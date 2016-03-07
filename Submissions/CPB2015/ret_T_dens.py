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


File_to_write = r'E:\PhD Study\Submissions\CPB2015\SctmData\ret_T_dens\voltage.txt'


def get_condition(prj_name):
    splits = prj_name.split('_')
    temperature, dens = splits[0], splits[1][3:]
    return temperature, dens


def read_vfb_shift(prj_path):
    # current_folder = os.path.join(prj_path, 'Miscellaneous')
    try:
        time_list, vfb_list = comm.read_vfb(prj_path)
    except FileNotFoundError:
        return 0
    vfb_shift = vfb_list[200]
    return vfb_shift


def main():
    main_prj = os.path.join(Directory_CPB2015, 'ret_T_dens')
    temperature_list, dens_list, vfb_shift_list = [], [], []
    for prj_name in os.listdir(main_prj):
        if prj_name == 'sample':
            continue
        if 'txt' in prj_name:
            continue
        temperature, dens = get_condition(prj_name)
        prj_path = os.path.join(main_prj, prj_name)
        vfb_shift = read_vfb_shift(prj_path)
        dens_list.append(dens)
        temperature_list.append(temperature)
        vfb_shift_list.append(vfb_shift)
    comm.write_data(os.path.join(main_prj, 't_dens.txt'), temperature_list, dens_list,
                    vfb_shift_list)
    return None


if __name__ == '__main__':
    main()