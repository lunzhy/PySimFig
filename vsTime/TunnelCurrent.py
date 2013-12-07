__author__ = 'Lunzhy'
import matplotlib.pyplot as plt
import numpy as np
import os
import re
import math

directory = r'E:\PhD Study\SimCTM\SctmTest\SolverPackTest\Current'

def sorted_ls(path):
  mtime = lambda f: os.stat(os.path.join(path, f)).st_mtime
  return list(sorted(os.listdir(path), key=mtime))

def getTime(line):
  match = re.search(r'\[.+\]', line)
  time = match.group()
  return time[1:-1]

def getCurrent(line):
  str = line.split()[-1]
  val = float(str)
  return math.fabs(val)

def analyse(file):
  f = open(file)
  lines = f.readlines()
  first = lines[0]
  second = lines[1]
  last = lines[-1]
  time = getTime(first)
  currIn = getCurrent(second)
  currOut = getCurrent(last)
  return time, currIn, currOut

times = []
currs_in = []
currs_out = []
for file in sorted_ls(directory):
  if 'eCurrDens' in file:
    filename = os.path.join(directory, file)
    time, curr_in, curr_out = analyse(filename)
    times.append(time)
    currs_in.append(curr_in)
    currs_out.append(curr_out)

#plt.ylim(1e-10, 1e-3)
plt.plot(times, currs_in, marker = 'o', label = 'tunnel in')
plt.plot(times, currs_out, marker = 'o', label = 'tunnel out')
plt.yscale('log')
plt.xscale('log')
plt.legend(loc='lower right')
plt.show()