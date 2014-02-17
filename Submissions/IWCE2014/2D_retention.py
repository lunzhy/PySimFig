__author__ = 'Lunzhy'
import os
import math

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager

import lib.common as common
from Submissions.IWCE2014 import *


Base_dir = r'E:\PhD Study\SimCTM\SctmTest\Retention_2D'
Main_project_name = r'Vt2D' # Demo, Vt2D
# Prj_list = ['300K', '375K', '425K']
Prj_list = ['300K', '400K']
Time_list = [4e4, 1e5, 5e5]

Trap_file_pattern = 'trapOccupation'

def plotSingleTime(ax, filename):
  x, y, etrap, trapOcc = common.readData2D(filename, 1)
  grid_z = common.makeValueGridZ(x, y, etrap)
  im = ax.imshow(grid_z, cmap=plt.cm.jet, vmin=0.8e19, vmax=4e19, origin='lower',
                  extent=[min(x), max(x), min(y), max(y)], aspect='auto')


  return im


def analyseTime(time):
  super = math.floor(math.log10(time))
  coeff = int(time/math.pow(10, super))
  return coeff, super

def plotTimesteps():
  fig = plt.figure()
  for prj_index, prj in enumerate(Prj_list):
    prj_path = os.path.join(Base_dir, Main_project_name, prj)
    for time_index, time in enumerate(Time_list):
      trap_path = os.path.join(prj_path, common.TrapDistr_Folder)
      ax = fig.add_subplot(2, 3, prj_index*3+time_index+1)
      coeff, super = analyseTime(time)
      title_str = (r'$\mathbf{t = '+str(coeff)+r'\times10^'+str(super)+'s}$')
      ax.set_title(title_str)
      ax.set_xlabel(r'x (nm)')
      ax.set_ylabel(r'y (nm)')
      time_file = common.searchFileNameByTime(trap_path, Trap_file_pattern, time)
      im = plotSingleTime(ax, time_file)

  ## set the figures
  ## tick
  labels_font = font_manager.FontProperties(family='times new roman', style='normal',
                                            size=20, weight='normal', stretch='normal')
  ticks_font = font_manager.FontProperties(family='times new roman', style='normal',
                                           size=20, weight='normal', stretch='normal')

  for ax in fig.axes:
    x_start, x_end = ax.get_xlim()
    y_start, y_end = ax.get_ylim()
    ax.xaxis.set_ticks(np.arange(x_start+1, x_end, 2))
    ax.yaxis.set_ticks(np.arange(y_start, y_end, 2))
    for item in (ax.get_xticklabels() + ax.get_yticklabels()):
      item.set_fontproperties(ticks_font)
    for item in ([ax.xaxis.label, ax.yaxis.label]):
      item.set_fontproperties(labels_font)


  plt.tight_layout()
  ## set color bar
  fig.subplots_adjust(right=0.85)
  ax_cb = fig.add_axes([0.87, 0.15, 0.03, 0.7])
  cb = plt.colorbar(im, cax=ax_cb)
  cb.set_label('Trapped electron density ($\mathbf{cm^{-3}}$)', rotation=270, labelpad=25)
  cb.set_ticks(np.linspace(1, 3.8, 5)*1e19)
  for item in (cb.ax.get_yticklabels() + cb.ax.get_xticklabels()):
    item.set_fontproperties(labels_font)
  for item in ([cb.ax.yaxis.label]):
    item.set_fontproperties(labels_font)

  return


def main():
  plotTimesteps()
  # plt.show()

  fig_name = os.path.join(Save_Fig_Folder, '2D_tunnel')
  plt.savefig(fig_name, dpi = 1020, bbox_inches = 'tight', pad_inches = 0.1)

  return


if __name__ == '__main__': main()