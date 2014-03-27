__author__ = 'Lunzhy'
import matplotlib.pyplot as plt
import os, sys

Path = os.path.abspath(os.path.join('..\..', 'lib'))
if not Path in sys.path:
    sys.path.append(Path)
from fitting import *
# from lib.ft import *

############# process the data from experiment ############
# Padovani, EDL09', Sample C, 4/8.7/11.5
# (time, voltage)
Exp_8V = [(8.55E-04, 0), (0.00178825, 0), (0.00373952, 0), (0.00864755, 0), (0.0180835, 0.0421053),
          (0.0378155, 0.0421053), (0.0874475, 0.0421053), (0.182867, 0.0210526), (0.382406, 0.0421053),
          (0.884305, 0.0631579), (1.78825, 0.105263)]
Exp_10V = [(1.81E-05, 0), (3.78E-05, 0), (8.74E-05, 0), (1.83E-04, 0), (3.82E-04, 0), (8.55E-04, 0), (0.00184923, 0),
           (0.00373952, 0.0210526), (0.00836238, 0.0631579), (0.0180835, 0.126316), (0.0378155, 0.252632),
           (0.0845638, 0.421053), (0.182867, 0.631579), (0.369795, 0.905263), (0.855143, 1.22105)]
Exp_12V = [(9.78E-07, 0), (2.96E-06, 0), (7.82E-06, 0), (1.75E-05, 0), (3.78E-05, 0), (8.74E-05, 0),
           (1.83E-04, 0.0421053), (3.82E-04, 0.0842105), (8.84E-04, 0.210526), (0.00184923, 0.421053),
           (0.00386704, 0.673684), (0.00864755, 1.01053), (0.0187001, 1.34737), (0.0391051, 1.70526),
           (0.0874475, 2.10526), (0.189103, 2.42105), (0.382406, 2.73684), (0.884305, 3.07368), (1.84923, 3.34737)]
Exp_14V = [(9.78E-07, 0), (2.96E-06, 0.0421053), (7.82E-06, 0.0631579), (1.75E-05, 0.126316), (3.78E-05, 0.273684),
           (8.74E-05, 0.547368), (1.83E-04, 0.863158), (3.82E-04, 1.26316), (8.84E-04, 1.70526), (0.00184923, 2.10526),
           (0.00386704, 2.46316), (0.00894245, 2.90526), (0.0187001, 3.30526), (0.0391051, 3.62105),
           (0.0874475, 3.97895), (0.182867, 4.27368), (0.382406, 4.52632), (0.884305, 4.82105), (1.84923, 4.98947)]
Exp_16V = [(9.78E-07, 0.126316), (2.96E-06, 0.315789), (8.09E-06, 0.673684), (1.75E-05, 1.13684), (3.78E-05, 1.6),
           (8.74E-05, 2.14737), (1.89E-04, 2.61053), (3.82E-04, 3.07368), (8.55E-04, 3.55789), (0.00184923, 3.95789),
           (0.00386704, 4.27368), (0.00864755, 4.67368), (0.0187001, 4.98947), (0.0378155, 5.26316),
           (0.0874475, 5.53684), (0.189103, 5.78947), (0.382406, 5.97895), (0.855143, 6.21053), (1.84923, 6.4)]
Exp_18V = [(1.01E-06, 0.842105), (2.96E-06, 1.51579), (8.09E-06, 2.21053), (1.81E-05, 2.8), (3.78E-05, 3.32632),
           (8.74E-05, 3.89474), (1.83E-04, 4.37895), (3.82E-04, 4.82105), (8.84E-04, 5.24211), (0.00184923, 5.6),
           (0.00373952, 5.89474), (0.00864755, 6.23158), (0.0180835, 6.46316), (0.0378155, 6.71579),
           (0.0874475, 6.98947), (0.182867, 7.2), (0.369795, 7.41053), (0.855143, 7.64211)]
Exp_list = [Exp_12V, Exp_14V, Exp_16V, Exp_18V]
############################################################

Fitting_base_dir = r'E:\PhD Study\SimCTM\SctmTest\Fitting\Padovani_C'
Main_project_name = [r'Paper']  # Demo, Paper
Prj_list = ['12V', '14V', '16V', '18V']

fig = figure()
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])

for prj_index, prj in enumerate(Prj_list):
    plotExpVfb(ax, prj_index, getTimeList(Exp_list[prj_index]), getFlatbandList(Exp_list[prj_index], True))
    for main_index, main_prj in enumerate(Main_project_name):
        prj_path = os.path.join(Fitting_base_dir, main_prj, prj)
        sim_time, sim_flatband = readVfb(prj_path)
        if len(sim_time) == 0: pass
        plotFittingVfb(ax, (main_index, prj_index), sim_time, sim_flatband, prj)

handles, labels = ax.get_legend_handles_labels()
hl = sorted(zip(handles, labels), key=lambda x: x[1])
handles_new, labels_new = zip(*hl)

#TODO: label order has to be enhanced
ax.legend(handles_new, labels_new, loc='upper left', ncol=3, columnspacing=1)
ax.set_xlabel('Programming Time ($s$)')
ax.set_ylabel('Flatband Voltage Shift ($V$)')

ax.set_xscale('log')
ax.set_xlim(1e-10, 2)
ax.set_ylim(0, 10)

plt.show()

sys.path.remove(Path)