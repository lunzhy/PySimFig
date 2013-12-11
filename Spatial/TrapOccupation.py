__author__ = 'Lunzhy'
import matplotlib.pyplot as plt
import Common

directory = Common.directory + r'\Trap'
filenameBase = 'trapOccupation'
yLimit = 1e-4
xLimit = 0

files = Common.getFiles(directory, filenameBase)
xList, xVertCnt = Common.sliceX(files[0])

fig = plt.figure()
ax = fig.add_axes([0.1, 0.1, 0.55, 0.8])
for file in files:
  y, occup = Common.readData1D(file, xVertCnt)
  xLimit = max(y)
  if Common.isPlot(file) and max(occup) > yLimit:
    time, timelabel = Common.getTimeLabel(file)
    ax.plot(y, occup, lw=2, label=timelabel)

ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
ax.set_xlabel('Coordinates along trapping layer (${nm}$)')
ax.set_ylabel('Trap occupation rate')
ax.set_yscale('log')
ax.set_xlim(0, xLimit)
ax.set_ylim(yLimit, 2)
plt.show()