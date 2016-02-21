__author__ = 'Lunzhy'
#! /usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Lunzhy'

import platform, os

if platform.system() == 'Linux':
    Directory_CPB2015 = r'/home/lunzhy/SimCTM/projects/CPB2015'
    Folder_Save_Figure = r'figures'
elif platform.system() == 'Windows':
    Directory_CPB2015 = r'E:\PhD Study\Submissions\CPB2015\SctmData'
    Folder_Save_Figure = r'py_figures'
    File_Write_Data = r'E:\PhD Study\Submissions\CPB2015\SctmData\data.txt'

Is_Save_Figure = False


def save_figure(fig, name):
    if Is_Save_Figure:
        fig_path = os.path.join(Directory_CPB2015, Folder_Save_Figure, name)
        fig.savefig(fig_path+'.png', dpi=800, bbox_inches='tight', pad_inches=0.1)
    return