__author__ = 'Lunzhy'
import matplotlib.pyplot as plt
import numpy as np
import os
import re

colors = ['r', 'g', 'b', 'c', 'm', 'y', 'k']
directory = r'E:\PhD Study\SimCTM\SctmTest\SolverPackTest\Current'
filenameBase = 'eCurrDens_s[].txt'

def getColor(index):
  i = (index - 1) % len(colors)
  return colors[i]

def fileCount():
  num = 0
  for file in os.listdir(directory):
    if 'eCurrDens' in file:
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
  file = open(filename)
  title = file.readline()
  file.close()
  match = re.search(r'\[.+\]', title)
  time = match.group()
  return 'Time = ' + time[1:-1] + 's'

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
  plt.plot(y, eDens, lw = 2, c = getColor(index), label = getTimeLabel(filename))

#plt.ylim(1e-7, 1e-3)
#plt.xlim(0, 10)
plt.yscale('log')
#plt.legend(loc = 'lower left')
plt.show()


