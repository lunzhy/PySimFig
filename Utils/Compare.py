__author__ = 'Lunzhy'
import matplotlib.pyplot as plt
import Common, os
import numpy as np

yLimit = 1e-4
xLimit = 6.5

def plotOccupation(index, directory, title, fig):
  """
  plot the trap occupation rate of the conditions withe various parameters.
  @param index: the index of the subplot
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
    if Common.isPlot(file) and max(occup) > yLimit:
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
  file = os.path.join(directory, Common.vfbFileBaseName)
  if not os.path.exists(file):
    pass
  data = np.loadtxt(file, skiprows=1)
  times, Vfbs = data[:, 0], data[:, 1]
  ax.plot(times, Vfbs, marker='o', mec=Common.getColor(index), c=Common.getColor(index),
          label=lineLabel)
  return


def plotCompare(paraName, paraUnit):
  """
  plot the comparision result
  @param paraName: name of the parameter, like Xsection
  @param paraUnit: the unit of the parameter, used in the axis title, like $cm^{-2}$
  @return:
  """
  maindir = os.path.join(Common.cmpDir, paraName)

  fig = plt.figure()
  axVfb = fig.add_axes([0.1, 0.1, 0.8, 0.8])
  figOcc = plt.figure()

  for index, file in enumerate(os.listdir(maindir)):
    labelTitle = paraName + ' = ' + file + ' ' + paraUnit
    prjdir = os.path.join(maindir, file)
    # plot Vfb
    plotVfb(index, prjdir, labelTitle, axVfb)
    # plot trap occupation
    occdir = os.path.join(prjdir, 'Trap')
    plotOccupation(index, occdir, labelTitle, figOcc)

  axVfb.set_xlim(1e-8, 1)
  axVfb.set_xscale('log')
  axVfb.legend(loc='upper left')

  for subplotaxe in figOcc.axes:
    subplotaxe.set_yscale('log')
    subplotaxe.set_ylim(yLimit, 2)
    subplotaxe.set_xlim(0, xLimit)

  figOcc.subplots_adjust(right=0.8)
  axOcc = figOcc.get_axes()
  h, l = axOcc[0].get_legend_handles_labels()
  plt.figlegend(h, l, loc='upper left', bbox_to_anchor=(0.8, 0.7))
  plt.show()