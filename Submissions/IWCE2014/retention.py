__author__ = 'Lunzhy'

import os
import sys

Path = os.path.abspath(os.path.join('..', 'lib'))
if not Path in sys.path:
  sys.path.append(Path)
import lib.common as common
from Submissions.IWCE2014 import *
from matplotlib import font_manager

###########################################################
Fitting_base_dir = r'E:\PhD Study\SimCTM\SctmTest\Retention_2D'
Main_project_name = ['Vt2D', 'noT2B'] # Demo, Vt2D, noT2B
Prj_list =['300K', '400K']


fig = figure()
ax = fig.add_axes([0.17, 0.17, 0.75, 0.75])


for prj_index, prj in enumerate(Prj_list):
  color_index = prj_index
  for t2b_index, t2b in enumerate(Main_project_name):
    ls_index = t2b_index
    prj_path = os.path.join(Fitting_base_dir, t2b, prj)
    time_sim, vfb_sim = readVfb(prj_path)
    ax.plot(time_sim, vfb_sim, color=common.getColor(color_index), lw=4, ls=getLinestyle(ls_index), label=prj+t2b)

# legend = ax.legend([r'T = 300K With TBT', r'T = 300K W/O TBT', r'T = 400K With TBT', r'T = 400K W/O TBT'],
#          loc='lower left', handlelength=3, bbox_to_anchor=(0.02, 0.05))
legend = ax.legend([r'Thermal + TBT @ T = 300K', r'Thermal @ T = 300K',
                    r'Thermal + TBT @ T = 400K', r'Thermal @ T = 400K'],
          loc='lower left', handlelength=3, bbox_to_anchor=(0, 0))
ax.set_xlabel('Retention Time ($s$)')
ax.set_ylabel('Flatband Voltage Shift ($V$)')


ax.set_xscale('log')
ax.set_xlim(1, 1e6)
ax.set_ylim(2, 6)
### boders
for axis in ['top','bottom','left','right']:
  ax.spines[axis].set_linewidth(3)

### legend
legend_font = font_manager.FontProperties(family='times new roman', style='normal',
                                          size=23, weight='normal', stretch='normal')
for item in (legend.get_texts()):
  item.set_fontproperties(legend_font)
legend.set_frame_on(False)

### ticks
for tick in ax.get_xaxis().get_major_ticks():
  tick.set_pad(8.)
### axis label
ticks_font = font_manager.FontProperties(family='times new roman', style='normal',
                                         size=24, weight='normal', stretch='normal')
labels_font = font_manager.FontProperties(family='times new roman', style='normal',
                                          size=26, weight='normal', stretch='normal')
for item in ([ax.xaxis.label, ax.yaxis.label] ):
  item.set_fontproperties(labels_font)
for item in (ax.get_xticklabels() + ax.get_yticklabels()):
  item.set_fontproperties(ticks_font)

### axis tick
ax.xaxis.set_tick_params(which='major', width=2, size=5)
ax.xaxis.set_tick_params(which='minor', width=2, size=3)
ax.yaxis.set_tick_params(which='major', width=2, size=5)
ax.yaxis.set_tick_params(which='minor', width=2, size=3)

# plt.show()

fig_path = os.path.join(Save_Fig_Folder, 'retention')
fig.savefig(fig_path, dpi = 1020, bbox_inches='tight', pad_inches=0.1)

sys.path.remove(Path)