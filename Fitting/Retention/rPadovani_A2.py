__author__ = 'Lunzhy'

import os, sys
import matplotlib.pyplot as plt

path = os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), '..\..'))
if not path in sys.path:
    sys.path.append(path)
import lib.compare as cmp
import lib.fitting as ft

############# process the data from experiment ############
# Padovani, APL09', Sample A2, 4.5/7/12
# (time, voltage)
Exp_300K = [(100.742, 4.88192), (988.973, 4.88192), (9926.35, 4.8627), (87218.8, 4.80778)]
Exp_375K = [(98.5325, 4.86545), (1011.15, 4.74462), (9926.35, 4.62929), (87218.8, 4.45629)]
Exp_425K = [(100.742, 4.7611), (988.973, 4.53867), (9926.35, 4.31076), (87218.8, 3.98124)]

items = [('300K', Exp_300K), ('375K', Exp_375K), ('425K', Exp_425K)]
Expr = dict(items)
###########################################################
Fitting_base_dir = r'E:\PhD Study\SimCTM\SctmTest\Fitting\Retention\Padovani_A2'
# Fitting_base_dir = r'E:\PhD Study\SimCTM\SctmTest\Retention_2D'
Main_project_name = r'Demo'  # Demo
Prj_list = ['375K', '425K']

fig = plt.figure()
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])

for prj_index, prj in enumerate(Prj_list):
    time_exp = ft.getTimeList(Expr[prj])
    vfb_exp = ft.getFlatbandList(Expr[prj], True)
    ft.plotExpVfb(ax, prj_index, time_exp, vfb_exp, prj)
    prj_path = os.path.join(Fitting_base_dir, Main_project_name, prj)
    time_sim, vfb_sim = ft.readVfb(prj_path)
    ft.plotFittingVfb(ax, (prj_index,), time_sim, vfb_sim, prj)

ax.legend(loc='lower left', ncol=3, columnspacing=1)
ax.set_xlabel('Programming Time ($s$)')
ax.set_ylabel('Flatband Voltage Shift ($V$)')

ax.set_xscale('log')
ax.set_xlim(1, 1e6)
ax.set_ylim(2, 5.5)

plt.show()

sys.path.remove(path)