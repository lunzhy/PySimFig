__author__ = 'Lunzhy'
T = 'ab'
import os, re, sys
# path = os.path.abspath(os.path.dirname(__file__))
path = os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), os.pardir))
if not path in sys.path:
    sys.path.append(path)
import lib.common as cm

# physics constant
eps0 = 8.854187817e-14 # [F/cm]
q_charge = 1.602176487e-19 # [C]


def get_param_value(param_name, prj_path):
    default_param_path = cm.Default_Parfile_Path
    user_param_path = os.path.join(prj_path, cm.User_Param_File)
    # first search the default parameters
    for file in [default_param_path, user_param_path]:
        if not os.path.exists(file):
            print('This file does not exist. %s' % file)
            continue
        f = open(file)
        lines = f.read()
        pattern = re.compile(param_name + r'\s*:.*')
        match = re.search(pattern, lines)
        if match is not None:
            found_line = match.group()
        else:
            print(param_name)
            exit(0)
        split_line = re.split(':|#', found_line)
        value = split_line[1].strip()
    return value


def test():
    get_param_value('tc.tunnel.thick', cm.Debug_Folder_Path)


if __name__ == '__main__':
    test()