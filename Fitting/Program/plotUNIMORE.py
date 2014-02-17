__author__ = 'Lunzhy'
import matplotlib.pyplot as plt
import os, sys
Path = os.path.abspath(os.path.join('..\..', 'lib'))
if not Path in sys.path:
  sys.path.append(Path)
from fitting import *
# from lib.fitting import *

############# process the data from experiment ############
# (time, voltage)
exp_14V = [(9.80374E-07, 0.0630252), (3.09510E-06, 0.189076), (8.33855E-06, 0.462185), (1.77095E-05, 0.777311),
           (3.76117E-05, 1.17647), (8.99682E-05, 1.63866), (1.83649E-04, 2.07983), (3.90036E-04, 2.43697),
           (8.96715E-04, 2.87815), (1.90445E-03, 3.19328), (3.88750E-03, 3.52941), (8.59019E-03, 3.86555),
           (1.89817E-02, 4.09664), (3.72408E-02, 4.36975), (8.56186E-02, 4.62185), (1.89191E-01, 4.81092),
           (3.86190E-01, 5.02101), (8.53362E-01, 5.21008), (1.88567E+00, 5.37815)]

exp_16V = [(1.10418E-06, 0.672269), (2.97480E-06, 1.2605), (7.70295E-06, 1.89076), (1.77095E-05, 2.39496),
           (3.76117E-05, 2.87815), (8.99682E-05, 3.36134), (1.91076E-04, 3.7395), (3.90036E-04, 4.07563),
           (8.96715E-04, 4.45378), (1.83043E-03, 4.7479), (3.88750E-03, 5.02101), (8.93757E-03, 5.31513),
           (1.89817E-02, 5.54622), (3.87468E-02, 5.7563), (8.90809E-02, 6.05042), (1.89191E-01, 6.2605),
           (4.01807E-01, 6.44958), (8.87871E-01, 6.68067), (1.96193E+00, 6.84874)]

exp_18V = [(9.42269E-07, 1.9958), (2.85918E-06, 2.77311), (7.70295E-06, 3.46639), (1.77095E-05, 3.97059),
           (3.76117E-05, 4.39076), (8.64714E-05, 4.83193), (1.83649E-04, 5.16807), (3.74876E-04, 5.46218),
           (8.61862E-04, 5.79832), (1.83043E-03, 6.07143), (3.73640E-03, 6.32353), (8.93757E-03, 6.65966),
           (1.82440E-02, 6.93277), (3.72408E-02, 7.16387), (8.90809E-02, 7.43697), (1.89191E-01, 7.71008),
           (3.86190E-01, 7.92017), (8.53362E-01, 8.15126)]
Exp_list = [exp_14V, exp_16V, exp_18V]
############################################################

Fitting_base_dir = r'E:\PhD Study\SimCTM\SctmTest\Fitting\Padovani_B'
Main_project_name = [r'WithT2B-J', r'Squeeze'] # Demo, Squeeze, WithT2B-J, WithT2B-V, noT2B-J
Prj_list = ['14V', '16V', '18V']

fig = figure()
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])

for prj_index, prj in enumerate(Prj_list):
  plotExpVfb(ax, prj_index, getTimeList(Exp_list[prj_index]), getFlatbandList(Exp_list[prj_index], True))
  for main_index, main_prj in enumerate(Main_project_name):
    prj_path = os.path.join(Fitting_base_dir, main_prj, prj)
    sim_time, sim_flatband = readVfb(prj_path)
    plotFittingVfb(ax, (main_index, prj_index), sim_time, sim_flatband, prj)


handles, labels = ax.get_legend_handles_labels()
hl = sorted(zip(handles, labels), key=lambda x: x[1])
handles_new, labels_new = zip(*hl)

#TODO: label order has to be enhanced
ax.legend(handles_new, labels_new, loc='upper left', ncol=3, columnspacing=1)
ax.set_xlabel('Programming Time ($s$)')
ax.set_ylabel('Flatband Voltage Shift ($V$)')

ax.set_xscale('log')
ax.set_xlim(1e-12, 2)
ax.set_ylim(0, 10)

plt.show()

sys.path.remove(Path)

