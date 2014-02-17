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
Frequency_list = [int(10), int(100), int(1e3), int(1e4), int(1e5), int(1e6)]



def plotFrequency():
  fig = plt.figure()
  ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
  main_prj_path = os.path.join(Base_dir, 'Frequency_B2T')
  compare.plotVfbComparation(ax, main_prj_path, Frequency_list)

  labels = ['frequency = %sHz' % fre for fre in Frequency_list ]
  ax.legend(labels, loc='lower left')

  ax.set_xlabel('Retetion Time ($s$)')
  ax.set_ylabel('Flatband Voltage Shift ($V$)')
  ax.set_xscale('log')

  # figname = os.path.join(common.Dir_SaveFig, 'Frequency_B2T')
  # plt.savefig(figname, dpi=600)
  return


def plotMassB2T():
  fig = plt.figure()
  ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
  main_prj_path = os.path.join(Base_dir, 'eMassBlock_B2T')
  compare.plotVfbComparation(ax, main_prj_path, BlockEmass_list)

  labels = ['emass = %s m0' % fre for fre in BlockEmass_list]
  ax.legend(labels, loc='lower left')

  ax.set_xlabel('Retetion Time ($s$)')
  ax.set_ylabel('Flatband Voltage Shift ($V$)')
  ax.set_xscale('log')

  # figname = os.path.join(common.Dir_SaveFig, 'eMassBlock_B2T')
  # plt.savefig(figname, dpi=600)
  return


def plotTrapDepthB2T():
  fig = plt.figure()
  ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
  main_prj_path = os.path.join(Base_dir, 'TrapDepth_B2T')
  compare.plotVfbComparation(ax, main_prj_path, TrapDepth_list)

  labels = ['Trap Depth = %s eV' % depth for depth in TrapDepth_list]
  ax.legend(labels, loc='lower left')

  ax.set_xlabel('Retetion Time ($s$)')
  ax.set_ylabel('Flatband Voltage Shift ($V$)')
  ax.set_xscale('log')

  # figname = os.path.join(common.Dir_SaveFig, 'TrapDepth_B2T')
  # plt.savefig(figname, dpi=600)
  return

def main():
  plotFrequency()
  plotMassB2T()
  plotTrapDepthB2T()
  plt.show()
  sys.path.remove(Path)
  return


if __name__ == '__main__': main()
