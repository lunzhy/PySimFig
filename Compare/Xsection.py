__author__ = 'Lunzhy'
import matplotlib.pyplot as plt
import Common, os
import numpy as np

maindir = os.path.join(Common.cmpDir, 'Xsection')
vfbFileBaseName = 'VfbShift.txt'
yLimit = 1e-4
xLimit = 6.5


def plotOccupation(index, directory, title):
  files = Common.getFiles(directory, 'trap')
  xList, xVertCnt = Common.sliceX(files[0])
  axOcc = figOcc.add_subplot(2, 3, index + 1)
  for file in files:
    y, occup = Common.readData1D(file, xVertCnt)
    xLimit = max(y)
    if Common.isPlot(file) and max(occup) > yLimit:
      time, timelabel = Common.getTimeLabel(file)
      axOcc.set_title(title)
      axOcc.plot(y, occup, lw=2, label=timelabel, c=Common.getColor_time(time))
  axOcc.set_yscale('log')
  axOcc.set_ylim(yLimit, 2)
  axOcc.set_xlim(0, xLimit)
  return


def plotVfb(index, directory, lineLabel):
  file = os.path.join(directory, vfbFileBaseName)
  if not os.path.exists(file):
    pass
  data = np.loadtxt(file, skiprows=1)
  times, Vfbs = data[:, 0], data[:, 1]
  axVfb.plot(times, Vfbs, marker='o', mec=Common.getColor(index), c=Common.getColor(index),
             label=lineLabel)
  return


fig = plt.figure()
axVfb = fig.add_axes([0.1, 0.1, 0.8, 0.8])
figOcc = plt.figure()

for index, file in enumerate(os.listdir(maindir)):
  labelTitle = 'Xsection = ' + file + ' $cm^{-2}$'
  prjdir = os.path.join(maindir, file)
  # plot Vfb
  plotVfb(index, prjdir, labelTitle)
  # plot trap occupation
  occdir = os.path.join(prjdir, 'Trap')
  plotOccupation(index, occdir, labelTitle)

axVfb.set_xlim(1e-8, 1)
axVfb.set_xscale('log')
axVfb.legend(loc='upper left')

figOcc.subplots_adjust(right=0.8)
axOcc = figOcc.get_axes()
h, l = axOcc[0].get_legend_handles_labels()
plt.figlegend(h, l, loc='upper left', bbox_to_anchor=(0.8, 0.7))
plt.show()