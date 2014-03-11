__author__ = 'Lunzhy'
import matplotlib.pyplot as plt
import os, sys

Path = os.path.abspath(os.path.join('..', 'lib'))
if not Path in sys.path:
    sys.path.append(Path)
import common

Main_Prj_Path = r'E:\PhD Study\SimCTM\SctmTest\Temp\T2B'


def main():
    fig = plt.figure()
    ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
    for file in os.listdir(Main_Prj_Path):
        prj_path = os.path.join(Main_Prj_Path, file)
        time_list, vfb_list = common.readVfb(prj_path, True)
        ax.plot(time_list, vfb_list)

    ax.set_xscale('log')
    plt.show()
    return


if __name__ == '__main__':
    main()
    sys.path.remove(Path)