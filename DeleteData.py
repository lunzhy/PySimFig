__author__ = 'Lunzhy'
import os

directory = r'E:\PhD Study\SimCTM\SctmTest\SolverPackTest'


def delFiles(path):
  for file in os.listdir(path):
    file_path = os.path.join(path, file)
    if os.path.isfile(file_path):
      os.remove(file_path)
    else:
      delFiles(file_path)


delFiles(directory)