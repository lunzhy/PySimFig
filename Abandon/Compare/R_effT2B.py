__author__ = 'Lunzhy'
import matplotlib.pyplot as plt
import os, sys

Path = os.path.abspath(os.path.join('..', 'lib'))
if not Path in sys.path:
    sys.path.append(Path)
import common

Base_dir = r'E:\PhD Study\SimCTM\SctmTest\RetentionTest'


def main():
    fig = plt.figure()
    ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])

    main_prj_path = os.path.join(Base_dir, 'T2B-halfTrap')  # T2B, T2B-halfTrap, T2B-fullTrap
    for index, prj in enumerate([True, False]):
        prj_path = os.path.join(main_prj_path, str(prj))
        time_list, vfb_list = common.readVfb(prj_path)
        ax.plot(time_list, vfb_list, lw=2, c=common.getColor(index))

    labels = ['With Trap-to-Band', 'W/O Trap-to-Band']
    ax.legend(labels, loc='lower left')
    ax.set_xlabel('Retetion Time ($s$)')
    ax.set_ylabel('Flatband Voltage Shift ($V$)')
    ax.set_ylim(0, 5.2)
    ax.set_xlim(1, 1e6)
    ax.set_xscale('log')

    figname = os.path.join(common.Dir_SaveFig, 'B2T-halfTrap')
    plt.savefig(figname, dpi=600)
    # plt.show()
    return


if __name__ == '__main__':
    main()
    sys.path.remove(Path)
