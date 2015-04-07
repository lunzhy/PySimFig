#! /usr/bin/env python3
# -*- coding: utf-8 -*- 
__author__ = 'lunzhy'
import platform, os

if platform.system() == 'Linux':
    Directory_Journal2015 = r'/home/lunzhy/SimCTM/projects/Journal2015'
    Folder_Save_Figure = r'figures'
elif platform.system() == 'Windows':
    Directory_Journal2015 = r'E:\PhD Study\Submissions\Journal2015\Revision\SctmData'
    Folder_Save_Figure = r'py_figures'
    Folder_Write_Data = r'E:\PhD Study\Submissions\Journal2015\Revision\SctmData\data.txt'

Is_Save_Figure = False


def save_figure(fig, name):
    if Is_Save_Figure:
        fig_path = os.path.join(Directory_Journal2015, Folder_Save_Figure, name)
        fig.savefig(fig_path+'.png', dpi=800, bbox_inches='tight', pad_inches=0.1)
    return