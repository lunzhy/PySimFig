__author__ = 'Lunzhy'
import matplotlib.pyplot as plt

path = os.path.abspath(os.path.join('..', 'lib'))
if not path in sys.path:
  sys.path.append(path)
from Fitting import *

############# process the data from experiment
exp_time_17V = [1.00000E-08, 1.01612E-07, 4.89570E-07, 9.78905E-07, 4.97461E-06, 9.94684E-06, 4.79243E-05, 9.58256E-05,
                4.86968E-04, 9.73702E-04]
exp_voltage_17V = [-2.05226, -0.74216, 0.651568, 1.09756, 2.18467, 2.51916, 3.27178, 3.63415, 4.10801, 4.41463]

exp_time_18V = [1.00000E-08, 1.01612E-07, 4.89570E-07, 9.78905E-07, 4.97461E-06, 9.94684E-06, 4.92186E-05, 9.58256E-05,
                5.00120E-04, 9.73702E-04]
exp_voltage_18V = [-2.05226, -0.240418, 1.12544, 1.68293, 2.74216, 3.10453, 3.80139, 4.08014, 4.74913, 4.94425]

exp_time_19V = [1.00000E-08, 1.01612E-07, 4.89570E-07, 9.78905E-07, 4.97461E-06, 9.94684E-06, 4.92186E-05, 9.58256E-05]
exp_voltage_19V = [-2.05226, 0.205575, 1.76655, 2.35192, 3.3554, 3.71777, 4.41463, 4.69338]

exp_flatband_17V = [x - min(exp_voltage_17V) for x in exp_voltage_17V]
exp_flatband_18V = [x - min(exp_voltage_18V) for x in exp_voltage_18V]
exp_flatband_19V = [x - min(exp_voltage_19V) for x in exp_voltage_19V]

#############
exp_time_list = [exp_time_17V, exp_flatband_18V, exp_flatband_19V]
exp_flatband_list = [exp_flatband_17V, exp_flatband_18V, exp_flatband_19V]

Fitting_base_dir = r'E:\PhD Study\SimCTM\SctmTest\Fitting\TANOS'
Main_project_name = r'Demo'
Prj_list = ['17V', '18V', '19V']

fig = figure()
ax = fig.add_axes([0.1, 0.1, 0.7, 0.7])

for index, prj in enumerate(Prj_list):
  prj_path = os.path.join(Fitting_base_dir, Main_project_name, prj)
  sim_time, sim_flatband = readVfb(prj_path)
  plotFittingVfb(ax, index, exp_time_list[index], exp_flatband_list[index], sim_time, sim_flatband)

ax.set_xscale('log')
plt.show()

sys.path.remove(path)
