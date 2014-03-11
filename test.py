__author__ = 'Lunzhy'
import os


def saveFigures():
    os.system('Detrapping.py')
    os.system('EffTunMass.py')
    os.system('Fermi.py')
    os.system('GateVoltage.py')
    os.system('TrapEnergy.py')
    os.system('TrapMass.py')
    os.system('Xsection.py')


if __name__ == '__main__':
    saveFigures()
