__author__ = 'Lunzhy'
#! /usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Lunzhy'

import platform, os

if platform.system() == 'Linux':
    Directory_Dissertation = r'/home/lunzhy/SimCTM/projects/Dissertation'
    Folder_Save_Figure = r'figures'
elif platform.system() == 'Windows':
    Directory_Dissertation = r'E:\PhD Study\Submissions\Dissertation\SctmData'
    Folder_Save_Figure = r'py_figures'
    File_Write_Data = r'E:\PhD Study\Submissions\Dissertation\SctmData\data.txt'

Is_Save_Figure = False


def save_figure(fig, name):
    if Is_Save_Figure:
        fig_path = os.path.join(Directory_Dissertation, Folder_Save_Figure, name)
        fig.savefig(fig_path+'.png', dpi=800, bbox_inches='tight', pad_inches=0.1)
    return