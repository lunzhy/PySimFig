#! /usr/bin/env python3
# -*- coding: utf-8 -*- 
__author__ = 'Lunzhy'

import platform, os

if platform.system() == 'Linux':
    Directory_RTED2014 = r'/home/lunzhy/SimCTM/projects/R_TED2014'
    Folder_Save_Figure = r'figures'
elif platform.system() == 'Windows':
    Directory_RTED2014 = r'E:\PhD Study\Submissions\R_TED2014\SctmData'
    Folder_Save_Figure = r'py_figures'