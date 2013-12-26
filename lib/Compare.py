__author__ = 'Lunzhy'
import os

import numpy as np

import Common


occLimit = 1e-4
xLimit = 6.5

def plotOccupation(index, directory, title, fig):
  """
  plot the trap occupation rate of the conditions withe various parameters.
  @param index: the index of the subplot, in 2 row * 3 column
  @param directory: the directory of the trap occupation data
  @param title: the title of the subplot
  @param fig: the figure which contains the suplots
  @return:
  """
  files = Common.getFiles(directory, 'Occ')
  xList, xVertCnt = Common.sliceX(files[0])
  axOcc = fig.add_subplot(2, 3, index + 1)
  for file in files:
    y, occup = Common.readData1D(file, xVertCnt)
    xLimit = max(y)
    if Common.isPlot(file) and max(occup) > occLimit:
      time, timelabel = Common.getTimeLabel(file)
      axOcc.set_title(title)
      axOcc.plot(y, occup, lw=2, label=timelabel, c=Common.getColor_time(time))
  return


def plotVfb(index, directory, lineLabel, ax):
  """
  plot the flat band voltage shift of the certain condition
  @param index: the index of the line
  @param directory: the directory containing the vfb data file
  @param lineLabel: the label of the line
  @param ax: the ax containing the line
  @return:
  """
  file = os.path.join(directory, Common.vfbFileName)
  if not os.path.exists(file):
    pass
  data = np.loadtxt(file)
  times, Vfbs = data[:, 0], data[:, 1]
  ax.plot(times, Vfbs, marker='o', mec=Common.getColor(index), c=Common.getColor(index),
          label=lineLabel)
  return


def plotCmpVfb(fig, paraDir, paraUnit):
  """
  plot the flat band voltage comparision result
  @param fig: the figure containing the plots
  @param paraDir: name of the parameter, like Xsection, same with the directory name
  @param paraUnit: the unit of the parameter, used in the axis title, like $cm^{-2}$
  @return:
  """
  maindir = os.path.join(Common.cmpDir, paraDir)
  ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])

  for index, file in enumerate(os.listdir(maindir)):
    prjdir = os.path.join(maindir, file)
    if not os.path.isdir(prjdir):
      continue
    labelTitle = paraDir + ' = ' + file + ' ' + paraUnit
    # plot Vfb
    plotVfb(index, prjdir, labelTitle, ax)

  ax.set_xlim(1e-8, 1)
  ax.set_xscale('log')
  ax.set_ylim(0, 8)
  ax.legend(loc='upper left')
  return


def plotCmpOccupation(fig, paraDir, paraUnit):
  """
  plot the comparison result of trap occupation in 2x3 fashion
  @param fig: the figure containing the plots
  @param paraDir: name of the parameter, like Xsection
  @param paraUnit: the unit of the parameter, used in the axis title, like $cm^{-2}$
  @return:
  """
  maindir = os.path.join(Common.cmpDir, paraDir)

  for index, file in enumerate(os.listdir(maindir)):
    prjdir = os.path.join(maindir, file)
    if not os.path.isdir(prjdir):
      continue
      # plot trap occupation
    labelTitle = paraDir + ' = ' + file + ' ' + paraUnit
    occdir = os.path.join(prjdir, 'Trap')
    plotOccupation(index, occdir, labelTitle, fig)

  for subplotaxe in fig.axes:
    subplotaxe.set_yscale('log')
    subplotaxe.set_ylim(occLimit, 2)
    subplotaxe.set_xlim(0, xLimit)

  fig.subplots_adjust(right=0.8)
  axes = fig.get_axes()
  h, l = axes[0].get_legend_handles_labels()
  fig.legend(h, l, loc='upper left', bbox_to_anchor=(0.8, 0.7))
  return


def plotW_woCompare(fig, dirc):
  """
  plot the with/without comparison result
  @param fig: the fig containing the plot
  @param dirc: the name directory of the mechanism
  @return:
  """
  maindir = os.path.join(Common.w_woDir, dirc)
  rows, cols = 1, 2
  axVfb = fig.add_subplot(rows, cols, 1)
  axOcc = fig.add_subplot(rows, cols, 2)
  for index, prjdir in enumerate(['With', 'Without']):
    title = prjdir + ' ' + dirc
    prjdir = os.path.join(maindir, prjdir)
    # plot Vfb
    times, vfbs = Common.readVfb(prjdir)
    axVfb.plot(times, vfbs, marker='o', mec=Common.getColor(index),
               c=Common.getColor(index), label=title)
    # plot trap occupation rate
    pltDir = os.path.join(prjdir, 'Trap')
    files = Common.getFiles(pltDir, 'Occ')
    xList, xVertCnt = Common.sliceX(files[0])
    for file in files:
      y, occ = Common.readData1D(file, xVertCnt)
      if Common.isPlot(file) and max(occ) > occLimit:
        time, timelabel = Common.getTimeLabel(file)
        axOcc.plot(y, occ, lw=2, c=Common.getColor_time(time),
                   ls=Common.getLinestyle(index))
        # plot ...

  # set the property of each axis
  # for Vfb plots
  axVfb.set_xlim(1e-8, 1)
  axVfb.set_xscale('log')
  axVfb.set_ylim(0, 8)
  axVfb.legend(loc='upper left')
  #for trap occupation plots
  axOcc.set_xlim(0, xLimit)
  axOcc.set_ylim(occLimit, 2)
  axOcc.set_yscale('log')
  #for ...

  return