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
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
from matplotlib.colors import SymLogNorm


def get_condition(prj_name):
    splits = prj_name.split('_')
    trap_energy, frq = float(splits[0][1:]), float(splits[1][1:])
    return trap_energy, frq


def read_vfb_shift(prj_path):
    # current_folder = os.path.join(prj_path, 'Miscellaneous')
    try:
        time_list, vfb_list = comm.read_vfb(prj_path)
    except FileNotFoundError:
        return 0
    vfb_shift = vfb_list[-1] - vfb_list[0]
    return vfb_shift


def main():
    main_prj = os.path.join(Directory_CPB2015, 'ret_trap_energy_frq')
    frq_list, trap_energy_list, vfb_shift_list = [], [], []
    for prj_name in os.listdir(main_prj):
        if prj_name == 'sample':
            continue
        if 'txt' in prj_name:
            continue
        trap_energy, frq = get_condition(prj_name)
        prj_path = os.path.join(main_prj, prj_name)
        vfb_shift = read_vfb_shift(prj_path)
        frq_list.append(frq)
        trap_energy_list.append(trap_energy)
        vfb_shift_list.append(vfb_shift)
    comm.write_data(os.path.join(main_prj, 'trap_frq.txt'), trap_energy_list, frq_list,
                    vfb_shift_list)
    return None


if __name__ == '__main__':
    main()