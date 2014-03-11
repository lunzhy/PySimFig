__author__ = 'Lunzhy'
import matplotlib.pyplot as plt
import os, sys

Path = os.path.abspath(os.path.join('..', 'lib'))
if not Path in sys.path:
    sys.path.append(Path)
import common, compare


Base_dir = r'E:\PhD Study\SimCTM\SctmTest\RetentionTest'
TrapDepth_list = [0.8, 1.0, 1.2, 1.4, 1.6, 1.8]
BlockEmass_list = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6]


def main():
    fig = plt.figure()
    ax_emass = fig.add_axes([0.1, 0.1, 0.8, 0.8])
    ######
    main_prj_path = os.path.join(Base_dir, 'eMassBlock')
    compare.plotVfbComparation(ax_emass, main_prj_path, BlockEmass_list)
    labels_emass = ['Emass = %s m0' % emass for emass in BlockEmass_list]

    ax_emass.legend(labels_emass, loc='lower left')
    ax_emass.set_xlabel('Retetion Time ($s$)')
    ax_emass.set_ylabel('Flatband Voltage Shift ($V$)')
    ax_emass.set_xscale('log')

    # figname = os.path.join(common.Dir_SaveFig, 'eMassBlock')
    # plt.savefig(figname, dpi=600)

    ######
    fig = plt.figure()
    ax_trap = fig.add_axes([0.1, 0.1, 0.8, 0.8])
    main_prj_path = os.path.join(Base_dir, 'TrapDepth')
    compare.plotVfbComparation(ax_trap, main_prj_path, TrapDepth_list)
    labels_emass = ['Trap Depth = %seV' % trapDepth for trapDepth in TrapDepth_list]

    ax_trap.legend(labels_emass, loc='lower left')
    ax_trap.set_xlabel('Retetion Time ($s$)')
    ax_trap.set_ylabel('Flatband Voltage Shift ($V$)')
    ax_trap.set_xscale('log')

    # figname = os.path.join(common.Dir_SaveFig, 'TrapDepth')
    # plt.savefig(figname, dpi=600)
    plt.show()
    return


if __name__ == '__main__':
    main()
    sys.path.remove(Path)