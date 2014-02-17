import matplotlib.pyplot as plt
import os, sys

Path = os.path.abspath(os.path.join('..', 'lib'))
if not Path in sys.path:
  sys.path.append(Path)
import common

Work_Directory = r'E:\PhD Study\SimCTM\SctmTest\SolverPackTest\Band'
File_Name_Base = 'band_s[].txt'

File_Name_Plot = os.path.join(Work_Directory, 'band_s1.txt')

def main():
  fig = plt.figure()
  ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
  common.plotSingleFile(ax, File_Name_Plot)
  plt.show()

  sys.path.remove(Path)
  return


if __name__ == '__main__': main()