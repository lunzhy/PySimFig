__author__ = 'Lunzhy'
import matplotlib.pyplot as plt
import numpy as np

filename = r'E:\PhD Study\SimCTM\SctmTest\SolverPackTest\Miscellaneous\VfbShift.txt'

data = np.loadtxt(filename)
times, Vfbs = data[:, 0], data[:, 1]

plt.plot(times, Vfbs, marker='o')
plt.xlim(1e-7, 1)
plt.xscale('log')
plt.show()