__author__ = 'lunzhy'
from matplotlib import font_manager
from mpl_toolkits.mplot3d import Axes3D

def setAxesLabel(ax, label_size=26, tick_size=24):
    ### borders
    for axis in ['top', 'bottom', 'left', 'right']:
        ax.spines[axis].set_linewidth(2)

    ### axis label
    ticks_font = font_manager.FontProperties(family='Arial', style='normal',
                                             size=tick_size, weight='normal', stretch='normal')
    labels_font = font_manager.FontProperties(family='Arial', style='normal',
                                              size=label_size, weight='normal', stretch='normal')
    labels = [ax.xaxis.label, ax.yaxis.label]
    if isinstance(ax, Axes3D):
        labels += [ax.zaxis.label]
    for label_item in (labels):
        label_item.set_fontproperties(labels_font)
    for label_item in (ax.get_xticklabels() + ax.get_yticklabels()):
        label_item.set_fontproperties(ticks_font)
    if isinstance(ax, Axes3D):
        for label_item in (ax.get_zticklabels() + ax.get_zticklabels()):
            label_item.set_fontproperties(ticks_font)

    offset_text = ax.yaxis.get_offset_text()
    if not offset_text is None:
        offset_text.set_fontproperties(ticks_font)

    return

def setAxesTicks(ax):
    ### axis tick
    ax.xaxis.set_tick_params(which='major', width=2, size=5)
    ax.xaxis.set_tick_params(which='minor', width=2, size=3)
    ax.yaxis.set_tick_params(which='major', width=2, size=5)
    ax.yaxis.set_tick_params(which='minor', width=2, size=3)

    for tick in ax.get_xaxis().get_major_ticks():
        tick.set_pad(8.)
    return


def setLegend(legend, font_size=22):
    ### legend
    legend_font = font_manager.FontProperties(family='times new roman', style='normal',
                                              size=font_size, weight='normal', stretch='normal')
    for legend_item in (legend.get_texts()):
        legend_item.set_fontproperties(legend_font)
    legend.set_frame_on(False)
    return


def setColorbar(cb, font_size=26):
    cb_font = font_manager.FontProperties(family='times new roman', style='normal',
                                          size=font_size, weight='normal', stretch='normal')
    for label_item in (cb.ax.get_yticklabels() + cb.ax.get_xticklabels()):
        label_item.set_fontproperties(cb_font)
    for label_item in ([cb.ax.yaxis.label]):
        label_item.set_fontproperties(cb_font)

    # set the offset text
    offset_text = cb.ax.yaxis.get_offset_text()
    if not offset_text is None:
        offset_text.set_fontproperties(cb_font)
    return
