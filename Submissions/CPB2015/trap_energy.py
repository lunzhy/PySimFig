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

Prj_name = 'trap_energy_400K'


def write_current():
    trap_energy = ['1.0', '1.6', '1.7', '1.8', '1.9', '2.0',
                   '2.1', '2.2', '2.3', '2.4', '2.5', '2.6', '2.7']
    current_list = []
    for energy in trap_energy:
        prj_path = os.path.join(Directory_CPB2015, Prj_name, 'trap_%s' % energy)
        file_path = comm.searchFilePathByTime(os.path.join(prj_path, 'Current'), 'eTAT', 1e-2)
        x, y, current = comm.read_data(file_path)
        current_list.append(current[0])
    comm.write_data(os.path.join(Directory_CPB2015, Prj_name, 'data.txt'), trap_energy,
                    current_list)
    return


def main():
    write_current()

if __name__ == '__main__':
    main()