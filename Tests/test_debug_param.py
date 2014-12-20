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


def test_call_pyt():
    fig = plt.figure()
    ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])

    prj_base = '/home/lunzhy/SimCTM/projects/R_TED2014/call_pyt/p14V_'
    prj_list = [prj_base + prj for prj in ('every', 'major', 'initial')]
    for prj in prj_list:
        plot_vfb(ax, prj, cell_type='triple', label=prj)
    ax.legend()
    plt.show()


if __name__ == '__main__':
    test_call_pyt()