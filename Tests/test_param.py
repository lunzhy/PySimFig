#! /usr/bin/env python3
# -*- coding: utf-8 -*- 
__author__ = 'lunzhy'
import matplotlib.pyplot as plt
import os, sys
path = os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), '..'))
if not path in sys.path:
    sys.path.append(path)
import lib.common as cm
from QuickView.VfbShift import plot_vfb


def test_mobility():
    fig = plt.figure()
    ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])

    prj_base = '/home/lunzhy/SimCTM/projects/R_TED2014/program/%s'
    prj_list = ['p14V_u0.1', 'p14V_u0.01', 'p14V_u0.001']
    for prj_name in prj_list:
        prj = prj_base % prj_name
        plot_vfb(ax, prj, cell_type='triple', label=prj_name)
    ax.legend(loc='upper left')
    plt.show()


if __name__ == '__main__':
    test_mobility()