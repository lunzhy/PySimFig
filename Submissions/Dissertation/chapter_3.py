__author__ = 'lunzhy'
import os, sys
path = os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), os.pardir, os.pardir))
if not path in sys.path:
    sys.path.append(path)
import lib.common as cm
import matplotlib.pyplot as plt



Target_project = r'E:\PhD Study\Submissions\SCIS2015\SctmData\R_375K_previous'
File_to_write = r'E:\PhD Study\Submissions\SCIS2015\SctmData\data.txt'

Time_list = [1e1, 1e2, 1e3]


def write(prpty, keyword, time_list):
    data = ()
    for index, time in enumerate(time_list):
        prpty_dir = os.path.join(Target_project, prpty)
        file = cm.searchFilePathByTime(prpty_dir, keyword, time)
        if prpty == 'Trap':
            x, y, trap_e, occ_e, trap_h, occ_h = cm.cutAlignXY(file, coord_in_nm=0, align='x')
        else:
            x, y, trap_e = cm.cutAlignXY(file, coord_in_nm=0, align='x')
        data = data + (trap_e,)
    data = (y, ) + data
    cm.write_data(File_to_write, *data)
    return

if __name__ == '__main__':
    #  write('Trap', 'trap', Time_list)
    write('Density', 'eDens', Time_list)
