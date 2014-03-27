__author__ = 'Lunzhy'
import matplotlib.pyplot as plt
import os, sys
path = os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), os.pardir, os.pardir))
if not path in sys.path:
    sys.path.append(path)

import lib.fitting as ft

############# process the data from experiment
exp_time_17V = [1.00000E-08, 1.01612E-07, 4.89570E-07, 9.78905E-07, 4.97461E-06, 9.94684E-06, 4.79243E-05, 9.58256E-05,
                4.86968E-04, 9.73702E-04]
exp_voltage_17V = [-2.05226, -0.74216, 0.651568, 1.09756, 2.18467, 2.51916, 3.27178, 3.63415, 4.10801, 4.41463]

exp_time_18V = [1.00000E-08, 1.01612E-07, 4.89570E-07, 9.78905E-07, 4.97461E-06, 9.94684E-06, 4.92186E-05, 9.58256E-05,
                5.00120E-04, 9.73702E-04]
exp_voltage_18V = [-2.05226, -0.240418, 1.12544, 1.68293, 2.74216, 3.10453, 3.80139, 4.08014, 4.74913, 4.94425]

exp_time_19V = [1.00000E-08, 1.01612E-07, 4.89570E-07, 9.78905E-07, 4.97461E-06, 9.94684E-06, 4.92186E-05, 9.58256E-05]
exp_voltage_19V = [-2.05226, 0.205575, 1.76655, 2.35192, 3.3554, 3.71777, 4.41463, 4.69338]

exp_17V = [(time, voltage) for time, voltage in zip(exp_time_17V, exp_voltage_17V)]
exp_18V = [(time, voltage) for time, voltage in zip(exp_time_18V, exp_voltage_18V)]
exp_19V = [(time, voltage) for time, voltage in zip(exp_time_19V, exp_voltage_19V)]
#############
Exp_list = [exp_17V, exp_18V, exp_19V]

Fitting_base_dir = r'E:\PhD Study\SimCTM\SctmTest\Fitting\TANOS'
Main_project_name = r'SISPAD'  #Demo, Squeeze, Nitride, LargeXsection. SISPAD
Prj_list = ['17V', '18V', '19V']

fig = plt.figure()
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])

for index, prj in enumerate(Prj_list):
    prj_path = os.path.join(Fitting_base_dir, Main_project_name, prj)
    ft.plotExpVfb(ax, index, ft.getTimeList(Exp_list[index]), ft.getFlatbandList(Exp_list[index], False))
    sim_time, sim_flatband = ft.readVfb(prj_path)
    ft.plotFittingVfb(ax, (index, ), sim_time, sim_flatband, prj)

handles, labels = ax.get_legend_handles_labels()
hl = sorted(zip(handles, labels), key=lambda x: x[1])
handles_new, labels_new = zip(*hl)

ax.legend(handles_new, labels_new, loc='upper left', ncol=2, columnspacing=1)
ax.set_xlabel('Programming Time ($s$)')
ax.set_ylabel('Flatband Voltage Shift ($V$)')

ax.set_xscale('log')
ax.set_xlim(1e-9, 1e-2)
ax.set_ylim(-0.5, 8)

plt.show()

# figname = os.Path.join(Common.Dir_SaveFig, 'TANOS_Fitting')
# plt.savefig(figname, dpi=600)
# saveFigure(plt, 'TANOS_Fitting')

sys.path.remove(path)
