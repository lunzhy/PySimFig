import matplotlib.pyplot as plt
import os, sys
path = os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), '..'))
if not path in sys.path:
    sys.path.append(path)
import lib.common as cm

Band_directory = r'E:\PhD Study\SimCTM\SctmTest\SolverPackTest\Band'

def main():
    fig = plt.figure()
    ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
    time = 1.5e-9
    file = cm.searchFilePathByTime(Band_directory, 'band', time)
    yCoords, cb_edge = cm.getDataAlongY_1D(file, 2)  # the fourth column in the file
    dummy, vb_edge = cm.getDataAlongY_1D(file, 3)
    ax.plot(yCoords, cb_edge, yCoords, vb_edge)
    plt.show()
    return


if __name__ == '__main__': main()