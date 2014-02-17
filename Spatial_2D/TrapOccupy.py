__author__ = 'Lunzhy'
import os
import lib.common as common
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm


TrapDistr_directory = os.path.join(common.Directory_Debug, common.TrapDistr_Folder)
Trap_file_pattern = 'trapOccupation'


def plotSingleTime(filename):
  x, y, etrap, trapOcc = common.readData2D(filename, 1)
  grid_z = common.makeValueGridZ(x, y, etrap)
  im = plt.imshow(grid_z, cmap=plt.cm.coolwarm, vmin=1e19, vmax=5e19, origin='lower',
             extent=[min(x), max(x), min(y), max(y)], aspect='equal')
  return im


def plotTimesteps():
  fig = plt.figure()
  for index, time in enumerate([1, 10, 500, 1000, 2000, 3000, 5000]):
    ax = fig.add_subplot(3, 3, index+1)
    time_file = common.searchFileNameByTime(TrapDistr_directory, Trap_file_pattern, time)
    im = plotSingleTime(time_file)
  fig.subplots_adjust(right=0.8)
  ax_cb = fig.add_axes([0.85, 0.15, 0.05, 0.7])
  cb = plt.colorbar(im, cax=ax_cb)
  return


def main():
  # hit_file = common.searchFileNameByTime(TrapDistr_directory, Trap_file_pattern, 1)
  # plotSingleTime(hit_file)
  plotTimesteps()
  plt.show()
  return


if __name__ == '__main__': main()