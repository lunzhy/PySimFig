__author__ = 'Lunzhy'
## This file is used to plot the electron distribution after program
import os
import sys
import matplotlib.pyplot as plt
from matplotlib import font_manager
Path = os.path.abspath(os.path.join('..', 'lib'))
if not Path in sys.path:
    sys.path.append(Path)
import lib.common as common
from matplotlib.ticker import FuncFormatter


def to_percent(y, position):
    s = str(int(100 * float(y)))
    # The percent symbol needs escaping in latex
    return s


def to_distance(x, position):
    s = x - 4
    return int(s)


Prj_base_dir = r'E:\PhD Study\SimCTM\SctmTest\Fitting\Padovani_C'
Main_project_name = r'Distribution'  # Demo, Paper, Distribution
Prj_list = ['16V', '18V']
Time_list = ['5e-3s', '5e-1s']
Trap_file_pattern = 'trapOccupation'

fig = plt.figure()
ax = fig.add_axes([0.15, 0.15, 0.8, 0.8])

for prj_index, prj_name in enumerate(reversed(Prj_list)):
    color_ind = prj_index
    prj_path = os.path.join(Prj_base_dir, Main_project_name, prj_name)
    for time_index, time_str in enumerate(reversed(Time_list)):
        ls_index = time_index
        time = float(time_str[:-1])
        trap_path = os.path.join(prj_path, common.TrapDistr_Folder)
        file = common.searchFilePathByTime(trap_path, Trap_file_pattern, time)
        yCoords, eTrapped = common.getDataAlongY_1D(file, 4)  # the fourth column in the file
        leg_label = 'Vprg = %s@t = %0.es' % (prj_name, time)
        ax.plot(yCoords, eTrapped, lw=4, ls=common.getLinestyle(ls_index), color=common.getColor(color_ind),
                label=leg_label)

legend = ax.legend(loc='upper right', handlelength=3)
ax.set_xlim(4, 12.8)
ax.set_xlabel('Distance Along Trapping Layer (nm)')
ax.set_ylabel('Trap Occupation Percentage (%)')

formatter = FuncFormatter(to_percent)
formatter_x = FuncFormatter(to_distance)
ax.yaxis.set_major_formatter(formatter)
ax.xaxis.set_major_formatter(formatter_x)

### boders
for axis in ['top', 'bottom', 'left', 'right']:
    ax.spines[axis].set_linewidth(3)

### legend
legend_font = font_manager.FontProperties(family='times new roman', style='normal',
                                          size=23, weight='normal', stretch='normal')
for item in (legend.get_texts()):
    item.set_fontproperties(legend_font)
legend.set_frame_on(False)

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

# fig_path = os.path.join(Save_Fig_Folder, 'TrapOccupy')
# fig.savefig(fig_path, dpi = 1020, bbox_inches='tight', pad_inches=0.1)
plt.show()
sys.path.remove(Path)