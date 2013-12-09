__author__ = 'Lunzhy'
import matplotlib.pyplot as plt
import numpy as np
import os
import math

filename = r'E:\PhD Study\SimCTM\SctmTest\SolverPackTest\VfbShift.txt'

data = np.loadtxt(filename)
times, Vfbs = data[:, 0], data[:, 1]

plt.plot(times, Vfbs, marker = 'o')
plt.xlim(1e-7, 10)
plt.xscale('log')
plt.show()