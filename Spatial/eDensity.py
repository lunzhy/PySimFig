import matplotlib.pyplot as plt
import numpy as np
import os
import re
import math

colors = ['r', 'g', 'b', 'c', 'm', 'y', 'k']
directory = r'E:\PhD Study\SimCTM\SctmTest\SolverPackTest\Density'
filenameBase = 'eDensity_s[].txt'

def getColor(index):
  i = (index - 1) % len(colors)
  return colors[i]

def fileCount():
  num = 0
  for file in os.listdir(directory):
    if 'eDensity' in file:
      num += 1
  return num

def slice(file):
  f = open(file)
  info = f.readline()
  currY = 0
  xList = []
  while(True):
    aLine = f.readline()
    aList = aLine.split()
    if len(xList) == 0 or currY == aList[1]:
      xList.append(aList[0])
    else:
      break
  return xList, len(xList)

def getTimeLabel(filename):
  f = open(filename)
  title = f.readline()
  f.close()
  match = re.search(r'\[.+\]', title)
  time = match.group()
  return time[1:-1], 'Time = ' + time[1:-1] + 's'

def selectivePlot(filename, index):
  time, labelTime = getTimeLabel(filename)
  time = float(time)
  if math.log10(time) == math.floor(math.log10(time)):
    plt.plot(y, eDens, lw=2, c=getColor(index), label=labelTime)

fileCnt = fileCount()
file = filenameBase.replace('[]', '1')
file = os.path.join(directory, file)
xList, xVertCnt = slice(file)

for index in range(1, fileCnt + 1):
  filename = filenameBase.replace('[]', str(index))
  filename = os.path.join(directory, filename)
  data = np.loadtxt(filename, skiprows=1)
  x, y, eDens = data[:, 0], data[:, 1], data[:, 2]
  x, y = x / 1e-7, y / 1e-7
  x, y = x - min(x), y - min(y)
  y = y[::xVertCnt]
  eDens= eDens[::xVertCnt]
  selectivePlot(filename, index)

#plt.ylim(1e10, 1e11)
#plt.xlim(9, 10)
plt.yscale('log')
#plt.legend(loc = 'lower left')
plt.show()

