#! /usr/bin/env python3
# -*- coding: utf-8 -*- 
__author__ = 'Lunzhy'

import platform, os

if platform.system() == 'Linux':
    Directory_RTED2014 = r'/home/lunzhy/SimCTM/projects/R_TED2014'
    Folder_Save_Figure = r'figures'
elif platform.system() == 'Windows':
    Directory_RTED2014 = r'E:\PhD Study\Submissions\TED2014\Revision\SctmData'
    Folder_Save_Figure = r'py_figures'
    Folder_Write_Data = r'E:\PhD Study\Submissions\TED2014\Revision\SctmData\data.txt'

Is_Save_Figure = True


def save_figure(fig, name):
    if Is_Save_Figure:
        fig_path = os.path.join(Directory_RTED2014, Folder_Save_Figure, name)
        fig.savefig(fig_path+'.png', dpi=800, bbox_inches='tight', pad_inches=0.1)
    return