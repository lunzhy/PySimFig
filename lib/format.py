__author__ = 'lunzhy'
from matplotlib import font_manager


def setAxes(ax):
    ### borders
    for axis in ['top', 'bottom', 'left', 'right']:
        ax.spines[axis].set_linewidth(2)

    ### axis label
    ticks_font = font_manager.FontProperties(family='times new roman', style='normal',
                                             size=24, weight='normal', stretch='normal')
    labels_font = font_manager.FontProperties(family='times new roman', style='normal',
                                              size=26, weight='normal', stretch='normal')
    for label_item in ([ax.xaxis.label, ax.yaxis.label]):
        label_item.set_fontproperties(labels_font)
    for label_item in (ax.get_xticklabels() + ax.get_yticklabels()):
        label_item.set_fontproperties(ticks_font)

    ### axis tick
    ax.xaxis.set_tick_params(which='major', width=2, size=5)
    ax.xaxis.set_tick_params(which='minor', width=2, size=3)
    ax.yaxis.set_tick_params(which='major', width=2, size=5)
    ax.yaxis.set_tick_params(which='minor', width=2, size=3)

    for tick in ax.get_xaxis().get_major_ticks():
        tick.set_pad(8.)
    return


def setLegend(legend):
    ### legend
    legend_font = font_manager.FontProperties(family='times new roman', style='normal',
                                              size=22, weight='normal', stretch='normal')
    for legend_item in (legend.get_texts()):
        legend_item.set_fontproperties(legend_font)
    legend.set_frame_on(False)
    return


def setColorbar(cb):
    cb_font = font_manager.FontProperties(family='times new roman', style='normal',
                                              size=26, weight='normal', stretch='normal')
    for label_item in (cb.ax.get_yticklabels() + cb.ax.get_xticklabels()):
        label_item.set_fontproperties(cb_font)
    for label_item in ([cb.ax.yaxis.label]):
        label_item.set_fontproperties(cb_font)
    return
