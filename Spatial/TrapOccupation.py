__author__ = 'Lunzhy'
import matplotlib.pyplot as plt
import Common

directory = Common.directory + r'\Trap'
filenameBase = 'trapOccupation'

files = Common.getFiles(directory, filenameBase)
xList, xVertCnt = Common.sliceX(files[0])

for file in files:
  y, occup = Common.readData1D(file, xVertCnt)
  if Common.isPlot(file):
    time, timelabel = Common.getTimeLabel(file)
    plt.plot(y, occup, lw=2, label=timelabel)


plt.ylim(1e-3, 2)
plt.yscale('log')
plt.show()