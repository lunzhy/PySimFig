__author__ = 'Lunzhy'
import os

from matplotlib.pyplot import *


Colors = ['black', 'blue', 'fuchsia', 'gray', 'green', 'purple', 'maroon', 'red',
          'navy', 'olive', 'orange', 'lime', 'silver', 'aqua', 'teal']
Linestyles = ['-', '--']
Flatband_file_relpath = 'Miscellaneous\VfbShift.txt'


def getColor(index):
  """
  get color in the colors list
  """
  i = index % len(Colors)
  return Colors[i]


def readVfb(prj_path):
  """
  read the flat band voltage shift file in given project directory
  @param directory: the directory of the project
  @return: time list and vfb list
  """
  file = os.path.join(prj_path, Flatband_file_relpath)
  data = np.loadtxt(file)
  times, vfbs = data[:, 0], data[:, 1]
  return times, vfbs


def plotFittingVfb(ax, index, exp_time, exp_flatband, sim_time, sim_flatband):
  ax.plot(exp_time, exp_flatband, marker='o', ls='None', ms=3, mec=getColor(index), c=getColor(index))
  ax.plot(sim_time, sim_flatband, lw=2, c=getColor(index))
  return


def test():
  file = os.path.join('E:\PhD Study\SimCTM\SctmTest\SolverPackTest', Flatband_file_relpath)


if __name__ == '__main__': test()