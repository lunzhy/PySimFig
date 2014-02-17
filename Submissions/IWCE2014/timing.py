__author__ = 'Lunzhy'
import os

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager

from Submissions.IWCE2014 import *


## 5000, 10000, 15000 points
possoin_time = [515, 1367, 2025]
dd_time = [662, 2427, 4785]
total_time = [1294, 4030, 7151]
others_time = [total_time[i]-possoin_time[i]-dd_time[i] for i in range(0, 3)]

ind = np.arange(0.2, 1.6, 0.5)
width = 0.3

fig = plt.figure()
ax = fig.add_axes([0.13, 0.13, 0.8, 0.8])
ax.set_xlim(0, 1.7)

b1 = ax.bar(ind, others_time, width, color='r', linewidth=0)
b2 = ax.bar(ind, possoin_time, width, bottom=others_time, color=r'#E6DACE', linewidth=0)
b3 = ax.bar(ind, dd_time, width, bottom=[others_time[i]+possoin_time[i] for i in range(0,3)], color='b', linewidth=0)
ax.set_xticks(ind+width/2)
ax.set_xticklabels(['5000', '10000', '15000'])
legend = ax.legend(['Others', 'Poisson', 'Transport'], loc='upper left', prop={'size':32})
ax.set_xlabel('Number of Vertices (#)')
ax.set_ylabel('Excution Time Elapsed (s)')

ax.set_yticks([0, 2000, 4000, 6000, 8000])
ax.set_yticklabels(['0', '2k', '4k', '6k', '8k'])

### boders
for axis in ['top','bottom','left','right']:
  ax.spines[axis].set_linewidth(2)

### legend
legend_font = font_manager.FontProperties(family='times new roman', style='normal',
                                          size=26, weight='normal', stretch='normal')
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
ax.xaxis.set_tick_params(which='major', width=2, size=0)
ax.yaxis.set_tick_params(which='major', width=2, size=0)

# plt.show()
fig_path = os.path.join(Save_Fig_Folder, 'timing')
fig.savefig(fig_path, dpi = 1020, bbox_inches = 'tight', pad_inches = 0.1)


