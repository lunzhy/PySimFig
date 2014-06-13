__author__ = 'lunzhy'
import os, sys
path = os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), os.pardir, os.pardir))
if not path in sys.path:
    sys.path.append(path)
from Submissions.CPB2014 import *
import matplotlib.pyplot as plt
import lib.common as comm


Main_path = os.path.join(Directory_CPB2014, 'ret_tb_pf')


def plotCompareTwoMechanism():
    prj_list = ['330K', '360K', '380K', '400K']
    for index, prj in enumerate(prj_list):
        prj_path = os.path.join(Main_path, prj)
        time, tun_subs_acc, tb_subs_acc, tun_gate_acc, tb_gate_acc = comm.readTunnelOut()
    return


def plotCompareTbPf():
    return


def main():
    return


if __name__ == '__main__':
    main()
