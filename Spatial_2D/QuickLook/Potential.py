__author__ = 'Lunzhy'
import os, sys, scipy
path = os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), '..\..'))
if not path in sys.path:
    sys.path.append(path)
import lib.common as cm
import matplotlib.pyplot as plt
import numpy as np

Prj_path = os.path.join(cm.Directory_Debug, cm.Potential_Folder)

def plot2D(prj_path, time):
    fig = plt.figure()
    ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
    x, y, potential = cm.readData2D(file_path, 1)
    grid_z = cm.makeValueGridZ(x, y, potential)
    im = ax.imshow(grid_z, cmap=plt.cm.jet, vmin=min(potential), vmax=max(potential), origin='lower',
                    extent=[1, 16, 1, 16], aspect='equal')
    plt.colorbar(im)
    plt.show()


if __name__ == '__main__':
    plotSingle(Potential_to_plot)