__author__ = 'Lunzhy'
import re, math, os
import numpy as np

############ the common functions of PySimFig ##############
directory = r'E:\PhD Study\SimCTM\SctmTest\SolverPackTest'
cmpDir = r'E:\PhD Study\SimCTM\SctmTest\ParameterCheck'
colors = ['r', 'g', 'b', 'c', 'm', 'y', 'k']
vfbFileBaseName = 'VfbShift.txt'

def getColor(index):
  """
  get color in the colors list
  """
  i = (index - 1) % len(colors)
  return colors[i]

def getColor_time(time):
  """
  get color according to the time
  @param time:
  @return:
  """
  arg = int(abs(math.log10(time)))
  return getColor(arg)


def fileCount(nameString):
  """
  count the file with specified name string
  """
  num = 0
  for file in os.listdir(directory):
    if nameString in file:
      num += 1
  return num

def sliceX(file):
  """
  slice gets the list of x coordinates and the number of vertex in x direction
  @param file:
  @return:
  """
  f = open(file)
  info = f.readline()
  currY = 0
  xList = []
  while (True):
    aLine = f.readline()
    aList = aLine.split()
    if len(xList) == 0 or currY == aList[1]:
      xList.append(aList[0])
    else:
      break
  f.close()
  return xList, len(xList)

def getTimeLabel(filename):
  """
  get the time string and corresponding label for plotting
  @param filename:
  @return: time string and label for plotting
  """
  f = open(filename)
  title = f.readline()
  f.close()
  match = re.search(r'\[.+\]', title)
  time = match.group()
  time = float(time[1:-1])
  # time = '%.0e' % time
  label = 'Time = ' + str(time) + 's'
  return time, label

def isPlot(filename):
  """
  plot only when the expotential argument is integer
  @param filename:
  @return:
  """
  time, labelTime = getTimeLabel(filename)
  time = float(time)
  return math.log10(time) == math.floor(math.log10(time))

def getStepNumber(filename):
  """
  get the step number from file name
  @param filename:
  @return:
  """
  match = re.search(r's.+\.', filename)
  suffix = match.group()
  return int(suffix[1:-1])

def getFiles(directory, filenameBase):
  """
  get the full filenames of correct sequence in a directory containing the fileNameBase
  @param directory:
  @param filenameBase:
  @return:
  """
  fileList = []
  for file in os.listdir(directory):
    if filenameBase in file:
      fileList.append(file)
  fileList = sorted(fileList, key=getStepNumber)
  for index, file in enumerate(fileList):
    file = os.path.join(directory, file)
    fileList[index] = file
  return fileList

########## specificly used in plotting 1D figures ##########
def readData1D(file, xSkip):
  """
  read the file and get the data list for 1D plotting
  @param file:
  @param xSkip:
  @return:
  """
  data = np.loadtxt(file, skiprows=1)
  x, y, val = data[:, 0], data[:, 1], data[:, 2]
  x, y = x / 1e-7, y / 1e-7
  x, y = x - min(x), y - min(y)
  # get the first slice of the data, i.e. the slice with x=0
  y, val = y[::xSkip], val[::xSkip]
  return y, val



########## specificly used in plotting 2D figures ##########