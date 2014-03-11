__author__ = 'Lunzhy'
import os

directory = r'E:\PhD Study\SimCTM\SctmTest\SolverPackTest'
files_remain = ['user.param', 'substrate.in']

def delFiles(path):
    for file in os.listdir(path):
        if file in files_remain:
            continue
        file_path = os.path.join(path, file)
        if os.path.isfile(file_path):
            os.remove(file_path)
        else:
            delFiles(file_path)


delFiles(directory)