__author__ = 'Lunzhy'
import matplotlib.pyplot as plt
import os, sys
path = os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), '..\..'))
if not path in sys.path:
    sys.path.append(path)
import lib.common as cm

def viewTrapOcc(prj_path, time):

    return