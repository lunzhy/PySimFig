__author__ = 'Lunzhy'
import matplotlib.pyplot as plt
import os, sys
import numpy as np

path = os.path.abspath(os.path.join('..\..', 'lib'))
if not path in sys.path:
  sys.path.append(path)
from fitting import *
import common

############# process the data from experiment ############
exp_time_5V = [1.07613E-07, 2.08288E-07, 4.66870E-07, 9.96512E-07, 2.12701E-06, 4.65241E-06, 9.93036E-06, 2.17207E-05,
               4.63619E-05, 1.01407E-04, 2.16450E-04, 4.62002E-04, 9.86121E-04, 2.15695E-03, 4.71789E-03, 1.00701E-02,
               2.14942E-02, 4.70144E-02, 1.00350E-01, 2.19496E-01, 4.68504E-01, 9.75838E-01]
exp_flatband_5V = [-1.56742, -1.55712, -1.56742, -1.46442, -1.37172, -1.21723, -1.11423, -0.877341, -0.63015, -0.36236,
                   -0.146067, 0.121723, 0.410112, 0.636704, 0.863296, 1.05899, 1.34738, 1.56367, 1.72846, 1.87266,
                   2.09925, 2.21255]

exp_time_6V = [1.05013E-07, 2.13445E-07, 4.55589E-07, 9.96512E-07, 2.12701E-06, 4.65241E-06, 9.93036E-06, 2.11959E-05,
               4.63619E-05, 9.89573E-05, 2.11220E-04, 4.62002E-04, 1.01054E-03, 2.15695E-03, 4.71789E-03, 1.00701E-02,
               2.14942E-02, 4.70144E-02, 1.00350E-01, 2.19496E-01, 4.68504E-01, 1.00000E+00]
exp_flatband_6V = [-1.52622, -1.46442, -1.32022, -1.21723, -0.90824, -0.640449, -0.372659, -0.053370, 0.235019,
                   0.533708, 0.791199, 1.08989, 1.37828, 1.61517, 1.84176, 1.97566, 2.26404, 2.31554, 2.51124, 2.70693,
                   2.72753, 2.84082]

exp_time_7V = [1.00000E-07, 2.13445E-07, 4.55589E-07, 9.96512E-07, 2.12701E-06, 4.54000E-06, 9.93036E-06, 2.17207E-05,
               4.63619E-05, 1.01407E-04, 2.16450E-04, 4.62002E-04, 1.01054E-03, 2.15695E-03, 4.71789E-03, 1.00701E-02,
               2.14942E-02, 4.70144E-02, 1.00350E-01, 2.19496E-01, 4.68504E-01, 1.00000E+00]
exp_flatband_7V = [-1.43352, -1.27903, -0.918539, -0.61985, -0.166667, 0.19382, 0.502809, 0.852996, 1.20318, 1.53277,
                   1.74906, 2.00655, 2.22285, 2.34644, 2.49064, 2.75843, 2.77903, 2.85112, 2.77903, 2.90262, 2.89232,
                   2.96442]

exp_time_8V = [1.00000E-07, 2.13445E-07, 4.55589E-07, 9.96512E-07, 2.12701E-06, 4.54000E-06, 9.93036E-06, 2.11959E-05,
               4.63619E-05, 9.89573E-05, 2.16450E-04, 4.62002E-04, 9.86121E-04, 2.15695E-03, 4.60390E-03, 1.00701E-02,
               2.14942E-02, 4.58784E-02, 1.00350E-01, 2.19496E-01, 4.68504E-01, 1.00000E+00]
exp_flatband_8V = [-1.26873, -0.825843, -0.259363, 0.20412, 0.688202, 1.06929, 1.52247, 1.79026, 2.09925, 2.33614,
                   2.57303, 2.73783, 2.86142, 2.89232, 2.94382, 2.92322, 2.91292, 2.90262, 2.91292, 2.91292, 2.87172,
                   2.80993]

# the first item in tuple is time, the second is flatband voltage
exp_5V = [(time, voltage) for time, voltage in zip(exp_time_5V, exp_flatband_5V)]
exp_6V = [(time, voltage) for time, voltage in zip(exp_time_6V, exp_flatband_6V)]
exp_7V = [(time, voltage) for time, voltage in zip(exp_time_7V, exp_flatband_7V)]
exp_8V = [(time, voltage) for time, voltage in zip(exp_time_8V, exp_flatband_8V)]


#############
exp_list = [exp_5V, exp_6V, exp_7V, exp_8V]

Fitting_base_dir = r'E:\PhD Study\SimCTM\SctmTest\Fitting\MANOS'
Main_project_name = r'Demo' # Demo, woMFN
Prj_list = ['5V', '6V', '7V', '8V']

fig = figure()
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])

for index, prj in enumerate(Prj_list):
  prj_path = os.path.join(Fitting_base_dir, Main_project_name, prj)
  sim_time, sim_flatband = readVfb(prj_path)
  plotFittingVfb(ax, index, getTimeList(exp_list[index]), getFlatbandList(exp_list[index]), sim_time, sim_flatband, prj)

handles, labels = ax.get_legend_handles_labels()
hl = sorted(zip(handles, labels), key=lambda x: x[1])
handles_new, labels_new = zip(*hl)

ax.legend(handles_new, labels_new, loc='upper left', ncol=2, columnspacing=1)
ax.set_xlabel('Programming Time ($s$)')
ax.set_ylabel('Flatband Voltage Shift ($V$)')

ax.set_xscale('log')
ax.set_xlim(1e-7, 1)
ax.set_ylim(-0.5, 6)

# plt.show()

Common.saveFigure(plt, 'MANOS_MFN')

sys.path.remove(path)

