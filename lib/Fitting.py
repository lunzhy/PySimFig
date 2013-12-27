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


def plotFittingVfb(ax, index, exp_time, exp_flatband, sim_time, sim_flatband, prj_label=""):
  """
  plot the comparison result
  @param ax:
  @param index:
  @param exp_time:
  @param exp_flatband:
  @param sim_time:
  @param sim_flatband:
  @param prj_label:
  @return:
  """
  exp_label = 'exp %s' % prj_label
  sim_label = 'sim %s' % prj_label
  ax.plot(exp_time, exp_flatband, marker='o', ls='None', fillstyle='none', ms=8, mew=3, mec=getColor(index),
          c=getColor(index), label=exp_label)
  ax.plot(sim_time, sim_flatband, lw=2, c=getColor(index), label=sim_label)
  return


def getFlatbandList(exp_data, isShift=False):
  """
  get the flatband voltage shift value list from experiment data
  @param exp_data:
  @param isShift: check if the experiment data is voltage shift
  @return:
  """
  exp_data = sorted(exp_data, key=lambda x: x[1])
  if not isShift:
    min_voltage_tuple = min(exp_data, key=lambda x: x[1])
    min_voltage = min_voltage_tuple[1]
  else:
    min_voltage = 0
  flatband_list = [x[1] - min_voltage for x in exp_data]
  return flatband_list


def getTimeList(exp_data):
  """
  get the time list from experiment data
  @param exp_data:
  @param isShift: check if the experiment data is voltage shift
  @return:
  """
  exp_data = sorted(exp_data, key=lambda x: x[1])
  time_list = [x[0] for x in exp_data]
  return time_list


def test():
  file = os.path.join('E:\PhD Study\SimCTM\SctmTest\SolverPackTest', Flatband_file_relpath)


if __name__ == '__main__': test()