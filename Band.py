import matplotlib.pyplot as plt
import numpy as np
import os

colors = ['r', 'g', 'b', 'c', 'm', 'y', 'k']
directory = r'E:\PhD Study\SimCTM\SctmTest\SolverPackTest\Band'
filenameBase = 'band_s[].txt'

def getColor(index):
  i = (index - 1) % len(colors)
  return colors[i]

def fileCount():
  num = 0
  for file in os.listdir(directory):
    if 'band' in file:
      num += 1
  return num

def slice(file):
  f = open(file)
  info = f.readline()
  xList = []
  while(True):
    aLine = f.readline()
    aList = aLine.split()
    currY = aList[1]
    if currY == '0':
      xList.append(aList[0])
    else:
      break
  return xList, len(xList)

fileCnt = fileCount()
file = filenameBase.replace('[]', '1')
file = os.path.join(directory, file)
xList, xVertCnt = slice(file)

for index in range(1, fileCnt + 1):
  filename = filenameBase.replace('[]', str(index))
  filename = os.path.join(directory, filename)
  data = np.loadtxt(filename, skiprows=1)
  x, y, cbedge, vbedge = data[:, 0], data[:, 1], data[:, 2], data[:, 3]
  x, y = x / 1e-7, y / 1e-7
  x, y = x - min(x), y - min(y)
  y = y[::xVertCnt]
  cbedge, vbedge = cbedge[::xVertCnt], vbedge[::xVertCnt]
  plt.plot(y, cbedge, y, vbedge, lw = 2, c = getColor(index))

plt.show()
